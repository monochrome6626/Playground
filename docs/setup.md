# Setup

## Prerequisites

- Docker Desktop or a local PostgreSQL + Python + Node toolchain
- PostgreSQL 17 installed if running without Docker
- Node.js 20+
- Python 3.12+

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
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Immediate next tasks

1. install frontend dependencies and verify the app starts
2. replace fixture routes with database-backed repositories
3. add Alembic migrations
4. implement real astronomy calculations and tests
