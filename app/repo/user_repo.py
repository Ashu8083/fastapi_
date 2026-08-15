from app.model.user_model import User as Users
from sqlalchemy.orm import Session
from app.core.logger_config import logger


class UserRepository:
    

    def create_user(self, user: Users, db_session: Session):
        try :
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user)
            logger.info("Record for user is create")
        except Exception as e:
            logger.error(f"Record can't create {e}")
            raise ValueError("Database error")
        return user

    def get_user_by_id(self,user_id : int ,db :Session):
        try:
            user = db.query(Users).filter(Users.id == user_id).first()
        except Exception  as e:
             logger.info("error")
             raise  ValueError("User not Found")
        return user
        
    def get_user_by_email(self,user_eamil : str ,db :Session):
            user = db.query(Users).filter(Users.email == user_eamil).first()
            return user

user_repo = UserRepository()