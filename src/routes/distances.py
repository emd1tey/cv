# src/routes/distances.py
import logging
from typing import List

from fastapi import APIRouter
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from pydantic import BaseModel

from src.config.settings import CITIES, GDANSK_COORDS, KRAKOW_COORDS

router = APIRouter()
geolocator = Nominatim(user_agent="polish_city_distances")

logger = logging.getLogger(__name__)


class CityDistance(BaseModel):
    city: str
    latitude: float
    longitude: float
    distance_to_krakow: float
    distance_to_gdansk: float


@router.get("/api/distances", response_model=List[CityDistance])
async def get_distances():
    distances = []
    for city in CITIES:
        location = geolocator.geocode(city + ", Poland")
        if location:
            city_coords = (location.latitude, location.longitude)
            distance_to_krakow = geodesic(city_coords, KRAKOW_COORDS).kilometers
            distance_to_gdansk = geodesic(city_coords, GDANSK_COORDS).kilometers
            distances.append(
                CityDistance(
                    city=city,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    distance_to_krakow=distance_to_krakow,
                    distance_to_gdansk=distance_to_gdansk,
                )
            )
            logger.info(f"Processed city: {city}")
        else:
            logger.warning(f"Could not find location for city: {city}")

    return distances
