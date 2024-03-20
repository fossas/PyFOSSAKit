from typing import List

class SecurityIssue:
    def __init__(self, cve: str, createdAt: str, cveURL: str, cvss: float, cwes: List[str], description: str, issuedOn: str, projectId: str, references: List[str], resolvedAt: str, revisionId: str, severity: float, severityType: str):
        self.cve = cve
        self.createdAt = createdAt
        self.cveURL = cveURL
        self.cvss = cvss
        self.cwes = cwes
        self.description = description
        self.issuedOn = issuedOn
        self.projectId = projectId
        self.references = references
        self.resolvedAt = resolvedAt
        self.revisionId = revisionId
        self.severity = severity
        self.severityType = severityType