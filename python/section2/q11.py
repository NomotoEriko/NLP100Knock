from q10 import load_pure_hightmp
from pprint import pprint
if __name__ == '__main__':
    lines = load_pure_hightmp()
    lines = [l.replace('\t', ' ') for l in lines]
    pprint(lines)
