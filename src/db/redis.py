from redis.asyncio import Redis

from src.db.ICashe import ICache

class RedisRepository(ICache):
    def __init__(self, redis: Redis):
        self._redis = redis

    async def get(self, key: str) -> str:
        return self._redis.get(key)

    async def set(self, key: str, value: str, expire_at: int | None = None) -> str:
        if expire_at:
            return self._redis.set(key, value, ex=expire_at)
        return self._redis.set(key, value)

    async def delete(self, key: str) -> str:
        return self._redis.delete(key)