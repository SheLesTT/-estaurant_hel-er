import asyncio

from src.schemas.menu_items import BaseMenuItem
from src.serivces.Base_protocol import MongoRepo

class RecipesRepo(MongoRepo):
    def __init__(self):
        super().__init__("recipes", BaseMenuItem)

mg=  RecipesRepo()
asyncio.run(mg.get_all_items())



# print(asyncio.run(mg.get_one_item("258c2eb9-3424-48be-8112-b7a8af688dfd")))
