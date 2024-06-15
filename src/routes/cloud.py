import logging
from fastapi import APIRouter
import requests
from src.config.settings import ZONES_URL, HEADERS

router = APIRouter()
logger = logging.getLogger(__name__)

def get_zones():
    response = requests.get(ZONES_URL, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error fetching zones: {response.status_code} {response.text}")

    zones = response.json().get('result', [])
    return zones


def get_dns_records(zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error fetching DNS records for zone {zone_id}: {response.status_code} {response.text}")

    dns_records = response.json().get('result', [])
    return dns_records


@router.get("/api/dns")
async def get_dns_data():
    zones = get_zones()
    result = {}
    for zone in zones:
        zone_name = zone['name']
        dns_records = get_dns_records(zone['id'])
        zone_records = []

        for record in dns_records:
            # Создаем словарь для каждой DNS записи
            record_dict = {
                "type": record['type'],
                "name": record['name'],
                "content": record['content']
            }
            # Добавляем запись в список для текущей зоны
            zone_records.append(record_dict)

        # Добавляем список записей в словарь по имени зоны
        result[zone_name] = zone_records

    # Преобразуем результат в JSON формат и возвращаем его
    return result
