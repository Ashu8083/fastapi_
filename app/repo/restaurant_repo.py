

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


    def get_restaurant_location(self,location):
        restaurant = self.db.query(Restaurant).filter(Restaurant.location == location).all()

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


        