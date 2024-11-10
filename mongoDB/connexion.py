from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
def connexion():
    uri = "mongodb+srv://alaemghirbi:alaemghirbi@alae.8wk9s.mongodb.net/?retryWrites=true&w=majority&appName=alae"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return(client)
# Sélectionner une base de données
client=connexion()
db = client['ma_base_de_donnees']

# Sélectionner ou créer une collection
collection = db['ma_collection']

document = { "nom": "Jean", "age": 30, "ville": "Paris" }
result = collection.insert_one(document)
'''
documents=[
    {"nom": "Alae", "age": 21 , "ville":"Nabeul"},
    {"nom": "Rania", "age": 21 , "ville":"Tunis"},
    {"nom": "Emna", "age": 21 , "ville":"BenArous"},
    {"nom": "Karim", "age": 21 , "ville":"HammemLinf"}
]
result = collection.insert_many(documents)
for doc in collection.find():
    print(doc)
'''