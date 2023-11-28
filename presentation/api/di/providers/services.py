from fastapi import Depends

from presentation.api.di.providers.Cashe_provider import get_cache
from src.db.db import get_db
from src.serivces.menu_item_service import MenuItemService


def get_menu_item_service(uow=Depends( get_db),cache =  Depends(get_cache)) -> MenuItemService:
    return MenuItemService(uow, cache)