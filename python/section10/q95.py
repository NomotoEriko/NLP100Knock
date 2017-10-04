# -*- coding: utf-8 -*-
import pandas as pd
from scipy.stats import spearmanr


def spear(file="q94_set1.csv"):
    df = pd.read_csv(file).dropna()
    human = df["Human (mean)"].values
    w2v = df["w2v"].values
    correlation, pvalue = spearmanr(human, w2v)
    return correlation, pvalue


if __name__ == '__main__':
    c, p = spear("q94_set1.csv")
    print("correlation", c, "\tpvalue", p)
    c, p = spear("q94_set2.csv")
    print("correlation", c, "\tpvalue", p)
