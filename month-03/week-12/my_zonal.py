
import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask

polygons = gpd.read_file(
    "data/ibadan_north_analysis_v2.gpkg",
    layer="ibadan_north_analysis_v2"
)

results = []

with rasterio.open("data/processed/my_ndvi.tif") as src:

    polygons = polygons.to_crs(src.crs)

    print("Raster CRS:", src.crs)
    print("Polygon CRS:", polygons.crs)
    print("Number of polygons:", len(polygons))

    for _, feature in polygons.iterrows():
        block_id = feature["block_id"]
        geometry = feature.geometry

        try:
            cells, _ = mask(
                src,
                [geometry],
                crop=True,
                filled=False
            )

            ndvi_values = cells[0].compressed()

            if len(ndvi_values) > 0:
                mean_ndvi = float(ndvi_values.mean())
                valid_pixels = len(ndvi_values)
            else:
                mean_ndvi = np.nan
                valid_pixels = 0

        except ValueError:
            mean_ndvi = np.nan
            valid_pixels = 0

        results.append({
            "block_id": block_id,
            "mean_ndvi": mean_ndvi,
            "valid_pixels": valid_pixels
        })

stats = pd.DataFrame(results)

output = "month-03/week-12/my_zonal_stats.csv"
stats.to_csv(output, index=False)

print("\nZONAL STATISTICS SUMMARY")
print("Total polygons:", len(stats))
print("Polygons with valid NDVI:", stats["mean_ndvi"].notna().sum())
print("Polygons without valid NDVI:", stats["mean_ndvi"].isna().sum())
print("Overall mean of polygon means:", round(stats["mean_ndvi"].mean(), 3))
print("\nSample results:")
print(stats.head())

print("\nSaved:", output)
