from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from starlette import status

from app.dependency.service_dependency import get_user_service, get_auth_service
from app.repo.user_repo import UserRepository
from app.security.auth_dependency import auth_dependency
from app.security.authService import AuthService
from app.service.user_service import UserService
from app.db.database import get_db
from app.core.logger_config import logger
from app.schema.user_schema import UserCreateSchema,UserCreateResponse
from app.custom_execption.custom_exception import UserNotFoundException
from app.security.tokenHandel import  generate_token,decode_auth_token

user_router = APIRouter()


@user_router.post("/users")
async def create_user(user_create_schema :UserCreateSchema , request : Request, user_service :UserService= Depends(get_user_service)):
    logger.info(f"Creating user with ID: {user_create_schema.email}")
    
    user = user_service.create_user(user_create_schema)
    user_response = UserCreateResponse(
        username= user.username,
        email= user.email,
        age= user.age
    )
    
    return JSONResponse(
    
        content= user_response.model_dump(),
        status_code = 200
        )


@user_router.post("/login-users")
def login(user_email: str, password: str , request : Request, auth_service : AuthService = Depends(get_auth_service)):

    token =  auth_service.create_user_token(user_email, password)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content= {"token": token}
    )
# @user_router.get("/users/{user_id}")
# async def get_user(user_id: int,db: Session = Depends(get_db)):
#
#         user = user_service.get_user_by_id_service(user_id,db)
#         token = generate_token(user.id)
#
#         return JSONResponse(
#             content= token,
#             status_code = 200
#         )
#
# @user_router.post("/token-payload/{token}")
# async def get_user_payload(
#     token: str,
#     db: Session = Depends(get_db)
# ):
#     logger.info("Getting user from token")
#
#     payload = decode_auth_token(token)
#
#     user = user_service.get_user_by_id_service(
#         payload["user_id"],
#         db
#     )
#
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )
#
#     return payload
        

  
   



