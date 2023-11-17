
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config.settings import settings



uri = f"mongodb://{settings.user_name}:{settings.password}@{settings.host_name}"


client = AsyncIOMotorClient("mongodb://localhost:27017", settings.port, server_api=ServerApi('1'), )

    # Send a ping to confirm a successful connection


database = client.restourant