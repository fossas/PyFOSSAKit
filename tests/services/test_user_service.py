import pytest
from unittest.mock import Mock, patch
from services.user_service import list_users, get_user, delete_user, set_user_permission, enable_disable_user, set_user_team_roles, list_roles, list_teams, create_team, update_team, assign_team_projects, edit_team_users, invite_user_to_organization

@pytest.fixture
def mock_client():
    mock_client = Mock()
    mock_client._request.return_value = None  # Adjust based on expected response
    return mock_client

def test_list_users_calls_correct_endpoint(mock_client):
    email = "test@example.com"
    list_users(mock_client, email=email)
    mock_client._request.assert_called_once_with('GET', "/users", params={'email': email})

def test_get_user_calls_correct_endpoint(mock_client):
    user_id = 1
    get_user(mock_client, user_id)
    mock_client._request.assert_called_once_with('GET', f"/users/{user_id}")

def test_delete_user_calls_correct_endpoint(mock_client):
    user_id = 1
    response = delete_user(mock_client, user_id)
    mock_client._request.assert_called_once_with('DELETE', f"/users/{user_id}")
    assert response == {"message": "User deleted successfully."}

def test_set_user_permission_calls_correct_endpoint(mock_client):
    user_id = 1
    role_id = 2
    set_user_permission(mock_client, user_id, role_id)
    mock_client._request.assert_called_once_with('PUT', f"/user/{user_id}/permission", data={'roleId': role_id})

def test_enable_disable_user_calls_correct_endpoint(mock_client):
    user_id = 1
    enabled = True
    enable_disable_user(mock_client, user_id, enabled)
    mock_client._request.assert_called_once_with('PUT', f"/user/{user_id}/enabled", data={'enabled': enabled})

def test_set_user_team_roles_calls_correct_endpoint(mock_client):
    user_id = 1
    team_roles = [{"teamId": 1, "roleId": 2}]
    set_user_team_roles(mock_client, user_id, team_roles)
    mock_client._request.assert_called_once_with('PUT', f"/user/{user_id}/team-roles", json=team_roles)

def test_list_roles_calls_correct_endpoint(mock_client):
    list_roles(mock_client)
    mock_client._request.assert_called_once_with('GET', "/roles")

def test_list_teams_calls_correct_endpoint(mock_client):
    list_teams(mock_client)
    mock_client._request.assert_called_once_with('GET', "/teams")

def test_create_team_calls_correct_endpoint(mock_client):
    team_data = {"name": "Team 1"}
    create_team(mock_client, team_data)
    mock_client._request.assert_called_once_with('POST', "/teams", json=team_data)

def test_update_team_calls_correct_endpoint(mock_client):
    team_id = 1
    team_data = {"name": "Updated Team 1"}
    update_team(mock_client, team_id, team_data)
    mock_client._request.assert_called_once_with('PUT', f"/teams/{team_id}", json=team_data)

def test_assign_team_projects_calls_correct_endpoint(mock_client):
    team_id = 1
    projects = ["project1", "project2"]
    assign_team_projects(mock_client, team_id, projects)
    mock_client._request.assert_called_once_with('PUT', f"/teams/{team_id}/projects", json={'projects': projects})

def test_edit_team_users_calls_correct_endpoint(mock_client):
    team_id = 1
    action = "add"
    users = [{"userId": 1}, {"userId": 2}]
    edit_team_users(mock_client, team_id, action, users)
    mock_client._request.assert_called_once_with('PUT', f"/teams/{team_id}/users", json={'action': action, 'users': users})

def test_invite_user_to_organization_calls_correct_endpoint(mock_client):
    organization_id = 1
    emails = ["user1@example.com", "user2@example.com"]
    invite_user_to_organization(mock_client, organization_id, emails)
    mock_client._request.assert_called_once_with('POST', f"/organizations/{organization_id}/invite", json={'emails': emails})