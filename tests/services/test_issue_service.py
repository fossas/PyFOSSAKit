import pytest
from unittest.mock import Mock, patch
from services.issue_service import export_issues_json

@pytest.fixture
def mock_client():
    mock_client = Mock()
    mock_client._request.return_value = [{"issue_id": 1, "description": "Test Issue"}]
    return mock_client

def test_export_issues_json_calls_correct_endpoint(mock_client):
    project_locator = "project123"
    export_issues_json(mock_client, project_locator)
    mock_client._request.assert_called_once_with('GET', f'/projects/{project_locator}/export-issues/json', params={})

def test_export_issues_json_returns_parsed_response(mock_client):
    project_locator = "project123"
    expected_issues = [{"issue_id": 1, "description": "Test Issue"}]
    issues = export_issues_json(mock_client, project_locator)
    assert issues == expected_issues




