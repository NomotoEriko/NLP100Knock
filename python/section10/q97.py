# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def いい感じに表示する(string, sep='\t', max=100):
    flag = 0
    for w in string:
        if flag > max:
            if sep == w:
                print()
                flag = 0
            else:
                print(w, end='')
                flag += 1
        else:
            print(w, end='')
            flag += 1


if __name__ == '__main__':
    df = pd.read_pickle("q96.pickle")
    国名 = np.array(df["国名"].values)
    arr = np.array([i.reshape(300) for i in df["vec"].values])
    kmeans = KMeans(n_clusters=5, random_state=0).fit(arr)
    for i in range(5):
        cluster = 国名[kmeans.labels_ == i]
        print("*"*125)
        いい感じに表示する("\t".join(cluster))
        print()
        print("*"*125, end="\n\n\n")
