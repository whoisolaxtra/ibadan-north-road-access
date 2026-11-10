
import geopandas as gpd

# =====================================================
# CHALLENGE 2: POINT-IN-POLYGON COUNTING
# Project: Ibadan North
# =====================================================

# 1. Load settlement polygons and road network
settlements = gpd.read_file(
    "data/ibadan_north_analysis_v2.gpkg",
    layer="ibadan_north_analysis_v2"
)

roads = gpd.read_file(
    "data/ibadan_north_roads.gpkg",
    layer="ibadan_north_roads"
)

# 2. Reproject roads to match settlement CRS
roads = roads.to_crs(settlements.crs)

print("SETTLEMENT CRS:", settlements.crs)
print("ROAD CRS:", roads.crs)

# 3. Generate representative points from road features
road_points = gpd.GeoDataFrame(
    {"road_id": range(1, len(roads) + 1)},
    geometry=roads.geometry.representative_point(),
    crs=roads.crs
)

print("\nINPUT DATA SUMMARY")
print("Settlement polygons:", len(settlements))
print("Road features:", len(roads))
print("Generated road points:", len(road_points))

# 4. Count road points within settlement polygons
joined = gpd.sjoin(
    settlements[["block_id", "geometry"]],
    road_points[["road_id", "geometry"]],
    how="left",
    predicate="contains"
)

# 5. Calculate point counts, retaining zero-count polygons
point_counts = (
    joined.groupby("block_id")["road_id"]
    .count()
    .rename("road_point_count")
)

settlements["road_point_count"] = (
    settlements["block_id"]
    .map(point_counts)
    .fillna(0)
    .astype(int)
)

# 6. Calculate polygon count statistics
with_points = (
    settlements["road_point_count"] > 0
).sum()

without_points = (
    settlements["road_point_count"] == 0
).sum()

total_points_counted = settlements["road_point_count"].sum()

# 7. Validate point assignment
unmatched = gpd.sjoin(
    road_points,
    settlements[["block_id", "geometry"]],
    how="left",
    predicate="within"
)

unmatched_points = unmatched["index_right"].isna().sum()

# 8. Display sample results
print("\nPOINT-IN-POLYGON RESULTS")

print(
    settlements[
        ["block_id", "road_point_count"]
    ].head(10).to_string(index=False)
)

# 9. Display summary statistics
print("\nSUMMARY")
print("Settlement polygons:", len(settlements))
print("Generated road points:", len(road_points))
print("Polygons containing road points:", with_points)
print("Polygons with zero road points:", without_points)
print("Total points counted:", total_points_counted)

# 10. Display point assignment validation
print("\nPOINT ASSIGNMENT VALIDATION")
print("Generated points:", len(road_points))
print("Assigned points:", total_points_counted)
print("Unassigned points:", len(road_points) - total_points_counted)
print("Points outside settlement polygons:", unmatched_points)

# 11. Calculate assignment percentage
assignment_percentage = (
    total_points_counted / len(road_points) * 100
    if len(road_points) > 0 else 0
)

print(
    "Point assignment percentage:",
    round(assignment_percentage, 2),
    "%"
)

# 12. Export results
output_path = (
    "month-03/week-11/outputs/my_count_results.gpkg"
)

settlements.to_file(
    output_path,
    driver="GPKG"
)

print("\nResults exported successfully.")
print("Output:", output_path)
