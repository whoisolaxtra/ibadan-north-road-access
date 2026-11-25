# Week 12: Rasters with Rasterio

## Overview

This week focused on raster data inspection, raster metadata, NumPy arrays, NoData handling, coordinate transformations, Landsat reflectance scaling, NDVI calculation, raster clipping, zonal statistics and reprojection.

The practical work used the Ibadan North study area in Oyo State, Nigeria, with a 30 m SRTM DEM and Landsat 9 Collection 2 Level-2 surface reflectance imagery.

## 1. Datasets

| Dataset | Description | CRS |
|---|---|---|
| `dem.tif` | SRTM elevation model, 30 m resolution | EPSG:32631 |
| `LC09_L2SP_191055_20260115_20260117_02_T1_SR_B4.TIF` | Landsat 9 Red band | EPSG:32631 |
| `LC09_L2SP_191055_20260115_20260117_02_T1_SR_B5.TIF` | Landsat 9 Near Infrared band | EPSG:32631 |
| `ibadan_north_analysis_v2.gpkg` | Settlement polygons for zonal NDVI analysis | EPSG:32631 |

**Landsat scene information**

- Sensor: Landsat 9
- Product: Collection 2 Level-2 Surface Reflectance
- Scene ID: `LC09_L2SP_191055_20260115_20260117_02_T1`
- Acquisition date: 15 January 2026
- Processing date: 17 January 2026
- Bands used: SR_B4 (Red) and SR_B5 (Near Infrared)
- Cloud cover: Not recorded in this analysis. Refer to the scene metadata for the reported percentage.

The DEM and Landsat bands are retained locally and are not committed to GitHub.

## 2. Guided exercises

Nine guided scripts were completed.

| Script | Practical task |
|---|---|
| `inspect_raster.py` | Inspect raster dimensions, bands, CRS, resolution, bounds, data type, NoData and transform |
| `read_values.py` | Read raster values and handle NoData using masked arrays |
| `pixel_coords.py` | Convert between raster pixel positions and map coordinates |
| `sample_points.py` | Extract elevation values at facility locations |
| `ndvi.py` | Calculate NDVI from Landsat Red and NIR bands |
| `plot_raster.py` | Plot the NDVI raster with a colour bar |
| `clip_raster.py` | Clip the DEM to the study boundary |
| `zonal_stats.py` | Calculate mean elevation per ward |
| `reproject_raster.py` | Reproject the DEM from EPSG:32631 to EPSG:4326 |

### Selected guided results

**DEM inspection**

- Dimensions: 241 columns x 315 rows
- Resolution: 30 x 30 m
- CRS: EPSG:32631
- Data type: float32
- NoData: -9999
- Valid elevation range: 138.9 to 302.3 m
- Mean elevation: 228.2 m
- NoData cells: 1,446

**NDVI calculation**

- Minimum NDVI: 0.000
- Maximum NDVI: 0.905
- Mean NDVI: 0.533
- Output: `data/processed/ndvi.tif`

**DEM clipping**

- Original dimensions: 241 x 315 pixels
- Clipped dimensions: 222 x 296 pixels
- Output: `data/processed/dem_ibadan_north.tif`

**Zonal elevation statistics**

Mean elevation was calculated for 12 wards. Sabo recorded the highest mean elevation (273.9 m), while Samonda recorded the lowest (164.5 m).

**Raster reprojection**

The DEM was reprojected from EPSG:32631 to EPSG:4326. The resulting pixel size was approximately 0.00027152 degrees.

## 3. Independent challenges

The independent challenges used the project's own Ibadan North datasets.

### Challenge 1: `my_inspect.py`

Inspected the project's DEM and checked the relationship between raster dimensions, resolution and spatial bounds.

Results:
- Dimensions: 241 x 315 pixels
- Valid cells: 74,469
- NoData cells: 1,446
- Minimum elevation: 138.92 m
- Maximum elevation: 302.31 m
- Mean elevation: 228.22 m
- Raster width: 7,230 m
- Raster height: 9,450 m

The calculated dimensions agreed with the raster bounds.

### Challenge 2: `my_index.py`

Calculated NDVI using the Landsat 9 Red and Near Infrared bands.

Reflectance scaling:

`Reflectance = Stored value * 0.0000275 - 0.2`

NDVI:

`NDVI = (NIR - Red) / (NIR + Red)`

Results:
- Valid pixels: 74,951
- Minimum NDVI: 0.000
- Maximum NDVI: 0.905
- Mean NDVI: 0.533
- Output: `data/processed/my_ndvi.tif`

### Challenge 3: `my_zonal.py`

Calculated mean NDVI for the 2,029 settlement polygons in `ibadan_north_analysis_v2.gpkg`.

Results:
- Total polygons: 2,029
- Polygons with valid NDVI: 1,961
- Polygons without valid NDVI: 68
- Overall mean of polygon means: 0.584
- Output: `my_zonal_stats.csv`

The overall mean of polygon means (0.584) differs from the raster-wide mean (0.533) because each polygon contributes equally to the former, whereas each valid raster pixel contributes equally to the latter.

### NDVI map

`my_map.py` generated `my_map.png`, showing the NDVI raster with a colour bar.

## 4. Technical considerations and limitations

- EPSG:32631 (WGS 84 / UTM Zone 31N) was retained for metric spatial analysis in Ibadan North.
- Raster and vector datasets were aligned to a common CRS before spatial operations.
- NoData values were excluded from raster statistics using masked arrays.
- Bilinear resampling was used for the continuous elevation raster during reprojection.
- The NDVI validity mask excluded zero-valued input pixels and zero denominators.
- The NDVI processing did not apply the Landsat QA_PIXEL cloud and cloud-shadow mask. Cloud contamination may therefore affect some pixel values.
- The 68 settlement polygons without valid NDVI were retained as missing values rather than assigned zero.
- The map was generated with a fixed display range of -1 to +1. Its spatial pattern should be interpreted alongside the source imagery and boundary data.

## 5. Software and libraries

- Python
- Rasterio
- GeoPandas
- NumPy
- Pandas
- Matplotlib

## 6. Reproducing the work

Run scripts from the repository root with the activated project environment:

```powershell
uv run python month-03/week-12/inspect_raster.py
uv run python month-03/week-12/read_values.py
uv run python month-03/week-12/pixel_coords.py
uv run python month-03/week-12/sample_points.py
uv run python month-03/week-12/ndvi.py
uv run python month-03/week-12/plot_raster.py
uv run python month-03/week-12/clip_raster.py
uv run python month-03/week-12/zonal_stats.py
uv run python month-03/week-12/reproject_raster.py
```

Independent challenges:

```powershell
uv run python month-03/week-12/my_inspect.py
uv run python month-03/week-12/my_index.py
uv run python month-03/week-12/my_zonal.py
uv run python month-03/week-12/my_map.py
```

## 7. Outputs and repository hygiene

The Week 12 folder contains the guided and independent Python scripts, the zonal statistics CSV, the NDVI map and this README.

Generated raster files, including `.tif` outputs, remain local and are not committed to GitHub. The original DEM and Landsat bands also remain outside the committed deliverables.

