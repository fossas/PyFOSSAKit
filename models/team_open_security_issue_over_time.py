from models.team_security_issue_severity import TeamSecurityIssueSeverity

class TeamOpenSecurityIssueOverTime(TeamSecurityIssueSeverity):
    def __init__(self, team_id: int, date: str, issue_severity=None):
        super().__init__(team_id=team_id)
        self.date = date
        if issue_severity is not None:
            self.add_severity(self.date, issue_severity)