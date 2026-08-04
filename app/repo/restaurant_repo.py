

from app.model.food_model import Food
from app.model.restaurant import Restaurant
from sqlalchemy.orm import Session


class RestaurantRepo:
    def __init__(self, db : Session):
        self.db = db

    def create_restaurant(self,name : str,email_input:str, location: str):

        restaurant = Restaurant(
                    email = email_input,
                    name = name,
                    location = location
                    )
        try :
           self.db.add(restaurant)
           self.db.commit()
           self.db.refresh(restaurant)
           return restaurant
        except Exception as e:
           self.db.rollback()
           raise ValueError("Internal Error")
    def get_restaurant_id_by_name_and_loaction(self,name:str,location:str):
        restaurant_id = self.db.query(Restaurant.id).filter(Restaurant.name == name, Restaurant.location == location).scalar()
        return restaurant_id
    
    def get_restaurant_location(self,location)-> list[Restaurant]:
        restaurant = self.db.query(Restaurant).filter(Restaurant.location == location).all()

        return restaurant
    def get_restaurant_name(self,name)-> Restaurant:
            restaurant = self.db.query(Restaurant).filter(Restaurant.name == name).first()
            return restaurant

    def get_restaurnt_by_name(self,name):
        restaurant = self.db.query(Restaurant).filter(Restaurant.name == name).all()
        return restaurant
    def get_restaurant_by_email(self, email):
        restaurant = self.db.query(Restaurant).filter(Restaurant.email == email).first()

        return restaurant

    def update_restaurent_update_name(self,email,name):
        restaurant = self.db.query(Restaurant).filter(Restaurant.email == email).first()

        if not restaurant:
            raise ValueError("Restarant Is NOT EXIST")

        restaurant.name = name
        
        try:    
            self.db.add(restaurant)
            self.db.commit()
        except Exception as e:

            self.db.rollback()

    def delete_restaurent_by_email(self,emial):
        restaurant = self.db.query(Restaurant).filter(Restaurant.email == emial).first()

        if not restaurant:
            raise ValueError("Record not Found")

        self.db.delete(restaurant)
        self.db.commit()

        return "Record Deleted"


    def get_restaurant_location_and_rating(self,location,rating):
        # statement  = self.db.select(Restaurant).where(Restaurant.location == location , Restaurant.rating == rating)
        # restaurant = self.db.execute(statement).scalars().all()
        restaurant = self.db.query(Restaurant).filter(Restaurant.location== location , Restaurant.rating == rating).all()
        return restaurant

    def get_restaurant_food_by_restaurant_id(self,restaurant_id):
        restaurant = (
                    self.db.query(Restaurant)
                    .join(Food)
                    .filter(Restaurant.id == restaurant_id)
                    .all()
                )
        return restaurant
    
        