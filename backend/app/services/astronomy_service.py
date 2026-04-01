from dataclasses import dataclass


@dataclass
class CelestialPosition:
    azimuth_deg: float
    altitude_deg: float


class AstronomyService:
    def get_solar_position(self, latitude: float, longitude: float) -> CelestialPosition:
        return CelestialPosition(azimuth_deg=114.22, altitude_deg=1.84)

    def get_lunar_position(self, latitude: float, longitude: float) -> CelestialPosition:
        return CelestialPosition(azimuth_deg=93.10, altitude_deg=0.95)
