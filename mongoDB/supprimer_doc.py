import connexion
client=connexion.connexion()
db=client['ma_base_de_donnees']
db=client['Data_sample']
collection=db['ma_collection']
collection.delete_one({'nom':'Jean'})

#Supprimer plusieurs documents:
collection.delete_many({'age':28})
print(collection.find())
