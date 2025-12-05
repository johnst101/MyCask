"""
Tests for security utility functions.
"""

import pytest
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.security import (
    hash_password,
    verify_password,
    validate_password_strength,
    create_access_token,
    create_refresh_token,
    verify_access_token,
    verify_refresh_token,
    SECRET_KEY,
    ALGORITHM
)


class TestPasswordHashing:
    """Tests for password hashing functions."""

    def test_hash_password_creates_different_hashes(self):
        """Test that same password creates different hashes (salt)."""
        password = "TestPassword123!"
        hash1 = hash_password(password)
        hash2 = hash_password(password)
        
        # Hashes should be different due to salt
        assert hash1 != hash2
        # But both should be valid
        assert verify_password(password, hash1)
        assert verify_password(password, hash2)

    def test_verify_password_correctly_verifies_hashed_passwords(self):
        """Test that verify_password correctly verifies hashed passwords."""
        password = "TestPassword123!"
        hashed = hash_password(password)
        
        assert verify_password(password, hashed) is True
        assert verify_password("WrongPassword", hashed) is False

    def test_verify_password_with_plain_text_fails(self):
        """Test that verify_password fails with plain text."""
        password = "TestPassword123!"
        assert verify_password(password, password) is False


class TestPasswordValidation:
    """Tests for password strength validation."""

    def test_validate_password_strength_accepts_valid_password(self):
        """Test that valid password passes validation."""
        valid_password = "ValidPassword123!"
        is_valid, error = validate_password_strength(valid_password)
        assert is_valid is True
        assert error == ""

    def test_validate_password_strength_rejects_short_password(self):
        """Test that password shorter than 8 characters fails."""
        short_password = "Short1!"
        is_valid, error = validate_password_strength(short_password)
        assert is_valid is False
        assert "8 characters" in error.lower()

    def test_validate_password_strength_rejects_long_password(self):
        """Test that password longer than 128 characters fails."""
        long_password = "A" * 129 + "1!"
        is_valid, error = validate_password_strength(long_password)
        assert is_valid is False
        assert "128 characters" in error.lower()

    def test_validate_password_strength_rejects_no_uppercase(self):
        """Test that password without uppercase fails."""
        no_upper = "nouppercase123!"
        is_valid, error = validate_password_strength(no_upper)
        assert is_valid is False
        assert "uppercase" in error.lower()

    def test_validate_password_strength_rejects_no_lowercase(self):
        """Test that password without lowercase fails."""
        no_lower = "NOLOWERCASE123!"
        is_valid, error = validate_password_strength(no_lower)
        assert is_valid is False
        assert "lowercase" in error.lower()

    def test_validate_password_strength_rejects_no_number(self):
        """Test that password without number fails."""
        no_number = "NoNumbers!"
        is_valid, error = validate_password_strength(no_number)
        assert is_valid is False
        assert "number" in error.lower()

    def test_validate_password_strength_rejects_no_special_char(self):
        """Test that password without special character fails."""
        no_special = "NoSpecial123"
        is_valid, error = validate_password_strength(no_special)
        assert is_valid is False
        assert "special" in error.lower()


class TestTokenCreation:
    """Tests for JWT token creation functions."""

    def test_create_access_token_creates_valid_jwt(self):
        """Test that create_access_token creates valid JWT."""
        data = {"sub": "test@example.com"}
        token = create_access_token(data)
        
        # Decode and verify
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["sub"] == "test@example.com"
        assert payload["type"] == "access"
        assert "exp" in payload

    def test_create_refresh_token_creates_valid_jwt(self):
        """Test that create_refresh_token creates valid JWT."""
        data = {"sub": "test@example.com"}
        token = create_refresh_token(data)
        
        # Decode and verify
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["sub"] == "test@example.com"
        assert payload["type"] == "refresh"
        assert "exp" in payload

    def test_create_access_token_has_correct_expiration(self):
        """Test that access token has correct expiration time."""
        from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES
        
        data = {"sub": "test@example.com"}
        token = create_access_token(data)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Check expiration is in the future
        exp_time = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
        now = datetime.now(timezone.utc)
        assert exp_time > now
        
        # Check expiration is approximately correct (within 1 minute)
        expected_exp = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        time_diff = abs((exp_time - expected_exp).total_seconds())
        assert time_diff < 60  # Within 1 minute

    def test_create_refresh_token_has_correct_expiration(self):
        """Test that refresh token has correct expiration time."""
        from app.core.security import REFRESH_TOKEN_EXPIRE_DAYS
        
        data = {"sub": "test@example.com"}
        token = create_refresh_token(data)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Check expiration is in the future
        exp_time = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
        now = datetime.now(timezone.utc)
        assert exp_time > now
        
        # Check expiration is approximately correct (within 1 day)
        expected_exp = now + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        time_diff = abs((exp_time - expected_exp).total_seconds())
        assert time_diff < 86400  # Within 1 day


class TestTokenVerification:
    """Tests for JWT token verification functions."""

    def test_verify_access_token_validates_access_tokens(self):
        """Test that verify_access_token validates access tokens correctly."""
        data = {"sub": "test@example.com"}
        token = create_access_token(data)
        
        payload = verify_access_token(token)
        assert payload["sub"] == "test@example.com"
        assert payload["type"] == "access"

    def test_verify_access_token_rejects_refresh_token(self):
        """Test that verify_access_token rejects refresh tokens."""
        from fastapi import HTTPException
        
        data = {"sub": "test@example.com"}
        refresh_token = create_refresh_token(data)
        
        with pytest.raises(HTTPException) as exc_info:
            verify_access_token(refresh_token)
        assert exc_info.value.status_code == 401

    def test_verify_access_token_rejects_invalid_token(self):
        """Test that verify_access_token rejects invalid tokens."""
        from fastapi import HTTPException
        
        with pytest.raises(HTTPException) as exc_info:
            verify_access_token("invalid.token.here")
        assert exc_info.value.status_code == 401

    def test_verify_refresh_token_validates_refresh_tokens(self):
        """Test that verify_refresh_token validates refresh tokens correctly."""
        data = {"sub": "test@example.com"}
        token = create_refresh_token(data)
        
        payload = verify_refresh_token(token)
        assert payload["sub"] == "test@example.com"
        assert payload["type"] == "refresh"

    def test_verify_refresh_token_rejects_access_token(self):
        """Test that verify_refresh_token rejects access tokens."""
        from fastapi import HTTPException
        
        data = {"sub": "test@example.com"}
        access_token = create_access_token(data)
        
        with pytest.raises(HTTPException) as exc_info:
            verify_refresh_token(access_token)
        assert exc_info.value.status_code == 401

    def test_verify_refresh_token_rejects_invalid_token(self):
        """Test that verify_refresh_token rejects invalid tokens."""
        from fastapi import HTTPException
        
        with pytest.raises(HTTPException) as exc_info:
            verify_refresh_token("invalid.token.here")
        assert exc_info.value.status_code == 401

    def test_verify_access_token_rejects_expired_token(self):
        """Test that verify_access_token rejects expired tokens."""
        from fastapi import HTTPException
        
        # Create expired token
        expired_time = datetime.now(timezone.utc) - timedelta(hours=1)
        expired_token = jwt.encode(
            {
                "sub": "test@example.com",
                "type": "access",
                "exp": expired_time
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        
        with pytest.raises(HTTPException) as exc_info:
            verify_access_token(expired_token)
        assert exc_info.value.status_code == 401

