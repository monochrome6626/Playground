from dataclasses import dataclass
from datetime import date, datetime, timedelta
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.landmark import Landmark
from app.models.match import Match
from app.models.search_request import SearchRequest
from app.models.spot import Spot
from app.services.alignment_service import AlignmentService
from app.services.astronomy_service import AstronomyService
from app.services.geometry_service import GeometryService


@dataclass(frozen=True)
class EventDefinition:
    body: str
    event_type: str


EVENT_TO_BODY = {
    "sunrise": "sun",
    "sunset": "sun",
    "moonrise": "moon",
    "moonset": "moon",
}


class SearchService:
    def __init__(self) -> None:
        self._astronomy = AstronomyService()
        self._geometry = GeometryService()
        self._alignment = AlignmentService()

    def generate_matches(self, db: Session, request: SearchRequest) -> list[Match]:
        spot = db.get(Spot, request.spot_id)
        landmark = db.get(Landmark, request.landmark_id)
        if spot is None or landmark is None:
            return []

        event_definitions = self._resolve_events(request)
        if not event_definitions:
            return []

        landmark_direction = self._geometry.get_landmark_direction(
            spot_lat=spot.latitude,
            spot_lon=spot.longitude,
            spot_elevation_m=spot.elevation_m or 0.0,
            landmark_lat=landmark.latitude,
            landmark_lon=landmark.longitude,
            landmark_base_elevation_m=landmark.base_elevation_m or 0.0,
            landmark_height_m=landmark.height_m,
        )

        matches: list[Match] = []
        for target_date in self._date_range(request.date_from, request.date_to):
            for event in event_definitions:
                matches.extend(self._matches_for_event(request, spot, landmark, landmark_direction, target_date, event))
        return matches

    def _matches_for_event(
        self,
        request: SearchRequest,
        spot: Spot,
        landmark: Landmark,
        landmark_direction,
        target_date: date,
        event: EventDefinition,
    ) -> list[Match]:
        try:
            event_time = self._astronomy.event_time(
                event.body,
                event.event_type,
                latitude=spot.latitude,
                longitude=spot.longitude,
                elevation_m=spot.elevation_m or 0.0,
                target_date=target_date,
            )
        except Exception:
            return []

        if event_time is None:
            return []

        interval_sec = max(request.interval_sec, 5)
        start = event_time - timedelta(minutes=30)
        end = event_time + timedelta(minutes=30)

        current = start
        created: list[Match] = []
        while current <= end:
            try:
                body_position = self._astronomy.position(
                    event.body,
                    latitude=spot.latitude,
                    longitude=spot.longitude,
                    elevation_m=spot.elevation_m or 0.0,
                    observed_at=current,
                )
            except Exception:
                current += timedelta(seconds=interval_sec)
                continue

            azimuth_diff_deg = self._alignment.azimuth_diff(body_position.azimuth_deg, landmark_direction.azimuth_deg)
            altitude_diff_deg = self._alignment.altitude_diff(body_position.altitude_deg, landmark_direction.altitude_deg)

            if self._alignment.is_match(
                azimuth_diff_deg=azimuth_diff_deg,
                altitude_diff_deg=altitude_diff_deg,
                azimuth_tolerance_deg=request.azimuth_tolerance_deg,
                altitude_tolerance_deg=request.altitude_tolerance_deg,
            ):
                score = self._alignment.score(azimuth_diff_deg, altitude_diff_deg)
                created.append(
                    Match(
                        id=f"match-{uuid4().hex[:12]}",
                        search_request_id=request.id,
                        spot_id=spot.id,
                        landmark_id=landmark.id,
                        body=event.body,
                        event_type=event.event_type,
                        observed_at=current,
                        body_azimuth_deg=body_position.azimuth_deg,
                        body_altitude_deg=body_position.altitude_deg,
                        landmark_azimuth_deg=landmark_direction.azimuth_deg,
                        landmark_altitude_deg=landmark_direction.altitude_deg,
                        azimuth_diff_deg=azimuth_diff_deg,
                        altitude_diff_deg=altitude_diff_deg,
                        score=score,
                        weather_summary=None,
                    )
                )

            current += timedelta(seconds=interval_sec)

        return created

    @staticmethod
    def _date_range(date_from: date, date_to: date):
        cursor = date_from
        while cursor <= date_to:
            yield cursor
            cursor += timedelta(days=1)

    @staticmethod
    def _resolve_events(request: SearchRequest) -> list[EventDefinition]:
        resolved: list[EventDefinition] = []
        body_set = set(request.body_types)
        for event in request.event_types:
            body = EVENT_TO_BODY.get(event)
            if body is None:
                continue
            if body not in body_set:
                continue
            resolved.append(EventDefinition(body=body, event_type=event))
        return resolved
