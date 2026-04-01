from sqlalchemy import select

from app.core.db import SessionLocal
from app.models.landmark import Landmark


DEFAULT_LANDMARKS = [
    {
        "id": "landmark-skytree",
        "name": "Tokyo Skytree",
        "latitude": 35.7101,
        "longitude": 139.8107,
        "base_elevation_m": 0.0,
        "height_m": 634.0,
        "target_point_type": "top",
    },
    {
        "id": "landmark-tokyo-tower",
        "name": "Tokyo Tower",
        "latitude": 35.6586,
        "longitude": 139.7454,
        "base_elevation_m": 0.0,
        "height_m": 333.0,
        "target_point_type": "top",
    },
]


def seed_landmarks() -> None:
    with SessionLocal() as db:
        for item in DEFAULT_LANDMARKS:
            exists = db.scalar(select(Landmark.id).where(Landmark.id == item["id"]))
            if exists:
                continue
            db.add(Landmark(**item))
        db.commit()


if __name__ == "__main__":
    seed_landmarks()
    print("Landmarks seeded.")
