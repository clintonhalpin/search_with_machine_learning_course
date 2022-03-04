# Week 3 Notes


```python
pip install -r ../requirements_week3.txt
```

---
## Product Name Stemmer & Tokenizer


```python
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

names = [
    'Peavey - GT10 10W Guitar Amplifier', 
    'Roland - 20W Guitar Amplifier',
    'PhoneMate - 5.8GHz Expandable Cordless Phone',
    'Whirlpool - 17.5 Cu. Ft. Chest Freezer - White'
]

stemmer = SnowballStemmer('english')

def transform_name(product_name):
    words = nltk.word_tokenize(product_name)
    new_words=[word for word in words if word.isalnum()]
    stemmed_name=" ".join([stemmer.stem(word) for word in new_words])
    return stemmed_name


for name in names:
    print(name, '=>', transform_name(name))
```

    Peavey - GT10 10W Guitar Amplifier => peavey gt10 10w guitar amplifi
    Roland - 20W Guitar Amplifier => roland 20w guitar amplifi
    PhoneMate - 5.8GHz Expandable Cordless Phone => phonem expand cordless phone
    Whirlpool - 17.5 Cu. Ft. Chest Freezer - White => whirlpool cu ft chest freezer white


---
## Exercise 1 
## Precision and Recall (Category Depth 4)
categoryPath ex. `abcat0712003` = `Board & Puzzle`


```bash
%%bash
echo "p@1"
~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test
echo "p@5"
~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test 5
```

    p@1
    N	9549
    P@1	0.526
    R@1	0.526
    p@5
    N	9549
    P@5	0.154
    R@5	0.771


## Precision and Recall (Category Depth 3)
categoryPath ex. `abcat0705002` = `PSP`


```bash
%%bash
echo "p@1"
~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test
echo "p@5"
~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test 5
```

    p@1
    N	9920
    P@1	0.671
    R@1	0.671
    p@5
    N	9920
    P@5	0.172
    R@5	0.86


---
## Project Assement
### For classifying product names to categories:

What precision (P@1) were you able to achieve?
- .56

What fastText parameters did you use?
- epoch=25, wordNGrams=2, learningRate=1.0
- I also checked out the autotuner but didn't get it working

How did you transform the product names?
- Used the snowball stemmer, nltk tokenizer

How did you prune infrequent category labels, and how did that affect your precision?
- Used a pandas dataframe to count items in a category

How did you prune the category tree, and how did that affect your precision?
- Using a higher level category increased precision by 16%

### For deriving synonyms from content:
What 20 tokens did you use for evaluation?

What fastText parameters did you use?

How did you transform the product names?

What threshold score did you use?

What synonyms did you obtain for those tokens?


### For integrating synonyms with search:
How did you transform the product names (if different than previously)?

What threshold score did you use?

Were you able to find the additional results by matching synonyms?