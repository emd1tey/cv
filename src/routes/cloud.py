import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from src.config.settings import ZONES_URL, HEADERS
from src.utils.mdhelp import dict_to_markdown_table

router = APIRouter()
logger = logging.getLogger(__name__)

def get_zones():
    try:
        logger.info(f"ZONES_URL: {ZONES_URL} || HEADERS: {HEADERS}")
        response = requests.get(ZONES_URL, headers=HEADERS)
        logger.info(f"{response}")
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)
        zones = response.json().get('result', [])
        return zones
    except requests.exceptions.HTTPError as http_err:
        logger.exception(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logger.exception(f"Error fetching zones: {err}")


def get_dns_records(zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        logger.exception(f"Error fetching DNS records for zone {zone_id}: {response.status_code} {response.text}")

    dns_records = response.json().get('result', [])
    return dns_records


@router.get("/api/dns")
async def get_dns_data():
    try:
        zones = get_zones()
        result = {}
        for zone in zones:
            zone_name = zone['name']
            dns_records = get_dns_records(zone['id'])
            zone_records = []

            for record in dns_records:
                record_dict = {
                    "type": record['type'],
                    "name": record['name'],
                    "content": record['content']
                }
                zone_records.append(record_dict)

            result[zone_name] = zone_records

        mds = await dict_to_markdown_table(result)
        for md in mds:
            logger.info(md)
        return result
    except Exception:
        logger.exception("/api/dns failed, check cred!!!!")
        return JSONResponse(
            status_code=418,
            content={"message": "Oops! There goes a rainbow..."},
        )
