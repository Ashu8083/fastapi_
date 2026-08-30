import datetime
from datetime import timezone

from fastapi import HTTPException,status
from jose import jwt,ExpiredSignatureError,JWTError

from app.core.logger_config import logger

SECRET_KEY = 'asutoshGoud673248563496061436ygae7' # Secrete key
ALGORITHM = 'HS256'        # Algorithm which going to use to encode
def generate_token(user_id : int):
    user_id = str(user_id)
    payload = {
        "user_id":user_id,
        "exp":datetime.datetime.now(timezone.utc) + datetime.timedelta(minutes=60),
    }

    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)  # use for encoding and return a token
    logger.info(f"user with {user_id} has this {token}")
    return token

# Decode Token Process

def decode_auth_token(auth_token : str):
    try:
        payload = jwt.decode(auth_token,  # use for decode the token and return the payload
                         SECRET_KEY,
                         algorithms=ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,)

    logger.info(f"user with {auth_token} has this {payload['user_id']}")
    return payload



