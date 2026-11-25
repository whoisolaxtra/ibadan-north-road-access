
import geopandas as gpd
import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    facilities = gpd.read_file(
        "data/processed/facilities.gpkg",
        layer="facilities"
    ).to_crs(src.crs)

    coords = [(p.x, p.y) for p in facilities.geometry]

    values = src.sample(coords)

    facilities["elevation_m"] = [
        value[0] for value in values
    ]

print(facilities[["name", "elevation_m"]].head())
