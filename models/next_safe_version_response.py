from typing import Dict

class NextSafeVersionResponse:
    def __init__(self, next_safe_versions: Dict[str, str]):
        self.next_safe_versions = next_safe_versions