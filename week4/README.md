# Week 4 Notebook
Query Understanding notebook

## Task 1: Prune the category taxonomy.
Work on cleaning queries / stemming etc

```python
import pandas as pd
df = pd.read_csv('/workspace/datasets/train.csv')[['category', 'query']]
df.head(n=5)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>query</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abcat0101001</td>
      <td>Televisiones Panasonic  50 pulgadas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abcat0101001</td>
      <td>Sharp</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pcmcat193100050014</td>
      <td>nook</td>
    </tr>
    <tr>
      <th>3</th>
      <td>abcat0101001</td>
      <td>rca</td>
    </tr>
    <tr>
      <th>4</th>
      <td>abcat0101005</td>
      <td>rca</td>
    </tr>
  </tbody>
</table>
</div>



### Stem, Clean queries
Originally I had a much more robust `clean_query` function but it seemed to take forever across the 3M records. I trimed this down significantly


```python
import utilities.functions as fn

test_df = df[0:10];
test_df.assign(stemmed = test_df['query'].apply(fn.clean_query))
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>query</th>
      <th>stemmed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abcat0101001</td>
      <td>Televisiones Panasonic  50 pulgadas</td>
      <td>television panason 50 pulgada</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abcat0101001</td>
      <td>Sharp</td>
      <td>sharp</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pcmcat193100050014</td>
      <td>nook</td>
      <td>nook</td>
    </tr>
    <tr>
      <th>3</th>
      <td>abcat0101001</td>
      <td>rca</td>
      <td>rca</td>
    </tr>
    <tr>
      <th>4</th>
      <td>abcat0101005</td>
      <td>rca</td>
      <td>rca</td>
    </tr>
    <tr>
      <th>5</th>
      <td>pcmcat143200050016</td>
      <td>Flat screen tvs</td>
      <td>flat screen tv</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pcmcat247400050001</td>
      <td>macbook</td>
      <td>macbook</td>
    </tr>
    <tr>
      <th>7</th>
      <td>pcmcat171900050028</td>
      <td>Blue tooth headphones</td>
      <td>blue tooth headphon</td>
    </tr>
    <tr>
      <th>8</th>
      <td>abcat0107004</td>
      <td>Tv antenna</td>
      <td>tv antenna</td>
    </tr>
    <tr>
      <th>9</th>
      <td>pcmcat186100050006</td>
      <td>memory card</td>
      <td>memori card</td>
    </tr>
  </tbody>
</table>
</div>



### Create Tranining and Test Data
Through stemming and cleaning of categories we get a much cleaner dataset


```bash
%%bash
python ../week4/create_labeled_queries.py --min_queries=200
head -n 10 /workspace/datasets/labeled_query_data.txt
wc -l /workspace/datasets/labeled_query_data.txt
```

    > cleaning_queries
    > checking for min_queries
    > original unique categories=1451
    > final categories=776
    __label__abcat0102003 blu ray player
    __label__abcat0201011 ipod
    __label__cat02015 tae guk gi
    __label__pcmcat180400050000 canon camera
    __label__pcmcat209000050008 hp touchpad
    __label__cat02002 the sim
    __label__pcmcat209000050007 dryer
    __label__abcat0101001 lcd tv
    __label__abcat0403000 gopro
    __label__pcmcat183800050007 usb car adapt
    994279 /workspace/datasets/labeled_query_data.txt


## Task 2: Train a query classifier.
Use the labeled data to build a fast test model


```bash
%%bash
./create_qu_model.sh
```

    Training data
    __label__abcat0102003 blu ray player
    __label__abcat0201011 ipod
    __label__cat02015 tae guk gi
    __label__pcmcat180400050000 canon camera
    __label__pcmcat209000050008 hp touchpad
    __label__cat02002 the sim
    __label__pcmcat209000050007 dryer
    __label__abcat0101001 lcd tv
    __label__abcat0403000 gopro
    __label__pcmcat183800050007 usb car adapt
    Test data
    __label__pcmcat174700050005 star war
    __label__cat09000 tmnt
    __label__cat02719 t pain
    __label__abcat0515028 laptop case
    __label__cat02015 land befor time
    __label__cat02015 barbi
    __label__abcat0807001 epson photo
    __label__pcmcat180400050000 digit camera
    __label__pcmcat158900050018 lcd projector
    __label__pcmcat246100050002 bluetooth


    Read 0M words
    Number of words:  683
    Number of labels: 672
    Progress: 100.0% words/sec/thread:   28668 lr:  0.000000 avg.loss:  1.611424 ETA:   0h 0m 0s


    p@1 test
    N	9941
    P@1	0.435
    R@1	0.435
    p@5 test
    N	9941
    P@5	0.125
    R@5	0.623


## Updating labels
Wanting higher P&R updating my training data to require queries to have more min_queries


