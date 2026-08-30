from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi import HTTPException, Depends
from app.repo.user_repo import UserRepository
from app.model.user_model import User as Users
from app.core.logger_config import logger
from app.schema.user_schema import UserCreateSchema
from app.custom_execption.custom_exception import UserAlreadyExist,UserNotFoundException

class UserService:
    # You can pass a database session here if needed
    def __init__(self,user_repo,db):
        self.user_repository = user_repo
        self.db = db



    def create_user(self,user_create_schema : UserCreateSchema):

        user = Users(username=user_create_schema.username,
                     email=user_create_schema.email,
                     password=user_create_schema.password,
                     age=user_create_schema.age)

        user_store =self.user_repository.create_user(user)
        logger.debug(f"user with user id{id} is created ")
        return user_store


    # def get_user_by_id_service(self,user_id : int ,db):
    #
    #         user= user_repo.get_user_by_id(db=db ,user_id= user_id)
    #         if not user:
    #             logger.info("inside service user not found")
    #             raise UserNotFoundException(message = f"User with {user_id}. not found")
    #         return user
    #
    #
    #
    # def get_user_email_service(self,user_email :str ,db):
    #         try :
    #             user= user_repo.get_user_by_email(db=db , user_eamil= user_email)
    #             return user
    #         except Exception as e:
    #             raise UserNotFoundException(f"User with {user_email}. not found")
