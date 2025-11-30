'''
CRUD operations for users.
'''

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import User
from typing import Optional

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Get a user by their ID."""
    return db.query(User).filter(User.id == user_id, User.is_active == True).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get a user by their email."""
    return db.query(User).filter(User.email == email, User.is_active == True).first()

def get_any_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get a user by their email."""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password_hash: str, username: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None) -> User:
    """Create a new user."""
    user = User(
        email=email,
        password_hash=password_hash,
        username=username,
        first_name=first_name,
        last_name=last_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)  # Get the ID and timestamps from DB
    return user

def update_user(db: Session, user_id: int, **kwargs) -> Optional[User]:
    """Update user fields."""
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    for key, value in kwargs.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> bool:
    """Soft delete a user (set is_active=False)."""
    user = get_user_by_id(db, user_id)
    if not user:
        return False
    
    user.is_active = False
    user.deleted_at = func.now()
    db.commit()
    return True

def full_delete_user(db: Session, user_email: str) -> bool:
    """Full delete a user (delete from database)."""
    user = get_any_user_by_email(db, user_email)
    if not user:
        return False
    
    db.delete(user)
    db.commit()
    return True