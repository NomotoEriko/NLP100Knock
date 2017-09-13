# -*- coding: utf-8 -*-
# $ mongod
# > show dbs
# admin          0.000GB
# knock100_2017  0.135GB
# local          0.000GB
# > use knock100_2017
# switched to db knock100_2017

# # q65
# db.q64.find({name: "Queen"})
# { "_id" : ObjectId("59b8748f0865b5136d57c1e7"), "tags" : [ { "value" : "kamen rider w", "count" : 1 }, { "value" : ...
# { "_id" : ObjectId("59b874900865b5136d588893"), "sort_name" : "Queen", "ended" : true, "id" : 192, "aliases" : [ { ...
# { "_id" : ObjectId("59b874910865b5136d5a42eb"), "name" : "Queen", "id" : 992994, "ended" : true, "gid" : "5eecaf18-...

# # q66
# > db.q64.count({area: "Japan"})
# 22821

# # q67
# > db.q64.find({"aliases.name": "女王"})
# { "_id" : ObjectId("59b874900865b5136d588893"), "sort_name" : "Queen", "ended" : true, "id" : 192, "aliases" : [ { ...

# # q68
# > db.q64.find({"tags.value": "dance"}).sort({"rating.count":-1}).limit(10)
# { "_id" : ObjectId("59b874910865b5136d599be4"), "gender" : "Female", "sort_name" : "Madonna", "ended" : true, "type...
# { "_id" : ObjectId("59b874900865b5136d58c56e"), "gender" : "Female", "sort_name" : "Björk", "ended" : true, "aliase...
# { "_id" : ObjectId("59b874920865b5136d5bf8af"), "sort_name" : "Prodigy, The", "ended" : true, "id" : 44954, "aliase...
# { "_id" : ObjectId("59b874930865b5136d5c2258"), "gender" : "Female", "sort_name" : "Rihanna", "ended" : true, "alia...
# { "_id" : ObjectId("59b8748a0865b5136d50b87c"), "gender" : "Female", "sort_name" : "Spears, Britney", "ended" : tru...
# { "_id" : ObjectId("59b874930865b5136d5c2a85"), "sort_name" : "Maroon 5", "ended" : true, "id" : 66179, "aliases" :...
# { "_id" : ObjectId("59b8748d0865b5136d548e19"), "gender" : "Male", "sort_name" : "Lambert, Adam", "ended" : true, "...
# { "_id" : ObjectId("59b8748f0865b5136d57f713"), "gender" : "Male", "sort_name" : "Fatboy Slim", "ended" : true, "al...
# { "_id" : ObjectId("59b874910865b5136d594259"), "sort_name" : "Basement Jaxx", "ended" : true, "id" : 1060, "aliase...
# { "_id" : ObjectId("59b874910865b5136d591038"), "sort_name" : "Cornershop", "ended" : true, "id" : 798, "aliases" :...


import pymongo
from pprint import pprint

if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.knock100_2017
    co = db.q64

    print("\nq65")
    for e in co.find({'name': 'Queen'}):
        pprint(e)

    print("\nq66")
    print(co.find({"area": "Japan"}).count())

    print("\nq67")
    for e in co.find({"aliases.name": "女王"}):
        pprint(e)

    print("\nq68")
    for e in co.find({"tags.value": "dance"}).sort("rating.count", pymongo.DESCENDING).limit(10):
        pprint(e)
