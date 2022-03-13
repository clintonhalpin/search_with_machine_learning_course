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
general.add_argument("--min_queries", default=1,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--sample_size", default=1000000,  help="Queries to sample from")
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
df = df.sample(n=sample_size)
df = df[df['category'].isin(categories)]

# IMPLEMENT ME: Convert queries to lowercase, and optionally implement other normalization, like stemming.
print('> cleaning_queries')
df['clean_query'] = df['query'].apply(fn.clean_query)

#
# How many queries in category?
#
counts = df['category'].value_counts();
def get_category_size(x):
    return counts.get(x, 0)

#
# Given category grab parent
#
def get_parent_category(frame, x):
    filt = frame['category'] == x
    parent = frame.loc[filt, 'parent'];
    if not parent.empty:
        return parent.item()
    return None

#
# Make sure that each category meets min queries requirements if not
# we keep rolling up to parent
#
cached_sizes = {}
def first_min_queries_match(x):
    size = 0;
    if x in cached_sizes:
        size = cached_sizes[x]
    else:
        size = get_category_size(x)
        
    if size >= min_queries:
        return x
    else:
        parent = get_parent_category(parents_df, x);
        print("< min_queries={0}, size={1}, parent={2}".format(x, size, parent))
        if parent is not None:
            return first_min_queries_match(parent)
        return x;    

# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
print('> checking for min_queries');
original_categories_len = df['category'].value_counts().size
# 
# Store list of categories which have less than min categories
#
less_than_min = df[df['category'].isin(df['category'].value_counts()[df['category'].value_counts() < min_queries].index)].category.unique()
print("number of queries to rollup={0}".format(len(less_than_min)))
#
# Only apply "expensive" roll up if in list
#
df['category'] = df['category'].apply(lambda x: first_min_queries_match(x) if x in less_than_min else x)

print("> original unique categories={0}".format(original_categories_len))
print("> trimmed categories={0}".format(df['category'].value_counts().size))

# Create labels in fastText format.
df['label'] = '__label__' + df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df['category'].isin(categories)]
df['output'] = df['label'] + ' ' + df['clean_query']
df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)