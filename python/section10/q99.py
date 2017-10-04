# -*- coding: utf-8 -*-
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    df = pd.read_pickle("q96.pickle")
    国名 = np.array(df["国名"].values)
    arr = np.array([i.reshape(300) for i in df["vec"].values])
    kmeans = KMeans(n_clusters=5, random_state=0).fit(arr)

    X_reduced = TSNE(n_components=2, random_state=0).fit_transform(arr)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=kmeans.labels_)
    plt.savefig("q99.jpg")
