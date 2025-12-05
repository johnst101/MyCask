"""
Tests for authentication middleware (dependencies).

These tests verify the authentication middleware by testing protected endpoints,
which is the most realistic way to test FastAPI dependencies.
"""

import pytest
from fastapi import status
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.security import SECRET_KEY, ALGORITHM, create_access_token


class TestGetCurrentUserMiddleware:
    """Tests for get_current_user dependency through protected endpoints."""

    def test_get_current_user_with_valid_token_returns_user(self, client, test_user, auth_headers):
        """Test that valid token allows access to protected endpoint."""
        # This tests get_current_user indirectly through /users/me
        response = client.get("/users/me", headers=auth_headers)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == test_user.email

    def test_get_current_user_with_invalid_token_raises_401(self, client):
        """Test that invalid token raises 401."""
        headers = {"Authorization": "Bearer invalid.token.here"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_expired_token_raises_401(self, client, test_user):
        """Test that expired token raises 401."""
        # Create expired token
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

    def test_get_current_user_with_missing_sub_raises_401(self, client):
        """Test that token without 'sub' field raises 401."""
        # Create token without 'sub'
        invalid_token = jwt.encode(
            {"type": "access"},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        
        headers = {"Authorization": f"Bearer {invalid_token}"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_nonexistent_user_raises_401(self, client):
        """Test that token for non-existent user raises 401."""
        # Create token for non-existent user
        token = create_access_token(data={"sub": "nonexistent@example.com"})
        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_with_missing_token_raises_401(self, client):
        """Test that missing token raises 401."""
        response = client.get("/users/me")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetCurrentActiveUserMiddleware:
    """Tests for get_current_active_user dependency through protected endpoints."""

    def test_get_current_active_user_with_active_user_succeeds(self, client, test_user, auth_headers):
        """Test that active user can access protected endpoint."""
        # This tests get_current_active_user indirectly through /users/me
        response = client.get("/users/me", headers=auth_headers)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == test_user.email

    def test_get_current_active_user_with_inactive_user_raises_403(self, client, inactive_user):
        """Test that inactive user raises 403."""
        access_token = create_access_token(data={"sub": inactive_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # get_current_user should succeed (finds user)
        # but get_current_active_user should fail (user is inactive)
        response = client.get("/users/me", headers=headers)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "inactive" in response.json()["detail"].lower()

    def test_get_current_active_user_dependency_chain(self, client, test_user, auth_headers):
        """Test that get_current_active_user correctly depends on get_current_user."""
        # If get_current_user fails, get_current_active_user should never be called
        # This is tested by the fact that invalid tokens return 401, not 403
        invalid_headers = {"Authorization": "Bearer invalid.token"}
        response = client.get("/users/me", headers=invalid_headers)
        # Should be 401 (from get_current_user), not 403 (from get_current_active_user)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

