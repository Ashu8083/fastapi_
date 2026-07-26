from fastapi import APIRouter, HTTPException
from app.service.user_service import UserService

user_router = APIRouter()

@user_router.post("/users")
async def create_user(id: int, username: str, email: str, age: int):
    user = UserService().create_user(id, username, email, age)
    return {"message": "User created successfully", "user": user.__dict__}  

@user_router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = UserService().get_user(user_id)
    if user:
        return {"user": user.__dict__}
    else:
        raise HTTPException(status_code=404, detail="User not found")   


