import streamlit.components.v1 as components
import os
import pandas as pd
import geopandas as gpd
import json


_component_funct = components.declare_component(
    "map",
    path=os.path.join(os.path.dirname(__file__), "frontend", "dist")
                                        )
def st_map(points_df):

    

    if not points_df.empty:

        # Create a regular DataFrame
        # df = pd.DataFrame(points) # do this before sending to map

        # Convert to GeoDataFrame with Point geometry
        gdf = gpd.GeoDataFrame(
            points_df,
            geometry=gpd.points_from_xy(points_df["longitude"], points_df["latitude"]),
            crs="EPSG:4326"  # WGS84
        )

        # gdf = gpd.GeoDataFrame(points, geometry=gpd.points_from_xy(points["longitude"], points["latitude"]))
        geojson = gdf.to_json()

        component_value = _component_funct(points=geojson)
        return component_value

    component_value = _component_funct(points=json.dumps({}))
    return component_value
