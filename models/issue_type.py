from enum import Enum

class IssueType(Enum):
    UNLICENSED_DEPENDENCY = "unlicensed_dependency"
    POLICY_CONFLICT = "policy_conflict"
    POLICY_FLAG = "policy_flag"
    VULNERABILITY = "vulnerability"
    OUTDATED_DEPENDENCY = "outdated_dependency"
    BLACKLISTED_DEPENDENCY = "blacklisted_dependency"