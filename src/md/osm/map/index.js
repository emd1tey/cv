function GetMap() {
    map = new OpenLayers.Map("OSMap");//инициализация карты
    var mapnik = new OpenLayers.Layer.OSM();//создание слоя карты
    map.addLayer(mapnik);//добавление слоя
    map.setCenter(new OpenLayers.LonLat(27.5613, 53.9007) //(долгота, широта)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	  ), 12// масштаб
        );
    var layerMarkers = new OpenLayers.Layer.Markers("Markers");//создаем новый слой маркеров
    map.addLayer(layerMarkers);//добавляем этот слой к карте
        var size = new OpenLayers.Size(35, 35);//размер картинки для маркера
        var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h); //смещение картинки для маркера
        var icon = new OpenLayers.Icon('/icon.png', size, offset);//картинка для маркера

// Попиздовал генератор на питоне

layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613,53.9007).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5813,53.9107).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5413,53.9107).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5813,53.8907).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5413,53.8907).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6013,53.9207).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5213,53.9207).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6013,53.8807).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5213,53.8807).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6213,53.9307).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5013,53.9307).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6213,53.8707).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5013,53.8707).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6413,53.9407).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.4813,53.9407).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6413,53.8607).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.4813,53.8607).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
}
