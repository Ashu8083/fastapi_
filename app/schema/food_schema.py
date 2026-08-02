from pydantic import BaseModel
from app.enums.food_type import FOODTYPE


class CreateFood(BaseModel):
    name: str
    price: int
    category: FOODTYPE
    