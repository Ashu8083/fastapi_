from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.db.database import get_db,Base,engine
from app.model.user_model import User
from app.model.food_model import Food
from app.api.user_api import user_router
from app.api.resturant_router import router as restaurant_router
from app.api.food_api import food_router


app = FastAPI()

app.include_router(user_router) 
app.include_router(restaurant_router)
app.include_router(food_router)  # Include your restaurant_router here
Base.metadata.create_all(bind=engine)  # Create tables in the database
  # Include your user_service_router here

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}
