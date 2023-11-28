
import asyncio

import mongomock_motor
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config.settings import settings



uri = f"mongodb://{settings.user_name}:{settings.password}@{settings.host_name}"

client = AsyncIOMotorClient("mongodb://localhost:27017", settings.port, server_api=ServerApi('1'), )
    # Send a ping to confirm a successful connection


database = client.restourant

def db_provider(client):
    yield client["restourant"]


def get_db():
    raise NotImplementedError



class DB_provider():
    def __init__(self, uri, port, database_name):
        self.uri = uri
        self.port = port
        self.database_name = database_name
        self.client=  AsyncIOMotorClient(self.uri, self.port, server_api=ServerApi('1'))
    async def provide_db(self):

        return self.client[self.database_name]


async def get_session(client):
    print("get session")
    async with await client.start_session() as session:

        yield session
        print("end session")

# AsyncMongoSession.Test = True
# a = AsyncMongoSession()
# a.print_me()