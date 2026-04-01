from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.landmark import Landmark
from app.models.spot import Spot
from app.repositories.search_request_repository import SearchRequestRepository
from app.schemas.search import SearchRequestCreate, SearchRequestResponse
from app.services.search_job_runner import search_job_runner

router = APIRouter(prefix="/searches", tags=["searches"])
search_repository = SearchRequestRepository()


@router.post("", response_model=SearchRequestResponse, status_code=201)
def create_search(payload: SearchRequestCreate, db: Session = Depends(get_db)) -> SearchRequestResponse:
    if payload.date_from > payload.date_to:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="date_from must be earlier than date_to.")

    spot = db.get(Spot, payload.spot_id)
    if spot is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spot not found.")

    landmark = db.get(Landmark, payload.landmark_id)
    if landmark is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Landmark not found.")

    search_id = f"search-{uuid4().hex[:12]}"
    record = search_repository.create(db, search_id=search_id, payload=payload, status="queued")
    search_job_runner.enqueue(record.id)

    return SearchRequestResponse.model_validate(record)


@router.get("/{search_id}", response_model=SearchRequestResponse)
def get_search(search_id: str, db: Session = Depends(get_db)) -> SearchRequestResponse:
    record = search_repository.get(db, search_id)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Search request not found.")
    return SearchRequestResponse.model_validate(record)
