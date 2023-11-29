from fastapi import Depends

from src.presentation.api.di.providers.cache import get_cache
from src.infrastructure.db.db import get_db
from src.domain.menu.usecases.menu_item_service import MenuItemService


def get_menu_item_service(uow=Depends( get_db),cache =  Depends(get_cache)) -> MenuItemService:
    return MenuItemService(uow, cache)