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
//    map.events.register('preaddlayer', map, function (e) {
        var size = new OpenLayers.Size(25, 25);//размер картинки для маркера
        var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h); //смещение картинки для маркера
        var icon = new OpenLayers.Icon('/1024px-Smiley.svg.png', size, offset);//картинка для маркера
//       layerMarkers.addMarker(//добавляем маркер к слою маркеров
//            new OpenLayers.Marker(map.getLonLatFromViewPortPx(e.xy), //координаты вставки маркера
//            icon));//иконка маркера

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613, 53.9007)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon));

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5554, 53.9581)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon.clone()));

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5091, 53.9411)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon.clone()));

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5791, 53.9415)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon.clone()));

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613, 53.9007)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon.clone()));

    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613, 53.9007)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
            new OpenLayers.Projection("EPSG:900913") // переобразование проекции
	    ),icon.clone()));

//    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613,53.9007),icon));
//    layerMarkers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(27.5613,53.9007),icon.clone()));
}
