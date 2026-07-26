from fastapi import APIRouter, HTTPException
from app.service.user_service import user_service

user_router = APIRouter()

@user_router.post("/users")
async def create_user(id: int, username: str, email: str, age: int):
    user = user_service.create_user(id, username, email, age)
    return {"message": "User created successfully", "user": user.__dict__}  

@user_router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    print(user)
    if user:
        return {"user": user.__dict__}
    if not user:
        raise HTTPException(status_code=404, detail="User not found")   


