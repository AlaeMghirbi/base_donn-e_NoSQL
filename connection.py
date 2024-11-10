import redis
from redisbloom.client import Client
rb = Client(host='localhost', port=6379)

rb.bfAdd('myBloom', 'element1')
rb.bfAdd('myBloom', 'element2')

# Vérifier si un élément est présent dans le filtre
exists = rb.bfExists('myBloom', 'element1')  # True
not_exists = rb.bfExists('myBloom', 'element3')  # False

print(f'element1 exists: {exists}')
print(f'element3 exists: {not_exists}')