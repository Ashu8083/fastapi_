from app.model.food_model import Food, Users
from sqlalchemy.orm import Session


class FoodRepository:
    def create_food(self, food: Food, db_session: Session):
        db_session.add(food)
        db_session.commit()
        db_session.refresh(food)
        return food

    def get_food_by_id(self, food_id: int, db_session: Session):
        return db_session.query(Food).filter(Food.id == food_id).first()
    