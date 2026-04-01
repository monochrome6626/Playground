from datetime import date

from pydantic import BaseModel, Field


class SearchRequestCreate(BaseModel):
    spot_id: str
    landmark_id: str
    date_from: date
    date_to: date
    body_types: list[str] = Field(default_factory=lambda: ["sun", "moon"])
    event_types: list[str] = Field(default_factory=lambda: ["sunrise", "sunset", "moonrise", "moonset"])
    azimuth_tolerance_deg: float = 0.3
    altitude_tolerance_deg: float = 0.25
    interval_sec: int = 20


class SearchRequestResponse(SearchRequestCreate):
    id: str
    status: str

    model_config = {"from_attributes": True}
