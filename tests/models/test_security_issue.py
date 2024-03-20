import pytest
from models.security_issue_severity import SecurityIssueSeverity

def test_security_issue_severity_initialization():
    # Initialize SecurityIssueSeverity with severity levels
    severity = SecurityIssueSeverity(critical=5.0, high=4.0, medium=3.0, low=2.0, unknown=1.0, total=15.0)

    # Assertions to verify that all attributes are correctly assigned
    assert severity.critical == 5.0
    assert severity.high == 4.0
    assert severity.medium == 3.0
    assert severity.low == 2.0
    assert severity.unknown == 1.0
    assert severity.total == 15.0
