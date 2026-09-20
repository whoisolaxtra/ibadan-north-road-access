# Data Notes

## Project

**Project:** Road Accessibility to Settlement Areas in Ibadan North LGA, Oyo State, Nigeria

**Research question:** Which settlement areas in Ibadan North Local Government Area, Oyo State, are farthest from the nearest mapped road?

This file documents the datasets used for the project, including their sources, feature counts, geometry, important attributes, coordinate reference systems and data-quality observations.

---

## 1. Ibadan North LGA Boundary

**Dataset:** Ibadan North LGA Boundary

**Source:** GRID3 Nigeria Operational LGA Boundaries

**Source link:** https://grid3.org/geospatial-data-nigeria

### Description

The GRID3 Operational LGA Boundaries dataset provides administrative boundaries for Local Government Areas in Nigeria. The national dataset was used to extract the boundary of Ibadan North Local Government Area in Oyo State.

### Data used

- **Feature count:** 1
- **Geometry:** Polygon (MultiPolygon)
- **CRS:** EPSG:4326 — WGS 84
- **Format:** GeoJSON
- **Encoding:** UTF-8

### Key fields

| Field | Type | Purpose |
|---|---|---|
| `globalid` | String | Global feature identifier |
| `uniq_id` | Integer | Unique identifier |
| `lganame` | String | Local Government Area name |
| `lgacode` | String | LGA code |
| `statename` | String | State name |
| `statecode` | String | State code |
| `source` | String | Source information |
| `amapcode` | String | Administrative map code |

The selected feature represents **Ibadan North LGA**, with LGA code **31006** in **Oyo State**.

### Data quality observations

The extract contains one feature representing the study area. The geometry is stored as a MultiPolygon.

The dataset is stored in EPSG:4326, using geographic coordinates. This is suitable for displaying and storing the administrative boundary, but distance calculations should be performed using an appropriate projected CRS.

---

## 2. GRID3 Nigeria Settlement Extents v4.1

**Dataset:** GRID3 Nigeria Settlement Extents v4.1

**Source:** GRID3 Nigeria Geospatial Data for Nigeria

**Source link:** https://grid3.org/geospatial-data-nigeria

### Description

The GRID3 Settlement Extents dataset provides polygon features representing mapped settlement areas in Nigeria. The national dataset contains **2,546,560 features**. A spatial extraction was performed using the Ibadan North LGA boundary to obtain the settlement features within the study area.

### Data used

- **Feature count:** 2,029
- **Geometry:** Polygon (MultiPolygon)
- **CRS:** EPSG:3857 — WGS 84 / Pseudo-Mercator
- **Format:** GeoPackage (GPKG)
- **Encoding:** UTF-8
- **File size:** approximately 2.09 MB

### Key fields

| Field | Type | Purpose |
|---|---|---|
| `fid` | Integer64 | Feature identifier |
| `block_id` | String | Settlement block identifier |
| `block_area_sqm` | Real | Settlement block area |
| `block_perimeter` | Real | Settlement block perimeter |
| `block_neighbor_count` | Real | Number of neighbouring blocks |
| `building_count` | Integer | Number of buildings |
| `building_area_sum` | Float32 | Total building area |
| `building_area_median` | Real | Median building area |
| `building_area_percentage` | Float32 | Percentage of the block occupied by buildings |
| `extent_type` | String | Settlement extent classification |
| `ndvi_mean` | Real | Mean NDVI |
| `evi_mean` | Real | Mean EVI |
| `building_count_density` | Real | Building density |
| `bd_class` | String | Building-density classification |
| `ma_class` | String | Morphological classification |
| `composite_class` | String | Composite classification |

### Relevance to the project

This is the main settlement dataset for the project. Each settlement polygon represents a settlement area from which proximity to the nearest mapped road will be measured.

### Data quality observations

All **2,029 extracted settlement features have `extent_type = Built-up Area`**. No other `extent_type` value was found in the Ibadan North extract.

A NULL-value check of the four key fields (`block_id`, `block_area_sqm`, `building_count` and `extent_type`) returned **0 selected features**, indicating that none of these fields contains NULL values in the extract.

The dataset contains several attributes describing buildings, settlement structure and environmental characteristics. Most of these are not required for the initial nearest-road analysis.

The settlement extract uses EPSG:3857, while the LGA boundary and OSM road extract use EPSG:4326. QGIS can reproject the layers on the fly for visualisation, but a consistent projected CRS will be used before calculating distances.

---

## 3. OpenStreetMap Road Network

**Dataset:** OpenStreetMap Road Network

**Source:** OpenStreetMap data downloaded through Geofabrik

