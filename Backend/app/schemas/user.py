from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import UserRole

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.CASHIER

# Properties to return to client (NEVER return password)
class UserResponse(UserBase):
    id: int
    is_active: bool
    role: UserRole

    class Config:
        from_attributes = True

# Token response schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
