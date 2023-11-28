import  pytest



@pytest.mark.asyncio
async def test_post_menu_item(client, menu_item_data):
    async for client in client:
        menu_item = menu_item_data[0]
        responce = await  client.post("/menuitems/", json=menu_item)
        assert responce.status_code == 201
        id_created = responce.json()

        res_get  =  await  client.get(f"/menuitems/{id_created}")
        created_item = res_get.json()

        assert created_item["name"] == menu_item["name"]
        assert created_item["price"] == menu_item["price"]


@pytest.mark.asyncio
async def test_get_all_menu_item(add_menu_item_to_db,client,  menu_item_data):
    menu_items = menu_item_data
    async for _ in add_menu_item_to_db:
        async for  client in  client:

            res =  await  client.get("/menuitems/")
            res_data = res.json()


            assert res.status_code == 200
            assert len(res_data) == 2
            assert res_data[0]["name"] == menu_items[0]["name"]
            assert res_data[0]["price"] == menu_items[0]["price"]
