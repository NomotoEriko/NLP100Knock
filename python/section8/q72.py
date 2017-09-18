# -*- coding: utf-8 -*-
from q71 import get_dataset
from nltk.stem import PorterStemmer
import re
import pickle
stemmer = PorterStemmer()
stop_list = [w.strip() for w in open("stop_list.txt", "r")]
vocabulary = []


def one_Feature_extraction(data):
    label = int(data[:2])
    sentence = data[3:].strip()
    feature = []
    for w in re.sub(r"[^a-zA-Z ]", " ", sentence).strip().split(' '):
        w = stemmer.stem(w)
        if w in stop_list:
            continue
        if w in vocabulary:
            feature.append(vocabulary.index(w))
        else:
            feature.append(len(vocabulary))
            vocabulary.append(w)
    return label, feature


def Feature_extraction(path=None, save=None):
    if path:
        dataset = get_dataset(path)
    else:
        dataset = get_dataset()

    featured = [one_Feature_extraction(d) for d in dataset]
    if save:
        with open(save+'.pickle', 'wb') as f:
            pickle.dump(featured, f)
        with open(save+'.txt', 'w') as f:
            f.write('\n'.join([str(lf[0])+'\t'+','.join(str(fe) for fe in lf[1]) for lf in featured]))
        with open(save+'.vocab', 'w') as f:
            f.write('\n'.join(vocabulary))
    return featured


if __name__ == '__main__':
    Feature_extraction(save='featured')
