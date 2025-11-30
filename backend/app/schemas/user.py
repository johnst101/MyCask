'''
User schemas for the MyCask application.
'''

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: str
    username: str | None
    first_name: str | None
    last_name: str | None
    created_at: datetime
