from fastapi import FastAPI
from routers import api_router

app = FastAPI(title="Tournament API", version="0.1.0")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
