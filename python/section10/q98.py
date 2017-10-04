# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, ward
from matplotlib import pyplot as plt


if __name__ == '__main__':
    df = pd.read_pickle("q96.pickle")
    国名 = np.array(df["国名"].values)
    arr = np.array([i.reshape(300) for i in df["vec"].values])
    h_cls = ward(arr)
    plt.figure(figsize=(25*4, 10*2))
    dendrogram(h_cls, leaf_label_func=lambda i: 国名[i], leaf_font_size=10)
    plt.savefig("q98.jpg")
