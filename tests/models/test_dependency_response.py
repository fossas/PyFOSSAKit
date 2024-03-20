import pytest
from models.dependencies_response import DependenciesResponse

def test_dependencies_response_initialization():
    # Given
    loc = "location"
    licenses = ["MIT", "Apache"]
    discoveredLicenses = ["GPL"]
    locator = "locator_str"
    projectId = "project_id"
    resolved = True
    unsupported = False
    declaredLicense = "MIT"
    dependencyLock = {"lock": "data"}  # Assuming Any type can be a dict for this example
    project = {"name": "Project Name"}  # Assuming Any type can be a dict for this example
    unresolved_locators = ["unresolved_locator_1"]
    depth = 1
    ignored = False

    # When
    response = DependenciesResponse(loc, licenses, discoveredLicenses, locator, projectId, resolved, unsupported,
                                    declaredLicense, dependencyLock, project, unresolved_locators, depth, ignored)

    # Then
    assert response.loc == loc
    assert response.licenses == licenses
    assert response.discoveredLicenses == discoveredLicenses
    assert response.locator == locator
    assert response.projectId == projectId
    assert response.resolved == resolved
    assert response.unsupported == unsupported
    assert response.declaredLicense == declaredLicense
    assert response.dependencyLock == dependencyLock
    assert response.project == project
    assert response.unresolved_locators == unresolved_locators
    assert response.depth == depth
    assert response.ignored == ignored