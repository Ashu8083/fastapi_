from app.core.auth_cntx import AuthContext
from app.custom_execption.custom_exception import UserNotFoundException
from app.repo.user_repo import UserRepository
from app.security.tokenHandel import  generate_token,decode_auth_token

class AuthService:

    def __init__(self,user_repo : UserRepository):
        self.user_repo : UserRepository = user_repo

    def create_user_token(self,user_email,password):

        user = self.user_repo.get_user_by_email(user_email)
        if user is None:
            raise UserNotFoundException("Enter a valid email address")
        if user.password is None:
            raise ValueError("User has no password")
        if user.password != password :
            raise UserNotFoundException("Enter a valid password")
        user_auth_token = generate_token(user_id = user.id)
        return user_auth_token


    def verify_user_token(self,token):
        decoded_token = decode_auth_token(token)
        user = self.user_repo.get_user_by_id(decoded_token["user_id"])
        if user is None:
            raise UserNotFoundException("User does not exist")
        auth_cntx = AuthContext(user_id = user.id )
        return auth_cntx








