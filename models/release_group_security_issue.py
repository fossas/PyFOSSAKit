class CVE:
    def __init__(self, cve, cwe, cvss):
        self.cve = cve
        self.cwe = cwe
        self.cvss = cvss

class CWE:
    def __init__(self, cwe, title):
        self.cwe = cwe
        self.title = title

class Revision:
    def __init__(self, fetcher, package, revision):
        self.fetcher = fetcher
        self.package = package
        self.revision = revision

class ReleaseGroupSecurityIssue:
    def __init__(self, release_group_id, cve, created_at, cvss, cwe, description, issued_on, project_id, references, resolved_at, revision, revision_id, severity, severity_type):
        self.release_group_id = release_group_id
        self.cve = CVE(**cve)
        self.created_at = created_at
        self.cvss = cvss
        self.cwe = CWE(**cwe)
        self.description = description
        self.issued_on = issued_on
        self.project_id = project_id
        self.references = references
        self.resolved_at = resolved_at
        self.revision = Revision(**revision)
        self.revision_id = revision_id
        self.severity = severity
        self.severity_type = severity_type