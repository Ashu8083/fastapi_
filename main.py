from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.api.user_api import user_router


app = FastAPI()

app.include_router(user_router)  # Include your user_router here

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}
