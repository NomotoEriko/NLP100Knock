def load_pure_hightmp():
    DATADIR = '../../data/hightemp.txt'
    with open(DATADIR, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    lines = load_pure_hightmp()
    print(len(lines))
