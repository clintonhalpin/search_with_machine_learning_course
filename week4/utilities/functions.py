import nltk
import string
import re
from nltk.stem import PorterStemmer
nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
stemmer = PorterStemmer()

def clean_query(q):
    clean_query = " ".join((stemmer.stem(w) for w in re.sub("[^0-9a-zA-Z]+", " ", q).lower().split()));
    return clean_query;