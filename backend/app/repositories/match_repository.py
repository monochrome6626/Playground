from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.match import Match
from app.models.landmark import Landmark
from app.models.spot import Spot


class MatchRepository:
    def replace_for_search(self, db: Session, search_request_id: str, matches: list[Match]) -> None:
        db.execute(delete(Match).where(Match.search_request_id == search_request_id))
        if matches:
            db.add_all(matches)
        db.commit()

    def list_by_search(self, db: Session, search_request_id: str) -> list[Match]:
        stmt = select(Match).where(Match.search_request_id == search_request_id).order_by(Match.score.desc(), Match.observed_at.asc())
        return list(db.scalars(stmt).all())

    def get_detail(self, db: Session, match_id: str) -> tuple[Match, Spot, Landmark] | None:
        stmt = (
            select(Match, Spot, Landmark)
            .join(Spot, Spot.id == Match.spot_id)
            .join(Landmark, Landmark.id == Match.landmark_id)
            .where(Match.id == match_id)
        )
        row = db.execute(stmt).first()
        if row is None:
            return None
        return row[0], row[1], row[2]
