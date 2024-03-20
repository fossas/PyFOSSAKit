import requests
from typing import List, Dict
import logging
from models.project import Project
from models.user import User
from models.issue import Issue
from services import user_service
from services import project_service
from services import vulns_service
from services import issue_service
from models.vulnerability import Vulnerability
from services.issue_service import list_issues,get_security_issues_by_release_group,get_security_issues_by_team, export_issues_csv,export_issues_json
from services.project_service import delete_project,list_projects,get_project_details
from services.revision_service import get_revision_attribution_json,email_revision_attribution_report,get_revision_dependencies,list_revisions
from services.user_service import invite_user_to_organization, edit_team_users, assign_team_projects,update_team,create_team,list_teams,list_roles,set_user_team_roles,enable_disable_user,set_user_permission,delete_user,get_user,list_users
from services.vulns_service import get_vulnerabilities_by_locator, get_next_safe_versions, get_next_safe_version_for_revision
from config import API_KEY, BASE_URL

class FOSSAClient:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"token {self.api_key}"})
        # ... rest of your client code
logging.basicConfig(level=logging.INFO)

class FOSSAClientError(Exception):
    """A custom exception for the FOSSA client."""

class FOSSAClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://app.fossa.com/api"
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"token {self.api_key}"})

    def _request(self, method: str, endpoint: str, data: Dict = None, params: Dict = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, json=data, params=params)
            response.raise_for_status()
            return response.json() if response.content else {}
        except requests.exceptions.HTTPError as err:
            error_msg = f"HTTP error occurred: {err}; Status Code: {err.response.status_code}"
            if err.response.content:
                try:
                    error_details = err.response.json()
                    error_msg += f"; Details: {error_details}"
                except ValueError:
                    error_msg += f"; Response: {err.response.text}"
            logging.error(error_msg)
            raise FOSSAClientError(error_msg) from err
        except requests.exceptions.RequestException as err:
            logging.error(f"Error occurred: {err}")
            raise FOSSAClientError(f"Error occurred: {err}") from err

    # Project-related methods
    def export_project_issues_json(self, project_locator, revision_id=None):
        return export_issues_json(self, project_locator, revision_id)

    def export_project_issues_csv(self, project_locator, revision_id=None):
        return export_issues_csv(self, project_locator, revision_id)

    def get_project_details(self, project_id: str) -> Project:
        return project_service.get_project_details(self, project_id)

    def list_projects(self) -> List[Project]:
        return project_service.list_projects(self)

    def delete_project(self, project_id: str) -> Dict:
        return project_service.delete_project(self, project_id)
    
    #Revision-related methods
    def list_project_revisions(self, project_id, offset=None, count=None):
        return list_revisions(self, project_id, offset, count)

    def get_revision_dependencies(self, revision_locator: str):
        return get_revision_dependencies(self, revision_locator)

    def email_revision_attribution_report(self, revision_locator: str, format: str, email_address: str, **kwargs):
        return email_revision_attribution_report(self, revision_locator, format, email_address, **kwargs)

    def get_revision_attribution_json(self, revision_locator: str, **kwargs):
        return get_revision_attribution_json(self, revision_locator, **kwargs)

    # User-related methods
    def list_users(self, email=None) -> List[User]:
        return user_service.list_users(self, email)

    def get_user(self, user_id: int) -> User:
        return user_service.get_user(self, user_id)

    def delete_user(self, user_id: int) -> Dict:
        return user_service.delete_user(self, user_id)

    def set_user_permission(self, user_id: int, role_id: int) -> Dict:
        return user_service.set_user_permission(self, user_id, role_id)

    def enable_disable_user(self, user_id: int, enabled: bool) -> Dict:
        return user_service.enable_disable_user(self, user_id, enabled)

    def set_user_team_roles(self, user_id: int, team_roles: List[Dict]) -> Dict:
        return user_service.set_user_team_roles(self, user_id, team_roles)

    def list_roles(self) -> List[Dict]:
        return user_service.list_roles(self)

    def list_teams(self) -> List[Dict]:
        return user_service.list_teams(self)

    def create_team(self, team_data: Dict) -> Dict:
        return user_service.create_team(self, team_data)

    def update_team(self, team_id: int, team_data: Dict) -> Dict:
        return user_service.update_team(self, team_id, team_data)

    def assign_team_projects(self, team_id: int, projects: List[str]) -> Dict:
        return user_service.assign_team_projects(self, team_id, projects)

    def edit_team_users(self, team_id: int, action: str, users: List[Dict]) -> Dict:
        return user_service.edit_team_users(self, team_id, action, users)

    def invite_user_to_organization(self, organization_id: int, emails: List[str]) -> Dict:
        return user_service.invite_user_to_organization(self, organization_id, emails)

    # Issue-related methods
    def get_security_issues_by_team(self) -> List[Issue]:
        return issue_service.get_security_issues_by_team(self)

    def get_security_issues_by_release_group(self) -> List[Issue]:
        return issue_service.get_security_issues_by_release_group(self)

    def list_issues(self, scan_scope: Dict = None, count: int = None, offset: int = None, status: str = None, issue_type: str = None) -> List[Issue]:
        return issue_service.list_issues(self, scan_scope, count, offset, status, issue_type)

    # Vulnerability-related methods
    def get_next_safe_version_for_revision(self, revision_locator: str) -> Dict:
        return vulns_service.get_next_safe_version_for_revision(self, revision_locator)

    def get_next_safe_versions(self, revisions: List[str]) -> List[Dict]:
        return vulns_service.get_next_safe_versions(self, revisions)

    def get_vulnerabilities_by_locator(self, locators: List[str]) -> List[Vulnerability]:
        return vulns_service.get_vulnerabilities_by_locator(self, locators)