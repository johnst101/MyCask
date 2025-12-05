"""
Tests for user endpoints.
"""

import pytest
from fastapi import status
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM, create_access_token


class TestGetCurrentUser:
    """Tests for GET /users/me endpoint."""

    def test_get_current_user_with_valid_token_succeeds(self, client, test_user, auth_headers):
        """Test getting current user with valid access token."""
        response = client.get("/users/me", headers=auth_headers)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == test_user.id
        assert data["email"] == test_user.email
        assert data["username"] == test_user.username
        assert data["first_name"] == test_user.first_name
        assert data["last_name"] == test_user.last_name
        assert "created_at" in data
        assert "password" not in data  # Password should never be in response

    def test_get_current_user_without_token_fails(self, client):
        """Test accessing endpoint without token returns 401."""
        response = client.get("/users/me")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "credentials" in response.json()["detail"].lower()

    def test_get_current_user_with_invalid_token_fails(self, client):
        """Test accessing endpoint with invalid token returns 401."""
        headers = {"Authorization": "Bearer invalid.token.here"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_expired_token_fails(self, client, test_user):
        """Test accessing endpoint with expired token returns 401."""
        # Create an expired token (expired 1 hour ago)
        from datetime import datetime, timedelta, timezone
        expired_time = datetime.now(timezone.utc) - timedelta(hours=1)
        expired_token = jwt.encode(
            {
                "sub": test_user.email,
                "type": "access",
                "exp": expired_time
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        headers = {"Authorization": f"Bearer {expired_token}"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_refresh_token_fails(self, client, test_user):
        """Test accessing endpoint with refresh token instead of access token returns 401."""
        from app.core.security import create_refresh_token
        refresh_token = create_refresh_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {refresh_token}"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_inactive_user_fails(self, client, inactive_user):
        """Test accessing endpoint with token for inactive user returns 403."""
        access_token = create_access_token(data={"sub": inactive_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "inactive" in response.json()["detail"].lower()

    def test_get_current_user_returns_only_own_profile(self, client, test_user, auth_headers):
        """Test that user can only see their own profile."""
        response = client.get("/users/me", headers=auth_headers)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == test_user.id
        assert data["email"] == test_user.email

    def test_get_current_user_with_null_optional_fields(self, client, test_db):
        """Test getting user profile when optional fields are null."""
        from app.services.user import create_user
        from app.core.security import hash_password, create_access_token
        
        # Create user with only email and password
        user = create_user(
            test_db,
            email="minimal@example.com",
            password_hash=hash_password("TestPassword123!"),
            username=None,
            first_name=None,
            last_name=None
        )
        
        access_token = create_access_token(data={"sub": user.email})
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == "minimal@example.com"
        assert data["username"] is None
        assert data["first_name"] is None
        assert data["last_name"] is None

