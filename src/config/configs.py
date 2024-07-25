# src/config/configs.py

import logging
from fastapi import FastAPI
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from fastapi.staticfiles import StaticFiles
import os
from contextlib import asynccontextmanager

from src.config.settings import APP_NAME, SERVER_URL, SECRET_TOKEN, STATIC_DIR, OTEL_EXPORTER_OTLP_HEADERS
from src.routes import distances, cloud, debugs
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from src.utils.gendoc import create_doc

def configure_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

logger = configure_logging()

def configure_opentelemetry(app_name: str, server_url: str, secret_token: str):
    logger.info("Starting OpenTelemetry configuration")

    resource = Resource.create({SERVICE_NAME: app_name})
    trace_provider = TracerProvider(resource=resource)
    trace_exporter = OTLPSpanExporter(endpoint=server_url, headers=OTEL_EXPORTER_OTLP_HEADERS, insecure=True)
    trace_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

    metrics_exporter = OTLPMetricExporter(endpoint=server_url, headers=OTEL_EXPORTER_OTLP_HEADERS, insecure=True)
    metric_reader = PeriodicExportingMetricReader(exporter=metrics_exporter, export_interval_millis=15000)
    MeterProvider(resource=resource, metric_readers=[metric_reader])

    LoggingInstrumentor().instrument(set_logging_format=True)

    logger.info("OpenTelemetry configuration completed")
    return trace_provider

def configure_apm(app: FastAPI):
    apm_config = {
        'SERVICE_NAME': APP_NAME,
        'SERVER_URL': SERVER_URL,
        'ENVIRONMENT': 'dev',
        'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication',
        'SECRET_TOKEN': SECRET_TOKEN
    }
    apm_client = make_apm_client(apm_config)
    app.add_middleware(ElasticAPM, client=apm_client)
    return apm_client


def create_app():
    app = FastAPI(lifespan=lifespan)
    FastAPIInstrumentor().instrument_app(app)
    configure_apm(app)

    app.include_router(distances.router)
    app.include_router(cloud.router)
    app.include_router(debugs.router)

    os.makedirs(STATIC_DIR, exist_ok=True)
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
    return app

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await create_doc(app)
    yield
    logger.info("Application shutdown")
