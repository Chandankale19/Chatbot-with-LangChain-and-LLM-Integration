from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from src.interface.api import router
from src.utils.logger import setup_logger
from fastapi.staticfiles import StaticFiles
import os

logger = setup_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("FastAPI application started")
    yield
    # Shutdown logic
    logger.info("FastAPI application shutting down")

app = FastAPI(
    title="Teacher Registry Chatbot",
    description="A chatbot for querying teacher registry data using Google Gemini",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(router)

# Mount static files from the absolute or relative path correctly
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
