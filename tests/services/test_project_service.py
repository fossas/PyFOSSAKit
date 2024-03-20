import pytest
from unittest.mock import Mock
from services.project_service import get_project_details, list_projects, delete_project

@pytest.fixture
def mock_client():
    mock_client = Mock()
    mock_client._request.return_value = None  # Adjust based on expected response
    return mock_client

def test_get_project_details_calls_correct_endpoint(mock_client):
    project_id = "project123"
    get_project_details(mock_client, project_id)
    mock_client._request.assert_called_once_with('GET', f"/projects/{project_id}")

def test_list_projects_calls_correct_endpoint(mock_client):
    list_projects(mock_client)
    mock_client._request.assert_called_once_with('GET', "/projects")

def test_delete_project_calls_correct_endpoint_and_returns_confirmation(mock_client):
    project_id = "project123"
    response = delete_project(mock_client, project_id)
    mock_client._request.assert_called_once_with('DELETE', f"/projects/{project_id}")
    assert response == {"message": "Project deleted successfully."}