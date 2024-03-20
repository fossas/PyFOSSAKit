import pytest
from models.release_group_open_security_issue_over_time import ReleaseGroupOpenSecurityIssueOverTime
from models.release_group_security_issue_severity import ReleaseGroupSecurityIssueSeverity
from models.security_issue_severity import SecurityIssueSeverity
from models.team_open_security_issue_over_time import TeamSecurityIssueSeverity

def test_release_group_open_security_issue_over_time_creation():
    severity_instance = SecurityIssueSeverity(critical=5, high=10, medium=15, low=20, unknown=0, total=50)
    release_group_severity = ReleaseGroupSecurityIssueSeverity()
    release_group_severity.add_severity("some_release_group_id", severity_instance)

    date = "2021-01-01"
    issue_over_time = ReleaseGroupOpenSecurityIssueOverTime(date=date, security_issue_severity=release_group_severity)

    assert issue_over_time.date == date
    assert issue_over_time.security_issue_severity.get_severity("some_release_group_id") == severity_instance