import pytest
from models.team_open_security_issues_exposure_windows import TeamOpenSecurityIssuesExposureWindows
from models.team_security_issue_severity import TeamSecurityIssueSeverity
from models.security_issue_severity import SecurityIssueSeverity

def create_team_security_issue_severity(critical, high, medium, low, unknown, total):
    # This function simulates creating a TeamSecurityIssueSeverity instance
    severity = SecurityIssueSeverity(critical=critical, high=high, medium=medium, low=low, unknown=unknown, total=total)
    return TeamSecurityIssueSeverity(team_id=1, severity=severity)

def test_team_open_security_issues_exposure_windows_initialization():
    # Create instances of TeamSecurityIssueSeverity and add severities
    windows = []
    for i in range(4):
        team_issue_severity = TeamSecurityIssueSeverity(team_id=i)
        severity = SecurityIssueSeverity(critical=i+5.0, high=i+4.0, medium=i+3.0, low=i+2.0, unknown=i+1.0, total=i+15.0)
        team_issue_severity.add_severity(f'window{i}', severity)
        windows.append(team_issue_severity)
    
    # Initialize TeamOpenSecurityIssuesExposureWindows with the created windows
    exposure_windows = TeamOpenSecurityIssuesExposureWindows(exposure_windows=windows)
    
    # Assertions to verify that there are exactly 4 exposure windows
    assert len(exposure_windows.exposure_windows) == 4
    for window in exposure_windows.exposure_windows:
        assert isinstance(window, TeamSecurityIssueSeverity)