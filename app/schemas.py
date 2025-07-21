from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# ---------- USER SCHEMAS ----------

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# ---------- LOGIN SCHEMA ----------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- EXPENSE SCHEMAS ----------
class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseOut(ExpenseBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        orm_mode = True


# ---------- TOKEN SCHEMAS ----------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

