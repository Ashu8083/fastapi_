from fastapi.params import Depends

from app.model.user_model import User as Users
from sqlalchemy.orm import Session
from app.core.logger_config import logger
from app.db.database import get_db



class UserRepository:
    def __init__(self,db):
        self.db_session = db

    def create_user(self, user: Users):
        try :
               self.db_session.add(user)
               self.db_session.commit()
               self.db_session.refresh(user)
               logger.info("Record for user is create")
        except Exception as e:
            logger.error(f"Record can't create {e}")
            raise ValueError("Database error")
        return user

    def get_user_by_id(self,user_id : int ):
        try:
            user = self.db_session.query(Users).filter(Users.id == user_id).first()
        except Exception  as e:
             logger.info("error")
             raise  ValueError("User not Found")
        return user

    def get_user_by_email(self,user_email):
            user = self.db_session.query(Users).filter(Users.email == user_email).first()
            return user

