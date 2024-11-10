import jointure2json
import redis  # type: ignore
import json  # Assurez-vous d'importer le module json

# Connexion à Redis
r = redis.Redis(
    host='redis-14277.c56.east-us.azure.redns.redis-cloud.com',
    port=14277,
    password='5f4BL5tx413OrZkZgPg5HyaNi796nGS3'
)

# Lire les fichiers JSON
d1 = jointure2json.read_json_file('employes_data.json')
d2 = jointure2json.read_json_file('departement.json')

# Effectuer la jointure
resultat_jointure = jointure2json.jointure(d1, d2)  # `resultat_jointure` est une chaîne JSON

# Convertir la chaîne JSON en dictionnaire
resultat_dict = json.loads(resultat_jointure)  # Transforme la chaîne en dictionnaire

# Pour chaque clé dans le dictionnaire résultat, utilisez hset pour stocker les données dans Redis
for key, value in resultat_dict['resultat'].items():
    # Vérifier les types de valeurs et les convertir si nécessaire
    for sub_key, sub_value in value.items():
        if isinstance(sub_value, (dict, list)):
            value[sub_key] = json.dumps(sub_value)  # Convertir en JSON si c'est un dict ou une liste

    r.hset(key, mapping=value)  # Utiliser hset pour stocker des champs sous une clé

print("Données importées avec succès dans Redis.")
