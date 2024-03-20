import pytest
from models.nested_safe_version_response import NestedSafeVersionResponse

def test_nested_safe_version_response():
    # Create an instance with some initial properties
    response = NestedSafeVersionResponse(overall_remediation='4.1.2', version_3_1_2='4.1.2', version_3_2_2='4.1.2')

    # Test setting an additional version
    response['version_2_1_2'] = '3.1.0'

    # Verify the overall remediation
    assert response.overall_remediation == '4.1.2'

    # Verify the initially set versions
    assert response['version_3_1_2'] == '4.1.2'
    assert response['version_3_2_2'] == '4.1.2'

    # Verify the additional version set later
    assert response['version_2_1_2'] == '3.1.0'

    # Test the get_all_versions method
    all_versions = response.get_all_versions()
    expected_versions = {
        'version_3_1_2': '4.1.2',
        'version_3_2_2': '4.1.2',
        'version_2_1_2': '3.1.0',
        'overallRemediation': '4.1.2'
    }
    assert all_versions == expected_versions