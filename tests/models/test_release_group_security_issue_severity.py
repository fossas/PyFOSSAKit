import pytest
from models.release_group_security_issue_severity import ReleaseGroupSecurityIssueSeverity
from models.security_issue_severity import SecurityIssueSeverity

def test_add_and_get_severity():
    severity1 = SecurityIssueSeverity(critical=10, high=5, medium=2, low=1, unknown=0, total=18)
    severity2 = SecurityIssueSeverity(critical=8, high=4, medium=3, low=2, unknown=0, total=17)

    release_group_severity = ReleaseGroupSecurityIssueSeverity()

    release_group_severity.add_severity("rg1", severity1)
    release_group_severity.add_severity("rg2", severity2)

    assert release_group_severity.get_severity("rg1") == severity1
    assert release_group_severity.get_severity("rg2") == severity2

def test_get_severity_with_invalid_id_returns_none():
    release_group_severity = ReleaseGroupSecurityIssueSeverity()

    assert release_group_severity.get_severity("non_existing_id") is None

def test_get_default_severity():
    default_severity = SecurityIssueSeverity(critical=0, high=0, medium=0, low=0, unknown=0, total=0)

    release_group_severity = ReleaseGroupSecurityIssueSeverity()
    release_group_severity.add_severity(None, default_severity)

    assert release_group_severity.get_default_severity() == default_severity