#!/bin/sh
# Iniciar o aplicativo
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
