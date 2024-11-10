import csv
import json
from json import dump

def csv_to_json(csv_file , json_file):
    data_dict = {}
    with open(csv_file, encoding='latin1') as csvfile:
        my_reader = csv.DictReader(csvfile, delimiter=';')
        for row in my_reader:
            data_dict[row['Nom']] = row

# Convertir les deux fichiers CSV en JSON
    result_dict = {str(json_file[:-4]): data_dict}

    # Enregistrer le résultat dans un fichier JSON
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        dump(result_dict, jsonfile, ensure_ascii=False, indent=4)

    print(f"Data successfully written to {json_file}")


csv_to_json("departement.csv", "departement.json")
csv_to_json("employes_data.csv", "employes_data.json")

