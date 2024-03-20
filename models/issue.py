from typing import List, Any
from models.security_issue import SecurityIssue

class Issue:
    def __init__(self, id: int, type: Any, revisionId: str, resolved: bool, ruleId: int, vulnId: int, vulnerability: SecurityIssue, licenseId: int, parents: List[Any], createdAt: str, updatedAt: str):
        self.id = id
        self.type = type
        self.revisionId = revisionId
        self.resolved = resolved
        self.ruleId = ruleId
        self.vulnId = vulnId
        self.vulnerability = vulnerability
        self.licenseId = licenseId
        self.parents = parents
        self.createdAt = createdAt
        self.updatedAt = updatedAt
