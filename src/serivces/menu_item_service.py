from typing import Mapping

from src.api.exceptions import MenuItemNotFound
from src.api.utils import parse_request_parameters_into_mongo_filter
from src.schemas.all_schemas import BaseMenuItem
from src.serivces.Represitories.Base_repo import AbstractRepo
from src.serivces.Represitories.menu_item_repo import MenuItemRepo
from src.serivces.exceptions import MenuItemNotExists


class MenuItemService():
    def __init__(self,uow ):
        self.uow = uow

    async  def add_item(self, data: BaseMenuItem) -> str:

        created_item_id  = await  self.task_repo.create_item(data)
        return  created_item_id

    async  def get_all_items(self, filters: Mapping ) -> list[BaseMenuItem]:
        filters = parse_request_parameters_into_mongo_filter(filters)
        list_of_items = await self.task_repo.get_all_items(filters)
        return list_of_items

    async def get_one_item(self, id: str) -> BaseMenuItem:

        item = await self.task_repo.get_one_item(id)
        if not item:
            raise MenuItemNotExists
        return item

