from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Landmark(Base):
    __tablename__ = "landmarks"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    base_elevation_m: Mapped[float | None] = mapped_column(Float)
    height_m: Mapped[float] = mapped_column(Float, nullable=False)
    target_point_type: Mapped[str] = mapped_column(String(30), nullable=False)
