import asyncio
from abc import ABC, abstractmethod
from typing import Protocol, Type, Mapping

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel




class AbstractRepo(ABC):
    @abstractmethod
    def get_one_item(self, id: int) -> BaseModel:
        pass
    @abstractmethod
    def get_all_items(self, filters: Mapping) -> list[BaseModel]:
        pass
    @abstractmethod
    def create_item(self, item: BaseModel) -> str:
        pass

class MongoRepo(AbstractRepo):
    def __init__(self, collection, schema: Type[BaseModel]):
        self.collection = collection
        self.schema = schema
        self.session = None


    async def get_one_item(self,id: str) -> BaseModel:
        result = await self.collection.find_one({"_id": id}, session=self.session)
        if not result:
            return None
        return self.schema(**result)

    async def get_all_items(self, filters: Mapping) -> list[BaseModel]:
        cursor = self.collection.find(filters, session=self.session)
        items = await cursor.to_list(length=100)
        # print(items)
        return [self.schema(**item) for item in items]

    async def create_item(self, data: BaseModel) -> str:

            data= jsonable_encoder(data)
            result = await self.collection.insert_one(data, session=self.session)
            return result.inserted_id



