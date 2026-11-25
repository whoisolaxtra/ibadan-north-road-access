
import matplotlib.pyplot as plt
import rasterio

with rasterio.open("data/processed/my_ndvi.tif") as src:
    ndvi = src.read(1, masked=True)

fig, ax = plt.subplots(figsize=(8, 8))

image = ax.imshow(
    ndvi,
    cmap="RdYlGn",
    vmin=-1,
    vmax=1
)

fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("NDVI - Ibadan North, January 2026")
ax.set_axis_off()

fig.savefig(
    "month-03/week-12/my_map.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved month-03/week-12/my_map.png")
