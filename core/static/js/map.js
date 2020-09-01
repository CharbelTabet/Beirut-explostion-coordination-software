function createMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 33.894317, lng: 35.5002621},
        zoom: 14,
        streetViewControl: false,
        mapTypeControl: false,
    });
    return map
}

function addMarker(lat, lng, map, icon) {
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: map,
        icon: icons[icon],
        animation: google.maps.Animation.DROP,
        url: `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`
    });
    return marker
}

function clusterMarkers(map, markers) {
    new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

function addInfoWindow(htmlString='Hello world', marker) {
    let infoWindow = new google.maps.InfoWindow({
      content: htmlString
    });
    marker.addListener('click', () => {
      console.log('event started');
      infoWindow.open(map, marker);
    });
}

function addArea(lat, lng, radius) {
    circle = new google.maps.Circle({
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
        map,
        center: new google.maps.LatLng(lat, lng),
        radius: radius
    });
}

function addLegend(id) {
    var legend = document.getElementById(id);
    var table = document.createElement(table);
    for (iconName in icons) {
        // Table elements
        var tr = document.createElement('tr');
        var td = document.createElement('td');
        // Icon
        var icon = document.createElement('img');
        icon.src = icons[iconName];
        // Fill td
        td.appendChild(icon);
        td.innerHTML += ' ' + iconName;
        // Fill tr
        tr.appendChild(td);
        // Fill table
        table.appendChild(tr);
    }
    legend.appendChild(table);
}
