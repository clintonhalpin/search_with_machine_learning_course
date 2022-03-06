# Week 3 Notes


```python
pip install -r ../requirements_week3.txt
```

---
## Product Name Stemmer & Tokenizer
First attempt at nltk library. Goals to stem words and clean up strings of titles as much as possible!


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
### Precision and Recall (Category Depth 4)
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


### Precision and Recall (Category Depth 3)
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
## Exercise 2
Derive Synonyms from Content

Below Is my working function for cleaning up product names


```python
import nltk
import string
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)

names = [
    'Peavey - GT10 10W Guitar Amplifier', 
    'Roland - 20W Guitar Amplifier',
    'PhoneMate - 5.8GHz Expandable Cordless Phone',
    'Whirlpool - 17.5 Cu. Ft. Chest Freezer - White',
    'Apple - iPhone 13 Pro Max 5G 256GB - Sierra Blue (AT&T)'
    'Bose - Headphones 700 Wireless Noise Cancelling Over-the-Ear Headphones - Triple Black'
]


def transform_name(name):
    tokens = word_tokenize(name)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return " ".join(words)


for name in names:
    print(transform_name(name))
```

    peavey guitar amplifier
    roland guitar amplifier
    phonemate expandable cordless phone
    whirlpool cu ft chest freezer white
    apple iphone pro max sierra blue bose headphones wireless noise cancelling overtheear headphones triple black


# Synonyms from Title Model
I used the basic fasttext model builder, didn't experiment much with tuning. 

Build the model
```
~/fastText-0.9.2/fasttext skipgram -input /workspace/datasets/fasttext/titles.txt -output /workspace/datasets/fasttext/title_model
```

Test the model


```bash
%%bash
python testSynonyms.py
```

             queries  score                                                                                                                                                                       neighbors
    0          Phone    1.0                                     motorola(0.96), cell(0.95), mobil(0.95), verizon(0.94), earphon(0.94), tmobil(0.94), nocontract(0.94), gophon(0.94), htc(0.94), droid(0.94)
    1         Camera    1.0                                                    xs(0.99), vr(0.99), rebel(0.99), dslr(0.99), slr(0.99), nikon(0.99), zoom(0.99), finepix(0.99), cybershot(0.99), sigma(0.99)
    2         Laptop    1.0                                  processor(0.98), gateway(0.97), drive(0.97), ideapad(0.96), aspir(0.96), pavilion(0.96), vaio(0.96), ideacentr(0.96), duo(0.96), display(0.96)
    3   Refrigerator    1.0                                 thruthedoor(0.99), ice(0.99), freezer(0.99), french(0.99), sidebysid(0.98), order(0.98), cu(0.98), counterdepth(0.98), frostfre(0.98), ft(0.98)
    4         Guitar    0.6                           natur(0.97), acousticelectr(0.96), fullsiz(0.95), signatur(0.95), bass(0.94), cutaway(0.93), burst(0.93), string(0.93), dreadnought(0.93), star(0.92)
    5          Dryer    1.0                        steamdryer(0.99), washer(0.99), freezer(0.98), higheffici(0.98), ultralarg(0.98), super(0.98), fryer(0.98), refriger(0.98), spacemak(0.98), drawer(0.98)
    6             Tv    0.3                                            flatpanel(0.99), tvs(0.97), panel(0.94), flat(0.92), tube(0.92), bdi(0.91), flatb(0.89), flattub(0.88), furnitur(0.88), design(0.87)
    7      Subwoofer    1.0                              dualvoicecoil(0.99), singlevoicecoil(0.99), jbl(0.97), infin(0.96), abl(0.96), kenwood(0.95), polk(0.95), marin(0.95), coaxial(0.95), fosgat(0.95)
    8          Beats    0.4                                                  beatl(0.97), cheat(0.96), seat(0.94), great(0.94), heat(0.93), seattl(0.92), creat(0.92), begin(0.90), left(0.90), brain(0.90)
    9          Mouse    0.1                                       save(0.93), famous(0.92), songbook(0.92), piano(0.92), playbook(0.91), lifebook(0.91), book(0.90), compos(0.90), delay(0.89), ebook(0.89)
    10       Blender    1.0                                frogger(0.98), grinder(0.98), topper(0.98), whistler(0.98), murder(0.98), juicer(0.98), sharper(0.98), steeler(0.97), warmer(0.97), slicer(0.97)
    11       Macbook    1.0                                           lifebook(0.99), ebook(0.98), songbook(0.98), nook(0.98), essenti(0.96), leopard(0.96), us(0.96), xps(0.95), umd(0.95), alienwar(0.95)
    12         Apple    1.0                                                      vhf(0.99), nobl(0.99), subscript(0.99), pdas(0.99), cdrom(0.99), focus(0.98), klh(0.98), acdc(0.98), awg(0.98), impp(0.98)
    13       Samsung    0.0                             impact(0.92), extractor(0.91), silver(0.90), capacitor(0.89), sharpen(0.89), prepac(0.88), whitesilv(0.88), dispens(0.88), bluewhit(0.88), lg(0.88)
    14      Nintendo    1.0                                                       wii(0.97), danc(0.97), adventur(0.96), gamecub(0.95), advanc(0.95), nc(0.95), world(0.95), ds(0.95), psp(0.95), man(0.95)
    15          Sony    0.7                                                    jvc(0.96), everio(0.96), memorex(0.95), camcord(0.94), flip(0.94), g(0.94), ibm(0.93), dvdrrw(0.93), lenovo(0.93), dvr(0.93)
    16   Playstation    1.0                                            legendari(0.97), vol(0.96), pinbal(0.96), legend(0.96), b(0.96), playalong(0.96), real(0.95), pictur(0.95), aquarian(0.95), iv(0.95)
    17          Xbox    1.0                                                    world(0.97), legend(0.96), vol(0.96), rise(0.96), danc(0.96), adventur(0.96), evan(0.95), nanci(0.95), box(0.95), guid(0.95)
    18            Hp    1.0               pavilion(0.98), allinon(0.98), factoryrefurbish(0.97), touchsmart(0.97), eallinon(0.97), packag(0.96), desktop(0.96), compaq(0.96), processor(0.96), comput(0.96)
    19      Whirpool    1.0                          laundri(0.99), superba(0.99), whirlpool(0.99), frontload(0.99), titanium(0.99), accubak(0.99), front(0.99), cuisinart(0.99), frost(0.99), midsiz(0.98)
    20    Kitchenaid    1.0  biscuitonbiscuit(0.99), kitchen(0.99), bisqueonbisqu(0.99), bisqu(0.99), stainlesssteel(0.99), biscuit(0.99), whirlpool(0.99), architect(0.99), gas(0.99), stainlesslook(0.99)


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
- Phone,Camera,Laptop,Refrigerator,Guitar,Dryer,Tv,Subwoofer,Beats,Mouse,Blender,Macbook,Apple,Samsung,Nintendo,Sony,Playstation,Xbox,Hp,Whirpool,Kitchenaid

What fastText parameters did you use?
- 

How did you transform the product names?
- Lowercase, stemmed, removed punctuation, removed stop words

What threshold score did you use?
- .93

What synonyms did you obtain for those tokens?
- See output above


### For integrating synonyms with search:
How did you transform the product names (if different than previously)?

What threshold score did you use?

Were you able to find the additional results by matching synonyms?