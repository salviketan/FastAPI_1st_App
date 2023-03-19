from fastapi import APIRouter, Depends
from database import get_db
from models import User
from schemas import UserCreate, ShowUser
from hashing import Hasher
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/user', tags=["user"])
def get_user():
    return{"msg": "Hello user"}

@router.post("/users", tags= ["user"], response_model= ShowUser)
def create_user(user: UserCreate, db: Session= Depends(get_db)):
    user = User(email= user.email, hashed_password= Hasher.get_hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user