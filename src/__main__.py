# src/__main__.py
import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config.settings import STATIC_DIR
from src.routes import cv, distances
from src.utils.gendoc import build_mkdocs, create_cv, create_doc

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await create_doc(app)
    await create_cv()
    await build_mkdocs()
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(distances.router)
app.include_router(cv.router)

# Serve the static files
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


def main():
    uvicorn.run("src.__main__:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
