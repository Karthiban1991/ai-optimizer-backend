import redis

r = redis.Redis(host="redis", port=6379)

def set_cache(key, value):
    r.set(key, value)

def get_cache(key):
    return r.get(key)
