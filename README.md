# Road Accessibility to Settlement Areas in Ibadan North LGA

## Project Overview

This project examines the spatial accessibility of settlement areas to mapped roads in Ibadan North Local Government Area, Oyo State, Nigeria.

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

The project examines settlement proximity to the mapped road network using both continuous nearest-road distance and a 100 m road-proximity threshold.

The analysis uses:

**EPSG:32631 - WGS 84 / UTM Zone 31N**

Distances are calculated in metres.

### Week 3 - Nearest-Road Distance Analysis

The analysis-ready dataset contains **2,029 settlement features** with a nearest-road distance field.

Observed nearest-mapped-feature distances range from **0 m to approximately 185.05 m**.

- **1,978 settlement blocks** have a distance of 0 m.
- **51 settlement blocks** have a non-zero distance.
- The maximum observed distance is approximately **185.05 m**.

The Week 3 analysis provides a continuous measure of settlement proximity to the mapped road/path network.

**Documentation:**  
[`docs/03-data-preparation.md`](docs/03-data-preparation.md)

## Week 4 - Spatial Analysis

Week 4 focused on a **100 m road-proximity analysis** to examine the relationship between mapped roads and settlement areas.

### Spatial Operation

A 100 m buffer was created around the mapped OSM road network using **EPSG:32631 — WGS 84 / UTM Zone 31N**.

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

This result represents proximity to the **mapped OSM road dataset** and should not be interpreted as a complete measure of physical road accessibility. The result is dependent on the completeness, positional accuracy and classification of the mapped road data.

**Documentation:**  
[`docs/04-spatial-analysis.md`](docs/04-spatial-analysis.md)

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

The map shows the mapped road network, 100 m road-proximity zone, settlement areas, and the three settlement areas identified outside the 100 m threshold.

## Month 1 Integration Summary

The complete four-week project story, results and outputs are summarised in:

[`month-1-summary.md`](month-1-summary.md)

The summary connects the project from:

**Project question → Data acquisition → Data preparation → Spatial analysis → Result**

## Project Status

**Month 1 - Four-week project completed.**

The project progressed from project definition and data acquisition through data preparation, nearest-road distance analysis, threshold-based spatial analysis, validation and visualisation.

The Week 4 workflow included road filtering, 100 m buffering, geometry validation, buffer dissolution, settlement intersection and independent validation of settlement areas outside the 100 m threshold.

## Documentation

Detailed project documentation is organised by week:

- **Week 1 - Project Brief:** [`docs/01-project-brief.md`](docs/01-project-brief.md)
- **Week 2 - Data Notes:** [`docs/02-data-notes.md`](docs/02-data-notes.md)
- **Week 3 - Data Preparation:** [`docs/03-data-preparation.md`](docs/03-data-preparation.md)
- **Week 4 - Spatial Analysis:** [`docs/04-spatial-analysis.md`](docs/04-spatial-analysis.md)
- **Month 1 - Integration Summary:** [`month-1-summary.md`](month-1-summary.md)

## Repository Structure

```text
ibadan-north-road-access/
├── README.md
├── month-1-summary.md
├── data/
│   ├── Ibadan_North_LGA.geojson
│   ├── ibadan_north_roads.gpkg
│   ├── ibadan_north_settlements.gpkg
│   ├── ibadan_north_analysis_v2.gpkg
│   ├── ibadan_north_road_buffer_100m.gpkg
│   ├── ibadan_north_road_buffer_100m_dissolved.gpkg
│   ├── ibadan_north_settlements_within_100m.gpkg
│   └── ibadan_north_settlements_outside_100m.gpkg
├── docs/
│   ├── 01-project-brief.md
│   ├── 02-data-notes.md
│   ├── 03-data-preparation.md
│   └── 04-spatial-analysis.md
└── maps/
    └── week4-road-accessibility-100m.png
