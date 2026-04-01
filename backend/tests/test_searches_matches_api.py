from collections.abc import Generator
from datetime import date
from time import sleep

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.db import Base, get_db
from app.core.db import SessionLocal
from app.main import app
from app import models  # noqa: F401
from app.models.landmark import Landmark
from app.models.spot import Spot
from app.services.search_job_runner import search_job_runner


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
    search_job_runner.configure_session_factory(TestingSessionLocal)
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as db:
        db.add(
            Spot(
                id="spot-kasai",
                name="Kasai Rinkai Park",
                latitude=35.6444,
                longitude=139.8611,
                elevation_m=3.2,
                prefecture="Tokyo",
                memo="test spot",
            )
        )
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
    search_job_runner.configure_session_factory(SessionLocal)


def test_create_search_and_fetch_matches() -> None:
    create_payload = {
        "spot_id": "spot-kasai",
        "landmark_id": "landmark-skytree",
        "date_from": date(2026, 1, 15).isoformat(),
        "date_to": date(2026, 1, 15).isoformat(),
        "body_types": ["sun"],
        "event_types": ["sunrise"],
        "azimuth_tolerance_deg": 180.0,
        "altitude_tolerance_deg": 90.0,
        "interval_sec": 300,
    }

    create_response = client.post("/api/searches", json=create_payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["id"].startswith("search-")
    assert created["status"] == "queued"

    search_id = created["id"]
    search = None
    for _ in range(40):
        search_response = client.get(f"/api/searches/{search_id}")
        assert search_response.status_code == 200
        search = search_response.json()
        if search["status"] in {"completed", "failed"}:
            break
        sleep(0.05)

    assert search is not None
    assert search["id"] == search_id
    assert search["status"] == "completed"

    matches_response = client.get(f"/api/matches?search_request_id={search_id}")
    assert matches_response.status_code == 200
    matches_payload = matches_response.json()
    assert matches_payload["search_request_id"] == search_id
    assert isinstance(matches_payload["items"], list)
    assert matches_payload["total"] >= 0
