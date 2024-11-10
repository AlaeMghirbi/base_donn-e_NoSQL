import csv
import json
from json import dumps, loads
from ast import literal_eval

def csv_to_json_complex(csv_file):
    """
    Convertit un fichier CSV en un dictionnaire JSON-like, tout en gérant les types de données complexes (JSON, listes).
    """
    data_dict = {}
    
    with open(csv_file, encoding='utf-8') as csvfile:
        my_reader = csv.DictReader(csvfile)
        for my_row in my_reader:
            my_dict = {}
            
            for key, value in my_row.items():
                # Vérifier et convertir les valeurs complexes (JSON ou liste)
                try:
                    if str(value).startswith('{') and str(value).endswith('}'):
                        my_dict[key] = literal_eval(value)  # Transformer en dictionnaire
                    elif str(value).startswith('[') and str(value).endswith(']'):
                        my_dict[key] = literal_eval(value)  # Transformer en liste
                    else:
                        my_dict[key] = int(value) if value.isdigit() else value  # Entier ou chaîne de caractères
                except (ValueError, SyntaxError):
                    my_dict[key] = value  # Par défaut, considérer comme une chaîne de caractères
            
            # Ajouter la ligne transformée au dictionnaire final
            data_dict[my_row['id']] = my_dict
    
    # Retourner le dictionnaire sous forme de chaîne JSON
    return dumps({"test": data_dict})

def jointure(mc,id1,id2):

    print(type(mc),id1,id2)
    doc1 = mc.find({'_id':id1})
    doc2 = mc.find({'_id':id2})
    
    # Second, iterate through dictionaries
    d_res = {}
    for d1 in doc1:
        d11 = list(d1.keys())
        res1 = d1
        #print('==',d11,'==')
    for d2 in doc2:
        d22 = list(d2.keys())
        res2 = d2
        #print('==',d22,'==')
    for d_111 in d11:
       for d_222 in d22:
           if d_111 != '_id' and d_222 != '_id': 
               if d_111 == d_222:
                   d = {}
                   d.update(res1[d_111])
                   d.update(res2[d_222])
                   #print(d)
                   d_res[d_111] = d
                   #print("**",d_111,d_222,"**")
                   
    my_my_dict = {}
    my_my_dict['ids'] = d_res
    z = dumps(my_my_dict)

    # Save the join in the collection
    mc.insert_one(my_my_dict)

    return z

if __name__ == "__main__":
    from pymongo import MongoClient
    from pymongo.server_api import ServerApi
    # Connexion à MongoDB
    uri = "mongodb+srv://alaemghirbi:alaemghirbi@alae.8wk9s.mongodb.net/?retryWrites=true&w=majority&appName=alae"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['ma_base_de_donnees_complexe']
    mycol = db['ma_collection_complexe']
    # Convertir les CSV complexes en JSON
    json_one = csv_to_json_complex("C:/Users/alaem/OneDrive/Bureau/3BUT/BDD/mongoDB/csv1.csv")
    json_two = csv_to_json_complex("C:/Users/alaem/OneDrive/Bureau/3BUT/BDD/mongoDB/csv2.csv")
    # Convertir les JSON en dictionnaires Python
    d1_name = list(loads(json_one))[0]
    d2_name = list(loads(json_two))[0]
    d1 = loads(json_one)[d1_name]
    d2 = loads(json_two)[d2_name]
    # Insérer dans MongoDB
    post_id_one = mycol.insert_one(d1).inserted_id
    post_id_two = mycol.insert_one(d2).inserted_id
    # Effectuer la jointure entre les deux documents
    jointure_result = jointure(mycol, post_id_one, post_id_two)
    # Afficher les documents fusionnés après la jointure
    from pprint import pprint
    cursor = mycol.find({})
    for document in cursor: 
        pprint(document)
    


