import os
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv
import utilities.functions as fn

# Useful if you want to perform stemming.
import nltk
stemmer = nltk.stem.PorterStemmer()

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/labeled_query_data.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--sample_size", default=1000000,  help="The number of queries to parse (default 1M)")
general.add_argument("--min_queries", default=1,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)

if args.sample_size:
    sample_size = int(args.sample_size)    

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find('id').text
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
df = pd.read_csv(queries_file_name)[['category', 'query']]
df = df[df['category'].isin(categories)]

#
# Get Size of Category
#
def get_category_size(frame, category):
    return frame[frame['category'] == category].size;

# 
# Given a frame and category fetch the parent
# 
def get_parent_category(frame, category):
    return frame[frame['category'] == category]['parent'].item();    

# IMPLEMENT ME: Convert queries to lowercase, and optionally implement other normalization, like stemming.
# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
print("processing queries len={0}".format(df.size))




clean_queries = [];
for index, row in df.sample(n=sample_size).iterrows():
    print(index)
    query = row["query"]
    #
    # Clean the queries using shared function
    #
    normalized_query = fn.clean_query(query)
    # print('query="{0}" clean="{1}"'.format(query, normalized_query))
    #
    # Create new rows for cleaned queries
    #
    new_row = {};
    new_row["query"] = normalized_query;
    new_row["category"] = row["category"]

    category_size = get_category_size(df, row['category'])

    if category_size < min_queries:
        new_row["category"] = get_parent_category(parents_df, row['category'])

    clean_queries.append(new_row)

print('done_cleaning')
# 
# Create cleaned queries df and reassign df we are ready to write data
#
cleaned_queries_df = pd.DataFrame(clean_queries)
cleaned_queries_df.head();
df = cleaned_queries_df;

# Create labels in fastText format.
df['label'] = '__label__' + df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df['category'].isin(categories)]
df['output'] = df['label'] + ' ' + df['query']
df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)
