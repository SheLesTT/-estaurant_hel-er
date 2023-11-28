import datetime
import uuid
from typing import Optional, Any, Literal

from pydantic import BaseModel, Field


def str_uuid_factory():
    return str(uuid.uuid4())

class BaseMenuItem(BaseModel):
    # id : Optional[str] = Field(default_factory= str_uuid_factory, alias='_id' )
    id: Any = Field(default_factory= str_uuid_factory, alias='_id')
    name: str = Field(...)
    price: float= Field(...)
    menu_section: Literal['main','salat','soup', 'dessert', 'alcohol_drink','drink']

    class Config:
        populate_by_name = True

class BaseUser(BaseModel):
    id: Any = Field(default_factory= str_uuid_factory, alias='_id')
    name: str = Field(...)
    surname: str = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True

class BaseOrder(BaseModel):
    id: Any = Field(default_factory= str_uuid_factory, alias='_id')
    create_dt: datetime.datetime
    ordered_dishes: list[str]
    waiter: str

    class Config:
        populate_by_name = True
class MenuItemWithPicture(BaseMenuItem):
    picture: str

class FoodItem(BaseMenuItem):
    ingredients: list[str]
class DrinkItem(BaseMenuItem):
    pass



