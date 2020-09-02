function createMap() {
    let map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 33.894317, lng: 35.5002621},
        zoom: 14,
        streetViewControl: false,
        mapTypeControl: false,
    });
    return map
}

function addMarker(lat, lng, map, kind) {
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: map,
        icon: setIcons(kind),
        animation: google.maps.Animation.DROP,
        url: `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`
    });
    return marker
}

function clusterMarkers(map, markers) {
    new MarkerClusterer(map, markers,
        {styles: [
            {
                height: 38,
                url: icons["Damages Clusters"]["-10"],
                width: 38,
            },
            {
                height: 38,
                url: icons["Damages Clusters"]["10+"],
                width: 38,
            },
            {
                height: 38,
                url: icons["Damages Clusters"]["20+"],
                width: 38,
            },
            {
                height: 38,
                url: icons["Damages Clusters"]["30+"],
                width: 38,
            },
            {
                height: 38,
                url: icons["Damages Clusters"]["40+"],
                width: 38,
            }
        ]}
    );
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
    var legendTitle = document.createElement('h3');
    legendTitle.innerHTML = 'Legend';
    legend.appendChild(legendTitle);
    var row = document.createElement('div');
    row.classList.add("row");
    for (iconsSet in icons) {
        // Creating html elements
        var p = document.createElement('p');
        var col = document.createElement('div');
        var setTitle = document.createElement('h4');
        setTitle.innerHTML = iconsSet;
        col.classList.add("col-xl-3");
        col.classList.add("col-lg-4");
        col.classList.add("col-md-6");
        col.classList.add("col-xs-12");
        col.appendChild(setTitle);
        
        // Filling html elements
        for (iconName in icons[iconsSet]) {
            var span = document.createElement('span');
            var icon = document.createElement('img');
            icon.src = icons[iconsSet][iconName];
            span.appendChild(icon);
            span.innerHTML += ' ' + iconName;
            col.appendChild(span);
            col.innerHTML += '<br>';
        }
        col.append(p);
        row.appendChild(col);
    }
    legend.appendChild(row)
}
