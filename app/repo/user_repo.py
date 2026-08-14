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
user_repo = UserRepository()