import redis
from redis.cache import CacheConfig

r = redis.Redis(
    host='redis-14277.c56.east-us.azure.redns.redis-cloud.com',
    port=14277,
    password='5f4BL5tx413OrZkZgPg5HyaNi796nGS3',
    protocol=3,
    cache_config=CacheConfig(),
    decode_responses=True
)
r.set('alae','mghirbi')

cityNameAttempt1 = r.get("alae")    # Retrieved from Redis server and cached
cityNameAttempt2 = r.get("alae")    # Retrieved from cache