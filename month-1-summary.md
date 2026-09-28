# Month 1 Summary - Road Accessibility to Settlement Areas in Ibadan North LGA

## Project Question

Which settlement areas in Ibadan North Local Government Area, Oyo State, are farthest from the nearest mapped road?

## Month 1 Project Story

This project developed a GIS workflow to examine the spatial relationship between settlement areas and the mapped road network in Ibadan North Local Government Area, Oyo State, Nigeria.

The four weeks were designed as one continuous workflow rather than as separate exercises:

**Project question → Data acquisition → Data preparation → Spatial analysis → Result**

## Week 1 - Project Definition

The project began by defining the study area, research question, datasets and proposed analytical approach.

The focus was placed on settlement accessibility to mapped roads within Ibadan North LGA.

The initial project brief established the research question and identified the main datasets required for the analysis.

**Documentation:** [`docs/01-project-brief.md`](docs/01-project-brief.md)

## Week 2 - Data Acquisition and Assessment

The required spatial datasets were acquired and assessed:

- GRID3 Nigeria Operational LGA Boundaries
- GRID3 Nigeria Settlement Extents v4.1
- OpenStreetMap road data downloaded through Geofabrik

The extracted datasets were checked for their spatial coverage, geometry types, coordinate reference systems, attribute structure and suitability for the planned analysis.

**Documentation:** [`docs/02-data-notes.md`](docs/02-data-notes.md)

## Week 3 - Data Preparation

The datasets were prepared for spatial analysis.

The working layers were transformed to:

**EPSG:32631 - WGS 84 / UTM Zone 31N**

This projected coordinate reference system allowed distances to be calculated in metres.

The settlement, road and boundary datasets were checked and prepared as analysis-ready layers.

A nearest-road distance analysis was then conducted for the 2,029 settlement features.

Observed nearest-mapped-feature distances ranged from **0 m to approximately 185.05 m**.

- 1,978 settlement blocks had a distance of 0 m.
- 51 settlement blocks had a non-zero distance.
- The maximum observed distance was approximately 185.05 m.

**Documentation:** [`docs/03-data-preparation.md`](docs/03-data-preparation.md)

## Week 4 - Spatial Analysis

The project then moved from continuous nearest-road distance to a threshold-based spatial analysis.

A **100 m buffer** was created around the mapped OSM road network.

For this analysis, `path`, `footway` and `track` features were excluded from the road dataset, leaving **3,026 mapped road features**.

The buffer was dissolved into a continuous road-proximity zone and intersected with the settlement areas.

### Validation

The 100 m buffer geometry was checked before further analysis:

- Valid geometries: **3,026**
- Invalid geometries: **0**
- Errors: **0**

A spatial selection was also used to identify settlement areas disjoint from the dissolved 100 m buffer.

### Result

Of the **2,029 settlement areas**:

- **2,026 (99.85%)** intersected the 100 m road-proximity zone.
- **3 (0.15%)** were outside the 100 m threshold.

The three settlement areas outside the threshold were exported as a separate GeoPackage layer.

**Documentation:** [`docs/04-spatial-analysis.md`](docs/04-spatial-analysis.md)

**Map:** [`maps/week4-road-accessibility-100m.png`](maps/week4-road-accessibility-100m.png)

## What the Analysis Shows

The analysis shows that the mapped settlement areas in Ibadan North are predominantly located within the 100 m proximity zone around the mapped road network used in the Week 4 analysis.

However, the result represents proximity to **mapped OSM road features** and should not be interpreted as a complete measure of physical road accessibility.

The result depends on the completeness, positional accuracy and classification of the mapped road data.

The Week 3 and Week 4 analyses also use different road-feature selections:

- **Week 3:** nearest mapped OSM road/path feature
- **Week 4:** mapped road features after excluding `path`, `footway` and `track`

The two analyses therefore provide complementary perspectives on settlement-road proximity.

## Project Outputs

### Analysis Data

- [`data/ibadan_north_analysis_v2.gpkg`](data/ibadan_north_analysis_v2.gpkg)
- [`data/ibadan_north_road_buffer_100m.gpkg`](data/ibadan_north_road_buffer_100m.gpkg)
- [`data/ibadan_north_road_buffer_100m_dissolved.gpkg`](data/ibadan_north_road_buffer_100m_dissolved.gpkg)
- [`data/ibadan_north_settlements_within_100m.gpkg`](data/ibadan_north_settlements_within_100m.gpkg)
- [`data/ibadan_north_settlements_outside_100m.gpkg`](data/ibadan_north_settlements_outside_100m.gpkg)

### Final Map

[`maps/week4-road-accessibility-100m.png`](maps/week4-road-accessibility-100m.png)

## Month 1 Outcome

The first month established a complete geospatial workflow from project definition and data acquisition through data preparation, spatial analysis, validation and visualisation.

The project now has:

- A clearly defined research question
- Documented source datasets
- Analysis-ready spatial data
- A reproducible spatial-analysis workflow
- Validated analytical outputs
- A documented result
- A final map
- A structured GitHub repository containing the project history and outputs

The next stage can build on this foundation by extending the accessibility analysis beyond a simple distance threshold and considering additional factors relevant to accessibility.
