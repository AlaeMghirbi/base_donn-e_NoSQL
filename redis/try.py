import redis # type: ignore

client = redis.Redis(
  host='redis-14277.c56.east-us.azure.redns.redis-cloud.com',
  port=14277,
  password='5f4BL5tx413OrZkZgPg5HyaNi796nGS3')

# Création d'une clé
client.set('nom', 'Alae')

# Récupération de la valeur
nom = client.get('nom').decode('utf-8')
print("Nom :", nom)

#definition d'une clé temporaire 
client.setex('clé_60_sec', 60, 'temporaire')  # Expire après 60 secondes

#verifier l'existance d'une clé
existe = client.exists('nom')
print("La clé 'ma_cle' existe :", bool(existe))

# Manipulation des listes 
#Ajout d'éléments dans une liste
client.rpush('BUT3', 'alae', 'karim', 'emna')

# Récupérer toute la liste
BUT3 = client.lrange('BUT3', 0, -1)
BUT3 = [item.decode('utf-8') for item in BUT3]#j'ai ajouter cela pour telérer les lettres spéciaux
print("Liste :", BUT3)

# Manipulation des ensembles 
client.sadd('tunis', 'alae', 'rania')  # Ajoute des éléments à l'ensemble
print(r.smembers('tunis'))  # Renvoie tous les éléments de l'ensemble
client.srem('tunis', 'alae')  # Supprime "element1" de l'ensemble

#verification d'un element dans un ensemble : 
est_membre = client.sismember('tunis', 'alae')
print("Est-ce que 'alae' est dans tunis ?", est_membre)

#les ensemble triés
#Ajouter des éléments avec un score
client.zadd('classement', {'alae': 150, 'emna': 200})

#Récupérer les éléments triés par score (ordre croissant)
classement = client.zrange('classement', 0, -1, withscores=True)
classement = [(item[0].decode('utf-8'), item[1]) for item in classement]
print("Classement :", classement)

#Récupérer les éléments triés par score (ordre décroissant)
classement_desc = client.zrevrange('classement', 0, -1, withscores=True)
classement_desc = [(item[0].decode('utf-8'), item[1]) for item in classement_desc]
print("Classement (décroissant) :", classement_desc)


# les compteurs: incrementation et decrementation 
# Incrémenter un compteur
client.set('compteur', 0)
client.incr('compteur')
compteur_valeur = client.get('compteur').decode('utf-8')
print("Valeur après incrémentation :", compteur_valeur)

# Décrémenter un compteur
client.decr('compteur')
compteur_valeur = client.get('compteur').decode('utf-8')
print("Valeur après décrémentation :", compteur_valeur)