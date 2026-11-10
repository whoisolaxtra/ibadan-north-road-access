
import geopandas as gpd

# =====================================================
# CHALLENGE 4: GEOMETRY VALIDATION AND REPAIR
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

# 2. Inspect original geometry validity
settlement_invalid = ~settlements.geometry.is_valid
road_invalid = ~roads.geometry.is_valid

print("INITIAL GEOMETRY VALIDATION")
print("Settlement features:", len(settlements))
print("Invalid settlement geometries:", settlement_invalid.sum())

print("Road features:", len(roads))
print("Invalid road geometries:", road_invalid.sum())

# 3. Repair invalid settlement geometries
settlements.loc[settlement_invalid, "geometry"] = (
    settlements.loc[settlement_invalid, "geometry"].make_valid()
)

# 4. Repair invalid road geometries
roads.loc[road_invalid, "geometry"] = (
    roads.loc[road_invalid, "geometry"].make_valid()
)

# 5. Verify geometry validity after repair
settlement_invalid_after = ~settlements.geometry.is_valid
road_invalid_after = ~roads.geometry.is_valid

print("\nVALIDATION AFTER REPAIR")
print("Invalid settlement geometries:", settlement_invalid_after.sum())
print("Invalid road geometries:", road_invalid_after.sum())

# 6. Check geometry types
print("\nSETTLEMENT GEOMETRY TYPES")
print(settlements.geom_type.value_counts())

print("\nROAD GEOMETRY TYPES")
print(roads.geom_type.value_counts())

# 7. Export corrected datasets
settlements.to_file(
    "month-03/week-11/outputs/my_valid_settlements.gpkg",
    driver="GPKG"
)

roads.to_file(
    "month-03/week-11/outputs/my_valid_roads.gpkg",
    driver="GPKG"
)

print("\nCorrected datasets exported successfully.")
