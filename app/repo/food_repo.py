from app.model.food_model import Food
from sqlalchemy.orm import Session
from app.schema.food_schema import CreateFood


class FoodRepository:

    def __init__(self,db_session: Session):
        self.db_session = db_session

    def create_food_repo(self,create_food : CreateFood,resturent_id : int ):
        food = Food(
            name=create_food.name,
            price=create_food.price,
            food_type=create_food.category,
            restaurant_id=resturent_id
        )
        try:
            self.db_session.add(food)
            self.db_session.commit()
            self.db_session.refresh(food)
            return food
        except Exception as e:
            self.db_session.rollback()
            raise ValueError("Internal Error")

    def get_food_by_restaurant_id(self, restaurant_id: int):
        food_items = self.db_session.query(Food).filter(Food.restaurant_id == restaurant_id).all()
        return food_items
    def get_food_by_name(self, food_name: str):
        food = self.db_session.query(Food).filter(Food.name == food_name).first()
        return food
