async function fetchDistances() {
    const response = await fetch('/distances');
    return response.json();
}

async function initMap() {
    const cities = await fetchDistances();
    
    const map = L.map('map').setView([52.237049, 21.017532], 6); // Center on Poland

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    const krakowCoords = [50.0647, 19.9450];
    const gdanskCoords = [54.3520, 18.6466];

    const krakowMarker = L.marker(krakowCoords).addTo(map)
        .bindPopup('Krakow').openPopup();
    const gdanskMarker = L.marker(gdanskCoords).addTo(map)
        .bindPopup('Gdansk').openPopup();

    cities.forEach(city => {
        const cityCoords = [city.latitude, city.longitude];
        const cityMarker = L.marker(cityCoords).addTo(map)
            .bindPopup(`<b>${city.city}</b><br>Distance to Krakow: ${city.distance_to_krakow.toFixed(2)} km<br>Distance to Gdansk: ${city.distance_to_gdansk.toFixed(2)} km`);
        
        // Draw lines to Krakow and Gdansk
        L.polyline([cityCoords, krakowCoords], {color: 'red'}).addTo(map);
        L.polyline([cityCoords, gdanskCoords], {color: 'blue'}).addTo(map);
    });
}

document.addEventListener('DOMContentLoaded', initMap);

