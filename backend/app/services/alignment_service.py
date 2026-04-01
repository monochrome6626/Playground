class AlignmentService:
    def score(self, azimuth_diff_deg: float, altitude_diff_deg: float) -> float:
        return max(0.0, 100.0 - (azimuth_diff_deg * 80.0 + altitude_diff_deg * 80.0))
