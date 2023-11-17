import uuid
from typing import Optional

from pydantic import BaseModel, Field


def str_uuid_factory():
    return str(uuid.uuid4())

class BaseMenuItem(BaseModel):
    id : Optional[str] = Field(default_factory= str_uuid_factory, alias='_id' )
    name: str = Field(...)
    price: float= Field(...)

    class Config:
        populate_by_name = True

class MenuItemWithPicture(BaseMenuItem):
    picture: str

class FoodItem(BaseMenuItem):
    ingredients: list[str]
class DrinkItem(BaseMenuItem):
    pass


