
import geopandas as gpd

# Load wards and facilities in UTM Zone 31N
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

facilities = gpd.read_file(
    "data/processed/facilities.gpkg",
    layer="facilities"
).to_crs(epsg=32631)

# Create ward centroid points
centres = wards[["ward_name", "geometry"]].copy()
centres["geometry"] = centres.centroid

# Find the nearest facility to each ward centroid
nearest = gpd.sjoin_nearest(
    centres,
    facilities[["name", "geometry"]],
    how="left",
    distance_col="distance_m"
)

# Convert distance from metres to kilometres
nearest["distance_km"] = (
    nearest["distance_m"] / 1000
).round(2)

print(
    nearest[
        ["ward_name", "name", "distance_km"]
    ]
)
