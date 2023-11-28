from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.api import  menu_items_router
from src.db.db import  DB_provider, get_db
from src.config.settings import settings
from src.serivces.menu_item_service import MenuItemService


def setup_di(app: FastAPI, database_url: str, database_port:str, db_name:str)-> None:
    db_provider = DB_provider(database_url, database_port, db_name)

    app.dependency_overrides[get_db] = db_provider.provide_db
def build_app():
    app = FastAPI()

    setup_di(app, settings.database_url, settings.port, settings.db_name)
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

app = build_app()
