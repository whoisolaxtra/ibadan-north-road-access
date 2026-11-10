import geopandas as gpd

# 1. Load your Month 1/2 project datasets
settlements = gpd.read_file(
    "data/ibadan_north_analysis_v2.gpkg",
    layer="ibadan_north_analysis_v2"
)

roads = gpd.read_file(
    "data/ibadan_north_roads.gpkg",
    layer="ibadan_north_roads"
)

# 2. Inspect the original coordinate reference systems
print("SETTLEMENT CRS:", settlements.crs)
print("ROAD CRS:", roads.crs)

# 3. Identify a suitable projected CRS
projected_crs = settlements.estimate_utm_crs()
print("\nEstimated UTM CRS:", projected_crs)

# 4. Reproject both datasets for metric analysis
settlements_utm = settlements.to_crs(projected_crs)
roads_utm = roads.to_crs(projected_crs)

# 5. Calculate settlement area in square kilometres
settlements_utm["area_km2"] = (
    settlements_utm.geometry.area / 1_000_000
)

# 6. Calculate representative points for settlements
settlement_points = settlements_utm.geometry.representative_point()

# Combine roads into one geometry
road_network = roads_utm.geometry.union_all()

# Calculate distance from each settlement point to the road network
settlements_utm["nearest_road_m"] = (
    settlement_points.distance(road_network)
)

# 7. Display results
print("\nSETTLEMENT AREA AND ROAD DISTANCE")

print(
    settlements_utm[
        ["block_id", "area_km2", "nearest_road_m"]
    ].head(10)
)

print("\nTotal settlement area:",
      round(settlements_utm["area_km2"].sum(), 3), "km²")

print("Mean nearest road distance:",
      round(settlements_utm["nearest_road_m"].mean(), 2), "m")

# 8. Export results
settlements_utm.to_file(
    "month-03/week-11/outputs/my_crs_results.gpkg",
    driver="GPKG"
)

print("\nResults exported successfully.")