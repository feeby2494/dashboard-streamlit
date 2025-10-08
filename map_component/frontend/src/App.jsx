import { useEffect, useRef } from 'react'

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
import { Style, Circle as CircleStyle, Fill, Stroke, RegularShape } from 'ol/style';
import GeoJSON from 'ol/format/GeoJSON';

function App(props) {
  const mapRef = useRef(); // 🔹 Create a ref for the map container
  const points = props.args.points;
  console.log(props.args.points);


  useEffect(() => {

    const map = new Map({
      target: mapRef.current,
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      view: new View({
        center: [0, 0],
        zoom: 2,
      }),
    });

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
        console.log(anomalyAlerts)
      }
    } catch (error) {
        console.error("error loading geojson data: (Maybe no points): Ignoring error: ", error);
    }


    return () => map.setTarget(undefined)
  }, [points]);

  

  return (
    <>
      <div
      ref={mapRef}
      style={{ height: '100%', width: '100%'}}
      className="map-container"
      />
    </>
    
  );
}

export default withStreamlitConnection(App);
// export default App;
