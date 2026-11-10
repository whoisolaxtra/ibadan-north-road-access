
import geopandas as gpd

# Load ward polygons
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

# Load health facility points
facilities = gpd.read_file(
    "data/processed/facilities.gpkg",
    layer="facilities"
)

# Reproject facilities to match the ward CRS
facilities = facilities.to_crs(wards.crs)

# Create a 500-metre buffer around each facility
facilities_buffer = facilities.to_crs(epsg=32631)
facilities_buffer["geometry"] = facilities_buffer.geometry.buffer(500)

# Reproject buffers to the ward CRS
facilities_buffer = facilities_buffer.to_crs(wards.crs)

# Spatial join: identify facilities within wards
joined = gpd.sjoin(
    facilities,
    wards,
    how="left",
    predicate="within"
)

print("Total facilities:", len(facilities))
print("Total wards:", len(wards))
print("Spatial join records:", len(joined))
print("\nFacilities by ward:")
print(joined["ward_name"].value_counts(dropna=False))

print("\nBuffer features:", len(facilities_buffer))
