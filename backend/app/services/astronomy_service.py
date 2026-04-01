from dataclasses import dataclass
from datetime import date, datetime
from zoneinfo import ZoneInfo

from astral import Observer
from astral.moon import azimuth as moon_azimuth
from astral.moon import elevation as moon_elevation
from astral.moon import moonrise as astral_moonrise
from astral.moon import moonset as astral_moonset
from astral.sun import azimuth as sun_azimuth
from astral.sun import elevation as sun_elevation
from astral.sun import sun

JST = ZoneInfo("Asia/Tokyo")

@dataclass
class CelestialPosition:
    azimuth_deg: float
    altitude_deg: float


class AstronomyService:
    def _observer(self, latitude: float, longitude: float, elevation_m: float) -> Observer:
        return Observer(latitude=latitude, longitude=longitude, elevation=elevation_m)

    def event_time(
        self,
        body: str,
        event_type: str,
        *,
        latitude: float,
        longitude: float,
        elevation_m: float,
        target_date: date,
    ) -> datetime | None:
        observer = self._observer(latitude=latitude, longitude=longitude, elevation_m=elevation_m)

        if body == "sun":
            sun_data = sun(observer, date=target_date, tzinfo=JST)
            if event_type == "sunrise":
                return sun_data.get("sunrise")
            if event_type == "sunset":
                return sun_data.get("sunset")
            return None

        if body == "moon":
            if event_type == "moonrise":
                return astral_moonrise(observer, date=target_date, tzinfo=JST)
            if event_type == "moonset":
                return astral_moonset(observer, date=target_date, tzinfo=JST)
            return None

        return None

    def position(
        self,
        body: str,
        *,
        latitude: float,
        longitude: float,
        elevation_m: float,
        observed_at: datetime,
    ) -> CelestialPosition:
        observer = self._observer(latitude=latitude, longitude=longitude, elevation_m=elevation_m)

        if body == "sun":
            return CelestialPosition(
                azimuth_deg=float(sun_azimuth(observer, observed_at)),
                altitude_deg=float(sun_elevation(observer, observed_at)),
            )

        if body == "moon":
            return CelestialPosition(
                azimuth_deg=float(moon_azimuth(observer, observed_at)),
                altitude_deg=float(moon_elevation(observer, observed_at)),
            )

        raise ValueError(f"Unsupported body: {body}")
