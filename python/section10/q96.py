# -*- coding: utf-8 -*-
from gensim.models.word2vec import Word2Vec
import pickle
import pandas as pd
import sys
sys.path.append("/Users/nomotoeriko/Desktop/noer_2017/100knock/python/section9")
from q81 import get_国名リスト


if __name__ == '__main__':
    model = Word2Vec.load("q90.model")
    国名リスト = get_国名リスト()
    国名vec = []
    for 国名 in 国名リスト:
        国名 = 国名.replace(" ", "_")
        if 国名 in model.wv.vocab:
            vec = model.wv[国名]
            国名vec.append({"国名": 国名, "vec": vec.reshape(300)})
    df = pd.DataFrame(国名vec)
    pd.to_pickle(df, "q96.pickle")
"""
"""