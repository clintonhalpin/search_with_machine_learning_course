import argparse
import os
import random
import xml.etree.ElementTree as ET
from pathlib import Path
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import pandas as pd

stemmer = SnowballStemmer('english')

def transform_name(product_name):
    words = nltk.word_tokenize(product_name)
    new_words=[word for word in words if word.isalnum()]
    stemmed_name=" ".join([stemmer.stem(word) for word in new_words])
    return stemmed_name

# Directory for product data
directory = r'/workspace/search_with_machine_learning_course/data/pruned_products/'

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--input", default=directory,  help="The directory containing product data")
general.add_argument("--output", default="/workspace/datasets/fasttext/output.fasttext", help="the file to output to")

# Consuming all of the product data will take over an hour! But we still want to be able to obtain a representative sample.
general.add_argument("--sample_rate", default=1.0, type=float, help="The rate at which to sample input (default is 1.0)")

# IMPLEMENT: Setting min_products removes infrequent categories and makes the classifier's task easier.
general.add_argument("--min_products", default=0, type=int, help="The minimum number of products per category (default is 0).")

general.add_argument("--category_level", default=0, type=int, help="Change the category level")

args = parser.parse_args()
output_file = args.output
path = Path(output_file)
output_dir = path.parent
if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)

if args.input:
    directory = args.input
min_products = args.min_products
sample_rate = args.sample_rate
category_level = args.category_level
skipped = 0
names = []
categories = []

# Run on CLI
# python week3/createContentTrainingData.py --output /workspace/datasets/categories/output.fasttext --min_products=20

print("Writing results to %s" % output_file)
with open(output_file, 'w') as output:
    for filename in os.listdir(directory):
        should_process = filename.endswith(".xml")
        if should_process:
            print("Processing %s" % filename)
            f = os.path.join(directory, filename)
            tree = ET.parse(f)
            root = tree.getroot()
            for child in root:
                if (child.find('name') is not None and child.find('name').text is not None and
                    child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                    child.find('categoryPath')[len(child.find('categoryPath')) - category_level][0].text is not None):
                    name = child.find('name').text.replace('\n', ' ')
                    name = transform_name(name)
                    cat = child.find('categoryPath')[len(child.find('categoryPath')) - category_level][0].text
                    names.append(name);
                    categories.append(cat);

    print('Building df', len(names))
    productsDf = pd.DataFrame({
        "cat": categories,
        "name": names
    })
    productValueCount = productsDf['cat'].value_counts()
    productNameCount = productsDf['name'].value_counts()
    print(productsDf.head())

    for index, row in productsDf.iterrows():
        if productValueCount[row['cat']] > min_products:
            output.write("__label__%s %s\n" % (row['cat'], row['name']))
        else:
            skipped = skipped + 1

    print('skipped', skipped)