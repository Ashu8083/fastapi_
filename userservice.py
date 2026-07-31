# from fastapi.routing import APIRouter
# from sqlalchemy.orm import Session
# from fastapi import Depends

# from app.db.database import get_db
# from app.model.user_model import User


# router = APIRouter(prefix="/users-at-main", tags=["users"])



# @router.get("/users")
# async def get_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return {"users": [user.__dict__ for user in users]}

# @router.post("/users")
# async def create_user(id: int, username: str, email: str, age: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == id).first()
#     user.emp
#     if user:
#         return {"message": "User already exists"}

#     user = User(id=id, username=username, email=email, age=age)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"user": user.__dict__}  


