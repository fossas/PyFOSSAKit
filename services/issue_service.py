from models.issue import Issue

def export_issues_json(client, project_locator, revision_id=None):
    """
    Returns all issues for a project in JSON format.
    """
    params = {'revisionId': revision_id} if revision_id else {}
    return client._request('GET', f'/projects/{project_locator}/export-issues/json', params=params)

def export_issues_csv(client, project_locator, revision_id=None):
    """
    Returns all issues for a project in CSV format.
    """
    params = {'revisionId': revision_id} if revision_id else {}
    return client._request('GET', f'/projects/{project_locator}/export-issues/csv', params=params)

def get_security_issues_by_team(client):
    response = client.session.get(f"{client.base_url}/organizations/issues/security/teams")
    response.raise_for_status()
    return response.json()

def get_security_issues_by_release_group(client):
    response = client.session.get(f"{client.base_url}/organizations/issues/security/release_groups")
    response.raise_for_status()
    return response.json()

def list_issues(client, scan_scope=None, count=None, offset=None, status=None, issue_type=None):
    params = {k: v for k, v in locals().items() if v is not None and k != 'self'}
    if scan_scope:
        params.update({f'scanScope[{k}]': v for k, v in scan_scope.items()})
    response = client.session.get(f"{client.base_url}/issues", params=params)
    response.raise_for_status()
    return response.json()