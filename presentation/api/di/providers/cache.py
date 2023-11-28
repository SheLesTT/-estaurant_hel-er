from src.db.redis import RedisRepository


def get_cache() -> None:
    raise NotImplementedError

class CacheProvider:
    def __init__(self, redis):
        self._redis = redis

    def provide_cache(self):
        return RedisRepository(self._redis)