from src.domain.common.exceptions.base import AppException


class MenuItemException(AppException):
    """ Base menu item exception """

class MenuItemNotExists(MenuItemException):
    pass

class MenuItemAlreadyExists(MenuItemException):
    pass