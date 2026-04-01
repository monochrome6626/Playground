from datetime import datetime

from fastapi import APIRouter

from app.schemas.match import MatchDetailResponse, MatchListResponse, MatchResponse

router = APIRouter(prefix="/matches", tags=["matches"])


@router.get("", response_model=MatchListResponse)
def list_matches(search_request_id: str) -> MatchListResponse:
    return MatchListResponse(
        items=[
            MatchResponse(
                id="match-demo",
                observed_at=datetime.fromisoformat("2026-11-03T06:08:20+09:00"),
                body="sun",
                event_type="sunrise",
                score=98.4,
                azimuth_diff_deg=0.08,
                altitude_diff_deg=0.05,
                weather_summary="partly_cloudy",
            )
        ],
        total=1,
        search_request_id=search_request_id,
    )


@router.get("/{match_id}", response_model=MatchDetailResponse)
def get_match(match_id: str) -> MatchDetailResponse:
    return MatchDetailResponse(
        id=match_id,
        spot_name="Kasai Rinkai Park",
        landmark_name="Tokyo Skytree",
        body="sun",
        event_type="sunrise",
        observed_at=datetime.fromisoformat("2026-11-03T06:08:20+09:00"),
        body_azimuth_deg=114.22,
        body_altitude_deg=1.84,
        landmark_azimuth_deg=114.14,
        landmark_altitude_deg=1.79,
        azimuth_diff_deg=0.08,
        altitude_diff_deg=0.05,
        score=98.4,
    )
