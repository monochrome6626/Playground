from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.search_request import SearchRequest
from app.schemas.search import SearchRequestCreate


class SearchRequestRepository:
    def create(self, db: Session, search_id: str, payload: SearchRequestCreate, status: str) -> SearchRequest:
        record = SearchRequest(id=search_id, status=status, **payload.model_dump())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    def get(self, db: Session, search_id: str) -> SearchRequest | None:
        stmt = select(SearchRequest).where(SearchRequest.id == search_id)
        return db.scalar(stmt)

    def set_status(self, db: Session, search_id: str, status: str) -> SearchRequest | None:
        record = self.get(db, search_id)
        if record is None:
            return None
        record.status = status
        db.commit()
        db.refresh(record)
        return record
