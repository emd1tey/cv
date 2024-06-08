import argparse
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from pydantic import BaseModel
from typing import List
import os
import subprocess
import markdown
from fpdf import FPDF

app = FastAPI()
geolocator = Nominatim(user_agent="polish_city_distances")
output_pdf_path = "cv.pdf"

# Coordinates for Krakow and Gdansk
krakow_coords = (50.0647, 19.9450)
gdansk_coords = (54.3520, 18.6466)

class CityDistance(BaseModel):
    city: str
    latitude: float
    longitude: float
    distance_to_krakow: float
    distance_to_gdansk: float


@app.get("/api/distances", response_model=List[CityDistance])
async def get_distances():
    cities = [
        "Warsaw", "Krakow", "Gdansk", "Lodz", "Wroclaw", "Poznan", "Szczecin", 
        "Bydgoszcz", "Lublin", "Katowice", "Bialystok", "Gdynia"
    ]
    
    distances = []
    for city in cities:
        location = geolocator.geocode(city + ", Poland")
        if location:
            city_coords = (location.latitude, location.longitude)
            distance_to_krakow = geodesic(city_coords, krakow_coords).kilometers
            distance_to_gdansk = geodesic(city_coords, gdansk_coords).kilometers
            distances.append(
                CityDistance(
                    city=city,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    distance_to_krakow=distance_to_krakow,
                    distance_to_gdansk=distance_to_gdansk
                )
            )
    
    return distances

async def create_cv():
    markdown_file_path = "wiki/cv.md" 

    if not os.path.exists(markdown_file_path):
        raise HTTPException(status_code=404, detail="Markdown file not found")

    with open(markdown_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        html_content = markdown.markdown(content)

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CV</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    with open('static/cv.html', 'w') as f:
        f.write(html_template)

    pdf = FPDF()
    pdf.add_page()
    pdf.write_html(html_content)
    pdf.output("static/cv.pdf")


# Serve the static files
app.mount("/wiki", StaticFiles(directory="site", html=True), name="wiki")
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML and PDF")
    parser.add_argument(
        "--convert", 
        action="store_true", 
        help="Convert Markdown file to HTML and PDF"
    )
    args = parser.parse_args()

    if args.convert:
        import asyncio
        asyncio.run(create_cv())
