# -- coding: utf-8 --

from q17 import load_tablelike_hightmp
from pprint import pprint

if __name__ == '__main__':
    df = load_tablelike_hightmp()
    prefectures = df.groupby('a').count().sort_values('b', ascending=False).index.tolist()
    for p in prefectures:
        pprint(df[df['a'] == p])
