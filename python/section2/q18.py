# -- coding: utf-8 --

from q17 import load_tablelike_hightmp
from pprint import pprint

if __name__ == '__main__':
    df = load_tablelike_hightmp()
    pprint(df.sort_values('d', ascending=False))
