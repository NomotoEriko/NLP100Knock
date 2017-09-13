# -*- coding: utf-8 -*-
import leveldb
db = leveldb.LevelDB("db/name-area.ldb")


def search(name):
    return db.Get(name.encode('utf-8'))


if __name__ == '__main__':
    # for k, v in db.RangeIter():
    #     print(k.decode('utf-8'), v.decode('utf-8'))
    name = input('>>>')
    while 'q' != name:
        print(search(name))
        name = input(">>>")
