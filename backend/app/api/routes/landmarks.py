from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.repositories.landmark_repository import LandmarkRepository
from app.schemas.landmark import LandmarkResponse

router = APIRouter(prefix="/landmarks", tags=["landmarks"])

landmark_repository = LandmarkRepository()


@router.get("", response_model=list[LandmarkResponse])
def list_landmarks(db: Session = Depends(get_db)) -> list[LandmarkResponse]:
    landmarks = landmark_repository.list_landmarks(db)
    return [LandmarkResponse.model_validate(item) for item in landmarks]
