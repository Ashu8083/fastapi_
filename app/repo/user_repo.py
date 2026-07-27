from app.model.user_model import User as Users
from sqlalchemy.orm import Session


class UserRepository:
    

    def create_user(self, user: Users, db_session: Session):
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user
user_repo = UserRepository()