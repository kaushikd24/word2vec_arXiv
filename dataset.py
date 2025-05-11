#generate dataset
import nltk
from nltk.corpus import brown

nltk.download('brown')

brown_words = nltk.corpus.brown.words()

words_small = list(brown.words())[:100000]




    