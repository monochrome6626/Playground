class AlignmentService:
    @staticmethod
    def azimuth_diff(a_deg: float, b_deg: float) -> float:
        raw = abs(a_deg - b_deg) % 360.0
        return min(raw, 360.0 - raw)

    @staticmethod
    def altitude_diff(a_deg: float, b_deg: float) -> float:
        return abs(a_deg - b_deg)

    def is_match(
        self,
        *,
        azimuth_diff_deg: float,
        altitude_diff_deg: float,
        azimuth_tolerance_deg: float,
        altitude_tolerance_deg: float,
    ) -> bool:
        return azimuth_diff_deg <= azimuth_tolerance_deg and altitude_diff_deg <= altitude_tolerance_deg

    def score(self, azimuth_diff_deg: float, altitude_diff_deg: float) -> float:
        return max(0.0, 100.0 - (azimuth_diff_deg * 80.0 + altitude_diff_deg * 80.0))
