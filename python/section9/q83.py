# -*- coding: utf-8 -*-
from q80 import load_txt
import pickle
import json


def dict_append(d, e):
    if e in d.keys():
        d[e] += 1
    else:
        d[e] = 1


def main():
    t_c = load_txt("q82.txt")
    # t_c = load_txt("q83_test.txt")
    f_tc = {}
    f_t = {}
    f_c = {}
    n = 0
    for tc in t_c:
        t, c = tc.strip().split('\t')
        c = tuple(sorted(c.split(',')))
        dict_append(f_tc, (t, c))
        dict_append(f_t, t)
        dict_append(f_c, c)
        n += 1
    pickle.dump({"f_tc": f_tc, "f_t": f_t, "f_c": f_c, "N": n}, open("q83.pickle", "wb"))
    print("complete!")

if __name__ == '__main__':
    main()
