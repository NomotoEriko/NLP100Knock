# -*- coding: utf-8 -*-
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
vec = np.load("q85.npy")
t_idx = pickle.load(open("t_idx.pickle", "rb"))


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))


def q86(word="United_States"):
    return vec[t_idx.index(word)]


def q87(word1="United_States", word2="U.S"):
    vec1 = q86(word1)
    vec2 = q86(word2)
    return cosine_similarity(vec1, vec2)


def q88(word="England"):
    vec1 = q86(word).reshape(1, 300)
    sim = cosine_similarity(vec, vec1).reshape(300)
    idx = sim[np.argpartition(-sim, 10)].argsort()[::-1]
    for i in idx:
        print(t_idx[i], sim[i])


def q89(word1="Spain", word2="Madrid", word3="Athens"):
    vec1 = q86(word1) - q86(word2) + q86(word3)
    sim = cosine_similarity(vec, vec1.reshape(1, 300)).reshape(300)
    idx = sim[np.argpartition(-sim, 10)].argsort()[::-1]
    for i in idx:
        print(t_idx[i], sim[i])

if __name__ == '__main__':
    print("q86")
    print(q86())

    print("\nq87")
    print(q87())

    print("\nq88")
    q88()

    print("\nq89")
    q89()
