import redis # type: ignore

r = redis.Redis(
  host='redis-14277.c56.east-us.azure.redns.redis-cloud.com',
  port=14277,
  password='5f4BL5tx413OrZkZgPg5HyaNi796nGS3')
pipe = r.pipeline()
pipe.set('pip1', 5)
pipe.set('pip2', 18.5)
pipe.set('pip3', "hello world!")

print(pipe.execute())