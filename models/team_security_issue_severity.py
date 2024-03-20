from typing import Dict
from models.security_issue_severity import SecurityIssueSeverity

class TeamSecurityIssueSeverity:
    def __init__(self, team_id: int):
        self.team_id = team_id
        self.severities: Dict[str, SecurityIssueSeverity] = {}

    def add_severity(self, identifier: str, severity: SecurityIssueSeverity):
        self.severities[identifier] = severity

    def get_severity(self, identifier: str) -> SecurityIssueSeverity:
        return self.severities.get(identifier)