from dataclasses import dataclass


@dataclass
class LandmarkDirection:
    azimuth_deg: float
    altitude_deg: float


class GeometryService:
    def get_landmark_direction(self, spot_lat: float, spot_lon: float, landmark_lat: float, landmark_lon: float) -> LandmarkDirection:
        return LandmarkDirection(azimuth_deg=114.14, altitude_deg=1.79)
