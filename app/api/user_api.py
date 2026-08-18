from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.service.user_service import user_service
from app.db.database import get_db
from app.core.logger_config import logger
from app.schema.user_schema import UserCreateSchema,UserCreateResponse
from app.custom_execption.custom_exception import UserNotFoundException
from app.security.tokenHandel import  generate_token,decode_auth_token

user_router = APIRouter()


@user_router.post("/users")
async def create_user(user_create_schema :UserCreateSchema , request : Request, db: Session = Depends(get_db)):
    logger.info(f"Creating user with ID: {user_create_schema.email}")
    
    user = user_service.create_user(user_create_schema,db=db)
    user_response = UserCreateResponse(
        username= user.username,
        email= user.email,
        age= user.age
    )
    
    return JSONResponse(
    
        content= user_response.model_dump(),
        status_code = 200
        )
    

@user_router.get("/users/{user_id}")
async def get_user(user_id: int,db: Session = Depends(get_db)):
    
        user = user_service.get_user_by_id_service(user_id,db)
        token = generate_token(user.id)

        return JSONResponse(
            content= token,
            status_code = 200
        )

@user_router.post("/token-payload/{token}")
async def get_user_payload(
    token: str,
    db: Session = Depends(get_db)
):
    logger.info("Getting user from token")

    payload = decode_auth_token(token)

    user = user_service.get_user_by_id_service(
        payload["user_id"],
        db
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return payload
        

  
   



