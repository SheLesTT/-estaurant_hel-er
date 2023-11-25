from fastapi import Depends

from src.db.db import get_db
from src.serivces.Represitories.orders_repo import OrderRepo
from src.serivces.Represitories.menu_item_repo import MenuItemRepo
from src.serivces.menu_item_service import MenuItemService


def get_menu_item_service(session=Depends(get_db)) -> MenuItemService:
    a
    return MenuItemService(session)