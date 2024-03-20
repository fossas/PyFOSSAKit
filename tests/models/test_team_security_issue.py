import pytest
from models.security_issue import SecurityIssue
from models.team_security_issue import TeamSecurityIssue

def test_team_security_issue_initialization():
    issue_data = {
        "cve": "CVE-1234-5678",
        "createdAt": "2023-03-21T00:00:00Z",
        "cveURL": "http://example.com/cve/CVE-1234-5678",
        "cvss": 7.5,
        "cwes": ["CWE-79", "CWE-20"],
        "description": "Example vulnerability description",
        "issuedOn": "2023-03-21",
        "projectId": "project-123",
        "references": ["http://example.com/vuln1", "http://example.com/vuln2"],
        "resolvedAt": "2023-03-22T00:00:00Z",
        "revisionId": "revision-456",
        "severity": 7.5,
        "severityType": "High"
    }

    team_id = 1  # Example team ID

    # Create an instance of TeamSecurityIssue
    team_issue = TeamSecurityIssue(teamId=team_id, **issue_data)

    # Verify that the TeamSecurityIssue instance has all the expected attributes from SecurityIssue
    for key, value in issue_data.items():
        assert getattr(team_issue, key) == value

    # Verify the teamId attribute
    assert team_issue.teamId == team_id