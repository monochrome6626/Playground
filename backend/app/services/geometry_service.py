from dataclasses import dataclass
from math import atan2, degrees

from pyproj import Geod


@dataclass
class LandmarkDirection:
    azimuth_deg: float
    altitude_deg: float


class GeometryService:
    def __init__(self) -> None:
        self._geod = Geod(ellps="WGS84")

    def get_landmark_direction(
        self,
        *,
        spot_lat: float,
        spot_lon: float,
        spot_elevation_m: float,
        landmark_lat: float,
        landmark_lon: float,
        landmark_base_elevation_m: float,
        landmark_height_m: float,
    ) -> LandmarkDirection:
        forward_azimuth_deg, _back_azimuth, distance_m = self._geod.inv(
            spot_lon,
            spot_lat,
            landmark_lon,
            landmark_lat,
        )
        normalized_azimuth = (forward_azimuth_deg + 360.0) % 360.0
        vertical_delta_m = (landmark_base_elevation_m + landmark_height_m) - spot_elevation_m
        altitude_deg = degrees(atan2(vertical_delta_m, max(distance_m, 1.0)))

        return LandmarkDirection(azimuth_deg=normalized_azimuth, altitude_deg=altitude_deg)
