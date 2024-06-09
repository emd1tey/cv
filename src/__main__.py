# src/__main__.py
import argparse
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routes import cv, distances
from src.utils.cv_generator import create_cv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_cv()  # No need to pass FastAPI app instance here
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(distances.router)
app.include_router(cv.router)

# Serve the static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")


def main():
    parser = argparse.ArgumentParser(description="CV Generator")
    parser.add_argument(
        "command", choices=["runserver", "generate_cv"], help="Command to run"
    )
    args = parser.parse_args()

    if args.command == "runserver":
        uvicorn.run("src.__main__:app", host="0.0.0.0", port=8000, reload=True)
    elif args.command == "generate_cv":
        import asyncio

        asyncio.run(create_cv())


if __name__ == "__main__":
    main()
