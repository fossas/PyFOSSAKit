from models.vulns_by_locator_package_response import VulnsByLocatorPackageResponse

class VulnsByLocatorResponse:
    def __init__(self):
        self.vulns_by_locator = {}

    def add_package_response(self, locator: str, package_response: VulnsByLocatorPackageResponse):
        self.vulns_by_locator[locator] = package_response
