from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from app.service.user_service import foodservice
from app.db.database import get_db


food_router = APIRouter()

@food_router.post("/food")
async def create_food(name: str, price: int, db: Session = Depends(get_db)):
    food = foodservice.create_food(name, price, db=db)
    return {"food": food.__dict__}
