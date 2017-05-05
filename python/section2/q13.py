if __name__ == '__main__':
    cols = []
    for i in 1, 2:
        with open('col%d.txt' % i, 'r') as f:
            cols.append(f.readlines())
    with open('col12.txt', 'w') as fw:
        for row in zip(*cols*1):
            row = [r.strip() for r in row]
            fw.write('\t'.join(row)+'\n')
