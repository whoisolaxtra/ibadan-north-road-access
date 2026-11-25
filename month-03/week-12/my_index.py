
import numpy as np
import rasterio

folder = "data/raw/landsat/"
scene = "LC09_L2SP_191055_20260115_20260117_02_T1"

red_path = folder + scene + "_SR_B4.TIF"
nir_path = folder + scene + "_SR_B5.TIF"

with rasterio.open(red_path) as red_src:
    red_raw = red_src.read(1).astype("float32")
    profile = red_src.profile
    red_transform = red_src.transform
    red_crs = red_src.crs

with rasterio.open(nir_path) as nir_src:
    nir_raw = nir_src.read(1).astype("float32")

    if (
        nir_src.shape != red_raw.shape
        or nir_src.transform != red_transform
        or nir_src.crs != red_crs
    ):
        raise ValueError("Landsat bands are not spatially aligned.")

valid = (red_raw > 0) & (nir_raw > 0)

red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

total = nir + red
ok = valid & (total != 0)

ndvi = np.full(red.shape, -9999, dtype="float32")
ndvi[ok] = (nir[ok] - red[ok]) / total[ok]

print("NDVI ANALYSIS")
print("Valid pixels:", int(ok.sum()))
print("Minimum NDVI:", round(float(ndvi[ok].min()), 3))
print("Maximum NDVI:", round(float(ndvi[ok].max()), 3))
print("Mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(
    dtype="float32",
    nodata=-9999,
    count=1
)

output = "data/processed/my_ndvi.tif"

with rasterio.open(output, "w", **profile) as dst:
    dst.write(ndvi, 1)

print("Saved:", output)
