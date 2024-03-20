import pytest
from models.team_open_security_issue_over_time import TeamOpenSecurityIssueOverTime
from models.security_issue_severity import SecurityIssueSeverity

def test_team_open_security_issue_over_time_initialization():
    # Given values for initialization
    team_id = 1
    test_date = "2023-03-20"
    issue_severity = SecurityIssueSeverity(critical=5.0, high=4.0, medium=3.0, low=2.0, unknown=1.0, total=15.0)

    # Initialize TeamOpenSecurityIssueOverTime with the given values
    team_open_issue_over_time = TeamOpenSecurityIssueOverTime(team_id=team_id, date=test_date, issue_severity=issue_severity)

    # Assertions to verify initialization
    assert team_open_issue_over_time.date == test_date
    # Verify that the severity is correctly associated with the date
    retrieved_severity = team_open_issue_over_time.get_severity(test_date)
    assert retrieved_severity == issue_severity

    # Verify that the team_id is correctly set
    assert team_open_issue_over_time.team_id == team_id
