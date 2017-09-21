# -*- coding: utf-8 -*-
from os.path import join
from random import shuffle as シャッフル
from collections import Counter as 数え天狗
import codecs
データディレクトリ = "../../data/rt-polaritydata/rt-polaritydata"


def main():
    negs = ["-1 " + s for s in codecs.open(join(データディレクトリ, "rt-polarity.neg"), 'r', encoding='latin1')]
    poss = ["+1 " + s for s in codecs.open(join(データディレクトリ, "rt-polarity.pos"), 'r', encoding='latin1')]
    ネガポジ = negs + poss
    シャッフル(ネガポジ)
    print(ネガポジ[:3])
    with open('sentiment.txt', 'w') as f:
        f.write(''.join(ネガポジ))
    print(数え天狗(s[:2] for s in ネガポジ))

if __name__ == '__main__':
    main()
