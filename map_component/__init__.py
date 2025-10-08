import streamlit.components.v1 as components
import os
import pandas as pd
import geopandas as gpd
import json




_component_funct = components.declare_component(
    "map",
    path=os.path.join(os.path.dirname(__file__), "frontend", "dist")
                                        )
def st_map(points):

    

    if points:

        # Create a regular DataFrame
        df = pd.DataFrame(points)

        # Convert to GeoDataFrame with Point geometry
        gdf = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
            crs="EPSG:4326"  # WGS84
        )

        # gdf = gpd.GeoDataFrame(points, geometry=gpd.points_from_xy(points["longitude"], points["latitude"]))
        geojson = gdf.to_json()

        component_value = _component_funct(points=geojson)
        return component_value

    component_value = _component_funct(points=json.dumps({}))
    return component_value
