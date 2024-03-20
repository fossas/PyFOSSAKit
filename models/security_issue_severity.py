class SecurityIssueSeverity:
    def __init__(self, critical: float, high: float, medium: float, low: float, unknown: float, total: float):
        self.critical = critical
        self.high = high
        self.medium = medium
        self.low = low
        self.unknown = unknown
        self.total = total
