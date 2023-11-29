from pydantic import BaseModel, EmailStr, conint
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: int

class UserOut(BaseModel):
    id: int
    email:EmailStr
    created_at: datetime



class UserLogin(BaseModel):
    email: EmailStr
    password: str
