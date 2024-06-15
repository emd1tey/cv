from dotenv import load_dotenv
import os
load_dotenv()

#App
EXPOSE_PORT = 8000
APP_NAME = 'Organizer'
STATIC_DIR = "static"
OUTPUT_PDF_PATH = "cv/resume.pdf"
#OSM
KRAKOW_COORDS = (50.0647, 19.9450)
GDANSK_COORDS = (54.3520, 18.6466)
CITIES = [
    "Warsaw",
    "Krakow",
    "Gdansk",
    "Lodz",
    "Wroclaw",
    "Poznan",
    "Szczecin",
    "Bydgoszcz",
    "Lublin",
    "Katowice",
    "Bialystok",
    "Gdynia",
]
#CF
API_TOKEN = os.getenv('API_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}
ZONES_URL = 'https://api.cloudflare.com/client/v4/zones'
#ES
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SERVER_URL = 'https://6c18cf75b2ee4e6e851cf739641bb283.apm.us-central1.gcp.cloud.es.io:443'
