# Week 12 Raster Data Notes

## 1. Digital Elevation Model (DEM)

- File: `data/raw/dem.tif`
- Dataset: SRTM DEM
- CRS: EPSG:32631
- Pixel size: 30 m
- Dimensions: 241 columns x 315 rows
- NoData value: -9999
- Valid elevation range: 138.92 m to 302.31 m
- Mean elevation: 228.22 m

## 2. Landsat Imagery

- Data location: `data/raw/landsat/`
- Satellite: Landsat 9
- Product: Landsat Collection 2 Level-2 Surface Reflectance
- Scene ID: `LC09_L2SP_191055_20260115_20260117_02_T1`
- Acquisition date: 15 January 2026
- Processing date: 17 January 2026
- Bands used:
  - Band 4 (Red): `_SR_B4.TIF`
  - Band 5 (Near Infrared): `_SR_B5.TIF`
- Scale factor: 0.0000275
- Offset: -0.2
- Cloud cover: Not recorded in the available local metadata.
- Source: Existing raw data supplied in the project repository.

## 3. Processing Summary

The Landsat 9 surface reflectance bands were converted to float32 and scaled using the USGS scale factor and offset. NDVI was calculated using:

NDVI = (NIR - Red) / (NIR + Red)

The resulting NDVI raster was saved as `data/processed/my_ndvi.tif`.

The calculated NDVI values ranged from 0.0 to 0.905, with a mean of 0.533.

Zonal statistics were calculated for 2,029 settlement polygons in Ibadan North. Valid NDVI statistics were obtained for 1,961 polygons, while 68 polygons had no valid NDVI pixels.

The zonal statistics were exported to `month-03/week-12/my_zonal_stats.csv`.