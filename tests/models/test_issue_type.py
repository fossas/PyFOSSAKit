import pytest
from models.issue_type import IssueType

def test_issue_type_enum_members():
    # Test that all expected members are present
    assert IssueType.UNLICENSED_DEPENDENCY.value == "unlicensed_dependency"
    assert IssueType.POLICY_CONFLICT.value == "policy_conflict"
    assert IssueType.POLICY_FLAG.value == "policy_flag"
    assert IssueType.VULNERABILITY.value == "vulnerability"
    assert IssueType.OUTDATED_DEPENDENCY.value == "outdated_dependency"
    assert IssueType.BLACKLISTED_DEPENDENCY.value == "blacklisted_dependency"

    # Test the number of members to ensure no unexpected members are present
    assert len(IssueType) == 6

def test_issue_type_enum_uniqueness():
    # Test that all values are unique
    values = [member.value for member in IssueType]
    assert len(values) == len(set(values)), "Enum values are not unique!"