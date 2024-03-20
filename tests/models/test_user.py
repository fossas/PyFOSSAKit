import pytest
from models.user import User

def test_user_initialization():
    # Example data for initializing a User
    user_data = {
        "id": "user-123",
        "organizationId": "org-456",
        "email": "user@example.com",
        "username": "user123",
        "full_name": "User Name",
        "sso_only": False,
        "userRole": "admin",
        "enabled": True,
        "teamUsers": ["team-1", "team-2"],
        "email_verified": True,
        "tokens": ["token1", "token2"]
    }

    # Create an instance of User
    user = User(**user_data)

    # Verify that each attribute is correctly assigned
    assert user.id == user_data["id"]
    assert user.organizationId == user_data["organizationId"]
    assert user.email == user_data["email"]
    assert user.username == user_data["username"]
    assert user.full_name == user_data["full_name"]
    assert user.sso_only == user_data["sso_only"]
    assert user.userRole == user_data["userRole"]
    assert user.enabled == user_data["enabled"]
    assert user.teamUsers == user_data["teamUsers"]
    assert user.email_verified == user_data["email_verified"]
    assert user.tokens == user_data["tokens"]

    # Verify default values for optional parameters
    user_with_defaults = User(id="user-124")
    assert user_with_defaults.teamUsers == []
    assert user_with_defaults.tokens == []