**Source link:** https://download.geofabrik.de/africa/nigeria.html

### Description

The road dataset contains mapped road and path features from OpenStreetMap. The Nigeria data was obtained through Geofabrik and spatially extracted using the Ibadan North LGA boundary.

### Data used

- **Feature count:** 3,148
- **Geometry:** Line (MultiLineString)
- **CRS:** EPSG:4326 — WGS 84
- **Format:** GeoPackage (GPKG)
- **Encoding:** UTF-8
- **File size:** approximately 996 KB

### Key fields

| Field | Type | Purpose |
|---|---|---|
| `fid` | Integer64 | Local feature identifier |
| `osm_id` | String | OpenStreetMap feature identifier |
| `code` | Integer | Feature classification code |
| `fclass` | String | Road/feature classification |
| `name` | String | Road name where available |
| `ref` | String | Road reference where available |
| `oneway` | String | One-way indicator |
| `maxspeed` | Integer | Recorded maximum speed where available |
| `layer` | Integer64 | Layer information |
| `bridge` | String | Bridge indicator |
| `tunnel` | String | Tunnel indicator |

### Relevance to the project

The road network provides the mapped road features against which settlement proximity will be measured. The geometry will be used to determine the nearest mapped road for each settlement area.

### Road feature classes observed

The `fclass` field contains **16 unique values**:

- `motorway`
- `motorway_link`
- `trunk`
- `trunk_link`
- `primary`
- `primary_link`
- `secondary`
- `secondary_link`
- `tertiary`
- `tertiary_link`
- `residential`
- `unclassified`
- `service`
- `track`
- `footway`
- `path`

This shows that the extract contains both conventional roads and smaller mapped access/path features.

### Data quality observations

A check of the `name` field found that **2,773 of the 3,148 road features have NULL or empty road names**, representing approximately **88.1%** of the extract. The remaining **375 features (11.9%)** have a recorded name.

The large proportion of unnamed features does not prevent the dataset from being used for the current research question because the analysis depends on road geometry and proximity rather than road names.

The extracted road layer does not contain a `surface` field. Therefore, the current dataset does not provide a reliable basis for separating roads into paved and unpaved categories.

OpenStreetMap represents volunteered geographic information, so mapped road coverage may not perfectly represent all roads that physically exist in the study area. The analysis will therefore refer specifically to **mapped roads** rather than assuming complete road coverage.

---

## 4. Dataset Summary

| Dataset | Source | Features used | Geometry | CRS |
|---|---|---:|---|---|
| Ibadan North LGA Boundary | GRID3 | 1 | MultiPolygon | EPSG:4326 |
| GRID3 Settlement Extents v4.1 | GRID3 | 2,029 | MultiPolygon | EPSG:3857 |
| OSM Road Network | OpenStreetMap / Geofabrik | 3,148 | MultiLineString | EPSG:4326 |

---

## 5. Initial Data Assessment

All three datasets required for the project have been downloaded, opened and inspected in QGIS.

The LGA boundary defines the study area, the GRID3 settlement extents provide the settlement areas to be assessed, and the OpenStreetMap road network provides the mapped roads used for the nearest-road distance measurement.

The main coordinate-system issue identified is that the datasets were initially stored in different CRS: EPSG:4326 for the LGA boundary and road network, and EPSG:3857 for the settlement extract. A suitable projected CRS was therefore selected and used consistently before distance calculations.

The OSM data also shows substantial variation in attribute completeness. In particular, 88.1% of road features do not have a recorded road name. However, this does not directly affect the core distance analysis because road geometry, rather than road names, is required.

The data inspection also confirmed that all settlement features in the Ibadan North extract are classified as `Built-up Area` and that the OSM road layer contains 16 observed feature classes.

---

## 6. Coordinate Reference System Decision and Working Layers

The project uses **WGS 84 / UTM Zone 31N (EPSG:32631)** as the working projected coordinate reference system.

The UTM zone was selected based on the approximate longitude of Ibadan North (3.9°E). Using the UTM zone formula:

**UTM Zone = floor((longitude + 180) / 6) + 1**

For 3.9°E:

**floor((3.9 + 180) / 6) + 1 = 31**

Ibadan North is located in the Northern Hemisphere, giving **UTM Zone 31N**.

EPSG:32631 uses metres as its linear unit and is therefore appropriate for the project's nearest-road distance calculations.

The source and extracted datasets were retained in their original coordinate reference systems. Separate projected working layers were created for analysis:

- `ibadan_north_boundary`
- `ibadan_north_settlements_utm31`
- `ibadan_north_roads_utm31`

All three working layers were verified in QGIS as **EPSG:32631 — WGS 84 / UTM zone 31N**, with metres as the unit of measurement.

