import asyncio

import  pytest

from src.schemas.all_schemas import BaseMenuItem, BaseOrder
from src.serivces.Represitories.menu_item_repo import MenuItemRepo

@pytest.mark.asyncio
async def test_creating_recipe(set_db):
    async for test_db in set_db:

        test_collection = test_db.recipes
        data = BaseMenuItem(**{"name": "test", "price": 100})
        repo = MenuItemRepo(test_db)
        res = await repo.create_item(data)
        assert isinstance(res, str)

@pytest.mark.asyncio
async def test_get_one_recipes( add_recipe):

    test_collection = await add_recipe
    data = BaseMenuItem(**{"name": "test", "price": 100})
    repo = MenuItemRepo()
    id = await repo.create_item(data)

    res = await repo.get_one_item(id)

    assert isinstance(res, BaseMenuItem)
    assert res.name == "test"
    assert res.price == 100

@pytest.mark.asyncio
async def test_get_all_recipes( add_recipe):

    repo = await add_recipe
    res = await repo.get_all_items()
    assert isinstance(res, list)
    assert len(res) == 2
    assert isinstance(res[0], BaseMenuItem)
    assert res[0].name == "test"

@pytest.mark.asyncio
async def test_get_all_orders(orders_repo):
    repo = await  orders_repo
    res = await repo.get_all_items()
    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], BaseOrder)
    assert res[0].waiter == "258c2eb9-3424-48be-8112-b7a8af688dfd"
