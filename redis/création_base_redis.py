import redis

# Connexion au serveur Redis
r = redis.Redis(
    host='redis-14277.c56.east-us.azure.redns.redis-cloud.com',
    port=14277,
    password='5f4BL5tx413OrZkZgPg5HyaNi796nGS3'
)

# Dictionnaire contenant les informations de chaque employé
employes = {
    "Alae": {"age": 21, "departement": "Informatique", "performance": 85, "date_embauche": "2023-02-15"},
    "Rania": {"age": 28, "departement": "Ressources Humaines", "performance": 92, "date_embauche": "2021-06-20"},
    "Karim": {"age": 32, "departement": "Finance", "performance": 78, "date_embauche": "2019-10-01"},
    "Emna": {"age": 25, "departement": "Marketing", "performance": 88, "date_embauche": "2022-03-12"},
    "Yassine": {"age": 30, "departement": "Ventes", "performance": 80, "date_embauche": "2020-07-05"},
    "Hanen": {"age": 26, "departement": "Logistique", "performance": 76, "date_embauche": "2018-11-23"},
}

# Ajout des informations de chaque employé dans Redis
for nom, info in employes.items():
    # Enregistrement des informations de l'employé sous forme de hash dans Redis
    r.hset(nom, mapping=info)
