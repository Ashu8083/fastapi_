from fastapi import Depends

from app.db.database import get_db
from app.repo.restaurant_repo import RestaurantRepo
from app.service.resturant_service import ResturentService
from app.repo.food_repo import FoodRepository
from app.service.food_service import FoodService


def get_restaurant_service(db =Depends(get_db)):
    restaurant_repository = RestaurantRepo(db)
    restaurant_service = ResturentService(restaurant_repository)
    return restaurant_service

def get_food_service(db =Depends(get_db)):
    food_repository = FoodRepository(db)
    food_service = FoodService(food_repository)
    return food_service