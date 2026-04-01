from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.repositories.spot_repository import SpotRepository
from app.schemas.spot import SpotCreate, SpotResponse

router = APIRouter(prefix="/spots", tags=["spots"])

spot_repository = SpotRepository()


@router.get("", response_model=list[SpotResponse])
def list_spots(db: Session = Depends(get_db)) -> list[SpotResponse]:
    spots = spot_repository.list_spots(db)
    return [SpotResponse.model_validate(item) for item in spots]


@router.post("", response_model=SpotResponse, status_code=201)
def create_spot(payload: SpotCreate, db: Session = Depends(get_db)) -> SpotResponse:
    spot = spot_repository.create_spot(db, spot_id=f"spot-{uuid4().hex[:12]}", payload=payload)
    return SpotResponse.model_validate(spot)
