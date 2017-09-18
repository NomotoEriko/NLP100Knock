# -*- coding: utf-8 -*-
import codecs
from collections import Counter
from matplotlib import pyplot as plt
from functools import reduce
from math import log2
from pprint import pprint
from nltk.stem import PorterStemmer
import re
# from nltk.corpus import stopwords
stemmer = PorterStemmer()
# スタンフォードのトークナイズでdon't をdo n't に分けたりはできる


def get_dataset(path='sentiment.txt'):
    return [s for s in codecs.open(path, "r", encoding="utf-8", errors="ignore")]


def show_word_count(data):
    y = [log2(e) for e in sorted(
        Counter(reduce(lambda a, b: a+b,
                       [[stemmer.stem(w) for w in re.sub(r"[^a-zA-Z ]", " ", s[2:]).strip().split(' ')]
                        for s in data])).values(), reverse=True)]
    x = [log2(i) for i in range(1, len(y)+1)]
    plt.clf()
    plt.plot(x, y)
    plt.savefig("Zipf")
    # 出現回数が４〜２e８の奴だけ使います


def mk_stop_list(data, start=2, end=12):
    counter = Counter(reduce(lambda a, b: a+b,
                             [[stemmer.stem(w) for w in re.sub(r"[^a-zA-Z ]", " ", s[2:]).strip().split(' ')]
                              for s in data]))
    stop_word = [kv[0] for kv in counter.items() if log2(kv[1]) < start or log2(kv[1]) > end]
    with open("stop_list.txt", "w") as f:
        f.write('\n'.join(stop_word))
    return stop_word


def stop_or_not(words, stop_words=None):
    if stop_words:
        stop_list = stop_words
    else:
        stop_list = [w.strip() for w in open("stop_list.txt", "r")]

    return [(word, stemmer.stem(word) in stop_list) for word in words]


if __name__ == '__main__':
    data = get_dataset()
    # show_word_count(data)
    pprint(mk_stop_list(data))
    words = input(">>>")
    while words:
        pprint(stop_or_not(re.sub(r"[^a-zA-Z ]", " ", words).split(" ")))
        words = input(">>>")
