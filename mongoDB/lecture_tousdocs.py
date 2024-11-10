from diskcache import Cache
import connexion
client=connexion.connexion()
db=client['ma_base_de_donnees']
collection = db['ma_collection']
cache = Cache('cache_dir')  # Répertoire pour stocker le cache sur le disque
@cache.memoize()
def get_donnees():
    return db.collection.find_one()

# Utilisation de la fonction
result = get_donnees()