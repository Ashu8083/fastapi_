from fastapi import APIRouter, Depends
from app.dependency.service_dependency import get_restaurant_service
from app.service.resturant_service import ResturentService
from app.schema.restarant_schema import CreateRestaurantRequest, RestaurantResponse , RestaurantListResponse

router = APIRouter()


@router.post("/restaurants", response_model=RestaurantResponse)
def create_restaurant(restaurant_data: CreateRestaurantRequest, restaurant_service: ResturentService = Depends(get_restaurant_service)):
    return restaurant_service.create_restaurant(restaurant_data)

@router.get("/get-restaurants-by-location",
            response_model=list[RestaurantResponse])
def get_restaurant_by_location(location: str,
                                restaurant_service: ResturentService = Depends(get_restaurant_service)):
    return restaurant_service.get_restaurants_by_location(location=location)

@router.get("/get-restaurant-by-id",response_model=RestaurantListResponse)
def get_restaurant_by_id(location:str,rating :int
                         , restaurant_service: ResturentService = Depends(get_restaurant_service)):
    return restaurant_service.get_restaurant(location=location,rating=rating)

@router.get("/get-restaurant-by-name",response_model=RestaurantResponse)
def get_restaurant_by_name(name: str, restaurant_service: ResturentService = Depends(get_restaurant_service)):
    return restaurant_service.get_restaurant_by_name(restaurant_name=name)






