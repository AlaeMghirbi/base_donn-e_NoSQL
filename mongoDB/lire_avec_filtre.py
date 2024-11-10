import connexion
client=connexion.connexion()
db=client['ma_base_de_donnees']
collection=db['ma_collection']
for doc in collection.find({'age':{"$gt": 22 }}):
    print(doc)