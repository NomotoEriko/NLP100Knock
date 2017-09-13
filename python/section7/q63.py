# -*- coding: utf-8 -*-
import leveldb
from q60 import read_json
import pickle
from pprint import pprint


def mk_name_tags(data, db_name):
    db = leveldb.LevelDB(db_name)
    for e in data:
        if 'name' in e.keys() and 'tags' in e.keys():
            db.Put(e['name'].encode('utf-8'), pickle.dumps(e['tags']))
    return db


if __name__ == '__main__':
    # data = read_json("../../data/artist.json")
    # mk_name_tags(data, "db/name-tags.ldb")

    db = leveldb.LevelDB("db/name-tags.ldb")
    name = input('>>>')
    while 'q' != name:
        pprint(pickle.loads(db.Get(name.encode('utf-8'))))
        name = input(">>>")
