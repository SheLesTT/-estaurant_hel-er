
class AppException(Exception):
    pass

class MenuItemException(AppException):
    """ Base menu item exception """

class MenuItemNotExists(MenuItemException):
    pass

class MenuItemAlreadyExists(MenuItemException):
    pass