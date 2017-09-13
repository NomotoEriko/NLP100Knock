# -*- coding: utf-8 -*-
import leveldb
import json
import os
import codecs
from pprint import pprint


def read_json(path):
    if os.path.isfile(path):
        with codecs.open(path, 'r', encoding='utf-8') as f:
            data = f.read()
            data = json.loads("[" + data.replace("}\n{", "},{") + "]")
    else:
        print("E: %s is not file" % path)
        data = None
    return data


def mk_db(data, db_name):
    db = leveldb.LevelDB(db_name)
    pipe = db.Pipe
    for e in data:
        if 'name' in e.keys() and 'area' in e.keys():
            db.Put(e['name'].encode('utf-8'), e['area'].encode('utf-8'))
    return db

if __name__ == '__main__':
    data = read_json("../../data/artist.json")
    mk_db(data, "db/name-area.ldb")
