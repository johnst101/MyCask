'''
Authentication API endpoints.
'''

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.services.user import create_user, get_any_user_by_email, get_any_user_by_username
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token, validate_password_strength, verify_refresh_token
from app.schemas.token import RefreshTokenRequest, Token

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    '''Register a new user by providing email, password, username, first name, and last name'''
    if get_any_user_by_email(db, user_data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    if user_data.username and user_data.username.strip():
        if get_any_user_by_username(db, user_data.username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")

    # Validate password strength
    is_valid, error_message = validate_password_strength(user_data.password)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_message
        )

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
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed due to data conflict. Please try again."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed due to unexpected error. Please try again."
        )

    return UserResponse(
        id=new_user.id,
        email=new_user.email, 
        username=new_user.username,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        created_at=new_user.created_at
    )

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> Token:
    """
    Authenticate user and return JWT token.
    
    Uses OAuth2PasswordRequestForm for compatibility with FastAPI's OAuth2 flow.
    The 'username' field should contain the user's email address.
    
    Flow:
    1. User sends POST /auth/login with username (email) and password as form data
    2. Server looks up user by email
    3. Server verifies password hash matches
    4. Server creates JWT token with user email as subject
    5. Server returns token
    """
    # Look up user by email (OAuth2PasswordRequestForm uses 'username' field)
    user = get_any_user_by_email(db, form_data.username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    # Create JWT token with user email as subject
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})
    
    return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")

@router.post("/refresh", response_model=Token)
def refresh(request: RefreshTokenRequest, db: Session = Depends(get_db)) -> Token:
    """
    # TODO: Update to get refresh token from cookies instead of request body (copying and pasting right now is annoying)
    Refresh access token using a valid refresh token.
    
    Returns new access token and refresh token (token rotation).
    """
    try:
        # Verify the refresh token
        payload = verify_refresh_token(request.refresh_token)
        print(f"Payload: {payload}")
        user_email = payload.get("sub")
        
        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )
        
        # Optional: Verify user still exists and is active
        user = get_any_user_by_email(db, user_email)
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found or inactive"
            )
        
        # Create new tokens (token rotation)
        new_access_token = create_access_token(data={"sub": user_email})
        new_refresh_token = create_refresh_token(data={"sub": user_email})
        
        return Token(
            access_token=new_access_token,
            refresh_token=new_refresh_token,
            token_type="bearer"
        )
        
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token"
        )
    except Exception as e:
        # Log the error in production
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to refresh token"
        )