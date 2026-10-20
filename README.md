# Road Accessibility to Settlement Areas in Ibadan North LGA

## Project Overview

This project examines the spatial accessibility of settlement areas to mapped roads in Ibadan North Local Government Area, Oyo State, Nigeria.

The project began with GIS-based road proximity analysis and continues into Python development, reproducible project environments, and spatial data analysis workflows.

## Research Question

Which settlement areas in Ibadan North Local Government Area, Oyo State, are farthest from the nearest mapped road?

## Study Area

Ibadan North Local Government Area, Oyo State, Nigeria.

## Data Sources

- **Ibadan North LGA Boundary:** GRID3 Nigeria Operational LGA Boundaries  
  https://grid3.org/geospatial-data-nigeria

- **Settlement Extents:** GRID3 Nigeria Settlement Extents v4.1  
  https://grid3.org/geospatial-data-nigeria

- **Road Network:** OpenStreetMap data downloaded through Geofabrik  
  https://download.geofabrik.de/africa/nigeria.html

## Analysis

The project examines settlement proximity to the mapped road network using continuous nearest-road distance and a 100 m road-proximity threshold.

The spatial analysis uses:

**EPSG:32631 - WGS 84 / UTM Zone 31N**

Distances are calculated in metres.

### Week 3 - Nearest-Road Distance Analysis

The analysis-ready dataset contains **2,029 settlement features** with a nearest-road distance field.

Observed nearest-mapped-feature distances range from **0 m to approximately 185.05 m**.

- **1,978 settlement blocks** have a distance of 0 m.
- **51 settlement blocks** have a non-zero distance.
- The maximum observed distance is approximately **185.05 m**.

The Week 3 analysis provides a continuous measure of settlement proximity to the mapped road/path network.

**Documentation:** [`docs/03-data-preparation.md`](docs/03-data-preparation.md)

## Week 4 - Spatial Analysis

Week 4 focused on a **100 m road-proximity analysis** to examine the relationship between mapped roads and settlement areas.

### Spatial Operation

A 100 m buffer was created around the mapped OpenStreetMap road network using **EPSG:32631 — WGS 84 / UTM Zone 31N**.

The road dataset was filtered to exclude:

- `path`
- `footway`
- `track`

This left **3,026 mapped road features** for the Week 4 buffer analysis.

The 100 m buffer was dissolved to create a continuous road-proximity zone and then intersected with the settlement areas.

### Week 4 Results

The original settlement dataset contained **2,029 settlement areas**.

| Measure | Result |
|---|---:|
| Total settlement areas | 2,029 |
| Settlement areas within/intersecting 100 m | 2,026 |
| Settlement areas outside 100 m | 3 |
| Within 100 m | 99.85% |
| Outside 100 m | 0.15% |

The three settlement areas outside the 100 m road-proximity zone were independently identified using a spatial `disjoint` selection and exported as a separate layer.

### Validation

The 100 m buffer was checked for geometry validity before further analysis.

- **Valid geometries:** 3,026
- **Invalid geometries:** 0
- **Errors:** 0

The settlement result was also independently checked by selecting settlement areas that were disjoint from the dissolved 100 m buffer. This identified the same **3 settlement areas** outside the threshold.

### Interpretation

The analysis identified **2,026 of the 2,029 mapped settlement areas** as intersecting the 100 m road-proximity zone.

Only **3 settlement areas (0.15%)** were identified outside the 100 m threshold.

This result represents proximity to the **mapped OpenStreetMap road dataset** and should not be interpreted as a complete measure of physical road accessibility. The result depends on the completeness, positional accuracy and classification of the mapped road data.

**Documentation:** [`docs/04-spatial-analysis.md`](docs/04-spatial-analysis.md)

## Analysis-Ready Output

The Week 3 analysis-ready GeoPackage is:

`data/ibadan_north_analysis_v2.gpkg`

It contains the settlement features and the calculated nearest-road distance field.

## Week 4 Outputs

The Week 4 spatial analysis outputs are:

- `data/ibadan_north_road_buffer_100m.gpkg`
- `data/ibadan_north_road_buffer_100m_dissolved.gpkg`
- `data/ibadan_north_settlements_within_100m.gpkg`
- `data/ibadan_north_settlements_outside_100m.gpkg`

## Map Output

The final Week 4 map visualising the 100 m road-proximity analysis is available at:

[`maps/week4-road-accessibility-100m.png`](maps/week4-road-accessibility-100m.png)

The map shows the mapped road network, 100 m road-proximity zone, settlement areas and the three settlement areas identified outside the 100 m threshold.

## Month 1 Integration Summary

