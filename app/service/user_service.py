from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from app.repo.user_repo import user_repo
from app.model.user_model import User as Users
from app.core.logger_config import logger

class UserService:
    # You can pass a database session here if needed

    def create_user(self, id: int, username: str, email: str, age: int, db :Session):

        user = Users(id=id, username=username, email=email, age=age)

        
        try:
            user_store =user_repo.create_user(user,db_session=db)
            logger.debug(f"user with user id{id} is created ")
            return user_store
        except Exception as e:
            raise HTTPException(
                status_code= 500,
                detail= "Internal Server Error"
            )





user_service = UserService()