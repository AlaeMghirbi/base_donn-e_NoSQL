import redis
from redis.cache import CacheConfig
r = redis.Redis(host='localhost', port=6379)


# Activer le mode AOF
r.config_set('appendonly', 'yes')

# Définir la stratégie de synchronisation AOF
r.config_set('appendfsync', 'everysec') # Vous pouvez changer en 'always' ou 'no' selon vos besoins

# Vérifier les paramètres
append_only = r.config_get('appendonly')
append_sync = r.config_get('appendfsync')

print(f"AOF activé : {append_only['appendonly']}")
print(f"Stratégie de synchronisation AOF : {append_sync['appendfsync']}")