from uuid import UUID
from pydantic import BaseModel

class AuthContext(BaseModel):
    user_id : int
    #User's role , email name