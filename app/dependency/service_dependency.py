from fastapi import Depends

from app.db.database import get_db
from app.repo.restaurant_repo import RestaurantRepo
from app.service.resturant_service import ResturentService

def get_restaurant_service(db =Depends(get_db)):
    restaurant_repository = RestaurantRepo(db)
    restaurant_service = ResturentService(restaurant_repository)
    return restaurant_service
