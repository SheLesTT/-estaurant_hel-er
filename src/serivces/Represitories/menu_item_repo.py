from src.schemas.menu_items import BaseMenuItem
from src.serivces.Represitories.Base_protocol import MongoRepo
from src.db.db import database

class MenuItemRepo(MongoRepo):
    def __init__(self, db = database):
        super().__init__(db.recipes, BaseMenuItem)





# print(asyncio.run(mg.get_one_item("258c2eb9-3424-48be-8112-b7a8af688dfd")))
