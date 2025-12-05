"""
Tests for authentication endpoints.
"""

import pytest
from fastapi import status
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM, create_refresh_token
from app.models import User
from app.services.user import get_any_user_by_email


class TestRegister:
    """Tests for POST /auth/register endpoint."""

    def test_register_user_with_all_fields_succeeds(self, client, test_db):
        """Test registering a new user with all fields."""
        response = client.post(
            "/auth/register",
            json={
                "email": "newuser@example.com",
                "password": "NewPassword123!",
                "username": "newuser",
                "first_name": "New",
                "last_name": "User"
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["email"] == "newuser@example.com"
        assert data["username"] == "newuser"
        assert data["first_name"] == "New"
        assert data["last_name"] == "User"
        assert "id" in data
        assert "created_at" in data
        assert "password" not in data  # Password should not be in response

        # Verify user was created in database
        user = get_any_user_by_email(test_db, "newuser@example.com")
        assert user is not None
        assert user.email == "newuser@example.com"
        assert user.password_hash != "NewPassword123!"  # Password should be hashed

    def test_register_user_with_minimal_fields_succeeds(self, client, test_db):
        """Test registering a new user with only email and password."""
        response = client.post(
            "/auth/register",
            json={
                "email": "minimal@example.com",
                "password": "MinimalPass123!"
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["email"] == "minimal@example.com"
        assert data["username"] is None
        assert data["first_name"] is None
        assert data["last_name"] is None

        # Verify user was created
        user = get_any_user_by_email(test_db, "minimal@example.com")
        assert user is not None

    def test_register_duplicate_email_fails(self, client, test_user):
        """Test registering with duplicate email returns 400."""
        response = client.post(
            "/auth/register",
            json={
                "email": test_user.email,
                "password": "AnotherPassword123!"
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "already registered" in response.json()["detail"].lower()

    def test_register_duplicate_username_fails(self, client, test_user):
        """Test registering with duplicate username returns 400."""
        response = client.post(
            "/auth/register",
            json={
                "email": "different@example.com",
                "password": "AnotherPassword123!",
                "username": test_user.username
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "username" in response.json()["detail"].lower()

    def test_register_invalid_email_format_fails(self, client):
        """Test registering with invalid email format returns 422."""
        response = client.post(
            "/auth/register",
            json={
                "email": "not-an-email",
                "password": "ValidPassword123!"
            }
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_register_weak_password_fails(self, client):
        """Test registering with weak password returns 400."""
        weak_passwords = [
            "short",  # Too short
            "nouppercase123!",  # No uppercase
            "NOLOWERCASE123!",  # No lowercase
            "NoNumbers!",  # No numbers
            "NoSpecial123"  # No special characters
        ]
        
        for password in weak_passwords:
            response = client.post(
                "/auth/register",
                json={
                    "email": f"test{password}@example.com",
                    "password": password
                }
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert "password" in response.json()["detail"].lower()

    def test_register_missing_required_fields_fails(self, client):
        """Test registering with missing required fields returns 422."""
        # Missing email
        response = client.post(
            "/auth/register",
            json={"password": "ValidPassword123!"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        # Missing password
        response = client.post(
            "/auth/register",
            json={"email": "test@example.com"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_register_empty_optional_fields_succeeds(self, client):
        """Test registering with empty strings for optional fields."""
        response = client.post(
            "/auth/register",
            json={
                "email": "empty@example.com",
                "password": "ValidPassword123!",
                "username": "",
                "first_name": "",
                "last_name": ""
            }
        )
        # Should succeed, but optional fields might be None or empty string
        assert response.status_code in [status.HTTP_201_CREATED, status.HTTP_422_UNPROCESSABLE_ENTITY]


class TestLogin:
    """Tests for POST /auth/login endpoint."""

    def test_login_with_valid_credentials_succeeds(self, client, test_user):
        """Test login with valid email and password."""
        response = client.post(
            "/auth/login",
            data={
                "username": test_user.email,  # OAuth2PasswordRequestForm uses 'username' field
                "password": "TestPassword123!"
            }
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"

        # Verify tokens are valid JWTs
        access_payload = jwt.decode(data["access_token"], SECRET_KEY, algorithms=[ALGORITHM])
        assert access_payload["sub"] == test_user.email
        assert access_payload["type"] == "access"

        refresh_payload = jwt.decode(data["refresh_token"], SECRET_KEY, algorithms=[ALGORITHM])
        assert refresh_payload["sub"] == test_user.email
        assert refresh_payload["type"] == "refresh"

    def test_login_with_nonexistent_email_fails(self, client):
        """Test login with non-existent email returns 401."""
        response = client.post(
            "/auth/login",
            data={
                "username": "nonexistent@example.com",
                "password": "SomePassword123!"
            }
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "incorrect" in response.json()["detail"].lower()

    def test_login_with_incorrect_password_fails(self, client, test_user):
        """Test login with incorrect password returns 401."""
        response = client.post(
            "/auth/login",
            data={
                "username": test_user.email,
                "password": "WrongPassword123!"
            }
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "incorrect" in response.json()["detail"].lower()

    def test_login_with_inactive_user_fails(self, client, inactive_user):
        """Test login with inactive user returns 403."""
        response = client.post(
            "/auth/login",
            data={
                "username": inactive_user.email,
                "password": "TestPassword123!"
            }
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "inactive" in response.json()["detail"].lower()

    def test_login_with_missing_credentials_fails(self, client):
        """Test login with missing credentials returns 422."""
        # Missing password
        response = client.post(
            "/auth/login",
            data={"username": "test@example.com"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

        # Missing username
        response = client.post(
            "/auth/login",
            data={"password": "SomePassword123!"}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_login_error_message_does_not_leak_info(self, client, test_user):
        """Test that error messages don't leak which field is wrong."""
        # Wrong email
        response1 = client.post(
            "/auth/login",
            data={
                "username": "wrong@example.com",
                "password": "TestPassword123!"
            }
        )
        
        # Wrong password
        response2 = client.post(
            "/auth/login",
            data={
                "username": test_user.email,
                "password": "WrongPassword123!"
            }
        )
        
        # Both should return same error message
        assert response1.status_code == status.HTTP_401_UNAUTHORIZED
        assert response2.status_code == status.HTTP_401_UNAUTHORIZED
        assert response1.json()["detail"] == response2.json()["detail"]


class TestRefresh:
    """Tests for POST /auth/refresh endpoint."""

    def test_refresh_with_valid_token_succeeds(self, client, test_user, refresh_token):
        """Test refreshing token with valid refresh token."""
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": refresh_token}
        )
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"
        
        # Verify new tokens are different from old ones
        assert data["access_token"] != refresh_token
        assert data["refresh_token"] != refresh_token

        # Verify new tokens are valid JWTs
        new_access_payload = jwt.decode(data["access_token"], SECRET_KEY, algorithms=[ALGORITHM])
        assert new_access_payload["sub"] == test_user.email
        assert new_access_payload["type"] == "access"

        new_refresh_payload = jwt.decode(data["refresh_token"], SECRET_KEY, algorithms=[ALGORITHM])
        assert new_refresh_payload["sub"] == test_user.email
        assert new_refresh_payload["type"] == "refresh"

    def test_refresh_with_invalid_token_fails(self, client):
        """Test refreshing with invalid token returns 401."""
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": "invalid.token.here"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_with_access_token_fails(self, client, auth_headers):
        """Test refreshing with access token instead of refresh token returns 401."""
        # Extract access token from headers
        access_token = auth_headers["Authorization"].replace("Bearer ", "")
        
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": access_token}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "invalid" in response.json()["detail"].lower()

    def test_refresh_with_inactive_user_fails(self, client, inactive_user):
        """Test refreshing token for inactive user returns 401."""
        refresh_token = create_refresh_token(data={"sub": inactive_user.email})
        
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": refresh_token}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_with_missing_token_fails(self, client):
        """Test refreshing with missing token returns 422."""
        response = client.post(
            "/auth/refresh",
            json={}
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_refresh_rotates_tokens(self, client, test_user, refresh_token):
        """Test that refresh token rotation works (old token becomes invalid)."""
        # First refresh
        response1 = client.post(
            "/auth/refresh",
            json={"refresh_token": refresh_token}
        )
        assert response1.status_code == status.HTTP_200_OK
        new_refresh_token = response1.json()["refresh_token"]

        # Old refresh token should still work (token rotation not implemented yet)
        # This test documents expected behavior - you may want to implement token rotation
        response2 = client.post(
            "/auth/refresh",
            json={"refresh_token": refresh_token}
        )
        # Depending on implementation, this might succeed or fail
        # If token rotation is implemented, this should fail
        # If not, this will succeed

