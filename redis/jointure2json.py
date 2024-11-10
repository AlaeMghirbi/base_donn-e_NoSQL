import json

def jointure(json1, json2):
    # Pas besoin de transformer en dictionnaires car json1 et json2 sont deja des dictionnaires

    # Utiliser les noms des clés du premier JSON
    d1_name = list(json1.keys())[0]  # On prend le nom de la première clé dans json1
    d2_name = list(json2.keys())[0]  # On prend le nom de la première clé dans json2

    d1 = json1[d1_name]
    d2 = json2[d2_name]

    # Dictionnaire pour stocker le resultat de la jointure
    d_res = {}
    
    # Deux boucles imbrquée pour faire la jointure
    for key1, val1 in d1.items():
        for key2, val2 in d2.items():
            if key1 == key2:
                d = {}
                d.update(val1)  # Mettre a jur avec les valeurs de val1
                d.update(val2)  # Mettre à jour avec les valeurs de val2
                d_res[key1] = d  # Ajouter le resultat dns d_res

    my_my_dict = {}
    my_my_dict['resultat'] = d_res  # Renommer la clé comme "resultat"
    z = json.dumps(my_my_dict)  # Convertir le dictionnaire final en JSON

    return z

# fonction pour ouvrir et lire un fichier JSON
def read_json_file(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Charger le contenu JSON dans une variable Python
    return data

# Main 
if __name__ == "__main__":
    d1 = read_json_file('employes_data.json')
    d2 = read_json_file('departement.json')
    d = jointure(d1, d2)  # Passer les dictionnaires directement
    print(d)
