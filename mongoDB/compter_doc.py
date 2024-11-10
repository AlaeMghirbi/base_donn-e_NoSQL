import connexion
client=connexion.connexion()
db=client['ma_base_de_donnees']
collection=db['ma_collection']

count=collection.count_documents({})
print('le nombre de documents dans la base est ', count )