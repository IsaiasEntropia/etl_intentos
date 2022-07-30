from pymongo import MongoClient
#client = MongoClient(*)
#print(client)
db = client.sample_airbnb #Base de datos
pruebas = db.listingsAndReviews # Collection
#pruebas.insert_one(personDocument)
item_details = pruebas.find( {"name": "Ribeira Charming Duplex"}).pretty()

for item in item_details:
    # This does not give a very readable output
    print(item)
#print(pruebas.find_one({ "name.last": "Turing" }))




