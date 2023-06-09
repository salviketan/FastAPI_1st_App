from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email : EmailStr
    password : str


class ShowUser(BaseModel):
    email: str
    is_active: bool

    class Config:
        orm_mode= True