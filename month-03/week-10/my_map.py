
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Load ward polygons
wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

# Load population data
pop = pd.read_csv("data/raw/ward_population.csv")


# Clean ward names for joining
def clean_name(name):
    return str(name).strip().upper().replace("-", " ")


wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

# Join population to ward polygons
joined = wards.merge(
    pop,
    on="join_key",
    how="left"
)

# Check population matches
matched = joined["population_2024"].notna().sum()
print("Population matches:", matched, "of", len(wards))

# Load health facility points
facilities = gpd.read_file(
    "data/processed/my_facilities.gpkg",
    layer="facilities"
)

# Ensure both layers use the same CRS
facilities = facilities.to_crs(joined.crs)

# Create the map
fig, ax = plt.subplots(figsize=(10, 10))

joined.plot(
    column="population_2024",
    cmap="Greens",
    linewidth=0.8,
    edgecolor="black",
    legend=True,
    legend_kwds={"label": "2024 Ward Population"},
    ax=ax
)

facilities.plot(
    ax=ax,
    color="red",
    markersize=18,
    marker="o"
)

# Add map title and legend
facility_symbol = Line2D(
    [0], [0],
    marker="o",
    color="w",
    markerfacecolor="red",
    markersize=7,
    label="Health facilities"
)

ax.legend(
    handles=[facility_symbol],
    loc="upper left"
)

ax.set_title(
    "Ward Population and Health Facilities in Ibadan North",
    fontsize=13
)

ax.set_axis_off()

# Save the map
plt.savefig(
    "month-03/week-10/my_map.png",
    dpi=200,
    bbox_inches="tight"
)

print("Map saved: month-03/week-10/my_map.png")

plt.show()
