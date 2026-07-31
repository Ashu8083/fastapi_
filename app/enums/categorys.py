from enum import Enum


class CategoryEnum(str, Enum):
    APPETIZER = "Appetizer"
    MAIN_COURSE = "Main Course"
    DESSERT = "Dessert"
    BEVERAGE = "Beverage"