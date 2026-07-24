from fastapi import FastAPI
from fastapi.routing import APIRouter


app = FastAPI()

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello, World!"}
