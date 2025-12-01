'''
User API endpoints.
'''

from fastapi import APIRouter, Depends
from app.models import User
from app.schemas.user import UserResponse
from app.core.auth import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)) -> UserResponse:
    """
    Get current authenticated user's information.
    
    Flow:
    1. Client sends GET /users/me with Authorization: Bearer <token>
    2. FastAPI extracts token using OAuth2PasswordBearer
    3. get_current_user() dependency decodes JWT, extracts user_id, looks up user
    4. get_current_active_user() checks if user is active
    5. Endpoint returns user data
    """
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        username=current_user.username,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        created_at=current_user.created_at
    )

