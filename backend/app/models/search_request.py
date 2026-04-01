from datetime import date

from sqlalchemy import Date, Float, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class SearchRequest(Base):
    __tablename__ = "search_requests"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    spot_id: Mapped[str] = mapped_column(String(64), nullable=False)
    landmark_id: Mapped[str] = mapped_column(String(64), nullable=False)
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    body_types: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    event_types: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    azimuth_tolerance_deg: Mapped[float] = mapped_column(Float, nullable=False)
    altitude_tolerance_deg: Mapped[float] = mapped_column(Float, nullable=False)
    interval_sec: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
