from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.spot import Spot
from app.schemas.spot import SpotCreate


class SpotRepository:
    def list_spots(self, db: Session) -> list[Spot]:
        stmt = select(Spot).order_by(Spot.name.asc())
        return list(db.scalars(stmt).all())

    def create_spot(self, db: Session, spot_id: str, payload: SpotCreate) -> Spot:
        spot = Spot(id=spot_id, **payload.model_dump())
        db.add(spot)
        db.commit()
        db.refresh(spot)
        return spot
