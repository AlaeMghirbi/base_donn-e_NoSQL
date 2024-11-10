import connexion
client=connexion.connexion()
db=client['ma_base_de_donnees']
collection=db['ma_collection']
#collection.update_one({'nom':'Jean'},{'$set':{'age':25}})
#print(collection.find_one({'nom':'Jean'}))
#maj plusieurs cocuments
collection.update_many({'nom':'Alae'},{'$set':{'age':27}})
collection.update_many({'nom':'Rania'},{'$set':{'age':23}})
for doc in collection.find():
    print(doc)
