
import pandas as pd
import geopandas as gpd

# Load the ward polygons and population table
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

pop = pd.read_csv("data/raw/ward_population.csv")

# First join: use the original ward names
first_try = wards.merge(
    pop,
    left_on="ward_name",
    right_on="ward",
    how="left"
)

matched_first = first_try["population_2024"].notna().sum()

print("Matched before cleaning:", matched_first, "of", len(wards))


# Clean ward names consistently
def clean_name(name):
    return str(name).strip().upper().replace("-", " ")


wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

# Second join: use the cleaned names
joined = wards.merge(
    pop,
    on="join_key",
    how="left"
)

matched_after = joined["population_2024"].notna().sum()

print("Matched after cleaning:", matched_after, "of", len(wards))

# Display the joined results
print(
    joined[["ward_name", "population_2024"]]
)
