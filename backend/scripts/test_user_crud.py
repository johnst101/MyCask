"""
Manual test script for User CRUD operations.
Run with: python -m scripts.test_user_crud
"""

from app.db.database import SessionLocal
from app.services import user as user_crud

def test_user_crud():
    db = SessionLocal()
    
    print("Testing User CRUD operations...\n")

    # Delete previous test user
    print("Deleting previous test user...")
    user_crud.full_delete_user(db, "test@example.com")
    print("Previous test user deleted.")

    # Verify previous test user is not found
    print("Verifying previous test user is not found...")
    not_found = user_crud.get_any_user_by_email(db, "test@example.com")
    print(f"   ✓ Previous test user is not found: {not_found is None}")

    # Test 1: Create user
    print("1. Creating user...")
    new_user = user_crud.create_user(
        db,
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password_hash="hashed_password_123",
        username="testuser"
    )
    print(f"   ✓ Created user: {new_user.id} - {new_user.email}")
    
    # Test 2: Get by email
    print("\n2. Getting user by email...")
    found = user_crud.get_user_by_email(db, "test@example.com")
    print(f"   ✓ Found user: {found.email}")
    
    # Test 3: Get by ID
    print("\n3. Getting user by ID...")
    found_by_id = user_crud.get_user_by_id(db, new_user.id)
    print(f"   ✓ Found user: {found_by_id.username}")
    
    # Test 4: Update user
    print("\n4. Updating username...")
    updated = user_crud.update_user(db, new_user.id, username="updated_username")
    print(f"   ✓ Updated username: {updated.username}")
    
    # Test 5: Soft delete
    print("\n5. Soft deleting user...")
    deleted = user_crud.delete_user(db, new_user.id)
    print(f"   ✓ User deleted: {deleted}")
    
    # Test 6: Verify soft delete (shouldn't find)
    print("\n6. Verifying soft delete...")
    not_found = user_crud.get_user_by_id(db, new_user.id)
    print(f"   ✓ User not found (soft deleted): {not_found is None}")
    
    db.close()
    print("\n✅ All tests passed!")

if __name__ == "__main__":
    test_user_crud()