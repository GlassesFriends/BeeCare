'{% load static %}'
var dataFamilys = [];
var dataSubfamilys = [];

$(function () {
    var coordsArray = [];
    var contentInfo = [];
    var contentImage = [];

    var dataSightingBees = [];
    var dataBees = [];

    //AL MOMENTO DE LA CARGA DE LA PAGINA SE INICIALIZA LA CARGA DEL MAPA
    window.addEventListener("load", async () => {
        await initialLoad();
    });

    //DURANTE LA CARGA SE MANDA LLAMAR EL METODO ENCARGADO 
    //DE MOSTRAR LA LISTA DE AVISTAMIENTOS
    const initialLoad = async () => {
        await listSightings(); 

    }

    //METODO QUE SE ENCARGA DE RECUPERAR LOS DATOS DE LOS AVISTAMIENTOS
    const listSightings = async () => {
        try {
            //SOLICITUD DE DATOS
            const response = await fetch("../coord/");
            const data = await response.json();
            
            //CONDICION QUE COMPRUEBA SI HAY DATOS
            if (data.message == "Success") {
                for (j = 0; j < data.sighting.length; j++) {

                    listlat = parseFloat(data.sighting[j]['sighLat']);
                    listlng = parseFloat(data.sighting[j]['sighLng']);

                    liststring = (data.sighting[j]['sighComment']);

                    listSightingBee = parseFloat(data.sighting[j]['sighBee_id']);

                    listImage = data.sighting[j]['sighPicture'];


                    coordsArray.push({ lat: listlat, lng: listlng });
                    contentInfo.push(liststring);
                    dataSightingBees.push([listSightingBee]);
                    contentImage.push("https://res.cloudinary.com/dwxkhmtb3/" + listImage);
                }
            }


            const response1 = await fetch("../bee/");
            const data1 = await response1.json();

            //CONDICION ENCARGADA DE COMPROBAR SI EXISTEN REGISTADAS ABEJAS
            if (data1.message == "Success") {

                //CICLO FOR ENCARGADO DE OBTENER LOS DATOS DE LAS ABEJAS
                for (k = 0; k < data1.bee.length; k++) {
                    listIdbees = (data1.bee[k]['id']);
                    listNamebees = (data1.bee[k]['beeName']);
                    dataBees.push([listIdbees, listNamebees])
                }
                for (n = 0; n < dataBees.length; n++) {
                    for (m = 0; m < dataSightingBees.length; m++) {
                        if (dataSightingBees[m]['0'] == dataBees[n]['0']) {
                            dataSightingBees[m]['1'] = dataBees[n]['1'];
                        }
                    }
                }
            }



            
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(getCoords, getError);
            }

            /*FUNCION ENCARGADA DE OBTENER LA UBICACION DEL
            USUARIO*/
            function getCoords(position) {
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;
                $('#sighLat').val(lat);
                $('#sighLng').val(lng);

                /*LLAMADA DE LA FUNCION initialize ENVIANDO COMO PARAMETROS 
                LAS COORDENADAS RECIEN OBTENIDAS*/
                initialize(lat, lng);
            }

            /*FUNCION ENCARGADA DE MANDAR COORDENADAS POR DEFAULT EN CASO DE NO
            ACTIVAR O CEDER PERMISOS */
            function getError(err) {
                initialize(32.4951447, -116.9407001);
            }

            /*FUNCION ENCARGADA DE INICIALIZAR EL MAPA, RECIBE LAS COORDENADAS COMO 
            PARAMETROS */
            function initialize(lat, lng) {

                var center = { lat: lat, lng: lng }

                var map = new google.maps.Map(document.getElementById('mapa'), {
                    zoom: 9,
                    center: center,
                    mapTypeId: 'hybrid',
                });

                /*INFORMACION QUE SE MUESTRA EN EL MARCADOR DEL MAPA */
                const infowindow1 = new google.maps.InfoWindow({
                    content: "Esta es tu posición actual...",
                    ariaLabel: "Uluru",
                });

                /*CREACION DEL MARCADOR EL CUAL TE MUESTRA EL PIN*/
                var marker1 = new google.maps.Marker({
                    position: new google.maps.LatLng(center),
                    map: map,
                    icon: "/static/img/icons/BeePin.png",
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    title: 'Colocame donde hay abejas!',
                });

                //EVENTO QUE DESENCADENA UNA ANIMACION Y MANDA LLAMAR LA VENTANA infowindow1
                marker1.addListener("click", () => {

                    if (marker1.getAnimation() !== null) {
                        marker1.setAnimation(null);
                    } else {
                        marker1.setAnimation(google.maps.Animation.BOUNCE);
                    }

                    infowindow1.open({
                        anchor: marker1,
                        map,
                    });
                })

                var infowindow2 = new google.maps.InfoWindow();
                var marker2, i;
                for (i = 0; i < coordsArray.length; i++) {

                    marker2 = new google.maps.Marker({
                        position: new google.maps.LatLng(coordsArray[i]),
                        map: map,
                        draggable: false,
                        title: 'Avistamientos de abejas',
                        icon: "/static/img/icons/BeeSighting.png",
                    });
                    google.maps.event.addListener(marker2, 'click', (function (marker2, i) {
                        return function () {
                            infowindow2.setContent(

                                "<table>" +
                                "<tr>" +
                                "<td>" + "<h4>" + dataSightingBees[i]['1'] + "</h4>" + "</td>" +
                                "<td>" + "</td>" +
                                "</tr>" +
                                "<tr>" +
                                "<td>" + contentInfo[i] + "</td>" +
                                "<td>" + `<div align="left"><img src="` + contentImage[i] + `"+ style="width: 80px;height:60px;border-radius:30%;">` + "</td>" +
                                "</tr>" +
                                "</table>"

                            );
                            infowindow2.open(map, marker2)
                        }
                    })(marker2, i));
                }

                google.maps.event.addListener(marker1, 'position_changed', function () {
                    getMarkerCoords(marker1);
                });

            }

            /*FUNCION ENCARGADA DE OBTENER LAS CORDENAS MEDIANTE MUEVES EL PIN O EL MARCADOR 
            EN EL MAPA */
            function getMarkerCoords(marker) {
                var markerCoords = marker.getPosition();
                $('#sighLat').val(markerCoords.lat());
                $('#sighLng').val(markerCoords.lng());
            }





            const response2 = await fetch("../family/");
            const data2 = await response2.json();

            /*CONDICION ENCARGADA DE COMPROBAR QUE EXISTEN DATOS */
            if (data2.message == "Success") {

                /*CICLO FOR ENCARGADO DE OBTENER LA INFORMACION Y CARGADA EN EL ARREGLO
                dataFamilys*/
                for (l = 0; l < data2.family.length; l++) {
                    listIdfamily = (data2.family[l]['id']);
                    listNamefamily = (data2.family[l]['familyName']);
                    dataFamilys.push([listIdfamily, listNamefamily]);
                }

                let options1 = ``;

                for (p = 0; p < dataFamilys.length; p++) {
                    options1 += `<option value='${dataFamilys[p][1]}'></option>`;
                }
                list2familyName.innerHTML = options1;
            }

            ///////////////////////////////////////////////////////////////////////

            const response3 = await fetch("../subfamily/");
            const data3 = await response3.json();

            //CONDICION ENCARGADA DE COMPROBAR SI EXISTEN DATOS
            if (data3.message == "Success") {

                /*CICLO FOR ENCARGADO DE OBTENER LA INFORMACION Y CARGADA EN EL ARREGLO
                dataSubFamilys*/
                for (q = 0; q < data3.subfamily.length; q++) {
                    listIdsubfamily = (data3.subfamily[q]['id']);
                    listNamesubfamily = (data3.subfamily[q]['subfamilyName']);
                    listFamilysubfamily = (data3.subfamily[q]['subfamilyFamily_id']);
                    dataSubfamilys.push([listIdsubfamily, listNamesubfamily, listFamilysubfamily]);
                }
            }

        } catch (error) {
            console.log(error)
        }
    };
});

function autoFieldSubfamily() {
    let famcommun = [];

    valueInputFamily = document.getElementById('familyName').value

    if (valueInputFamily != "" || valueInputFamily != null) {
        for (a = 0; a < dataFamilys.length; a++) {
            for (s = 0; s < dataSubfamilys.length; s++) {
                if (dataFamilys[a][0] == dataSubfamilys[s][2]) {
                    famcommun.push([dataSubfamilys[s][1], dataFamilys[a][1]]);
                }
            }
        }
        console.log(famcommun);

        let options2 = ``;
        for (t = 0; t < famcommun.length; t++) {
            if (famcommun[t][1] == valueInputFamily) {
                options2 += `<option value='${famcommun[t][0]}'></option>`;
            }
        }
        console.log(options2);
        list3subfamilyName.innerHTML = options2;
    }
}