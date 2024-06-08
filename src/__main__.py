# src/__main__.py
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.routes import distances, cv
from src.utils.cv_generator import create_cv
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_cv(app)  # Pass FastAPI app instance to the function
    logging.info("Application startup")
    yield
    logging.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(distances.router)
app.include_router(cv.router)

# Serve the static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("src.__main__:app", host="0.0.0.0", port=8000, reload=True)
