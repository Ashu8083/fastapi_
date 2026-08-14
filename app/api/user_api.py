from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from fastapi.requests import Request
from app.service.user_service import user_service
from app.db.database import get_db
from app.core.logger_config import logger

user_router = APIRouter()

@user_router.post("/users")
async def create_user(id: int, username: str, email: str, age: int , request : Request, db: Session = Depends(get_db)):
    logger.info(f"Creating user with ID: {email}")
    try:
        user = user_service.create_user(id, username, email, age, db=db)
    except Exception as e:
        logger.debug(f"User with {id} is create in db")
        raise HTTPException(status_code=409, detail="User already Exist ")
    return user    
    

@user_router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    print(user)
    if user:
        return {"user": user.__dict__}
    if not user:
        raise HTTPException(status_code=404, detail="User not found")   


