from typing import List, Any

class DependenciesResponse:
    def __init__(self, loc: str, licenses: List[str], discoveredLicenses: List[str], locator: str, projectId: str, resolved: bool, unsupported: bool, declaredLicense: str, dependencyLock: Any, project: Any, unresolved_locators: List[str], depth: int, ignored: bool):
        self.loc = loc
        self.licenses = licenses
        self.discoveredLicenses = discoveredLicenses
        self.locator = locator
        self.projectId = projectId
        self.resolved = resolved
        self.unsupported = unsupported
        self.declaredLicense = declaredLicense
        self.dependencyLock = dependencyLock
        self.project = project
        self.unresolved_locators = unresolved_locators
        self.depth = depth
        self.ignored = ignored