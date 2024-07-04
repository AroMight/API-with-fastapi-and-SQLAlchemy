from fastapi import APIRouter
from teams.controller import router as teams_router

api_router = APIRouter()
api_router.include_router(teams_router, prefix="/teams")
