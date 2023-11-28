
import asyncio

import mongomock_motor
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config.settings import settings
from src.db.unit_of_work import UnitOfWork

uri = f"mongodb://{settings.user_name}:{settings.password}@{settings.host_name}"

client = AsyncIOMotorClient("mongodb://localhost:27017", settings.port, server_api=ServerApi('1'), )
    # Send a ping to confirm a successful connection


database = client.restourant

def db_provider(client):
    yield 23


def get_db():
    raise NotImplementedError



class DB_provider():
    def __init__(self, pool, db_name):
        self.client=  pool
        self.db_name = db_name
    async def get_session(self):
        async with await self.client.start_session() as session:
            uow = UnitOfWork(session, self.client[self.db_name])
            yield uow

    async def provide_db(self):
        return self.client[self.database_name]



# AsyncMongoSession.Test = True
# a = AsyncMongoSession()
# a.print_me()