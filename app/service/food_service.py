from sqlalchemy.orm import Session

from app.repo.food_repo import FoodRepository
from app.model.food_model import Food

class FoodService:
    def __init__(self,foodRepository: FoodRepository):
       self.food_repo : FoodRepository = foodRepository

    def create_food(self, create_food, restaurant_id: int):
        return self.food_repo.create_food_repo(create_food, restaurant_id, )
    def get_food_by_restaurant_id(self, restaurant_id: int):
        return self.food_repo.get_food_by_restaurant_id(restaurant_id)
    
   



