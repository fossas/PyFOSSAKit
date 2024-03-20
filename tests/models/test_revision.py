import pytest
from models.revision import Revision

def test_revision_initialization():
    # Sample data to initialize a Revision instance
    loc = "locator_string"
    licenses = [{"name": "MIT"}]
    discovered_licenses = ["GPL-2.0"]
    locator = "another_locator_string"
    project_id = "project123"
    resolved = True
    unsupported = False
    parent_locator = "parent_locator_string"
    error = "error message"
    declared_license = "MIT"
    source_type = "git"
    author = "John Doe"
    unresolved_licensing_issue_count = 1
    unresolved_security_issue_count = 2
    unresolved_quality_issue_count = 3
    unresolved_issue_count = 6

    # Creating an instance of Revision
    revision = Revision(
        loc=loc,
        licenses=licenses,
        discoveredLicenses=discovered_licenses,
        locator=locator,
        projectId=project_id,
        resolved=resolved,
        unsupported=unsupported,
        parent_locator=parent_locator,
        error=error,
        declaredLicense=declared_license,
        source_type=source_type,
        author=author,
        unresolved_licensing_issue_count=unresolved_licensing_issue_count,
        unresolved_security_issue_count=unresolved_security_issue_count,
        unresolved_quality_issue_count=unresolved_quality_issue_count,
        unresolved_issue_count=unresolved_issue_count
    )

    # Assertions to verify that the properties are set correctly
    assert revision.loc == loc
    assert revision.licenses == licenses
    assert revision.discoveredLicenses == discovered_licenses
    assert revision.locator == locator
    assert revision.projectId == project_id
    assert revision.resolved == resolved
    assert revision.unsupported == unsupported
    assert revision.parent_locator == parent_locator
    assert revision.error == error
    assert revision.declaredLicense == declared_license
    assert revision.source_type == source_type
    assert revision.author == author
    assert revision.unresolved_licensing_issue_count == unresolved_licensing_issue_count
    assert revision.unresolved_security_issue_count == unresolved_security_issue_count
    assert revision.unresolved_quality_issue_count == unresolved_quality_issue_count
    assert revision.unresolved_issue_count == unresolved_issue_count

    # Testing default values
    # Create a new Revision with minimum parameters
    revision_defaults = Revision(loc=loc)
    assert revision_defaults.licenses == []
    assert revision_defaults.discoveredLicenses == []
