from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.landmark import Landmark


class LandmarkRepository:
    def list_landmarks(self, db: Session) -> list[Landmark]:
        stmt = select(Landmark).order_by(Landmark.name.asc())
        return list(db.scalars(stmt).all())
