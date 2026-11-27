# Week 13 - File Paths, Batch Processing and Error Handling

Week 13 focused on managing file paths, automating repetitive geospatial data processing tasks, and handling errors during batch operations using Python. The practical exercises applied `pathlib`, functions, loops, exception handling, logging and pandas to real project datasets.

## 1. Guided Practical Exercises

Two scripts were completed:

| Script | Description |
|---|---|
| `paths_demo.py` | Demonstrated file and folder management using `pathlib`, including checking directory existence, listing CSV files in a sorted order, inspecting file names and extensions, and creating output directories. |
| `batch_convert.py` | Automated the conversion of multiple LGA facility CSV files into point GeoPackages, including coordinate validation, CRS transformation, output management, error handling and processing summaries. |

### CSV-to-Point Conversion

The batch conversion script processed facility records from `data/raw/lga_facilities/`.

The source CSV files contained inconsistent coordinate column names. Five files used `latitude` and `longitude`, while the Egbeda dataset used `lat` and `lon`. The script was updated to standardise these column names before creating point geometries.

The processing workflow included:

- Reading CSV files using pandas.
- Standardising inconsistent column names.
- Validating coordinate fields.
- Converting coordinate values to numeric data types.
- Creating point geometries using GeoPandas.
- Assigning the source CRS, EPSG:4326.
- Reprojecting the point datasets to EPSG:32631.
- Exporting the results to GeoPackage.
- Skipping existing outputs unless overwrite is enabled.
- Recording processing outcomes in a CSV summary and log file.

### Guided Processing Results

Six LGA facility datasets were successfully converted:

| Dataset | Features |
|---|---:|
| Akinyele | 29 |
| Egbeda | 15 |
| Ibadan North | 28 |
| Ibadan North-East | 21 |
| Ibadan South-West | 17 |
| Ido | 10 |
| **Total** | **120** |

The Egbeda dataset initially failed because its coordinate fields used different column names. After correcting the field mapping, the dataset was successfully processed. The batch workflow also demonstrated that an individual file error did not prevent the remaining files from being processed.

## 2. Independent Challenge

An additional script, `my_batch.py`, was developed to batch-reproject existing GeoPackage datasets in the project workspace.

The script reads GeoPackages from `data/processed/` and saves reprojected copies in `data/processed/reprojected/`, preserving the original datasets.

The independent workflow implemented:

- Automatic discovery and sorted processing of GeoPackage files.
- CRS validation before reprojection.
- Reprojection from EPSG:4326 to EPSG:32631.
- Output management and skipping existing files.
- Validation of saved GeoPackage outputs.
- Exception handling to allow processing to continue after individual failures.
- Logging and CSV processing summaries.
- A deliberate missing-CRS test to verify the validation function.

### Independent Challenge Results

Five GeoPackages were successfully reprojected:

| Dataset | Features | Source CRS | Output CRS |
|---|---:|---|---|
| facilities.gpkg | 41 | EPSG:4326 | EPSG:32631 |
| my_facilities.gpkg | 41 | EPSG:4326 | EPSG:32631 |
| roads.gpkg | 25 | EPSG:4326 | EPSG:32631 |
| wards.gpkg | 12 | EPSG:4326 | EPSG:32631 |
| week10_outputs.gpkg | 12 | EPSG:4326 | EPSG:32631 |
| **Total** | **131** | | |

All five output GeoPackages were reopened and independently checked. Their feature counts were preserved, and each output was confirmed to have EPSG:32631.

The deliberate missing-CRS test also generated the expected warning:

`Deliberate failure test: Missing CRS: deliberate_test_dataset`

This confirmed that the validation function correctly identifies spatial datasets without an assigned CRS.

## 3. Key Learning Outcomes

- Used `pathlib` to manage file and directory paths.
- Applied sorted file discovery for predictable batch processing.
- Developed reusable functions for geospatial data processing.
- Used exception handling to prevent one failed file from terminating an entire batch.
- Applied logging to record processing events and errors.
- Used pandas to generate structured processing summaries.
- Applied GeoPandas for coordinate transformation and GeoPackage export.
- Implemented output validation and safeguards against unnecessary overwriting.

## 4. Tools and Technologies

- Python
- GeoPandas
- pandas
- pathlib
- logging
- Visual Studio Code
- uv
- GeoPackage

## 5. CRS and Methodological Considerations

The input point and GeoPackage datasets used EPSG:4326 (WGS 84), a geographic coordinate reference system.

EPSG:32631 (WGS 84 / UTM Zone 31N) was selected as the projected CRS for the Ibadan North project area. This provides coordinates in metres and is suitable for metric spatial operations within the study area.

The scripts preserve the original datasets by writing processed outputs to separate directories. The saved GeoPackages were reopened to verify their CRS and feature counts.

## 6. Week 13 Deliverables

### Guided Scripts

- [`paths_demo.py`](paths_demo.py) - file path and directory management.
- [`batch_convert.py`](batch_convert.py) - batch conversion of CSV facility records to point GeoPackages.
- [`batch_summary.csv`](batch_summary.csv) - guided batch processing summary.
- [`batch_run.log`](batch_run.log) - guided batch processing log.

### Independent Challenge

- [`my_batch.py`](my_batch.py) - independent GeoPackage batch reprojection workflow.
- [`my_batch_summary.csv`](my_batch_summary.csv) - independent processing summary.
- [`my_batch_run.log`](my_batch_run.log) - independent processing log.

The generated spatial outputs are stored under:

- `data/processed/lga_points/`
- `data/processed/reprojected/`

**Week 13 status:** Both guided scripts and the independent batch-reprojection challenge were executed successfully. The five independent GeoPackage outputs were independently verified, and the deliberate missing-CRS test was recorded in the processing log.