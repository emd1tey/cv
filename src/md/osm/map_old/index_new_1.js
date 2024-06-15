function GetMap() {
    map = new OpenLayers.Map("OSMap");//инициализация карты
    var mapnik = new OpenLayers.Layer.OSM();//создание слоя карты
    map.addLayer(mapnik);//добавление слоя
    map.setCenter(new OpenLayers.LonLat(27.5613, 53.9007) //(долгота, широта)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	  ), 10// масштаб
        );
    var layerMarkers = new OpenLayers.Layer.Markers("Markers");//создаем новый слой маркеров
    map.addLayer(layerMarkers);//добавляем этот слой к карте
        var size = new OpenLayers.Size(25, 25);//размер картинки для маркера
        var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h); //смещение картинки для маркера
        var icon = new OpenLayers.Icon('/1024px-Smiley.svg.png', size, offset);//картинка для маркера

layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5091,53.9007).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5291,53.9207).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5491,53.9407).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5691,53.9607).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5891,53.9807).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.6091,54.0007).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), icon.clone()));
}
