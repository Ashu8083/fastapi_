from pydantic import BaseModel, EmailStr


class CreateRestaurantRequest(BaseModel):
    name: str
    location: str
    email: EmailStr