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

The project calculates the distance from each settlement area to its nearest mapped OSM road/path feature.

The analysis uses:

**EPSG:32631 — WGS 84 / UTM Zone 31N**

Distances are calculated in metres.

## Current Results

The analysis-ready dataset contains **2,029 settlement features** with a nearest-road distance field.

Observed nearest-mapped-feature distances range from **0 m to approximately 185.05 m**.

- **1,978 settlement blocks** have a distance of 0 m.
- **51 settlement blocks** have a non-zero distance.
- The maximum observed distance is approximately **185.05 m**.

## Analysis-Ready Output

The final analysis-ready GeoPackage is:

`data/ibadan_north_analysis_v2.gpkg`

It contains the settlement features and the calculated nearest-road distance field.

## Project Status

**Week 3 — Data preparation completed.**

The project datasets were reprojected to EPSG:32631, quality checks were completed, and an analysis-ready GeoPackage was created.

## Repository Structure

```text
ibadan-north-road-access/
├── README.md
├── data/
│   ├── README.md
│   ├── Ibadan_North_LGA.geojson
│   ├── ibadan_north_roads.gpkg
│   ├── ibadan_north_settlements.gpkg
│   └── ibadan_north_analysis_v2.gpkg
└── docs/
    ├── 01-project-brief.md
    ├── 02-data-notes.md
    └── 03-data-preparation.md
