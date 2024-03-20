from typing import List
from models.security_issue_severity import SecurityIssueSeverity

class ReleaseGroupOpenSecurityIssuesExposureWindow:
    def __init__(self, windows):
        if len(windows) != 4:
            raise ValueError("There must be exactly 4 exposure windows.")
        self.windows = windows