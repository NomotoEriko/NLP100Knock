# -*- coding: utf-8 -*-
from gensim.models import word2vec


def train_model():
    sentences = word2vec.LineSentence("../section9/q81.txt")
    model = word2vec.Word2Vec(
        sentences,
        sg=0,  # use CBoW
        size=300,
        min_count=5,  # ignore all words with total frequency lower than 5
        window=5,  # the maximum distance between the current ans predicted word.
        negative=5  # use 5 words as negative sampling
    )
    model.save("q90.model")
    return model


def use_model(model=None):
    if not model:
        model = word2vec.Word2Vec.load("q90.model")
    print("q86")
    print(model.wv["United_States"])

    print("\nq87")
    print(model.wv.similarity("United_States", "U.S"))

    print("\nq88")
    for r in model.wv.most_similar_cosmul(positive=["England"], topn=10):
        print(r[0], r[1])

    print("\nq89")
    for r in model.wv.most_similar_cosmul(positive=["Spain", "Athens"], negative=["Madrid"], topn=10):
        print(r[0], r[1])


if __name__ == '__main__':
    model = None
    # model = train_model()
    use_model(model)
