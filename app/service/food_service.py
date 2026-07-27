from sqlalchemy.orm import Session

from app.repo.food_repo import food_repo
from app.model.food_model import Food

class FoodService:
    # You can pass a database session here if needed
    def create_food(self, name: str, price: int, db: Session):
        food = Food(name=name, price=price)
        return food_repo.create_food(food, db_session=db)
   



food_service = FoodService()