import asyncio
from abc import ABC, abstractmethod
from typing import Protocol, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from src.db.db import  database
from src.schemas.all_schemas import BaseMenuItem


class AbstractRepo(ABC):
    @abstractmethod
    def get_one_item(self, id: int) -> BaseModel:
        pass
    @abstractmethod
    def get_all_items(self) -> list[BaseModel]:
        pass
    @abstractmethod
    def create_item(self, item: BaseModel) -> str:
        pass

class MongoRepo(AbstractRepo):
    def __init__(self, collection, schema: Type[BaseModel]):
        self.collection = collection
        self.schema = schema


    async def get_one_item(self,id: str) -> BaseModel:
        result = await self.collection.find_one({"_id": id})
        print("i had result", result)
        return self.schema(**result)

    async def get_all_items(self, **filters) -> list[BaseModel]:
        cursor = self.collection.find(filters)
        items = await cursor.to_list(length=100)
        # print(items)
        return [self.schema(**item) for item in items]

    async def create_item(self, data: BaseModel) -> str:

            data= jsonable_encoder(data)
            result = await self.collection.insert_one(data)
            return result.inserted_id



