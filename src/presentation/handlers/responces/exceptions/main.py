from pydantic import Field, BaseModel


class ApiException(BaseModel):
    pass

class MenuItemNotFound(ApiException):
    detail :str = Field("Menu item not found" )