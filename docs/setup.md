# Setup

## Prerequisites

- Docker Desktop or a local PostgreSQL + Python + Node toolchain
- PostgreSQL 17 installed if running without Docker
- Node.js 20+
- Python 3.10+

## Environment variables

1. Copy `.env.example` to `.env`.
2. Adjust the database password and ports if needed.

## Docker workflow

```bash
docker compose up --build
```

Services:

- frontend: `http://localhost:3000`
- backend: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

## Manual workflow

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m alembic upgrade head
python -m app.scripts.seed_landmarks
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Immediate next tasks

1. implement real astronomy calculations and tests
2. replace fixture search/match responses with DB-backed handlers
3. add weather cache and asynchronous search execution
4. introduce PostGIS columns and map-aware query utilities
