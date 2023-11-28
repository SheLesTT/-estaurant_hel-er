import asyncio
from abc import ABC, abstractmethod
from typing import Protocol, Type, Mapping

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel




class AbstractRepo(ABC):
    @abstractmethod
    async def get_one_item(self, id: str) -> BaseModel | None:
        pass
    @abstractmethod
    async  def get_all_items(self, filters: Mapping) -> list[BaseModel] | None:
        pass
    @abstractmethod
    async def create_item(self, item: BaseModel) -> BaseModel:
        pass

class MongoRepo(AbstractRepo):
    def __init__(self, collection, schema: Type[BaseModel], session=None):
        self.collection = collection
        self.schema = schema
        self.session = session


    async def get_one_item(self,id: str) -> BaseModel | None:
        result = await self.collection.find_one({"_id": id}, session=self.session)
        if not result:
            return None
        return self.schema(**result)

    async def get_all_items(self, filters: Mapping) -> list[BaseModel] | None:
        cursor = self.collection.find(filters, session=self.session)
        items = await cursor.to_list(length=100)
        # print(items)
        return [self.schema(**item) for item in items]

    async def create_item(self, data: BaseModel) -> BaseModel:

            data= jsonable_encoder(data)

            created_id = await self.collection.insert_one(data, session=self.session)
            result = await self.collection.find_one({"_id": created_id.inserted_id}, session=self.session)
            result = self.schema(**result)
            return result



