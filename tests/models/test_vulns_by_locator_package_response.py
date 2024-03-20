import pytest
from models.vulns_by_locator_package_response import VulnsByLocatorPackageResponse

def test_vulns_by_locator_package_response_initialization():
    # Sample data for the test
    displayName = "Vulnerable Package"
    description = "This package has vulnerabilities."
    homepage = "https://example.com/vulnerable-package"

    # Initialize an instance of VulnsByLocatorPackageResponse
    package_response = VulnsByLocatorPackageResponse(displayName, description, homepage)

    # Assertions to verify that all attributes are correctly assigned
    assert package_response.displayName == displayName
    assert package_response.description == description
    assert package_response.homepage == homepage