The complete four-week project story, results, and outputs are summarised in:

[`month-1-summary.md`](month-1-summary.md)

The summary connects the project from:

**Project question → Data acquisition → Data preparation → Spatial analysis → Result**

## Project Status

**Month 1 - Four-week project completed.**

The project progressed from project definition and data acquisition through data preparation, nearest-road distance analysis, threshold-based spatial analysis, validation, and visualisation.

The Week 4 workflow included road filtering, 100 m buffering, geometry validation, buffer dissolution, settlement intersection, and independent validation of settlement areas outside the 100 m threshold.

## Documentation

Detailed Month 1 project documentation is organised by week:

- **Week 1 - Project Brief:** [`docs/01-project-brief.md`](docs/01-project-brief.md)
- **Week 2 - Data Notes:** [`docs/02-data-notes.md`](docs/02-data-notes.md)
- **Week 3 - Data Preparation:** [`docs/03-data-preparation.md`](docs/03-data-preparation.md)
- **Week 4 - Spatial Analysis:** [`docs/04-spatial-analysis.md`](docs/04-spatial-analysis.md)
- **Month 1 - Integration Summary:** [`month-1-summary.md`](month-1-summary.md)

---

# Month 2 - Development Environment and Early Python

## Week 5 - Python Development Environment

Week 5 marked the beginning of the development phase of the project.

A Python development environment was configured using:

- Python 3.14.8
- Visual Studio Code
- `uv`, the Python package and project manager
- The Python extension for Visual Studio Code

The project repository was opened as a trusted workspace in Visual Studio Code.

### Environment Verification

The development environment was verified from the project directory.

```powershell
python --version
Python 3.14.8

python hello.py
My setup works
```

The `hello.py` script confirmed that Python was installed and executable from the project workspace.

**Week 5 status:** Development environment installed and verified.

**Screenshot:** [`screenshots/week5.png`](screenshots/week5.png)

## Week 6 - Environments and Project Setup with uv

Week 6 focused on creating a reproducible Python project environment, installing a package, and recording the dependencies needed to rebuild the environment.

### Project Environment

The project was initialised using:

```powershell
uv init
```

The environment and project dependencies were synchronised using:

```powershell
uv sync
```

Pandas was installed into the project environment using:

```powershell
uv add pandas
```

This updated the project's dependency configuration and lock file.

### Project Files

The Week 6 project files are:

- **`pyproject.toml`** - describes the project and its declared dependencies.
- **`uv.lock`** - records the exact resolved versions of the project's dependencies.
- **`check.py`** - imports pandas and prints its installed version.
- **`.venv`** - the local virtual environment used by the project; it is not uploaded to GitHub.

### Verification Script

The `check.py` script contains:

```python
import pandas

print("pandas version:", pandas.__version__)
```

It was executed using:

```powershell
uv run check.py
```

The script completed successfully and printed:

```text
pandas version: 3.0.6
```

The `uv` installation was also verified:

```powershell
uv --version
uv 0.12.23
```

The environment uses Python **3.14.8**.

### Reproducibility

The combination of `pyproject.toml` and `uv.lock` records the project's declared dependencies and their resolved versions. The virtual environment can be rebuilt from the project configuration and lock file rather than uploading the local `.venv` directory.

### Week 6 Deliverables

The following files were added to the same public GitHub repository used for Month 1:

- [`pyproject.toml`](pyproject.toml)
- [`uv.lock`](uv.lock)
- [`check.py`](check.py)
- [`screenshots/week6.png`](screenshots/week6.png)

The screenshot records the VS Code editor and terminal showing the verification commands and the pandas version output.

**Week 6 status:** Pandas installed, verification script executed successfully, and project files uploaded to GitHub.

## Week 7 - Python Data Analysis

Week 7 applies Python fundamentals to a small dataset of settlement wards and their areas. The practical uses variables, data types, loops, conditional statements, list indexing, type conversion, and basic error handling.

### Dataset

The input file, `wards.csv`, contains four wards and their areas in square kilometres.

| Ward | Area (km²) |
|---|---:|
| Agodi | 12.4 |
| Bodija | 8.1 |
| Sabo | 5.7 |
| Mokola | 9.3 |

### Analysis Workflow

The `analyse.py` script:

1. Opens and reads `wards.csv`.
2. Uses `lines[1:]` to skip the CSV header row.
3. Splits each data row into its ward name and area.
4. Converts the area value from text to a floating-point number using `float()`.
5. Classifies each ward as `large` when its area is greater than 9 km², or `small` otherwise.
6. Prints the classification for each ward.

### Results

The script produces the following output:

```text
Agodi is large
Bodija is small
Sabo is small
Mokola is large
```

