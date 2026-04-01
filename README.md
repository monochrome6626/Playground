# AstroShot Planner

AstroShot Planner is a web application for finding dates and times in the Kanto region when sunrise, sunset, moonrise, and moonset align with Tokyo Skytree or Tokyo Tower for photography planning.

## Project layout

- `frontend`: Next.js UI for search, results, and map views.
- `backend`: FastAPI service for search orchestration and astronomy calculations.
- `worker`: Background job notes and future batch entrypoint.
- `infra`: local infrastructure assets such as database data and migrations.
- `docs`: requirements, architecture, API design, schema, algorithm notes, and setup.

## Initial scope

- Search candidate alignments for Tokyo Skytree and Tokyo Tower.
- Support sunrise, sunset, moonrise, and moonset windows.
- Register manual shooting spots in the Kanto region.
- Rank theoretical matches by azimuth and altitude deltas.

## Local development

1. Copy `.env.example` to `.env`.
2. Start PostgreSQL, backend, and frontend with `docker compose up --build`.
3. Open `http://localhost:3000` for the UI and `http://localhost:8000/docs` for the API.

## Backend bootstrap (manual)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m alembic upgrade head
python -m app.scripts.seed_landmarks
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Detailed setup steps live in [docs/setup.md](/C:/Users/ux3bl/Documents/Playground/docs/setup.md).
