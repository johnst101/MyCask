# MyCask API Tests

This directory contains unit tests for the MyCask API endpoints.

## Running Tests

### Install Dependencies

First, make sure test dependencies are installed:

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_auth.py
pytest tests/test_users.py
pytest tests/test_auth_middleware.py
pytest tests/test_security.py
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Coverage Report

```bash
pytest --cov=app --cov-report=html
```

### Run Tests Matching a Pattern

```bash
pytest -k "test_register"
pytest -k "test_login"
```

## Test Structure

- `conftest.py` - Shared fixtures and test configuration
- `test_auth.py` - Authentication endpoint tests (register, login, refresh)
- `test_users.py` - User endpoint tests (GET /users/me)
- `test_auth_middleware.py` - Authentication middleware tests
- `test_security.py` - Security utility function tests

## Test Database

Tests use an in-memory SQLite database by default (configured in `conftest.py`). Each test gets a fresh database that is created before the test and dropped after.

To use a different test database, set the `TEST_DATABASE_URL` environment variable:

```bash
export TEST_DATABASE_URL="postgresql://user:pass@localhost/test_db"
pytest
```

## Writing New Tests

When adding new endpoints, create corresponding test files following the existing patterns:

1. Use fixtures from `conftest.py` (`client`, `test_db`, `test_user`, etc.)
2. Test both success and error cases
3. Use descriptive test names: `test_<endpoint>_<scenario>_<expected_result>`
4. Group related tests in classes

Example:

```python
def test_create_bottle_with_valid_data_succeeds(self, client, auth_headers):
    response = client.post(
        "/bottles",
        headers=auth_headers,
        json={"name": "Test Bottle", "distillery": "Test Distillery"}
    )
    assert response.status_code == status.HTTP_201_CREATED
```

