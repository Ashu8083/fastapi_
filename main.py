from fastapi import FastAPI
from fastapi.routing import APIRouter


app = FastAPI()

router = APIRouter()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}
