import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import app
from src.config.settings import configure_logging

logger = configure_logging()

client = TestClient(app)

# Helper function to retrieve all GET routes
def get_get_routes(app: FastAPI):
    routes = []
    logger.info(app.routes)
    for route in app.routes:
        logger.info(route.__class__.__name__)
        if route.__class__.__name__ == "APIRoute":
            logger.info("huy")
            routes.append(route.path)
    logger.info(routes)
    return routes

@pytest.mark.parametrize("route", get_get_routes(app))
def test_get_routes(route):
    response = client.get(route)
    logger.info(response)
    assert response.status_code >= 200, f"Failed on {route} with status code {response.status_code}"
