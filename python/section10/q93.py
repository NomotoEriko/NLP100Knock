# -*- coding: utf-8 -*-
import numpy as np
import pandas


def accuracy(filename="q92_w2v.txt"):
    df = pandas.read_csv(filename, sep=' ', names=["word1", "word2", "word3", "correct", "answer", "score", "nan"])
    num, _ = df.shape
    cor_num = (df["correct"] == df["answer"]).sum()
    return cor_num/num


if __name__ == '__main__':
    print(accuracy())
