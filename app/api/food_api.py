from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from app.service.user_service import foodservice
from app.db.database import get_db


food_router = APIRouter()

