import nltk
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
stemmer = PorterStemmer()

def clean_query(q):
    tokens = word_tokenize(q)
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
    
    # Query cleaner can actually just return an empty query
    if len(words) == 0:
        return q

    return " ".join(words)