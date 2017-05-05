# -- coding: utf-8 --

import sys
from q10 import load_pure_hightmp
from pprint import pprint
from math import ceil

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        N = sys.argv[1]
        N = int(N)
    else:
        N = 3

    lines = load_pure_hightmp()
    num = ceil(len(lines)/N)
    files = []
    for i in range(N):
        files.append(lines[i*num:min((i+1)*num, len(lines))])

    pprint(files)
