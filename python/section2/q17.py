# -- coding: utf-8 --
import pandas as pd
from pprint import pprint

def load_tablelike_hightmp():
    DATADIR = '../../data/hightemp.txt'
    return pd.read_csv(open(DATADIR, 'r'), sep='\t', names=('a', 'b', 'c', 'd'))


if __name__ == '__main__':
    df = load_tablelike_hightmp()
    kinds = set(df.ix[:, 1].tolist())
    pprint(kinds)
