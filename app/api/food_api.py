from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from app.dependency.service_dependency import get_food_service
from app.schema.food_schema import CreateFood   
from app.db.database import get_db
from app.core.logger_config import logger


food_router = APIRouter(prefix="/food", tags=["Food"])

@food_router.post("/create-food")
def create_food(create_food: CreateFood, restaurant_id: int, foodservice = Depends(get_food_service)):
        logger.info("create-food api start")
        food = foodservice.create_food(create_food, restaurant_id)

        return {"message": "Food created successfully", "food": food}
@food_router.get("/get-food-by-restaurant-id")
def get_food_by_restaurant_id(restaurant_id: int, foodservice  = Depends(get_food_service)):
    logger.info("get-food-by-restaurant-id api start")
    food_items = foodservice.get_food_by_restaurant_id(restaurant_id)

    return {"food_items": food_items}
  

