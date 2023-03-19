from fastapi import APIRouter, Depends
from database import get_db
# from models import User
# from schemas import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/items',tags=["item"])
def get_items():
    return{"msg": "Hello items"}