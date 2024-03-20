import pytest
from models.next_safe_version_response import NextSafeVersionResponse

def test_next_safe_version_response_initialization():
    # Define a dictionary representing next safe versions
    next_safe_versions = {
        "library1": "1.2.3",
        "library2": "2.3.4",
    }

    # Create a NextSafeVersionResponse instance
    response = NextSafeVersionResponse(next_safe_versions=next_safe_versions)

    # Assert that the attribute is set correctly
    assert response.next_safe_versions == next_safe_versions
    assert response.next_safe_versions["library1"] == "1.2.3"
    assert response.next_safe_versions["library2"] == "2.3.4"