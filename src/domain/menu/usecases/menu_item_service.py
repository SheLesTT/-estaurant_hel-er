import json
import time
from typing import Mapping

from src.presentation.handlers.utils import parse_request_parameters_into_mongo_filter
from src.domain.menu.dto.all_schemas import BaseMenuItem

from src.infrastructure.db.Represitories.menu_item import MenuItemRepo
from src.domain.menu.exceptions.menu_item import MenuItemNotExists


class MenuItemService():
    def __init__(self,uow, cache):
        self.uow = uow
        self.cache = cache
        self.uow.set_collection("menu_items")
        self.uow.set_repo(MenuItemRepo)

    async  def add_item(self, data: BaseMenuItem) -> str:
        async with self.uow.session.start_transaction():
            created_item = await self.uow.repo.create_item(data,)

            await self.cache.delete("menu_items")
            await self.cache.set(created_item.id, json.dumps(created_item.model_dump()), expire_at=360)
            return created_item.id


    async  def get_all_items(self, filters: Mapping ) -> list[BaseMenuItem]:
        filters = parse_request_parameters_into_mongo_filter(filters)
        list_of_items = await self.cache.get("menu_items")
        if list_of_items:
            print(list_of_items, "from cache")
            return [BaseMenuItem(**item) for item in json.loads(list_of_items)]
        async with self.uow.session.start_transaction():
            list_of_items = await self.uow.repo.get_all_items(filters)

            await self.cache.set("menu_items", json.dumps([item.model_dump() for item in list_of_items], ),expire_at=360)
            time.sleep(2)
            return list_of_items

    async def get_one_item(self, id: str) -> BaseMenuItem:

        item_cache = await self.cache.get(id)
        if item_cache:
            return BaseMenuItem(**json.loads(item_cache))
        time.sleep(2)
        async with self.uow.session.start_transaction():
            item = await self.uow.repo.get_one_item(id)
            if not item:
                raise MenuItemNotExists
            return item

