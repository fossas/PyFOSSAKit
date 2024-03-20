import pytest
from unittest.mock import Mock
from services.revision_service import list_revisions, get_revision_dependencies, email_revision_attribution_report, get_revision_attribution_json

@pytest.fixture
def mock_client():
    mock_client = Mock()
    mock_client._request.return_value = None  # Adjust based on expected response
    return mock_client

def test_list_revisions_calls_correct_endpoint(mock_client):
    project_id = "project123"
    offset = 10
    count = 20
    list_revisions(mock_client, project_id, offset=offset, count=count)
    mock_client._request.assert_called_once_with('GET', "/revisions", params={'projectId': project_id, 'offset': offset, 'count': count})

def test_get_revision_dependencies_calls_correct_endpoint(mock_client):
    revision_locator = "revision123"
    get_revision_dependencies(mock_client, revision_locator)
    mock_client._request.assert_called_once_with('GET', f'/revisions/{revision_locator}/dependencies')

def test_email_revision_attribution_report_calls_correct_endpoint(mock_client):
    revision_locator = "revision123"
    format = "pdf"
    email_address = "test@example.com"
    email_revision_attribution_report(mock_client, revision_locator, format, email_address)
    mock_client._request.assert_called_once_with('GET', f'/revisions/{revision_locator}/attribution/email', params={'format': format, 'emailAddress': email_address})

def test_get_revision_attribution_json_calls_correct_endpoint(mock_client):
    revision_locator = "revision123"
    get_revision_attribution_json(mock_client, revision_locator)
    mock_client._request.assert_called_once_with('GET', f'/revisions/{revision_locator}/attribution/json', params={})