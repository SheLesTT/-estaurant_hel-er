from redis import Redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from src.presentation.handlers.menu import menu_items
from src.presentation.api.di.providers.cache import get_cache, CacheProvider
from src.ifrastructure.db.db import  DB_provider, get_db
from src.settings import settings


def setup_di(app: FastAPI,cache: Redis, pool: AsyncIOMotorClient, db_name: str):
    db_provider = DB_provider(pool, db_name)
    cache_provider = CacheProvider(cache)
    app.dependency_overrides[get_db] = db_provider.get_session
    app.dependency_overrides[get_cache] = cache_provider.provide_cache

def build_app():
    app = FastAPI()

    pool  =   AsyncIOMotorClient(settings.database_url, settings.port)
    cache = Redis(host=settings.redis_host, port=settings.redis_port,db=settings.redis_database,  decode_responses=True)
    setup_di(app,cache, pool, db_name=settings.db_name)
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

    app.include_router(menu_items.router)
    return app

app = build_app()
