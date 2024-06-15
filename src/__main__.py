import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config.settings import STATIC_DIR, EXPOSE_PORT, APP_NAME, SERVER_URL, SECRET_TOKEN
from src.config.settings import configure_opentelemetry, configure_logging, configure_apm
from src.routes import distances, cloud, debugs
from src.utils.gendoc import create
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

logger = configure_logging()
configure_opentelemetry(APP_NAME, SERVER_URL, SECRET_TOKEN)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await create(app)
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

FastAPIInstrumentor().instrument_app(app)
apm_client = configure_apm(app, APP_NAME, SERVER_URL, SECRET_TOKEN)

app.include_router(distances.router)
app.include_router(cloud.router)
app.include_router(debugs.router)

os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)
