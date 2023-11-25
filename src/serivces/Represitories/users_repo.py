from src.schemas.all_schemas import BaseUser
from src.serivces.Represitories.Base_repo import MongoRepo

from src.db.db import database


class OrderRepo(MongoRepo):
    def __init__(self,db = database ):
        super().__init__(db.users, BaseUser)