The classification uses a threshold of **greater than 9 km²**. An area equal to 9 km² would therefore be classified as small.

### Week 7 Deliverables

The practical files and evidence are:

- [`analyse.py`](analyse.py) - Python analysis script.
- [`wards.csv`](wards.csv) - input dataset.
- [`screenshots/week7.png`](screenshots/week7.png) - screenshot showing the code and successful terminal output.

**Week 7 status:** The script runs successfully and classifies all four wards.

## Week 8 - Python Data Inspection

Week 8 applies Python to the full settlement analysis dataset from the Month 1 road accessibility project. The exercise reads a CSV file, handles missing or invalid numeric values, and calculates descriptive statistics for two attributes.

### Objective

Use Python to inspect the settlement dataset and summarise nearest-road distance and settlement block area.

### Dataset

- **File:** `ibadan_north_analysis.csv`
- **Source:** The analysis-ready settlement dataset prepared for the Ibadan North road accessibility project.
- **Records analysed:** 2,029 settlement features.
- **Method:** Python's `csv.DictReader` reads the CSV using its column headers.

### Attributes Analysed

1. **`distance`** - nearest mapped road distance in metres.
2. **`block_area_sqm`** - settlement block area in square metres.

### Analysis Workflow

The `inspect_data.py` script:

1. Checks that the input CSV file exists.
2. Reads the dataset using `csv.DictReader`.
3. Counts the records and reports the available columns.
4. Converts the selected numeric fields to floating-point values.
5. Skips empty or invalid numeric cells.
6. Reports valid and missing or invalid values for each selected field.
7. Calculates the minimum, maximum and mean for both attributes.

### Results

The script processed **2,029 settlement records**.

| Statistic | Nearest-road distance (m) | Settlement block area (m²) |
|---|---:|---:|
| Valid records | 2,029 | 2,029 |
| Missing or invalid records | 0 | 0 |
| Minimum | 0.00 | 1,040.32 |
| Maximum | 185.05 | 2,999,664.52 |
| Mean | 0.92 | 21,713.63 |

### How to Run

From the repository root, execute:

```powershell
python inspect_data.py
```

The script uses Python's standard library and does not require an additional package for CSV reading or these summary statistics.

### Interpretation

The nearest-road distance results range from 0 to 185.05 metres, with a mean of 0.92 metres. The settlement block areas vary considerably, from 1,040.32 m² to 2,999,664.52 m².

The distance distribution is strongly concentrated at zero, consistent with the earlier spatial analysis in which most settlement blocks had a calculated distance of zero to the mapped road/path network. A zero distance indicates that the settlement geometry intersects or touches a mapped feature under the distance calculation; it does not establish direct access for every building.

These statistics describe the supplied settlement polygons and their calculated proximity to mapped features. They should not be interpreted as a complete measure of access for every individual building.

### Week 8 Deliverables

- [`inspect_data.py`](inspect_data.py) - Python data inspection script.
- [`ibadan_north_analysis.csv`](ibadan_north_analysis.csv) - input dataset.
- [`screenshots/week8.png`](screenshots/week8.png) - screenshot of the successful script execution, to be added to the repository.

**Week 8 status:** The script successfully processed 2,029 records and generated summary statistics for both selected attributes. The screenshot must be saved and uploaded to complete the evidence requirement.

## Repository Structure

The repository contains the Month 1 spatial analysis documentation and outputs, together with the Month 2 Python development files.

```text
ibadan-north-road-access/
├── data/
│   ├── ibadan_north_analysis_v2.gpkg
│   ├── Ibadan_North_LGA.geojson
│   ├── ibadan_north_road_buffer_100m.gpkg
│   ├── ibadan_north_road_buffer_100m_dissolved.gpkg
│   ├── ibadan_north_roads.gpkg
│   ├── ibadan_north_settlements.gpkg
│   ├── ibadan_north_settlements_within_100m.gpkg
│   └── ibadan_north_settlements_outside_100m.gpkg
├── docs/
│   ├── 01-project-brief.md
│   ├── 02-data-notes.md
│   ├── 03-data-preparation.md
│   └── 04-spatial-analysis.md
├── maps/
│   └── week4-road-accessibility-100m.png
├── screenshots/
│   ├── week5.png
│   ├── week6.png
│   ├── week7.png
│   └── week8.png
├── README.md
├── analyse.py
├── check.py
├── hello.py
├── ibadan_north_analysis.csv
├── inspect_data.py
├── month-1-summary.md
├── pyproject.toml
├── uv.lock
└── wards.csv
```

The `.venv` directory is maintained locally and is not included in the GitHub repository.
