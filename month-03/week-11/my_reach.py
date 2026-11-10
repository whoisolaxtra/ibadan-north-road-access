
import geopandas as gpd

# =====================================================
# CHALLENGE 3: ROAD COVERAGE AND ACCESSIBILITY GAPS
# Project: Ibadan North
# =====================================================

# 1. Load project datasets
settlements = gpd.read_file(
    "data/ibadan_north_analysis_v2.gpkg",
    layer="ibadan_north_analysis_v2"
)

roads = gpd.read_file(
    "data/ibadan_north_roads.gpkg",
    layer="ibadan_north_roads"
)

# 2. Reproject to UTM Zone 31N for metric analysis
projected_crs = settlements.estimate_utm_crs()

settlements = settlements.to_crs(projected_crs)
roads = roads.to_crs(projected_crs)

print("PROJECTED CRS:", projected_crs)

# 3. Generate representative points for settlement blocks
settlement_points = settlements.geometry.representative_point()

# 4. Create a 100-metre road coverage buffer
road_network = roads.geometry.union_all()

road_coverage = road_network.buffer(100)

# 5. Determine which settlement points fall within road coverage
within_coverage = settlement_points.within(road_coverage)

# 6. Calculate nearest road distance
nearest_road_distance = settlement_points.distance(road_network)

# 7. Add accessibility results to settlement polygons
settlements["nearest_road_m"] = nearest_road_distance

settlements["road_coverage"] = within_coverage.map({
    True: "Within 100m",
    False: "Outside 100m"
})

# 8. Display sample results
print("\nROAD COVERAGE RESULTS")

print(
    settlements[
        ["block_id", "nearest_road_m", "road_coverage"]
    ].head(10).to_string(index=False)
)

# 9. Summarise coverage and gaps
within_count = (settlements["road_coverage"] == "Within 100m").sum()
outside_count = (settlements["road_coverage"] == "Outside 100m").sum()

total = len(settlements)

print("\nCOVERAGE SUMMARY")
print("Total settlement blocks:", total)
print("Within 100m of roads:", within_count)
print("Outside 100m of roads:", outside_count)

print(
    "Coverage percentage:",
    round((within_count / total) * 100, 2), "%"
)

print(
    "Coverage gap percentage:",
    round((outside_count / total) * 100, 2), "%"
)

print(
    "Mean nearest road distance:",
    round(settlements["nearest_road_m"].mean(), 2),
    "metres"
)

# 10. Export results
settlements.to_file(
    "month-03/week-11/outputs/my_reach_results.gpkg",
    driver="GPKG"
)

print("\nResults exported successfully.")
