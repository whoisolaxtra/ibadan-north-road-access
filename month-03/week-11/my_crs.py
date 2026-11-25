
import geopandas as gpd

# =====================================================
# CHALLENGE 1: CRS IDENTIFICATION AND SPATIAL MEASUREMENT
# Project: Ibadan North
# =====================================================

# 1. Load Month 1/2 project datasets
settlements = gpd.read_file(
    "data/ibadan_north_analysis_v2.gpkg",
    layer="ibadan_north_analysis_v2"
)

roads = gpd.read_file(
    "data/ibadan_north_roads.gpkg",
    layer="ibadan_north_roads"
)

# 2. Inspect original coordinate reference systems
print("ORIGINAL COORDINATE REFERENCE SYSTEMS")
print("Settlement CRS:", settlements.crs)
print("Road CRS:", roads.crs)

print("\nINPUT DATA SUMMARY")
print("Settlement features:", len(settlements))
print("Road features:", len(roads))
print("Unique block IDs:", settlements["block_id"].nunique())

# 3. Estimate a suitable projected CRS
projected_crs = settlements.estimate_utm_crs()

print("\nESTIMATED PROJECTED CRS:", projected_crs)

# 4. Reproject both datasets
settlements_utm = settlements.to_crs(projected_crs)
roads_utm = roads.to_crs(projected_crs)

print("\nREPROJECTED CRS")
print("Settlements:", settlements_utm.crs)
print("Roads:", roads_utm.crs)

# 5. Calculate settlement area in square kilometres
settlements_utm["area_km2"] = (
    settlements_utm.geometry.area / 1_000_000
)

# 6. Calculate representative points for settlements
settlement_points = (
    settlements_utm.geometry.representative_point()
)

# Combine road geometries into one network
road_network = roads_utm.geometry.union_all()

# Calculate distance from each representative point
# to the nearest part of the road network
settlements_utm["nearest_road_m"] = (
    settlement_points.distance(road_network)
)

# 7. Validate the calculated results
print("\nRESULT VALIDATION")
print("Output features:", len(settlements_utm))
print("Unique block IDs:", settlements_utm["block_id"].nunique())
print(
    "Duplicate block IDs:",
    settlements_utm["block_id"].duplicated().sum()
)

print(
    "Missing road distances:",
    settlements_utm["nearest_road_m"].isna().sum()
)

print(
    "Zero road distances:",
    (settlements_utm["nearest_road_m"] == 0).sum()
)

# 8. Display sample results
print("\nSETTLEMENT AREA AND NEAREST ROAD DISTANCE")

print(
    settlements_utm[
        ["block_id", "area_km2", "nearest_road_m"]
    ].head(10).to_string(index=False)
)

# 9. Calculate summary statistics
print("\nSUMMARY STATISTICS")

print(
    "Total settlement area:",
    round(settlements_utm["area_km2"].sum(), 3),
    "km2"
)

print(
    "Mean nearest road distance:",
    round(settlements_utm["nearest_road_m"].mean(), 2),
    "metres"
)

print(
    "Maximum nearest road distance:",
    round(settlements_utm["nearest_road_m"].max(), 2),
    "metres"
)

print(
    "Minimum nearest road distance:",
    round(settlements_utm["nearest_road_m"].min(), 4),
    "metres"
)

# 10. Export results
output_path = (
    "month-03/week-11/outputs/my_crs_results.gpkg"
)

settlements_utm.to_file(
    output_path,
    driver="GPKG"
)

print("\nResults exported successfully:")
print(output_path)
