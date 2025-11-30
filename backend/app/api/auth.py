'''
Authentication API endpoints.
'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.services.user import create_user, get_any_user_by_email
from passlib.context import CryptContext
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/auth", tags=["authentication"])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@router.post("/register", status_code=201, response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    if len(user_data.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long"
        )
    if get_any_user_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    password_hash = hash_password(user_data.password)
    try:
        new_user = create_user(
            db,
            email=user_data.email,
            password_hash=password_hash,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
    except IntegrityError as e:
        db.rollback()
        if "username" in str(e.orig).lower():
            raise HTTPException(status_code=400, detail="Username already taken")
        raise HTTPException(
            status_code=400,
            detail="Registration failed due to data conflict"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Registration failed due to unexpected error"
        )
    return UserResponse(
        id=new_user.id,
        email=new_user.email, 
        username=new_user.username,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        created_at=new_user.created_at
    )