from models.security_issue_severity import SecurityIssueSeverity

class ReleaseGroupSecurityIssueSeverity:
    def __init__(self):
        self.severities = {}

    def add_severity(self, release_group_id, severity: SecurityIssueSeverity):
        self.severities[release_group_id] = severity

    def get_severity(self, release_group_id):
        return self.severities.get(release_group_id)

    def get_default_severity(self):
        return self.severities.get(None)