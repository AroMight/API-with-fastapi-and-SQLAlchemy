from fastapi import FastAPI
from src.routers import api_router

app = FastAPI(title="Tournament API", version="0.1.2")

app.include_router(api_router)
