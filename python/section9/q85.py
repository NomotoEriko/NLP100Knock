# -*- coding: utf-8 -*-
from sklearn.decomposition import PCA
from scipy.sparse import load_npz


def main():
    mat = load_npz("q84.npz").todense()
    pca = PCA(n_components=300)
    pca.fit(mat)
    mat_d = pca.transform(mat)
    mat_d.dump("q85.npy")
    print("complete!")


if __name__ == '__main__':
    main()
