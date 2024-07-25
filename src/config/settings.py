# src/config/settings.py

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration variables
EXPOSE_PORT = int(os.getenv('EXPOSE_PORT', 8000))
APP_NAME = os.getenv('APP_NAME', 'Organizer')
STATIC_DIR = os.getenv('STATIC_DIR', 'static')

#maps
KRAKOW_COORDS = (50.0647, 19.9450)
GDANSK_COORDS = (54.3520, 18.6466)
CITIES = [
    "Warsaw", "Krakow", "Gdansk", "Lodz", "Wroclaw", "Poznan", "Szczecin",
    "Bydgoszcz", "Lublin", "Katowice", "Bialystok", "Gdynia"
]

#cloudflare
API_TOKEN = os.getenv('API_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}
ZONES_URL = 'https://api.cloudflare.com/client/v4/zones'


SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SERVER_URL = "https://e7a3f6e6da864bc28f121e313a551771.apm.us-central1.gcp.cloud.es.io:443"
ENVIRONMENT = os.getenv('ENVIRONMENT', "dev")
#elastic
OTEL_EXPORTER_OTLP_ENDPOINT = f"{SERVER_URL}"
OTEL_EXPORTER_OTLP_HEADERS = f"Authorization=Bearer%20{SECRET_TOKEN}"
OTEL_METRICS_EXPORTER = os.getenv('OTEL_METRICS_EXPORTER', 'otlp')
OTEL_LOGS_EXPORTER = os.getenv('OTEL_LOGS_EXPORTER', 'otlp')
