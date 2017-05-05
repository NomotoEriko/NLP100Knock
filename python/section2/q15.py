# -- coding: utf-8 --

import sys
from q10 import load_pure_hightmp
from pprint import pprint

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        N = sys.argv[1]
        N = int(N)
    else:
        N = 5
    lines = load_pure_hightmp()[-N:]
    pprint(lines)
