from datetime import date

from pydantic import BaseModel, Field, field_validator, model_validator

ALLOWED_BODIES = {"sun", "moon"}
ALLOWED_EVENTS = {"sunrise", "sunset", "moonrise", "moonset"}


class SearchRequestCreate(BaseModel):
    spot_id: str
    landmark_id: str
    date_from: date
    date_to: date
    body_types: list[str] = Field(default_factory=lambda: ["sun", "moon"])
    event_types: list[str] = Field(default_factory=lambda: ["sunrise", "sunset", "moonrise", "moonset"])
    azimuth_tolerance_deg: float = Field(default=0.3, gt=0.0, le=180.0)
    altitude_tolerance_deg: float = Field(default=0.25, gt=0.0, le=90.0)
    interval_sec: int = Field(default=20, ge=10, le=3600)

    @field_validator("body_types")
    @classmethod
    def validate_body_types(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("body_types must not be empty.")
        invalid = [item for item in value if item not in ALLOWED_BODIES]
        if invalid:
            raise ValueError(f"Unsupported body_types: {', '.join(sorted(set(invalid)))}")
        return value

    @field_validator("event_types")
    @classmethod
    def validate_event_types(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("event_types must not be empty.")
        invalid = [item for item in value if item not in ALLOWED_EVENTS]
        if invalid:
            raise ValueError(f"Unsupported event_types: {', '.join(sorted(set(invalid)))}")
        return value

    @model_validator(mode="after")
    def validate_date_range(self):
        if self.date_from > self.date_to:
            raise ValueError("date_from must be earlier than or equal to date_to.")
        if (self.date_to - self.date_from).days > 366:
            raise ValueError("date range must be 366 days or fewer.")
        return self


class SearchRequestResponse(SearchRequestCreate):
    id: str
    status: str

    model_config = {"from_attributes": True}
