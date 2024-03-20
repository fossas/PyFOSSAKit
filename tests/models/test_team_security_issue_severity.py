import pytest
from models.team_security_issue_severity import TeamSecurityIssueSeverity
from models.security_issue_severity import SecurityIssueSeverity

def test_team_security_issue_severity_add_and_get():
    # Initialize TeamSecurityIssueSeverity with a team_id
    team_id = 1
    team_severity = TeamSecurityIssueSeverity(team_id=team_id)

    # Create instances of SecurityIssueSeverity
    severity1 = SecurityIssueSeverity(critical=5.0, high=4.0, medium=3.0, low=2.0, unknown=1.0, total=15.0)
    severity2 = SecurityIssueSeverity(critical=4.0, high=3.0, medium=2.0, low=1.0, unknown=0.5, total=10.5)

    # Add severities with unique identifiers
    identifier1 = "2023-03-21"
    identifier2 = "2023-03-22"
    team_severity.add_severity(identifier1, severity1)
    team_severity.add_severity(identifier2, severity2)

    # Retrieve and verify severities
    assert team_severity.get_severity(identifier1) == severity1
    assert team_severity.get_severity(identifier2) == severity2

    # Verify that retrieving a non-existent severity returns None
    assert team_severity.get_severity("non-existent") is None

    # Verify team_id is set correctly
    assert team_severity.team_id == team_id