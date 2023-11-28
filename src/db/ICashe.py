from typing import Protocol


class ICache(Protocol):
    async def get(self,value: str) -> str:
        ...
    async def set(self,key:str, value: str, expire_at: int | None = None) -> str:
        ...
    async def delete(self, key: str) -> str:
        ...
