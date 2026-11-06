
import pandas as pd
import geopandas as gpd

# Load the health facilities CSV
table = pd.read_csv("data/raw/health_facilities.csv")

print("Original facility types:")
print(table["type"].value_counts())

# Clean facility type names
table["type"] = table["type"].str.strip().replace({
    "PHC": "Primary Health Centre"
})

print("\nCleaned facility types:")
print(table["type"].value_counts())

# Convert coordinates into a GeoDataFrame
facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(
        table["longitude"],
        table["latitude"]
    ),
    crs="EPSG:4326"
)

# Save the point layer
facilities.to_file(
    "data/processed/my_facilities.gpkg",
    layer="facilities",
    driver="GPKG"
)

print("\nCRS:", facilities.crs)
print("Total facilities:", len(facilities))
print("Saved data/processed/my_facilities.gpkg")
