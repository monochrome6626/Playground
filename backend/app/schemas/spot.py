from pydantic import BaseModel


class SpotBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    elevation_m: float | None = None
    prefecture: str | None = None
    memo: str | None = None


class SpotCreate(SpotBase):
    pass


class SpotResponse(SpotBase):
    id: str
