# -*- coding: utf-8 -*-
import pickle
from scipy.sparse import lil_matrix, save_npz
from scipy import log
t_idx = []
c_idx = []


def mk_matrix(data):
    t_num = len(data["f_t"])
    c_num = len(data["f_c"])
    mat = lil_matrix((t_num, c_num))
    return mat


def get_idx(e_idx, e):
    if e in e_idx:
        return e_idx.index(e)
    else:
        i = len(e_idx)
        e_idx.append(e)
        return i


def main():
    d = pickle.load(open("q83.pickle", "rb"))
    # d = pickle.load(open("q84_test.pickle", "rb"))
    mat = mk_matrix(d)
    for k, v in d["f_tc"].items():
        t, c = k
        ti = get_idx(t_idx, t)
        ci = get_idx(c_idx, c)
        mat[ti, ci] = max(log(d["N"]*v / (d["f_t"][t]*d["f_c"][c])), 0) if v > 10 else 0
    save_npz("q84.npz", mat.tocsc())
    pickle.dump(t_idx, open("t_idx.pickle", "wb"))


if __name__ == '__main__':
    main()
