from dotenv import load_dotenv
import os
import logging
from fastapi import FastAPI
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Load environment variables
load_dotenv()

# Configuration
EXPOSE_PORT = int(os.getenv('EXPOSE_PORT', 8000))
APP_NAME = os.getenv('APP_NAME', 'Organizer')
STATIC_DIR = os.getenv('STATIC_DIR', 'static')
OUTPUT_PDF_PATH = os.getenv('OUTPUT_PDF_PATH', 'cv/resume.pdf')
KRAKOW_COORDS = (50.0647, 19.9450)
GDANSK_COORDS = (54.3520, 18.6466)
CITIES = [
    "Warsaw", "Krakow", "Gdansk", "Lodz", "Wroclaw", "Poznan", "Szczecin",
    "Bydgoszcz", "Lublin", "Katowice", "Bialystok", "Gdynia"
]
API_TOKEN = os.getenv('API_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}
ZONES_URL = 'https://api.cloudflare.com/client/v4/zones'
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SERVER_URL = "https://6c18cf75b2ee4e6e851cf739641bb283.apm.us-central1.gcp.cloud.es.io:443"
OTEL_EXPORTER_OTLP_ENDPOINT = "https://6c18cf75b2ee4e6e851cf739641bb283.apm.us-central1.gcp.cloud.es.io:443"
OTEL_EXPORTER_OTLP_HEADERS = f"Authorization=Bearer%20{SECRET_TOKEN}"
OTEL_METRICS_EXPORTER = os.getenv('OTEL_METRICS_EXPORTER', 'otlp')
OTEL_LOGS_EXPORTER = os.getenv('OTEL_LOGS_EXPORTER', 'otlp')

def configure_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def configure_opentelemetry(app_name: str, server_url: str, secret_token: str):
    logger = logging.getLogger(__name__)
    logger.info("Starting OpenTelemetry configuration")

    resource = Resource.create({SERVICE_NAME: app_name})
    trace_provider = TracerProvider(resource=resource)
    trace_exporter = OTLPSpanExporter(endpoint=server_url, headers=OTEL_EXPORTER_OTLP_HEADERS, insecure=True)
    trace_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

    metrics_exporter = OTLPMetricExporter(endpoint=server_url, headers=OTEL_EXPORTER_OTLP_HEADERS, insecure=True)
    metric_reader = PeriodicExportingMetricReader(exporter=metrics_exporter, export_interval_millis=15000)
    MeterProvider(resource=resource, metric_readers=[metric_reader])

    trace.set_tracer_provider(trace_provider)
    LoggingInstrumentor().instrument(set_logging_format=True)

    logger.info("OpenTelemetry configuration completed")

def configure_apm(app: FastAPI, app_name: str, server_url: str, secret_token: str):
    apm_config = {
        'SERVICE_NAME': app_name,
        'SERVER_URL': server_url,
        'ENVIRONMENT': 'dev',
        'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication',
        'SECRET_TOKEN': secret_token
    }
    apm_client = make_apm_client(apm_config)
    app.add_middleware(ElasticAPM, client=apm_client)
    return apm_client
