import { useEffect, useRef, useState } from 'react'

import './App.css'
import { 
	Streamlit, 
  withStreamlitConnection,
} from "streamlit-component-lib";
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import OSM from 'ol/source/OSM.js'
import 'ol/ol.css';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector'; 
import { Style, Circle as CircleStyle, Fill, Stroke, Icon } from 'ol/style';
import GeoJSON from 'ol/format/GeoJSON';
import { fromLonLat, toLonLat } from 'ol/proj';
import Overlay from 'ol/Overlay.js';
import { toStringHDMS } from 'ol/coordinate.js';
import KML from 'ol/format/KML';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

function App(props) {
  const mapRef = useRef(); // 🔹 Create a ref for the map container
  const points = props.args.points;
  const kml_json = props.args.kml_json;
  console.log(props.args.points);
  const popupRef = useRef();
  let [popover, setPopover] = useState(null);

  console.log(kml_json);

  // Placeholder function to get local points.
  function getLocalPoints(point, map) {
    const pointFeatures = [];
    const pixel = map.getEventPixel(point.originalEvent);

    // Now gets several nearby features; want to get the closest one only
    map.forEachFeatureAtPixel(pixel, function (pointFeature) {
        pointFeatures.push(pointFeature);
    });

    return pointFeatures;
  }



  useEffect(() => {

    

    const map = new Map({
      target: mapRef.current,
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      view: new View({
        center: fromLonLat([-96.99694730156556, 32.93556622680157]),
        zoom: 13,
      }),
    });

    // Popup showing the position the user clicked
    const popup = new Overlay({
      element: popupRef.current,
    });
    map.addOverlay(popup);

    Streamlit.setComponentValue("Map initialized");
    Streamlit.setFrameHeight(700);
    
    // Load GeoJSON data, if empty then print out error to console
    try { 
      if (Object.keys(points).length !== 0) {
          const anomalyAlerts = new VectorLayer({ 
              source: new VectorSource({ 
                  features: new GeoJSON().readFeatures(points, 
                      {
                          featureProjection: 'EPSG:3857'
                      }
                  ) 
              }),
            style: new Style({
              image: new CircleStyle({
                radius: 9,
                fill: new Fill({
                  // color: '#ff819f'
                  color: 'rgba(255,129,159,0.8)'
                }),
                stroke: new Stroke({
                  color: '#000',
                  width: 0.5
                })
              })
            }),
          });

          // Add the vector layer to the map 
        map.addLayer(anomalyAlerts);
        // console.log(anomalyAlerts);

        // Event handler for map clicks:
        map.on('singleclick', (evt) => {
          const coordinate = evt.coordinate;
          const hdms = toStringHDMS(toLonLat(coordinate));

          // console.log(evt)
          const localFeatures = getLocalPoints(evt, map)
          console.log(localFeatures)

          // Array holds each info for each feature received by localFeatures
          const featuresInfoList = [];

          // Populate featureInfo array => replace with array.map()?
          if (localFeatures.length > 0 ) {
            let i, ii
            for (i = 0, ii = localFeatures.length; i < ii; ++i) {

                // temp object to hold info for each point
                let FeatureInfoObj = localFeatures[i];

                featuresInfoList.push(FeatureInfoObj);
                
            }

            console.log(Object.entries(featuresInfoList[0]["values_"]).map((item) => {
                return `${item[0]} : ${item[1]}`
            }))      
            
            const info_content = 
                `
                    <div class="card-header">
                        Point Info
                    </div>
                    <div class="card-body">
                        <ul class="list-group list-group-flush fs-6">
                            ${
                                Object.entries(featuresInfoList[0]["values_"]).map(([key, value]) => {
                                    if(key !== "geometry") {
                                        return `<li class="list-group-item" key=${key}>
                                            ${key} : ${value}
                                        </li>`;
                                    }
                                }).join('')
                            }
                        </ul>
                    </div>
                `
            
            const latitude = featuresInfoList[0]["values_"]["latitude"]
            const longitude =  featuresInfoList[0]["values_"]["longitude"] 
            const name = featuresInfoList[0]["values_"]["name"]
            
            // Set element html to innerContent and display 
            let element = popupRef.current;
            popup.setPosition(coordinate);
            
            if (element) {
                element.style.display = 'block';
                element.innerHTML = info_content;
            } else {
                console.log("element is not there: ", element)
            }
              

            // if exit button clicked, then destory overlay popup       

            // Correctly serialize the popover instance data before sending to streamlit
            const popoverData = { 
                content: info_content, 
                title: "Point Info", 
            };
            Streamlit.setComponentValue(JSON.stringify({ "name": name, "lat": latitude, "long": longitude }));
              
              
          } else {
              // get rid of popup
              popup.setPosition(undefined);
              // return empty obj to streamlit
              Streamlit.setComponentValue(null);
          }

          console.log(featuresInfoList[0])


          
      });



        
        
        
      }
    } catch (error) {
        console.error("error loading geojson data: (Maybe no points): Ignoring error: ", error);
    }


    // add kml to map http://localhost:8502/dashboard/static
    const kmlLayer = new VectorLayer({
      title: "KML Layer",
      source: new VectorSource({
        url: "http://localhost:8502/dashboard/app/static/sampleRoute.kml",
        format: new KML({
          extractStyles: false,
        }),
      }),
      // style: new Style({
      //   stroke: new Stroke({
      //       color: "blue",
      //       width: 9,
      //       lineCap: 'round',
      //   })
      // })
      style: function (feature) {
        const geomType = feature.getGeometry().getType();
        if (geomType === 'LineString') {
          return new Style({
            stroke: new Stroke({
              color: 'rgba(255, 162, 219, 0.9)',
              width: 9,
              lineCap: 'round',
            }),
          });
        } else if (geomType === 'Point') {
          return new Style({
            image: new CircleStyle({
              radius: 9,
              fill: new Fill({
                // color: '#ff819f'
                color: 'rgba(255,129,159,0.8)'
              }),
              stroke: new Stroke({
                color: '#000',
                width: 0.5
              }) 
            })
          });
        }
      }
    });

    map.addLayer(kmlLayer);

    return () => map.setTarget(undefined)
  }, [points]);

  
 



  return (
    <>
      <div
      ref={mapRef}
      style={{ height: '100%', width: '100%'}}
      className="map-container"
      />
      <div id="popup" ref={popupRef} className="card p-0" style={{ display: 'none'}}/>
    </>
    
  );
}

export default withStreamlitConnection(App);
//export default App;
