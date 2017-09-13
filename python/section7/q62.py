# -*- coding: utf-8 -*-
import leveldb
db = leveldb.LevelDB("db/name-area.ldb")

if __name__ == '__main__':
    japanese = []
    for k, v in db.RangeIter():
        if 'Japan'.encode('utf-8') == v:
            japanese.append(k.decode('utf-8'))
    print(len(japanese))
