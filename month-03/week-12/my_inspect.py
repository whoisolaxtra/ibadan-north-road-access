import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    print("RASTER INSPECTION")
    print("Width:", src.width)
    print("Height:", src.height)
    print("Bands:", src.count)
    print("CRS:", src.crs)
    print("Resolution:", src.res)
    print("Bounds:", src.bounds)
    print("Data type:", src.dtypes)
    print("NoData:", src.nodata)

    elevation = src.read(1, masked=True)

    print("\nELEVATION STATISTICS")
    print("Valid cells:", elevation.count())
    print("Minimum:", round(float(elevation.min()), 2))
    print("Maximum:", round(float(elevation.max()), 2))
    print("Mean:", round(float(elevation.mean()), 2))
    print("NoData cells:", int(elevation.mask.sum()))

    print("\nDIMENSION CHECK")
    print("Width in metres:", src.width * src.res[0])
    print("Height in metres:", src.height * abs(src.res[1]))
    print("Raster bounds width:", src.bounds.right - src.bounds.left)
    print("Raster bounds height:", src.bounds.top - src.bounds.bottom)