'''
Security utilities for the MyCask API.
'''

from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import JWTError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict) -> str:
    """Create access token."""
    to_encode = data.copy()
    # Validate ACCESS_TOKEN_EXPIRE_MINUTES and use fallback if invalid
    if ACCESS_TOKEN_EXPIRE_MINUTES and ACCESS_TOKEN_EXPIRE_MINUTES > 0:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expires_delta = timedelta(minutes=15)  # Fallback to 15 minutes
    
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    """Create refresh token."""
    to_encode = data.copy()
    if REFRESH_TOKEN_EXPIRE_DAYS and REFRESH_TOKEN_EXPIRE_DAYS > 0:
        expires_delta = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    else:
        expires_delta = timedelta(days=7)  # Fallback to 7 days
    
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_refresh_token(token: str) -> dict:
    """Verify refresh token and return payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def verify_access_token(token: str) -> dict:
    """Verify access token and return payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain, hashed)

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)

def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate password strength.
    
    Returns:
        tuple: (is_valid, error_message)
        - is_valid: True if password meets requirements, False otherwise
        - error_message: Empty string if valid, otherwise error description
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if len(password) > 128:
        return False, "Password must be less than 128 characters"
    
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"

    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter"

    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number"

    # Check for at least one special character (non-alphanumeric)
    if not any(not char.isalnum() for char in password):
        return False, "Password must contain at least one special character"
    
    return True, ""