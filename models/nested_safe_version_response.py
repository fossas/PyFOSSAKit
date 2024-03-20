class NestedSafeVersionResponse:
    def __init__(self, overall_remediation: str, **additional_versions: str):
        self.overall_remediation = overall_remediation
        # Store additional properties dynamically
        self.additional_versions = additional_versions

    def __getitem__(self, item):
        # Allows dictionary-like access to additional properties
        return self.additional_versions.get(item)

    def __setitem__(self, key, value):
        # Allows setting additional properties like a dictionary
        self.additional_versions[key] = value

    def get_all_versions(self):
        # Combine overall_remediation with additional_versions for a complete view
        versions = self.additional_versions.copy()
        versions['overallRemediation'] = self.overall_remediation
        return versions