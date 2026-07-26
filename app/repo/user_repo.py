from app.model.user_model import User


class UserRepository:
    def __init__(self):
        self.users: list[User]= []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self):
        return self.users