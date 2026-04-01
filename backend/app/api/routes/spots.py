from fastapi import APIRouter

from app.schemas.spot import SpotCreate, SpotResponse

router = APIRouter(prefix="/spots", tags=["spots"])

_SPOT_FIXTURES = [
    SpotResponse(
        id="spot-kasai-rinkai",
        name="Kasai Rinkai Park",
        latitude=35.6444,
        longitude=139.8611,
        elevation_m=3.2,
        prefecture="Tokyo",
        memo="Good candidate for sunrise shots toward Tokyo Bay.",
    )
]


@router.get("", response_model=list[SpotResponse])
def list_spots() -> list[SpotResponse]:
    return _SPOT_FIXTURES


@router.post("", response_model=SpotResponse, status_code=201)
def create_spot(payload: SpotCreate) -> SpotResponse:
    return SpotResponse(id="spot-new", **payload.model_dump())
