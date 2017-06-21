# -*- coding: utf-8 -*-
import re
from nltk import PorterStemmer
from q51 import load_in_word

if __name__ == '__main__':
    words = load_in_word().split()
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(re.sub('[^a-zA-Z0-9]', '', w)) for w in words]
    print('\n'.join('%s\t%s' % ws for ws in zip(words, stemmed)))
