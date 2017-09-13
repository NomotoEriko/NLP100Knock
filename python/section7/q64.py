# -*- coding: utf-8 -*-
import pymongo
from q60 import read_json

client = pymongo.MongoClient()
db = client.knock100_2017
client.drop_database(db)


def mk_bd(data, db):
    co = db.q64
    co.insert_many(data)
    return db, co


if __name__ == '__main__':
    data = [e for e in read_json("../../data/artist.json") if 'name' in e.keys()]
    db, co = mk_bd(data, db)
    client = pymongo.MongoClient()
    co = client.knock100_2017.q64
    result_name = co.create_index([('name', pymongo.ASCENDING)])
    result_aliases_name = co.create_index([('aliases.name', pymongo.ASCENDING)])
    result_tags_value = co.create_index([('tags.value', pymongo.ASCENDING)])
    result_rating_value = co.create_index([('rating.value', pymongo.ASCENDING)])

