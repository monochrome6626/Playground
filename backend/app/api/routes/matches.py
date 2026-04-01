from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.search_request import SearchRequest
from app.repositories.match_repository import MatchRepository
from app.schemas.match import MatchDetailResponse, MatchListResponse, MatchResponse

router = APIRouter(prefix="/matches", tags=["matches"])
match_repository = MatchRepository()


@router.get("", response_model=MatchListResponse)
def list_matches(search_request_id: str, db: Session = Depends(get_db)) -> MatchListResponse:
    search = db.get(SearchRequest, search_request_id)
    if search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Search request not found.")

    matches = match_repository.list_by_search(db, search_request_id)
    return MatchListResponse(
        items=[MatchResponse.model_validate(item) for item in matches],
        total=len(matches),
        search_request_id=search_request_id,
    )


@router.get("/{match_id}", response_model=MatchDetailResponse)
def get_match(match_id: str, db: Session = Depends(get_db)) -> MatchDetailResponse:
    row = match_repository.get_detail(db, match_id)
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found.")
    match, spot, landmark = row

    return MatchDetailResponse(
        id=match.id,
        spot_name=spot.name,
        landmark_name=landmark.name,
        body=match.body,
        event_type=match.event_type,
        observed_at=match.observed_at,
        body_azimuth_deg=match.body_azimuth_deg,
        body_altitude_deg=match.body_altitude_deg,
        landmark_azimuth_deg=match.landmark_azimuth_deg,
        landmark_altitude_deg=match.landmark_altitude_deg,
        azimuth_diff_deg=match.azimuth_diff_deg,
        altitude_diff_deg=match.altitude_diff_deg,
        score=match.score,
        weather_summary=match.weather_summary,
    )
