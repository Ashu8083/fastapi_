from app.repo.restaurant_repo import RestaurantRepo


class ResturentService:
    def __init__(self, repository: RestaurantRepo):
        self.repository: RestaurantRepo = repository

    def get_restaurants_by_location(self, location: str):
        restaurants = self.repository.get_restaurant_location(location) 

        return restaurants

    def get_restaurant_by_location_and_rating(self, location: str, rating: int):
        restaurants = self.repository.get_restaurant_location_and_rating(location, rating)
         
        return restaurants
    
    def get_restaurant_by_name(self, restaurant_name: str):
        return self.repository.get_restaurant_name(restaurant_name)

    def create_restaurant(self, restaurant_data):
        resturent = self.repository.get_restaurant_by_email(restaurant_data.email)
        if resturent:
            raise ValueError("Restaurant with this email already exists")
        return self.repository.create_restaurant(
            name=restaurant_data.name,
            email_input=restaurant_data.email,
            location=restaurant_data.location
        )

    def update_restaurant(self, restaurant_id, restaurant_data):
        return 

    def delete_restaurant(self, restaurant_id):
        return 