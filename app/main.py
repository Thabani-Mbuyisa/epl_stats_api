from fastapi import FastAPI

from app.router.club import router as club_router
from app.router.epl_accumulated_player_stats_router import (
    router as accumulated_player_stats_router
)


app = FastAPI(
    title="Premier League Stats",
    version="1.0.0"
)


app.include_router(
    club_router,
    prefix="/api/v1"
)

app.include_router(
    accumulated_player_stats_router,
    prefix="/api/v1"
)