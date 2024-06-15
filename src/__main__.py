import logging
import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config.settings import STATIC_DIR, EXPOSE_PORT, SECRET_TOKEN, APP_NAME, SERVER_URL
from src.routes import distances, cloud
from src.utils.gendoc import create
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider



from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure OpenTelemetry for traces
resource = Resource.create({SERVICE_NAME: APP_NAME})
trace_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(trace_provider)
trace_exporter = OTLPSpanExporter(endpoint=SERVER_URL, insecure=True)
trace_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

# Configure OpenTelemetry for metrics
metrics_exporter = OTLPMetricExporter(endpoint=SERVER_URL, insecure=True)
metric_reader = PeriodicExportingMetricReader(exporter=metrics_exporter, export_interval_millis=15000)
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])

# Instrument logging
LoggingInstrumentor().instrument(set_logging_format=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await create(app)
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

# Configure Elastic APM
apm_config = {
    'SERVICE_NAME': APP_NAME,
    'SERVER_URL': SERVER_URL,
    'ENVIRONMENT': 'dev',
    'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication',
    'SECRET_TOKEN': SECRET_TOKEN
}
apm_client = make_apm_client(apm_config)
app.add_middleware(ElasticAPM, client=apm_client)

# Instrument FastAPI with OpenTelemetry
FastAPIInstrumentor().instrument_app(app)

# Register routes
app.include_router(distances.router)
app.include_router(cloud.router)

# Serve the static files
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("src.__main__:app", host="0.0.0.0", port=EXPOSE_PORT)
