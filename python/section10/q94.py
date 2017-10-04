# -*- coding: utf-8 -*-
from gensim.models.word2vec import Word2Vec


def expr_one_step(model, word1, word2):
    if word1 in model.wv.vocab and word2 in model.wv.vocab:
        sim = model.wv.similarity(word1, word2)
    else:
        sim = ''
    return sim


def expr_one_file(model, file="../../data/wordsim353/set1.csv"):
    with open("q94_" + file.split("/")[-1], "w") as f:
        head_flag = 1
        for line in open(file, "r"):
            if 1 == head_flag:
                f.write(line.strip()+",w2v"+"\n")
                head_flag = 0
            else:
                tmp = line.strip().split(",")
                if len(tmp) > 2:
                    word1, word2 = tmp[:2]
                    sim = expr_one_step(model, word1, word2)
                    if isinstance(sim, float):
                        sim = str(5*(sim+1))
                    tmp.append(sim)
                f.write(",".join(tmp)+"\n")
    print("complete!")


if __name__ == '__main__':
    model = Word2Vec.load("q90.model")
    expr_one_file(model, file="../../data/wordsim353/set1.csv")
    expr_one_file(model, file="../../data/wordsim353/set2.csv")
