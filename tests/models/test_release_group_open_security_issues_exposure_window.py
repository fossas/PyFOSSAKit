import pytest
from models.release_group_security_issue_severity import ReleaseGroupSecurityIssueSeverity
from models.security_issue_severity import SecurityIssueSeverity
from models.team_security_issue_severity import TeamSecurityIssueSeverity

def test_release_group_security_issue_severity():
    severity1 = SecurityIssueSeverity(critical=5, high=10, medium=15, low=20, unknown=0, total=50)
    severity2 = SecurityIssueSeverity(critical=3, high=8, medium=12, low=18, unknown=0, total=41)

    release_group_severity = ReleaseGroupSecurityIssueSeverity()

    release_group_id1 = "rg_123"
    release_group_id2 = "rg_456"
    release_group_severity.add_severity(release_group_id1, severity1)
    release_group_severity.add_severity(release_group_id2, severity2)

    assert release_group_severity.severities[release_group_id1] == severity1
    assert release_group_severity.severities[release_group_id2] == severity2

    assert release_group_severity.severities[release_group_id1].critical == 5
    assert release_group_severity.severities[release_group_id1].total == 50
    assert release_group_severity.severities[release_group_id2].critical == 3
    assert release_group_severity.severities[release_group_id2].total == 41