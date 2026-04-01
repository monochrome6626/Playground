from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.db import Base, get_db
from app.main import app
from app.models.landmark import Landmark


engine = create_engine(
    "sqlite+pysqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    future=True,
)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def override_get_db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


client = TestClient(app)


def setup_module() -> None:
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as db:
        db.add(
            Landmark(
                id="landmark-skytree",
                name="Tokyo Skytree",
                latitude=35.7101,
                longitude=139.8107,
                base_elevation_m=0.0,
                height_m=634.0,
                target_point_type="top",
            )
        )
        db.commit()


def teardown_module() -> None:
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.pop(get_db, None)


def test_create_and_list_spot() -> None:
    payload = {
        "name": "Kasai Rinkai Park",
        "latitude": 35.6444,
        "longitude": 139.8611,
        "elevation_m": 3.2,
        "prefecture": "Tokyo",
        "memo": "Sunrise alignment candidate",
    }

    create_response = client.post("/api/spots", json=payload)
    assert create_response.status_code == 201
    body = create_response.json()
    assert body["id"].startswith("spot-")
    assert body["name"] == "Kasai Rinkai Park"

    list_response = client.get("/api/spots")
    assert list_response.status_code == 200
    listed = list_response.json()
    assert len(listed) == 1
    assert listed[0]["name"] == "Kasai Rinkai Park"


def test_list_landmarks_from_db() -> None:
    response = client.get("/api/landmarks")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 1
    assert payload[0]["id"] == "landmark-skytree"
