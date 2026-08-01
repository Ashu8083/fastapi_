from fastapi import APIRouter, Depends
from app.dependency.service_dependency import get_restaurant_service
from app.service.resturant_service import ResturentService
from app.schema.restarant_schema import CreateRestaurantRequest

router = APIRouter()


@router.post("/restaurants")
def create_restaurant(restaurant_data: CreateRestaurantRequest, restaurant_service: ResturentService = Depends(get_restaurant_service)):
    return restaurant_service.create_restaurant(restaurant_data)
 



