import re
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, validator


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User email address", example="user@example.com")


class UserCreate(UserBase):
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=100, 
        description="User password",
        example="StrongP@ssw0rd"
    )

    
    @validator('password')
    def password_strength(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        return v


class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="User email address", example="user@example.com")
    password: str = Field(..., description="User password", example="StrongP@ssw0rd")


class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_at: datetime

    
    class Config:
        from_attributes = True


class User(UserBase):
    id: int
    created_at: datetime


    class Config:
        from_attributes = True
