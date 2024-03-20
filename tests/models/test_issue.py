import pytest
from models.issue import Issue
from models.security_issue import SecurityIssue

def test_issue_initialization():
    # Create a SecurityIssue instance for testing
    security_issue = SecurityIssue(
        cve="CVE-1234-5678",
        createdAt="2022-01-01",
        cveURL="https://example.com/cve-1234-5678",
        cvss=5.0,
        cwes=["CWE-123", "CWE-456"],
        description="Example vulnerability description.",
        issuedOn="2022-01-02",
        projectId="project-123",
        references=["https://reference1.com", "https://reference2.com"],
        resolvedAt="2022-03-01",
        revisionId="rev-123",
        severity=7.5,
        severityType="High"
    )

    # Create an Issue instance with various parameters
    issue = Issue(
        id=123,
        type="ExampleType",
        revisionId="rev-123",
        resolved=False,
        ruleId=456,
        vulnId=789,
        vulnerability=security_issue,
        licenseId=101112,
        parents=[],
        createdAt="2022-01-01",
        updatedAt="2022-02-01"
    )

    # Assert that Issue attributes are set correctly
    assert issue.id == 123
    assert issue.type == "ExampleType"
    assert issue.revisionId == "rev-123"
    assert issue.resolved == False
    assert issue.ruleId == 456
    assert issue.vulnId == 789
    assert issue.licenseId == 101112
    assert issue.parents == []
    assert issue.createdAt == "2022-01-01"
    assert issue.updatedAt == "2022-02-01"

    # Now check attributes of the nested SecurityIssue object
    assert issue.vulnerability.cve == "CVE-1234-5678"
    assert issue.vulnerability.createdAt == "2022-01-01"
    assert issue.vulnerability.cveURL == "https://example.com/cve-1234-5678"
    assert issue.vulnerability.cvss == 5.0
    assert issue.vulnerability.cwes == ["CWE-123", "CWE-456"]
    assert issue.vulnerability.description == "Example vulnerability description."
    assert issue.vulnerability.issuedOn == "2022-01-02"
    assert issue.vulnerability.projectId == "project-123"
    assert issue.vulnerability.references == ["https://reference1.com", "https://reference2.com"]
    assert issue.vulnerability.resolvedAt == "2022-03-01"
    assert issue.vulnerability.revisionId == "rev-123"
    assert issue.vulnerability.severity == 7.5
    assert issue.vulnerability.severityType == "High"