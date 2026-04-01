from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health, landmarks, matches, searches, spots
from app.core.config import settings


app = FastAPI(
    title="AstroShot Planner API",
    version="0.1.0",
    summary="API for astronomy-assisted photography planning in the Kanto region.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(spots.router, prefix="/api")
app.include_router(landmarks.router, prefix="/api")
app.include_router(searches.router, prefix="/api")
app.include_router(matches.router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AstroShot Planner API is running."}
