from models.vulnerability import Vulnerability

def get_next_safe_version_for_revision(client, revision_locator):
    return client._request('GET', f'/vulns/revisions/{revision_locator}/next-safe-version')

def get_next_safe_versions(client, revisions):
    data = {"revisions": revisions}
    return client._request('POST', '/vulns/revisions/next-safe-version', data=data)

def get_vulnerabilities_by_locator(client, locators):
    data = {"locators": locators}
    return client._request('POST', '/vulns/by-locator', data=data)