
import geopandas as gpd

# Load the Ibadan North wards layer
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

# Inspect the layer
print("Layer name: wards")
print("Number of features:", len(wards))
print("Number of columns:", len(wards.columns))
print("Columns:", list(wards.columns))
print("Geometry types:", wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)
