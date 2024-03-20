import pytest
from models.nested_vulns_by_locator_response import NestedVulnsByLocatorResponse
from models.vulns_by_locator_package_response import VulnsByLocatorPackageResponse
from models.vulnerability import Vulnerability

def test_nested_vulns_by_locator_response():
    # Setup the necessary data for packageData and vulnerabilities
    package_data = VulnsByLocatorPackageResponse(
        displayName="Example Package Display Name",
        description="Description of the example package",
        homepage="https://example.com/package-homepage"
    )
    vulnerability_1 = Vulnerability(
        id="VULN-1234",
        description="Example vulnerability 1",
        cwes=["CWE-79"],
        cvss=5.0,
        references=["https://vuln.example.com/VULN-1234"],
        affectedVersionRanges=["<=1.0.0"],
        unaffectedVersionRanges=[">1.0.0"],
        patchedVersionRanges=[">=1.0.1"],
        cve="CVE-1234",
        cvssV2Vector="AV:N/AC:L/Au:N/C:P/I:P/A:P",
        cvssV3Vector="CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        weaknesses=[{"id": "W-1", "description": "Weakness 1"}],
        nextSafeVersion="1.0.1"
    )
    vulnerability_2 = Vulnerability(
        id="VULN-5678",
        description="Example vulnerability 2",
        cwes=["CWE-80"],
        cvss=7.5,
        references=["https://vuln.example.com/VULN-5678"],
        affectedVersionRanges=["<=2.0.0"],
        unaffectedVersionRanges=[">2.0.0"],
        patchedVersionRanges=[">=2.0.1"],
        cve="CVE-5678",
        cvssV2Vector="AV:N/AC:L/Au:N/C:P/I:P/A:P",
        cvssV3Vector="CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        weaknesses=[{"id": "W-2", "description": "Weakness 2"}],
        nextSafeVersion="2.0.1"
    )

    # Create an instance of NestedVulnsByLocatorResponse
    response = NestedVulnsByLocatorResponse(packageData=package_data, vulnerabilities=[vulnerability_1, vulnerability_2])

    # Verify the packageData property
    assert response.packageData == package_data

    # Verify the vulnerabilities property
    assert len(response.vulnerabilities) == 2
    assert response.vulnerabilities[0].cve == "CVE-1234"
    assert response.vulnerabilities[0].description == "Example vulnerability 1"
    assert response.vulnerabilities[0].cvss == 5.0
    assert response.vulnerabilities[1].cve == "CVE-5678"
    assert response.vulnerabilities[1].description == "Example vulnerability 2"
    assert response.vulnerabilities[1].cvss == 7.5
