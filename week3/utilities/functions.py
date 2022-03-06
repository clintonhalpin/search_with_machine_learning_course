import nltk
import string
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)
stemmer = SnowballStemmer('english')

def extract_title_transform(name):
    tokens = word_tokenize(name)
    # stem
    tokens = [stemmer.stem(w) for w in tokens]
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return " ".join(words)