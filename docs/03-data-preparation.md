# Data Preparation

## Project

**Project:** Road Accessibility to Settlement Areas in Ibadan North LGA, Oyo State, Nigeria

**Research question:** Which settlement areas in Ibadan North Local Government Area, Oyo State, are farthest from the nearest mapped road?

This document records the coordinate reference system decision, data preparation, quality checks and analysis-ready output for the project.

---

## 1. Working Coordinate Reference System

The project uses **WGS 84 / UTM Zone 31N (EPSG:32631)** as the working projected coordinate reference system.

The UTM zone was selected based on the approximate longitude of Ibadan North (3.9°E). Using the UTM zone formula:

**UTM Zone = floor((longitude + 180) / 6) + 1**

For 3.9°E:

**floor((3.9 + 180) / 6) + 1 = 31**

Ibadan North is located in the Northern Hemisphere, giving **UTM Zone 31N**.

EPSG:32631 uses metres as its linear unit and is therefore appropriate for the project's nearest-road distance calculations.

---

## 2. Data Reprojection

The source and extracted datasets were initially stored in different coordinate reference systems:

- LGA boundary — EPSG:4326
- OSM road network — EPSG:4326
- GRID3 settlement extents — EPSG:3857

The datasets were reprojected to **EPSG:32631 — WGS 84 / UTM Zone 31N** for consistent spatial analysis and distance measurement.

The following working layers were created:

- `ibadan_north_boundary`
- `ibadan_north_settlements_utm31`
- `ibadan_north_roads_utm31`

All three working layers were verified in QGIS as EPSG:32631, with metres as the unit of measurement.

The original source/extract datasets were retained unchanged.

---

## 3. Study-Area Preparation

The Ibadan North LGA boundary was used to define the study area.

The national GRID3 settlement dataset and the OpenStreetMap road network were spatially extracted using the Ibadan North LGA boundary.

The resulting study-area datasets contained:

- **2,029 settlement features**
- **3,148 mapped road/path features**

The settlement and road datasets were subsequently reprojected to EPSG:32631 for analysis.

---

## 4. Quality Checks

Five quality checks were carried out before the distance analysis:

1. Positional accuracy
2. Attribute accuracy
3. Completeness
4. Currency
5. Fitness for purpose

### 4.1 Positional Accuracy

**Check performed:** The boundary, settlement polygons and mapped roads were overlaid with recent satellite imagery in QGIS for a visual positional check.

**Result:** The Ibadan North boundary aligned with the expected administrative area. The settlement polygons broadly corresponded with visible built-up areas in the sampled parts of the study area. The OSM road network also broadly followed visible road corridors, including major roads and numerous local streets. No obvious systematic positional offset was observed in the inspected areas.

**Decision:** No systematic positional problem was identified, so no geometric correction was applied. This was a visual plausibility check rather than a formal survey-grade positional accuracy assessment.

### 4.2 Attribute Accuracy

**Check performed:** Key identifying and analytical fields were inspected for completeness and consistency.

**Result:** The settlement extract contains valid `block_id` values and all 2,029 features are classified as `Built-up Area`. The NULL-value check for `block_id`, `block_area_sqm`, `building_count` and `extent_type` returned zero selected features.

The road layer contains 16 observed `fclass` values. However, 2,773 of 3,148 road features (88.1%) have no recorded road name, and the road extract has no `surface` field.

**Decision:** The missing road names were flagged but not treated as a blocker because the research question requires road geometry and distance, not road names. The absence of a `surface` field was also flagged, and paved/unpaved classification was not attempted.

### 4.3 Completeness

**Check performed:** Feature counts, attribute coverage and visual overlay were reviewed within the Ibadan North study area.

**Result:** The study-area extracts contain 2,029 settlement blocks and 3,148 mapped road/path features. Visual inspection of sampled areas showed broad correspondence between mapped settlements/roads and the visible landscape, with no obvious systematic coverage gap identified.

However, OpenStreetMap is volunteered geographic information and may omit roads that have not been mapped.

**Decision:** The datasets were retained as analysis-ready, but the road analysis is explicitly limited to **mapped OSM road/path features**. The results will not be interpreted as evidence that every physical road in Ibadan North has been captured.

### 4.4 Currency

**Check performed:** Dataset versions, release information and the OSM extraction timestamp were checked.

**Result:** GRID3 Settlement Extents v4.1 is identified as an **August 2026** release. The OSM extract used in this project was recorded as **14 September 2026 at 20:21:51 UTC** in the downloaded dataset metadata. The GRID3 Operational LGA Boundary dataset is an older administrative reference dataset, with the metadata indicating a March 2021 release.

**Decision:** The settlement and road datasets were retained because they represent recent available data for the project. The LGA boundary was retained as the administrative reference layer because the analysis requires a study-area boundary; its older release date is documented as a limitation rather than treated as a reason to discard the boundary.

### 4.5 Fitness for Purpose

**Check performed:** The datasets were assessed against the actual research question and intended measurement.

**Result:** The settlement polygons provide the spatial units to assess, the OSM network provides mapped linear features against which proximity can be measured, and all working layers were reprojected to EPSG:32631 so distance is calculated in metres.

The resulting analysis layer contains 2,029 settlement features with a nearest-road distance field and no NULL distance values.

The distance results range from **0 m to approximately 185.05 m**.

- **1,978 settlement blocks** have a distance of 0 m.
- **51 settlement blocks** have a non-zero distance.
- The maximum observed nearest-mapped-feature distance is approximately **185.05 m**.

**Decision:** The data is fit for the stated question when the result is interpreted as distance to the **nearest mapped OSM road/path feature**, not distance to every physical road.

The inclusion of `track`, `footway` and `path` features is documented because these are present in the extracted OSM layer. A separate paved/unpaved or motor-vehicle-road analysis would require additional classification or filtering data.

---

## 5. Analysis-Ready Output

The prepared analysis layer was created after reprojection and nearest-road distance processing.

**Analysis-ready file:** `ibadan_north_analysis_v2.gpkg`

**Repository location:** `data/ibadan_north_analysis_v2.gpkg`

The analysis layer contains **2,029 settlement features** and includes the original settlement attributes together with the nearest-road distance field.

The final working CRS is **EPSG:32631 — WGS 84 / UTM Zone 31N**, with distances expressed in metres.

The distance field is:

`distance`

The original source/extract files were retained separately so that the analysis can be reproduced without overwriting the source data.

---

## 6. Preparation Summary

| Requirement | Result |
|---|---|
| Study area | Ibadan North LGA |
| Settlement features | 2,029 |
| Road/path features | 3,148 |
| Working CRS | EPSG:32631 |
| Boundary reprojected | Yes |
| Settlements reprojected | Yes |
| Roads reprojected | Yes |
| Analysis-ready GeoPackage | `ibadan_north_analysis_v2.gpkg` |
| Distance field | `distance` |
| Distance unit | metres |
| NULL distance values | 0 |
| Maximum observed distance | 185.05 m |
| Quality checks completed | 5 |
| Main limitation | OSM mapped-road/path completeness and classification |

## 7. Reproducibility

The original extracted datasets are retained in the `data/` directory alongside the analysis-ready GeoPackage. The preparation workflow and quality decisions documented here provide a record of how the analysis-ready dataset was produced.
