from typing import AsyncGenerator, Any

import  pytest
import asyncio
from httpx import AsyncClient
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from starlette.middleware.cors import CORSMiddleware

from src.presentation import menu_items_router
from src.settings import settings
from src.infrastructure.db import DB_provider, get_db
from src.domain.menu.dto.all_schemas import BaseMenuItem


def setup_di(app: FastAPI, database_url: str, database_port: str, db_name: str)-> None:
    db_provider = DB_provider(database_url, database_port, db_name)
    app.dependency_overrides[get_db] = db_provider.provide_db
def build_app() -> FastAPI:
    app = FastAPI()

    setup_di(app, settings.database_url, settings.port, settings.test_db_name)
    origins = [
        "http://localhost",
        "http://localhost:8000",]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(menu_items_router.router)
    return app

@pytest.fixture(scope="function")
async def client()-> AsyncGenerator[TestClient, Any]:
    async with AsyncClient(app=build_app(), base_url="http://test") as client:
        yield client


client_db = AsyncIOMotorClient("mongodb://localhost:27017")
db = client_db.test
@pytest.fixture
async def set_db() -> AsyncGenerator[AsyncIOMotorDatabase, Any]:
    yield db
    collections = await  db.list_collection_names()
    for collection in collections:
        db[collection].drop()

@pytest.fixture
def menu_item_data()-> list[dict[str, int, str]]:
    return [{"name": "carbonara", "price": 300,  "menu_section": "main"},
            {"name": "pizza", "price": 500,  "menu_section": "main"}]
@pytest.fixture
async def add_menu_item_to_db(menu_item_data, set_db):
    async  for db in set_db:
        await db.menu_items.drop()
        for menu_item in menu_item_data:
            data = BaseMenuItem(**menu_item)
            await  db.menu_items.insert_one(jsonable_encoder(data))
        yield

@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
