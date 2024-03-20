import pytest
from models.project import Project

def test_project_creation():
    # Setup data
    locator = "project-locator"
    title = "Project Title"
    description = "Detailed description of the project."
    public = True
    policyId = 1
    securityPolicyId = 2
    qualityPolicyId = 3
    authors = ["Author 1", "Author 2"]
    organizationId = 4
    last_analyzed_revision = "revision-id"
    issue_tracker_url = "https://issue.tracker"
    issue_tracker_id = "tracker-id"
    issue_tracker_type = "tracker-type"
    createdAt = "2021-01-01T00:00:00"
    updatedAt = "2021-01-02T00:00:00"
    revisions = ["rev1", "rev2"]

    # Create a Project instance with all fields provided
    project = Project(
        locator=locator,
        title=title,
        description=description,
        public=public,
        policyId=policyId,
        securityPolicyId=securityPolicyId,
        qualityPolicyId=qualityPolicyId,
        authors=authors,
        organizationId=organizationId,
        last_analyzed_revision=last_analyzed_revision,
        issue_tracker_url=issue_tracker_url,
        issue_tracker_id=issue_tracker_id,
        issue_tracker_type=issue_tracker_type,
        createdAt=createdAt,
        updatedAt=updatedAt,
        revisions=revisions
    )

    # Assertions to verify that all attributes are correctly assigned
    assert project.locator == locator
    assert project.title == title
    assert project.description == description
    assert project.public is public
    assert project.policyId == policyId
    assert project.securityPolicyId == securityPolicyId
    assert project.qualityPolicyId == qualityPolicyId
    assert project.authors == authors
    assert project.organizationId == organizationId
    assert project.last_analyzed_revision == last_analyzed_revision
    assert project.issue_tracker_url == issue_tracker_url
    assert project.issue_tracker_id == issue_tracker_id
    assert project.issue_tracker_type == issue_tracker_type
    assert project.createdAt == createdAt
    assert project.updatedAt == updatedAt
    assert project.revisions == revisions

    # Test default values for optional parameters
    default_project = Project(locator="default-locator", title="Default Title")
    assert default_project.description is None
    assert default_project.public is None
    assert default_project.policyId is None
    assert default_project.securityPolicyId is None
    assert default_project.qualityPolicyId is None
    assert default_project.authors == []
    assert default_project.organizationId is None
    assert default_project.last_analyzed_revision is None
    assert default_project.issue_tracker_url is None
    assert default_project.issue_tracker_id is None
    assert default_project.issue_tracker_type is None
    assert default_project.createdAt is None
    assert default_project.updatedAt is None
    assert default_project.revisions == []