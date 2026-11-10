
import geopandas as gpd

# Load the ward layer
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

# Get the first coordinate of the first ward
first = wards.geometry.iloc[0].exterior.coords[0]

print("Original first corner:", first)

# Method 1: to_crs() transforms coordinate values
projected = wards.to_crs(epsg=32631)

projected_first = projected.geometry.iloc[0].exterior.coords[0]

print("After to_crs:", projected_first)

# Method 2: set_crs() changes only the CRS label
wrongly_labelled = wards.set_crs(
    epsg=32631,
    allow_override=True
)

wrong_first = wrongly_labelled.geometry.iloc[0].exterior.coords[0]

print("After set_crs:", wrong_first)
print("Label now says:", wrongly_labelled.crs)
