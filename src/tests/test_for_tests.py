import  pytest_asyncio
import pytest
import asyncio

@pytest.mark.asyncio
async def test_get_data(add_menu_item_to_db):
    db = await add_menu_item_to_db
    async  for document in db.menu_items.find({}):

@pytest.mark.asyncio
async def test_get_data(client, add_menu_item_to_db):
    await add_menu_item_to_db
    client = await client
    responce =   client.get("/menuitems/")
    assert responce.status_code == 200


