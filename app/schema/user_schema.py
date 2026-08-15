from pydantic import BaseModel,EmailStr

class UserCreateSchema(BaseModel):
    username : str
    email : EmailStr
    age :int

class UserCreateResponse(BaseModel):
    username : str
    email : EmailStr
    age :int

    class Config:
        orm_mode = True