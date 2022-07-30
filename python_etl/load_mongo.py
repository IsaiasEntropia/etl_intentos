import pymongo
#mongod

from pymongo import MongoClient
client = MongoClient()

#print(client)

db = client.test_database
db = client['test-database']
#print(db)


# Treaer una colecciòn
collection = db.test_collection
collection = db['test-collection']
print(collection)