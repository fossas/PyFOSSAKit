import pytest
from unittest.mock import patch, ANY
from unittest import mock
from unittest.mock import patch, MagicMock
from client import FOSSAClient
from models.project import Project
from models.user import User
from services import project_service
from services.project_service import get_project_details


class TestFOSSAClient:
    @patch('services.project_service.get_project_details')
    def test_get_project_details(self, mock_get_project_details):
        # Setup mock response
        mock_project = Project(locator="1", title="Test Project")
        mock_get_project_details.return_value = mock_project

        # Test get_project_details
        client = FOSSAClient(api_key='dummy_api_key')
        result = client.get_project_details('1')

        # Assertions to check the return type and expected data
        assert isinstance(result, Project)
        assert result.locator == "1"
        assert result.title == "Test Project"

        # Check that the service was called with the correct parameters
        mock_get_project_details.assert_called_once_with(client, '1')
    
    @patch.object(FOSSAClient, '_request', autospec=True)
    def test_export_project_issues_json(self, mock_request):
        # Given
        mock_request.return_value = {'issues': 'json_data'}
        client = FOSSAClient(api_key='dummy_api_key')
        project_locator = 'project_locator'
        revision_id = 'revision_id'
        
        # When
        result = client.export_project_issues_json(project_locator, revision_id)
        
        # Then
        assert result == {'issues': 'json_data'}
        mock_request.assert_called_once_with(client, 'GET', f'/projects/{project_locator}/export-issues/json', params={'revisionId': revision_id})

    @patch.object(FOSSAClient, '_request', autospec=True)
    def test_export_project_issues_csv(self, mock_request):
        # Given
        mock_request.return_value = 'csv_data'
        client = FOSSAClient(api_key='dummy_api_key')
        project_locator = 'project_locator'
        revision_id = 'revision_id'
        
        # When
        result = client.export_project_issues_csv(project_locator, revision_id)
        
        # Then
        assert result == 'csv_data'
        mock_request.assert_called_once_with(client, 'GET', f'/projects/{project_locator}/export-issues/csv', params={'revisionId': revision_id})

    @patch('services.project_service.list_projects')
    def test_list_projects(self, mock_list_projects):
        # Setup mock response
        mock_projects = [Project(locator="1", title="Test Project 1"), Project(locator="2", title="Test Project 2")]
        mock_list_projects.return_value = mock_projects

        # Test list_projects
        client = FOSSAClient(api_key='dummy_api_key')
        result = client.list_projects()

        # Assertions to check the return type and expected data
        assert all(isinstance(proj, Project) for proj in result)
        assert len(result) == 2
        assert result[0].locator == mock_projects[0].locator
        assert result[0].title == mock_projects[0].title

        # Check that the service was called
        mock_list_projects.assert_called_once_with(client)

    @patch('services.project_service.delete_project')
    def test_delete_project(self, mock_delete_project):
        # Setup mock response
        mock_delete_response = {"message": "Project deleted successfully."}
        mock_delete_project.return_value = mock_delete_response

        # Test delete_project
        client = FOSSAClient(api_key='dummy_api_key')
        project_id = 'project1'
        result = client.delete_project(project_id)

        # Assertions to check the return type and expected data
        assert result == mock_delete_response

        # Check that the service was called with the correct parameters
        mock_delete_project.assert_called_once_with(client, project_id)

    @patch('services.project_service.list_projects')
    def test_list_projects(self, mock_list_projects):
        # Given
        mock_list_projects.return_value = [MagicMock(), MagicMock()]  # Mock Project objects
        client = FOSSAClient(api_key='dummy_api_key')

        # When
        result = client.list_projects()

        # Then
        assert len(result) == 2  # assuming the mock returns two projects
        mock_list_projects.assert_called_once_with(client)

    @patch('services.project_service.delete_project')
    def test_delete_project(self, mock_delete_project):
        # Given
        mock_delete_project.return_value = {"message": "Project deleted successfully."}
        client = FOSSAClient(api_key='dummy_api_key')
        project_id = 'some_project_id'

        # When
        result = client.delete_project(project_id)

        # Then
        assert result == {"message": "Project deleted successfully."}
        mock_delete_project.assert_called_once_with(client, project_id)
    
    @patch('client.FOSSAClient._request')
    def test_list_project_revisions(self, mock_request):
        mock_request.return_value = ['revision1', 'revision2']
        client = FOSSAClient(api_key='dummy_api_key')
        project_id = 'project_id'

        result = client.list_project_revisions(project_id)

        assert result == ['revision1', 'revision2']
        mock_request.assert_called_once_with(
            'GET',
            '/revisions',
            params={'projectId': project_id}  # Reflect how params are passed in the actual implementation
        )