from pydantic import BaseModel


class LandmarkResponse(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    base_elevation_m: float | None = None
    height_m: float
    target_point_type: str
