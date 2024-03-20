from typing import List
from models.team_security_issue_severity import TeamSecurityIssueSeverity

class TeamOpenSecurityIssuesExposureWindows:
    def __init__(self, exposure_windows: List[TeamSecurityIssueSeverity]):
        if len(exposure_windows) != 4:
            raise ValueError("There must be exactly 4 exposure windows.")
        self.exposure_windows = exposure_windows