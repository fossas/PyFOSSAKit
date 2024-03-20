from models.security_issue import SecurityIssue

class TeamSecurityIssue(SecurityIssue):
    def __init__(self, teamId, **kwargs):
        super().__init__(**kwargs)
        self.teamId = teamId