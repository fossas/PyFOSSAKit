from models.release_group_security_issue_severity import ReleaseGroupSecurityIssueSeverity

class ReleaseGroupOpenSecurityIssueOverTime:
    def __init__(self, date: str, security_issue_severity: ReleaseGroupSecurityIssueSeverity):
        self.date = date
        self.security_issue_severity = security_issue_severity