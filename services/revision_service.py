from models.revision import Revision

def list_revisions(client, project_id, offset=None, count=None):
    params = {}
    if offset is not None:
        params['offset'] = offset
    if count is not None:
        params['count'] = count
    return client._request('GET', f"/revisions", params={'projectId': project_id, **params})

def get_revision_dependencies(client, revision_locator):
    """Get dependencies for a specific project revision."""
    return client._request('GET', f'/revisions/{revision_locator}/dependencies')

def email_revision_attribution_report(client, revision_locator, format, email_address, **kwargs):
    """Email an attribution report for a specific project revision."""
    params = kwargs
    params['format'] = format
    params['emailAddress'] = email_address
    return client._request('GET', f'/revisions/{revision_locator}/attribution/email', params=params)

def get_revision_attribution_json(client, revision_locator, **kwargs):
    """Get JSON data for an attribution report for a specific project revision."""
    return client._request('GET', f'/revisions/{revision_locator}/attribution/json', params=kwargs)