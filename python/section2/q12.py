from q10 import load_pure_hightmp

if __name__ == '__main__':
    cols = load_pure_hightmp()
    for i in 1, 2:
        with open('col%d.txt' % i, 'w') as f:
            for col in cols:
                print(col.split("\t")[i-1], file=f)
