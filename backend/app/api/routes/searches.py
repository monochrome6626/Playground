from datetime import date

from fastapi import APIRouter

from app.schemas.search import SearchRequestCreate, SearchRequestResponse

router = APIRouter(prefix="/searches", tags=["searches"])


@router.post("", response_model=SearchRequestResponse, status_code=201)
def create_search(payload: SearchRequestCreate) -> SearchRequestResponse:
    return SearchRequestResponse(
        id="search-demo",
        spot_id=payload.spot_id,
        landmark_id=payload.landmark_id,
        date_from=payload.date_from,
        date_to=payload.date_to,
        body_types=payload.body_types,
        event_types=payload.event_types,
        azimuth_tolerance_deg=payload.azimuth_tolerance_deg,
        altitude_tolerance_deg=payload.altitude_tolerance_deg,
        interval_sec=payload.interval_sec,
        status="queued",
    )


@router.get("/{search_id}", response_model=SearchRequestResponse)
def get_search(search_id: str) -> SearchRequestResponse:
    return SearchRequestResponse(
        id=search_id,
        spot_id="spot-kasai-rinkai",
        landmark_id="landmark-skytree",
        date_from=date(2026, 10, 1),
        date_to=date(2026, 12, 31),
        body_types=["sun", "moon"],
        event_types=["sunrise", "sunset", "moonrise", "moonset"],
        azimuth_tolerance_deg=0.3,
        altitude_tolerance_deg=0.25,
        interval_sec=20,
        status="processing",
    )
