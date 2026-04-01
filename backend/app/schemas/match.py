from datetime import datetime

from pydantic import BaseModel


class MatchResponse(BaseModel):
    id: str
    observed_at: datetime
    body: str
    event_type: str
    score: float
    azimuth_diff_deg: float
    altitude_diff_deg: float
    weather_summary: str | None = None

    model_config = {"from_attributes": True}


class MatchListResponse(BaseModel):
    items: list[MatchResponse]
    total: int
    search_request_id: str


class MatchDetailResponse(BaseModel):
    id: str
    spot_name: str
    landmark_name: str
    body: str
    event_type: str
    observed_at: datetime
    body_azimuth_deg: float
    body_altitude_deg: float
    landmark_azimuth_deg: float
    landmark_altitude_deg: float
    azimuth_diff_deg: float
    altitude_diff_deg: float
    score: float
    weather_summary: str | None = None
