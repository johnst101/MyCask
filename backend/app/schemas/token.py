'''
Token schemas for authentication.
'''

from pydantic import BaseModel
from typing import Optional

class RefreshTokenRequest(BaseModel):
    """Refresh token request schema."""
    refresh_token: str

class Token(BaseModel):
    """Token response schema."""
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    """Token data extracted from JWT."""
    email: Optional[str] = None
    username: Optional[str] = None
    id: Optional[int] = None