```bash
%%bash
python ../week4/create_labeled_queries.py --min_queries=1000
head -n 10 /workspace/datasets/labeled_query_data.txt
wc -l /workspace/datasets/labeled_query_data.txt
```

    > cleaning_queries
    > checking for min_queries
    > original unique categories=1453
    > final categories=502
    __label__abcat0811004 g2 batteri
    __label__pcmcat162100050040 virgin mobil
    __label__abcat0208007 lcd
    __label__pcmcat186100050006 extern hard drive
    __label__pcmcat174700050005 age of empir
    __label__abcat0511004 wireless printer
    __label__pcmcat209000050007 ipad
    __label__cat02716 ugk
    __label__pcmcat156300050010 fridg
    __label__pcmcat247400050001 macbook
    994302 /workspace/datasets/labeled_query_data.txt



```bash
%%bash
./create_qu_model.sh
```

    Training data
    __label__abcat0101001 lcd tv
    __label__pcmcat158900050018 projector
    __label__abcat0403004 flip video camera
    __label__cat02015 darker than black
    __label__cat02015 appl
    __label__cat02015 fast and furiou
    __label__abcat0515028 carri case for laptop
    __label__abcat0101001 42 panason plasma
    __label__pcmcat232900050017 metal gear
    __label__abcat0201011 samsung galaxi mp3
    Test data
    __label__cat02015 make the grade
    __label__abcat0504010 usb memori
    __label__abcat0703002 star war 3
    __label__abcat0208011 bose portabl
    __label__pcmcat218000050003 ipod case
    __label__pcmcat247400050000 2398896 2402035 5386263 5386272 6804112 8579932 8589878 9374278 9650424
    __label__pcmcat186400050002 camera
    __label__pcmcat231700050017 googl tv
    __label__abcat0101001 lcd tv
    __label__pcmcat253700050020 kiss


    Read 0M words
    Number of words:  712
    Number of labels: 426
    Progress: 100.0% words/sec/thread:    9359 lr:  0.000000 avg.loss:  1.474405 ETA:   0h 0m 0s


    p@1 test
    N	9952
    P@1	0.446
    R@1	0.446
    p@5 test
    N	9952
    P@5	0.128
    R@5	0.64


### Working Category Roll up Function
Still getting used to pandas. So scratching some notes here to test


```python
import xml.etree.ElementTree as ET
import pandas as pd
root_category_id = 'cat00000'

tree = ET.parse('/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml')
root = tree.getroot()

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

parents_df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>parent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abcat0010000</td>
      <td>cat00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>abcat0011000</td>
      <td>abcat0010000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>abcat0011001</td>
      <td>abcat0011000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>abcat0011002</td>
      <td>abcat0011000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>abcat0011003</td>
      <td>abcat0011000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4634</th>
      <td>pcmcat97200050013</td>
      <td>cat15205</td>
    </tr>
    <tr>
      <th>4635</th>
      <td>pcmcat97200050015</td>
      <td>cat15063</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>pcmcat99000050001</td>
      <td>pcmcat50000050006</td>
    </tr>
    <tr>
      <th>4637</th>
      <td>pcmcat99000050002</td>
      <td>pcmcat99000050001</td>
    </tr>
    <tr>
      <th>4638</th>
      <td>pcmcat99300050000</td>
      <td>cat15063</td>
    </tr>
  </tbody>
</table>
<p>4639 rows × 2 columns</p>
</div>



### Performant way to rollup categories
This took me several iterations to figure out. 
1. Create some helper functions lookup size, parent
2. Identify canidates
3. Roll up categories
4. Profit


```python
min_queries = 2
```


```python
counts = df['category'].value_counts();
def get_category_size(x):
    return counts.get(x, 0)

def get_parent_category(frame, x):
    filt = frame['category'] == x
    parent = frame.loc[filt, 'parent'];
    if not parent.empty:
        return parent.item()
    return None


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
```


```python
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
```

    > checking for min_queries
    number of queries to rollup=6
    < min_queries=pcmcat96200050052, size=1, parent=None
    < min_queries=pcmcat153700050010, size=1, parent=None
    < min_queries=abcat0410019, size=1, parent=None
    < min_queries=abcat0307010, size=1, parent=None
    < min_queries=cat02040, size=1, parent=None
    < min_queries=pcmcat197600050001, size=1, parent=None
    > original unique categories=1190
    > trimmed categories=1190


## Project Assessment

### For query classification:

How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 100? To 1000?
- I used 200 for min queries, catgories went from `1443` to `552`

What values did you achieve for P@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category as well as trying different fastText parameters or query normalization. Report at least 3 of your runs.
Best run

```
#params
~/fastText-0.9.2/fasttext supervised -input $TRAINING -output model_qu -lr .5 -epoch 25 -wordNgrams 2 -minCountLabel 10 -loss hs

#results
p@1 test
N       8369
P@1     0.527
R@1     0.527
p@5 test
N       8369
P@5     0.147
R@5     0.736
```

### For integrating query classification with search:

Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.
* laptop = `pcmcat247400050000`
* beats = `pcmcat144700050004`


Given 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.
* fridge = `cat02015`
