# Week 4 - Spatial Analysis

## Spatial Analysis Objective

The Week 4 spatial analysis examines the proximity of settlement areas to the mapped road network in Ibadan North Local Government Area, Oyo State, Nigeria.

The analysis uses a **100 m road-proximity threshold** to identify settlement areas that intersect the mapped road-access zone.

This analysis complements the continuous nearest-road distance analysis conducted previously by providing a defined proximity threshold.

## Spatial Operation

A **100 m buffer** was created around the mapped OSM road network using the **WGS 84 / UTM Zone 31N (EPSG:32631)** projected coordinate reference system.

The road dataset was filtered to exclude:

- `path`
- `footway`
- `track`

This left **3,026 mapped road features** for the Week 4 buffer analysis.

The buffer was created using a distance of **100 metres**, with rounded joins and end caps. The buffer was subsequently dissolved to produce a continuous road-proximity zone.

The primary settlement analysis was then performed using an **Intersection** operation between the dissolved 100 m road-proximity zone and the settlement areas.

## Expected Result

The expected result was that settlement areas located within 100 m of the mapped road network would intersect the dissolved buffer, while settlement areas located beyond the 100 m threshold would remain outside the buffer.

The exact number of settlement areas within the threshold was determined from the spatial intersection rather than assumed beforehand.

## Processing Workflow

1. Filtered the OSM road network to exclude `path`, `footway`, and `track` features.
2. Created a **100 m buffer** around the filtered mapped road network.
3. Checked the buffer geometry for validity.
4. Dissolved the individual buffer polygons into a continuous road-proximity zone.
5. Intersected the dissolved 100 m buffer with the settlement areas.
6. Checked the resulting feature count.
7. Used a spatial selection to identify settlement areas that do not intersect the 100 m road-proximity zone.
8. Exported the three settlement areas outside the 100 m zone as a separate GeoPackage layer.

## Validation

The original settlement dataset contained **2,029 settlement areas**.

The intersection between the settlement areas and the dissolved 100 m road-proximity zone produced **2,026 settlement features**.

A separate spatial selection using the `disjoint` relationship identified **3 settlement areas** that do not intersect the dissolved 100 m buffer.

The resulting counts were:

| Measure | Result |
|---|---:|
| Total settlement areas | 2,029 |
| Settlement areas within/intersecting 100 m zone | 2,026 |
| Settlement areas outside 100 m zone | 3 |
| Percentage within 100 m | 99.85% |
| Percentage outside 100 m | 0.15% |

The three settlement areas outside the 100 m threshold were visually checked and exported as a separate layer.

## Buffer Geometry Validation

The 100 m buffer was checked for geometric validity using the GEOS geometry validation method in QGIS.

The validation returned:

- **Valid geometries:** 3,026
- **Invalid geometries:** 0
- **Errors:** 0

This confirmed that all 3,026 buffer features used in the analysis had valid geometry before the buffer was dissolved and intersected with the settlement layer.

## Output Layers

The final Week 4 outputs are:

- `ibadan_north_road_buffer_100m.gpkg`
- `ibadan_north_road_buffer_100m_dissolved.gpkg`
- `ibadan_north_settlements_within_100m.gpkg`
- `ibadan_north_settlements_outside_100m.gpkg`

### Layer Names

The corresponding layer names are:

- `road_buffer_100m`
- `road_buffer_100m_dissolved`
- `settlements_within_100m`
- `settlements_outside_100m`

## Coordinate Reference System

All Week 4 spatial analysis was conducted using:

**WGS 84 / UTM Zone 31N**

**EPSG:32631**

The projected CRS was used because the analysis involves a distance threshold measured in metres.

## Interpretation

The analysis identified **2,026 of the 2,029 mapped settlement areas** as intersecting the 100 m road-proximity zone.

Only **3 settlement areas (0.15%)** were identified outside the 100 m threshold.

This indicates that the mapped settlement areas in the study area are predominantly located within 100 m of the mapped OSM road network used in this analysis.

However, the result represents proximity to the **mapped road dataset**, rather than a complete measure of physical road accessibility. The result is therefore dependent on the completeness, positional accuracy, and classification of the OSM road data.

In particular, the analysis should not be interpreted as confirming that every settlement area has direct or convenient physical access to a motorable road.

## Relationship to the Research Question

The Week 4 analysis provides a threshold-based perspective on the research question:

> **Which settlement areas in Ibadan North Local Government Area, Oyo State, are farthest from the nearest mapped road?**

The previous nearest-road distance analysis provides the continuous distance measurement, while the Week 4 100 m proximity analysis identifies settlement areas that fall outside a defined road-proximity threshold.

Together, the two analyses provide complementary measures of settlement-road accessibility.
