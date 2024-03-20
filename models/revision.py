class Revision:
    def __init__(self, loc, licenses=None, discoveredLicenses=None, locator=None, projectId=None, resolved=None, unsupported=None, parent_locator=None, error=None, declaredLicense=None, source_type=None, author=None, unresolved_licensing_issue_count=None, unresolved_security_issue_count=None, unresolved_quality_issue_count=None, unresolved_issue_count=None):
        self.loc = loc
        self.licenses = licenses if licenses is not None else []
        self.discoveredLicenses = discoveredLicenses if discoveredLicenses is not None else []
        self.locator = locator
        self.projectId = projectId
        self.resolved = resolved
        self.unsupported = unsupported
        self.parent_locator = parent_locator
        self.error = error
        self.declaredLicense = declaredLicense
        self.source_type = source_type
        self.author = author
        self.unresolved_licensing_issue_count = unresolved_licensing_issue_count
        self.unresolved_security_issue_count = unresolved_security_issue_count
        self.unresolved_quality_issue_count = unresolved_quality_issue_count
        self.unresolved_issue_count = unresolved_issue_count