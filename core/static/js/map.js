function createMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 33.894317, lng: 35.5002621},
        zoom: 14
    });
    return map
}

function markerIcon(type='material', icon='fiber_manual_record', color='red', size='large') {
    return `https://api.geoapify.com/v1/icon/?icon=${icon}&color=${color}&size=${size}&type=${type}&apiKey=f44d995e7b094f6c9c7583d0e57fd515`;
}

function setIcon(kind) {
    switch (kind) {
        case 'food':
            return markerIcon('awesome','utensils', 'green');

        case 'construction':
            return markerIcon('awesome', 'hard-hat', 'yellow');

        case 'ngo':
            return markerIcon('awesome', 'hands-helping', 'purple');

        case 'danger':
            return markerIcon('awesome', 'exclamation-triangle', 'yellow');

        case 'red cross':
            return markerIcon('awesome', 'ambulance', 'red');

        case 'damage':
            return 'https://api.geoapify.com/v1/icon/?type=awesome&color=red&icon=house-damage&iconSize=large&noWhiteCircle&apiKey=f44d995e7b094f6c9c7583d0e57fd515';

        default:
            return ''
    }
}

function addMarker(lat, lng, map, icon) {
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: map,
        icon: {url: setIcon(icon)},
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
