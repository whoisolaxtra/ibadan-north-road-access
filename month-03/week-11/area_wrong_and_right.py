
import geopandas as gpd

# Load the ward polygon layer
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

print("Original CRS:", wards.crs)

# Incorrect: calculate area while the layer is in EPSG:4326
wards["area_wrong"] = wards.area

print("\nArea calculated in geographic CRS:")
print(wards[["ward_name", "area_wrong"]].head(3))

# Identify a suitable projected CRS
print("\nSuggested UTM CRS:", wards.estimate_utm_crs())

# Correct: reproject to WGS 84 / UTM Zone 31N
wards_utm = wards.to_crs(epsg=32631)

# Calculate area in square kilometres
wards_utm["area_km2"] = (
    wards_utm.area / 1_000_000
)

print("\nArea calculated in projected CRS:")
print(wards_utm[["ward_name", "area_km2"]].head(3))

print(
    "\nIbadan North total:",
    round(wards_utm["area_km2"].sum(), 1),
    "km2"
)
