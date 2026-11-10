# Month 3 - Week 11
## Coordinate Reference Systems and Spatial Operations in Code

This directory contains the practical exercises and independent challenges completed for Month 3, Week 11 of GeoDev Lab Africa.

The exercises explore coordinate reference systems, coordinate transformations, spatial measurements, spatial joins, proximity analysis, overlay operations and geometry validation using Python and GeoPandas.

The independent challenges apply these techniques to the Ibadan North geospatial analysis project.

---

## Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Project Structure](#2-project-structure)
3. [Guided Exercises](#3-guided-exercises)
4. [Independent Challenges](#4-independent-challenges)
5. [CRS and Projection](#5-crs-and-projection)
6. [Software and Libraries](#6-software-and-libraries)
7. [Running the Scripts](#7-running-the-scripts)
8. [Methodological Considerations](#8-methodological-considerations)
9. [Assessment Breakdown](#9-assessment-breakdown)

---

## 1. Learning Objectives

The practical exercises cover:

- Understanding geographic and projected coordinate reference systems.
- Distinguishing between `set_crs()` and `to_crs()`.
- Transforming geographic coordinates into projected coordinates.
- Calculating area and distance using appropriate CRS.
- Performing spatial joins and nearest-feature analysis.
- Identifying coverage gaps through buffering and overlay operations.
- Applying clipping and dissolve operations.
- Validating and repairing vector geometries.

## 2. Project Structure

```text
week-11/
│
├── area_wrong_and_right.py
├── set_vs_to.py
├── one_point.py
├── spatial_ops.py
├── coverage_gap.py
├── nearest.py
├── clip_dissolve.py
├── fix_geometry.py
│
├── my_crs.py
├── my_count.py
├── my_reach.py
├── my_validity.py
│
├── outputs/
│   ├── wards_fixed.gpkg
│   ├── my_crs_results.gpkg
│   ├── my_count_results.gpkg
│   ├── my_reach_results.gpkg
│   ├── my_valid_roads.gpkg
│   └── my_valid_settlements.gpkg
│
└── README.md
```

## 3. Guided Exercises

Eight guided exercises were completed to demonstrate the application of CRS management and spatial operations in GeoPandas.

| No. | Script | Exercise |
|:---:|---|---|
| 01 | `area_wrong_and_right.py` | Comparing area calculations in geographic and projected CRS |
| 02 | `set_vs_to.py` | Understanding `set_crs()` versus `to_crs()` |
| 03 | `one_point.py` | Transforming geographic coordinates into UTM coordinates |
| 04 | `spatial_ops.py` | Spatial joins and buffer operations |
| 05 | `coverage_gap.py` | Identifying uncovered areas through buffering and overlay |
| 06 | `nearest.py` | Calculating distances to nearest facilities |
| 07 | `clip_dissolve.py` | Clipping road features and dissolving polygons |
| 08 | `fix_geometry.py` | Geometry validation and repair |

### Selected Results

| Analysis | Result |
|---|---:|
| Study area | 58.6 km² |
| Facilities processed | 41 |
| Ward polygons | 12 |
| Spatial join records | 41 |
| Roads within Agodi | 2 |
| Clipped road length | 1.21 km |

The guided nearest-facility exercise used ward centroids to estimate straight-line distances to the nearest facility.

The coverage-gap exercise identified uncovered areas in selected wards, with Samonda and Agbowo recording 100% uncovered area in the supplied training dataset.

## 4. Independent Challenges

The four independent challenges apply the Week 11 concepts to the Ibadan North project datasets.

### 4.1 CRS Identification and Spatial Measurement

**Script:** `my_crs.py`

**Datasets:**
- `ibadan_north_analysis_v2.gpkg`
- `ibadan_north_roads.gpkg`

**Operations performed:**
- Inspected the original coordinate reference systems.
- Estimated a suitable UTM projection.
- Reprojected the road network.
- Calculated settlement polygon areas.
- Calculated nearest-road distances from settlement representative points.

**Results**

| Indicator | Result |
|---|---:|
| Settlement features | 2,029 |
| Road features | 3,148 |
| Selected CRS | EPSG:32631 |
| Total settlement area | 44.032 km² |
| Mean nearest-road distance | 36.23 m |

**Output:** `outputs/my_crs_results.gpkg`

### 4.2 Point-in-Polygon Counting

**Script:** `my_count.py`

**Datasets:**
- `ibadan_north_analysis_v2.gpkg`
- `ibadan_north_roads.gpkg`

**Operations performed:**
- Loaded settlement polygons and the road network.
- Reprojected the road network to match the settlement CRS.
- Generated representative points from road geometries.
- Performed a point-in-polygon spatial join using the `contains` predicate.
- Counted road points within each settlement polygon.
- Retained polygons with zero matching points.
- Identified unmatched points through an additional spatial join.

**Results**

| Indicator | Result |
|---|---:|
| Settlement polygons | 2,029 |
| Road features | 3,148 |
| Generated road points | 3,148 |
| Polygons containing road points | 1,410 |
| Polygons with zero road points | 619 |
| Total points counted | 3,124 |
| Unmatched points | 24 |
| Point assignment percentage | 99.24% |

**Output:** `outputs/my_count_results.gpkg`

> **Methodological note:** Representative points were generated from road-segment geometries. The resulting counts describe the distribution of these derived road points within settlement polygons. They should not be interpreted as building counts, population estimates or road-intersection counts. Points outside polygon coverage, including potential boundary points, are not assigned by the `contains` predicate.

### 4.3 Road Coverage and Proximity Analysis

**Script:** `my_reach.py`

**Operations performed:**
- Reprojected the settlement and road datasets to EPSG:32631.
- Generated representative points for settlement blocks.
- Created a 100 m buffer around the road network.
- Classified settlement points by road proximity.
- Calculated nearest-road distances.

**Results**

| Indicator | Result |
|---|---:|
| Total settlement blocks | 2,029 |
| Within 100 m of roads | 1,981 |
| Outside 100 m of roads | 48 |
| Coverage percentage | 97.63% |
| Coverage gap percentage | 2.37% |
| Mean nearest-road distance | 36.23 m |

**Output:** `outputs/my_reach_results.gpkg`

> **Methodological note:** This is a geometric proximity assessment, not a network accessibility analysis. It does not account for road connectivity, road condition, travel time or actual building accessibility.

### 4.4 Geometry Validation and Repair

**Script:** `my_validity.py`

**Operations performed:**
- Checked settlement and road geometries for validity.
- Identified invalid features.
- Applied `make_valid()` where necessary.
- Rechecked geometry validity.
- Exported the resulting datasets.

**Results**

| Dataset | Features | Invalid before | Invalid after |
|---|---:|---:|---:|
| Settlements | 2,029 | 0 | 0 |
| Roads | 3,148 | 0 | 0 |

**Outputs:**
- `outputs/my_valid_settlements.gpkg`
- `outputs/my_valid_roads.gpkg`

> **Finding:** Both input datasets already contained valid geometries. No geometry repairs were required.

## 5. CRS and Projection

The independent Ibadan North analyses used:

**EPSG:32631 – WGS 84 / UTM Zone 31N**

The original datasets had different coordinate reference systems:

| Dataset | Original CRS |
|---|---|
| Settlement polygons | EPSG:32631 |
| Road network | EPSG:4326 |

The road network was transformed into the settlement dataset's projected CRS using `to_crs()` before metric spatial operations.

A projected CRS was used for area, buffering and distance calculations to avoid performing these measurements directly in geographic degrees.

## 6. Software and Libraries

| Software / Library | Application |
|---|---|
| Python | Scripting and automation |
| GeoPandas | Vector data management and spatial analysis |
| Shapely | Geometry operations and validation |
| PyProj | CRS transformation and projection management |
| Pandas | Attribute manipulation and summary statistics |

## 7. Running the Scripts

Run the scripts from the repository root with the project virtual environment activated.

**Example – Guided exercise**

```powershell
python .\month-03\week-11\area_wrong_and_right.py
```

**Independent challenges**

```powershell
python .\month-03\week-11\my_crs.py
python .\month-03\week-11\my_count.py
python .\month-03\week-11\my_reach.py
python .\month-03\week-11\my_validity.py
```

Generated GeoPackages are stored in the `outputs/` directory.

## 8. Methodological Considerations

The following considerations apply to the independent analyses:

1. **CRS suitability:** Area and distance calculations require an appropriate projected CRS. EPSG:32631 was used for the Ibadan North study area.
2. **Coordinate transformation:** `to_crs()` transforms coordinates, whereas `set_crs()` assigns or overrides CRS metadata without transforming coordinates.
3. **Representative points:** These provide a location proxy for each settlement polygon or road feature; they are not necessarily actual building or road-intersection locations.
4. **Point counting:** The generated road points demonstrate spatial counting but cannot be interpreted as independent population or building observations.
5. **Road proximity:** Straight-line distance does not represent network travel distance or accessibility.
6. **Buffer threshold:** The 100 m road buffer is an analytical threshold used to classify proximity.
7. **Geometry validation:** Valid geometry does not automatically guarantee positional accuracy, attribute completeness or the absence of duplicate features.

## 9. Assessment Breakdown

| Assessment component | Marks |
|---|---:|
| Eight guided scripts and outputs | 30 |
| Four independent challenges | 40 |
| README documentation | 20 |
| Repository hygiene | 10 |
| **Total** | **100** |

---


