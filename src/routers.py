from fastapi import APIRouter
from src.teams.controller import router as teams_router
from src.players.controller import router as players_router

api_router = APIRouter()
api_router.include_router(teams_router, tags=["teams"])
api_router.include_router(players_router, tags=["players"])
