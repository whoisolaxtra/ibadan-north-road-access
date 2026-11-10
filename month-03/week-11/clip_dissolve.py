
import geopandas as gpd

# Load wards and roads in UTM Zone 31N
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

roads = gpd.read_file(
    "data/processed/roads.gpkg",
    layer="roads"
).to_crs(epsg=32631)

# Select Agodi ward
agodi = wards[wards["ward_name"] == "Agodi"]

# Clip roads to the Agodi boundary
agodi_roads = gpd.clip(roads, agodi)

print("Roads in Agodi:", len(agodi_roads))

# Calculate total clipped road length in kilometres
print(
    "Road length in Agodi:",
    round(agodi_roads.length.sum() / 1000, 2),
    "km"
)

# Dissolve all wards into one LGA polygon
lga = wards.dissolve(by="lga_name")

print(lga.reset_index()[["lga_name"]])

# Calculate LGA area in square kilometres
print(
    "LGA area:",
    round(lga.area.iloc[0] / 1_000_000, 1),
    "km2"
)
