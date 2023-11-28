from src.schemas.all_schemas import BaseMenuItem
from src.serivces.Represitories.Base_repo import MongoRepo

class MenuItemRepo(MongoRepo):
    def __init__(self, collection,session):
        super().__init__(collection, BaseMenuItem, session)





# print(asyncio.run(mg.get_one_item("258c2eb9-3424-48be-8112-b7a8af688dfd")))
