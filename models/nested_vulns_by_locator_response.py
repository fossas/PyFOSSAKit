from typing import List
from models.vulns_by_locator_package_response import VulnsByLocatorPackageResponse
from models.vulnerability import Vulnerability

class NestedVulnsByLocatorResponse:
    def __init__(self, packageData: VulnsByLocatorPackageResponse, vulnerabilities: List[Vulnerability]):
        self.packageData = packageData
        self.vulnerabilities = vulnerabilities