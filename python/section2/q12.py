from q10 import load_pure_hightmp

if __name__ == '__main__':
    cols = load_pure_hightmp()[:2]
    for i in 1, 2:
        with open('col%d.txt' % i, 'w') as f:
             print(cols[i-1], file=f)
