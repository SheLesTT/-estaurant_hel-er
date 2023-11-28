import  pytest


@pytest.mark.asyncio
async  def test_add_menu_item(add_menu_item, menu_item_data):
    db = await add_menu_item_to_db
    data = menu_item_data
    res =  await db.menu_items.find_one({"name": "carbonara"})
    assert res["menu_section"] == "main"
    assert res["price"]== 300