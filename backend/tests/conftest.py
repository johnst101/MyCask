"""
Pytest configuration and shared fixtures for testing.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os
from dotenv import load_dotenv

from app.db.database import Base, get_db
from app.main import app
from app.models import (
    User, Bottle, UserBottle, BottlePurchase, BottlePrice,
    Tasting, TastingFlavor, FlavorTag, Wishlist
)  # Import all models so tables are created
from app.core.security import hash_password, create_access_token, create_refresh_token
from app.services.user import create_user

load_dotenv()

# Use SQLite in-memory database for testing
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL", 
    "sqlite:///:memory:"
)

# Create test engine with SQLite
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in TEST_DATABASE_URL else {},
    poolclass=StaticPool if "sqlite" in TEST_DATABASE_URL else None,
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def test_db():
    """
    Create a fresh database for each test.
    Creates tables, yields a session, then drops tables.
    """
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def client(test_db):
    """
    Create a test client with overridden database dependency.
    """
    def override_get_db():
        try:
            yield test_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(test_db):
    """
    Create a test user in the database.
    """
    user = create_user(
        test_db,
        email="test@example.com",
        password_hash=hash_password("TestPassword123!"),
        username="testuser",
        first_name="Test",
        last_name="User"
    )
    return user


@pytest.fixture
def inactive_user(test_db):
    """
    Create an inactive (soft-deleted) test user.
    """
    user = create_user(
        test_db,
        email="inactive@example.com",
        password_hash=hash_password("TestPassword123!"),
        username="inactiveuser",
        first_name="Inactive",
        last_name="User"
    )
    user.is_active = False
    test_db.commit()
    test_db.refresh(user)
    return user


@pytest.fixture
def auth_headers(test_user):
    """
    Generate authentication headers with valid access token.
    """
    access_token = create_access_token(data={"sub": test_user.email})
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture
def refresh_token(test_user):
    """
    Generate a refresh token for testing.
    """
    return create_refresh_token(data={"sub": test_user.email})

