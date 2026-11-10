
import geopandas as gpd

# Load ward polygons
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

# Check geometry validity before correction
print("Invalid before:", (~wards.geometry.is_valid).sum())

# Repair invalid geometries
wards["geometry"] = wards.geometry.make_valid()

# Check geometry validity after correction
print("Invalid after:", (~wards.geometry.is_valid).sum())

# Check geometry types
print("\nGeometry types:")
print(wards.geom_type.value_counts())

# Save the corrected layer
wards.to_file(
    "month-03/week-11/outputs/wards_fixed.gpkg",
    driver="GPKG"
)

print("\nCorrected layer saved successfully.")
