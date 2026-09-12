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

The main coordinate-system issue identified is that the datasets are currently stored in different CRS: EPSG:4326 for the LGA boundary and road network, and EPSG:3857 for the settlement extract. A suitable projected CRS will therefore be selected and used consistently before distance calculations are performed.

The OSM data also shows substantial variation in attribute completeness. In particular, 88.1% of road features do not have a recorded road name. However, this does not directly affect the core distance analysis because road geometry, rather than road names, is required.

The data inspection also confirmed that all settlement features in the Ibadan North extract are classified as `Built-up Area` and that the OSM road layer contains 16 observed feature classes.
