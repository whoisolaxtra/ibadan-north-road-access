
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

# Calculate ward area in square kilometres
wards["area_km2"] = wards.area / 1_000_000

# Create a 2 km buffer around each facility
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)

# Dissolve overlapping facility buffers
reach = reach.dissolve()

# Identify ward areas outside the facility coverage zones
uncovered = gpd.overlay(
    wards,
    reach,
    how="difference"
)

uncovered["uncovered_km2"] = uncovered.area / 1_000_000

# Retain ward names and uncovered areas
gaps = uncovered[["ward_name", "uncovered_km2"]]

# Merge uncovered areas back into all wards
result = wards.merge(
    gaps,
    on="ward_name",
    how="left"
)

result["uncovered_km2"] = result["uncovered_km2"].fillna(0)

# Calculate percentage of each ward not covered
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)

print(
    result[
        ["ward_name", "area_km2", "uncovered_km2", "uncovered_pct"]
    ].round(2)
)