The original datasets remain unchanged. The projected layers and the final analysis layer are separate working outputs.

---

## 7. Week 3 Quality Checks

Five quality checks were carried out before the distance analysis: positional accuracy, attribute accuracy, completeness, currency and fitness for purpose.

### 7.1 Positional accuracy

**Check performed:** The boundary, settlement polygons and mapped roads were overlaid with recent satellite imagery in QGIS for a visual positional check.

**Result:** The Ibadan North boundary aligned with the expected administrative area. The settlement polygons broadly corresponded with visible built-up areas in the sampled parts of the study area. The OSM road network also broadly followed visible road corridors, including major roads and numerous local streets. No obvious systematic positional offset was observed in the inspected areas.

**Decision:** No systematic positional problem was identified, so no geometric correction was applied. This was a visual plausibility check rather than a formal survey-grade positional accuracy assessment.

### 7.2 Attribute accuracy

**Check performed:** Key identifying and analytical fields were inspected for completeness and consistency.

**Result:** The settlement extract contains valid `block_id` values and all 2,029 features are classified as `Built-up Area`. The NULL-value check for `block_id`, `block_area_sqm`, `building_count` and `extent_type` returned zero selected features. The road layer contains 16 observed `fclass` values. However, 2,773 of 3,148 road features (88.1%) have no recorded road name, and the road extract has no `surface` field.

**Decision:** The missing road names were flagged but not treated as a blocker because the research question requires road geometry and distance, not road names. The absence of a `surface` field was also flagged, and paved/unpaved classification was not attempted.

### 7.3 Completeness

**Check performed:** Feature counts, attribute coverage and visual overlay were reviewed within the Ibadan North study area.

**Result:** The study-area extracts contain 2,029 settlement blocks and 3,148 mapped road/path features. Visual inspection of sampled areas showed broad correspondence between mapped settlements/roads and the visible landscape, with no obvious systematic coverage gap identified. However, OSM is volunteered geographic information and may omit roads that have not been mapped.

**Decision:** The datasets were retained as analysis-ready, but the road analysis is explicitly limited to **mapped OSM road/path features**. The results will not be interpreted as evidence that every physical road in Ibadan North has been captured.

### 7.4 Currency

**Check performed:** Dataset versions, release information and the OSM extraction timestamp were checked.

**Result:** GRID3 Settlement Extents v4.1 is identified as an **August 2026** release. The OSM extract used in this project was recorded as **14 September 2026 at 20:21:51 UTC** in the downloaded dataset metadata. The GRID3 Operational LGA Boundary dataset is an older administrative reference dataset, with the metadata indicating a March 2021 release.

**Decision:** The settlement and road datasets were retained because they represent recent available data for the project. The LGA boundary was retained as the administrative reference layer because the analysis requires a study-area boundary; its older release date is documented as a limitation rather than treated as a reason to discard the boundary.

### 7.5 Fitness for purpose

**Check performed:** The datasets were assessed against the actual research question and intended measurement.

**Result:** The settlement polygons provide the spatial units to assess, the OSM network provides mapped linear features against which proximity can be measured, and all working layers were reprojected to EPSG:32631 so distance is calculated in metres. The resulting analysis layer contains 2,029 settlement features with a nearest-road distance field and no NULL distance values.

The distance results range from **0 m to approximately 185.05 m**. A total of **1,978 settlement blocks have a distance of 0 m**, while **51 have a non-zero distance**. The maximum observed nearest-mapped-feature distance is approximately **185.05 m**.

**Decision:** The data is fit for the stated question when the result is interpreted as distance to the **nearest mapped OSM road/path feature**, not distance to every physical road. The inclusion of `track`, `footway` and `path` features is documented because these are present in the extracted OSM layer. A separate paved/unpaved or motor-vehicle-road analysis would require additional classification/filtering data.

---

## 8. Week 3 Analysis-Ready Output

The prepared analysis layer was created after reprojection and nearest-road distance processing.

**Analysis-ready file:** `ibadan_north_analysis_v2.gpkg`

**Expected repository location:** `data/ibadan_north_analysis_v2.gpkg`

The analysis layer contains **2,029 settlement features** and includes the original settlement attributes together with the nearest-road distance field.

The final working CRS is **EPSG:32631 — WGS 84 / UTM Zone 31N**, with distances expressed in metres.

The original source/extract files were retained separately so that the analysis can be reproduced without overwriting the source data.

---

## 9. Week 3 Preparation Summary

| Requirement | Result |
|---|---|
| Study area defined | Ibadan North LGA |
| Settlement features extracted | 2,029 |
| Road/path features extracted | 3,148 |
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
