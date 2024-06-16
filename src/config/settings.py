# src/config/settings.py

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration variables
EXPOSE_PORT = int(os.getenv('EXPOSE_PORT', 8001))
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
