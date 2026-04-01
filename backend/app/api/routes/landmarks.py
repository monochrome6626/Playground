from fastapi import APIRouter

from app.schemas.landmark import LandmarkResponse

router = APIRouter(prefix="/landmarks", tags=["landmarks"])

_LANDMARK_FIXTURES = [
    LandmarkResponse(
        id="landmark-skytree",
        name="Tokyo Skytree",
        latitude=35.7101,
        longitude=139.8107,
        base_elevation_m=0.0,
        height_m=634.0,
        target_point_type="top",
    ),
    LandmarkResponse(
        id="landmark-tokyo-tower",
        name="Tokyo Tower",
        latitude=35.6586,
        longitude=139.7454,
        base_elevation_m=0.0,
        height_m=333.0,
        target_point_type="top",
    ),
]


@router.get("", response_model=list[LandmarkResponse])
def list_landmarks() -> list[LandmarkResponse]:
    return _LANDMARK_FIXTURES
