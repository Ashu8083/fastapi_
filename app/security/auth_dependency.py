from email import message

from fastapi import Request, Depends, Security, HTTPException,status

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.logger_config import logger
from app.db.database import SessionLocal, get_db
from app.repo.user_repo import UserRepository
from app.security.authService import AuthService

bearer_scheme = HTTPBearer()

def auth_dependency(
        request :Request,
        credentials : HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            message = "Token is missing")

    db = SessionLocal()
    try:
        auth_service =  AuthService(user_repo= UserRepository(db))
        auth_cntx = auth_service.verify_user_token(token)
        request.state.auth = auth_cntx
        url = request.url
        logger.info(f"user request url: {url}")
        return auth_cntx
    finally:
        db.close()




