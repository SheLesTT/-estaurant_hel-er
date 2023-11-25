from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status


from src.schemas.menu_items import BaseMenuItem
from src.serivces.task_service import MenuItemService
from src.api.dependensies import menu_item_service


router = APIRouter(
    prefix='/menuitems',
    tags=["Posts"]
)


@router.get("/")
async def get_menu_items(
        item_service: Annotated[MenuItemService, Depends(menu_item_service)]
):
    menu_items = await item_service.get_all_items()
    return menu_items

@router.get("/{id}")
async def get_menu_items(id: str, item_service: Annotated[MenuItemService, Depends(menu_item_service)]):
    menu_item = await item_service.get_one_item(id)
    return menu_item

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_menu_item(
        menu_item: BaseMenuItem,
        item_service: Annotated[MenuItemService, Depends(menu_item_service)]
        ):
        menu_item_id = await item_service.add_item(menu_item)
        return menu_item_id