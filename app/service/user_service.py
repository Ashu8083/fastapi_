from app.repo.user_repo import UserRepository
from app.model.user_model import User

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, id: int, username: str, email: str, age: int):
        user = User(id=id, username=username, email=email, age=age)
        self.user_repo.add_user(user)
        return user

    def get_user(self, user_id: int):
        return self.user_repo.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repo.get_all_users()

user_service = UserService()