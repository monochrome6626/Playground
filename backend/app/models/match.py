from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    search_request_id: Mapped[str] = mapped_column(ForeignKey("search_requests.id"), nullable=False)
    spot_id: Mapped[str] = mapped_column(ForeignKey("spots.id"), nullable=False)
    landmark_id: Mapped[str] = mapped_column(ForeignKey("landmarks.id"), nullable=False)
    body: Mapped[str] = mapped_column(String(20), nullable=False)
    event_type: Mapped[str] = mapped_column(String(20), nullable=False)
    observed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    azimuth_diff_deg: Mapped[float] = mapped_column(Float, nullable=False)
    altitude_diff_deg: Mapped[float] = mapped_column(Float, nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
