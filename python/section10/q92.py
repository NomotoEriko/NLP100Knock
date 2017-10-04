# -*- coding: utf-8 -*-
from gensim.models.word2vec import Word2Vec


def expr_one_set(model, word1, word2, word3):
    if word1 in model.wv.vocab and word2 in model.wv.vocab and word3 in model.wv.vocab:
        word_sim = model.wv.most_similar_cosmul(positive=[word2, word3], negative=[word1], topn=1)[0]
    else:
        word_sim = ("", "")
    return word_sim


def main():
    model = Word2Vec.load("q90.model")
    with open("q92_w2v.txt", "w") as f:
        for line in open("../../data/questions_words_family.txt", "r"):
            word1, word2, word3, word4 = line.strip().split(" ")
            expr_word, sim = expr_one_set(model, word1, word2, word3)
            f.write(" ".join([word1, word2, word3, word4, expr_word, str(sim), "\n"]))
    print("complete!")

if __name__ == '__main__':
    main()
