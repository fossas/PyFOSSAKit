import pytest
from models.vulns_by_locator_response import VulnsByLocatorResponse
from models.vulns_by_locator_package_response import VulnsByLocatorPackageResponse
from models.vulnerability import Vulnerability

def test_vulns_by_locator_response_initialization():
    # Initialize an instance of VulnsByLocatorPackageResponse
    package_response = VulnsByLocatorPackageResponse(
        displayName="Vulnerable Package",
        description="This package has vulnerabilities.",
        homepage="https://example.com/vulnerable-package"
    )

    # Initialize an instance of VulnsByLocatorResponse and add the package response
    vulns_by_locator_response = VulnsByLocatorResponse()
    vulns_by_locator_response.add_package_response("npm+vulnerable-package$1.0.3", package_response)

    # Assertions to verify that the package response is correctly added
    assert "npm+vulnerable-package$1.0.3" in vulns_by_locator_response.vulns_by_locator
    assert vulns_by_locator_response.vulns_by_locator["npm+vulnerable-package$1.0.3"] == package_response
