# -*- coding: utf-8 -*-
from os.path import join
from random import shuffle
from collections import Counter
import codecs
data_dir = "../../data/rt-polaritydata/rt-polaritydata"


def main():
    negs = ["-1 " + s for s in codecs.open(join(data_dir, "rt-polarity.neg"), 'r', encoding='utf-8', errors='ignore')]
    poss = ["+1 " + s for s in codecs.open(join(data_dir, "rt-polarity.pos"), 'r', encoding='utf-8', errors='ignore')]
    neg_pos = negs + poss
    shuffle(neg_pos)
    print(neg_pos[:3])
    with open('sentiment.txt', 'w') as f:
        f.write(''.join(neg_pos))
    print(Counter(s[:2] for s in neg_pos))

if __name__ == '__main__':
    main()
