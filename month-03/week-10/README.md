# Week 10: GeoPandas — Loaded, Checked, Joined and Mapped

## 1. Project overview

This exercise applies Python, pandas and GeoPandas to geospatial data for Ibadan North LGA, Oyo State, Nigeria.

The work covers tabular data inspection, filtering, sorting, vector-layer inspection, geometry validation, coordinate conversion, attribute joins, map production and output management.

The independent challenge applies these techniques to data from my existing Ibadan North road-accessibility project.

## 2. Data sources

The exercise uses:

- `data/raw/ward_population.csv` — ward-level population data for 2024.
- `data/raw/health_facilities.csv` — health facility names, types and coordinates.
- `data/processed/wards.gpkg` — ward polygon layer.
- `data/processed/` — location for processed geospatial outputs.

The ward and facility datasets are used to demonstrate spatial data inspection, point creation, attribute joining and mapping.

## 3. Guided practical

The eight guided scripts are:

| Script | Purpose |
|---|---|
| `explore_pandas.py` | Loads and inspects the ward population CSV, including its structure, columns, data types and summary statistics. |
| `filter_sort.py` | Filters wards by population, sorts the results and creates a population-in-thousands column. |
| `explore_layer.py` | Inspects the ward GeoPackage, including its layers, feature count, geometry type, CRS and spatial bounds. |
| `geom_props.py` | Examines a polygon geometry, checks validity and calculates its centroid. |
| `csv_to_points.py` | Converts health facility coordinates from CSV into a GeoDataFrame and saves a point GeoPackage. |
| `join_population.py` | Joins population records to ward polygons and cleans inconsistent ward names to improve matching. |
| `make_map.py` | Produces a quick map of ward polygons and health facility locations. |
| `save_outputs.py` | Saves a ward layer to a new GeoPackage and exports its non-spatial attributes to CSV. |

### Guided practical outputs

- `facilities_map.png` — quick map of wards and health facilities.
- `wards_table.csv` — ward attribute table without geometry.
- `data/processed/week10_outputs.gpkg` — GeoPackage containing the `wards_copy` polygon layer.
- `data/processed/facilities.gpkg` — point layer created from the guided health facility CSV exercise.

## 4. Independent challenge

The independent challenge applies the Week 10 techniques to the Ibadan North training datasets, extending the guided exercises through additional data cleaning, spatial processing and mapping.

### `my_explore.py`

Inspects the ward polygon layer.

Results:
- 12 features.
- 4 columns, including geometry.
- Polygon geometry.
- CRS: EPSG:4326.
- Spatial bounds: 3.88, 7.38, 3.94, 7.46.

### `my_points.py`

Converts the health facility CSV into a point GeoPackage.

Results:
- 41 health facility records.
- Original categories included `Primary Health Centre` and `PHC`.
- The two categories were standardised as `Primary Health Centre`.
- Output CRS: EPSG:4326.
- Output: `data/processed/my_facilities.gpkg`.

### `my_join.py`

Joins ward population data to the ward polygons using cleaned ward names.

Results:
- Initial match: 9 of 12 wards.
- Match after cleaning: 12 of 12 wards.
- All 12 wards received a population value.

The cleaning function removes leading and trailing spaces, standardises capitalisation and replaces hyphens with spaces.

### `my_map.py`

Combines ward population and health facility data to produce a thematic map.

The map displays:
- Ward polygons shaded by 2024 population.
- Health facilities represented by red points.
- A population colour scale and facility legend.

Output: `my_map.png`.

## 5. How to run the scripts

Run commands from the repository root using the project's Python environment.

Example:

```powershell
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/filter_sort.py
uv run month-03/week-10/explore_layer.py
uv run month-03/week-10/geom_props.py
uv run month-03/week-10/csv_to_points.py
uv run month-03/week-10/join_population.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/save_outputs.py
```

Independent challenge:

```powershell
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
uv run month-03/week-10/my_map.py
```

## 6. Key findings and lessons

The exercises demonstrated how pandas and GeoPandas can be used together to inspect, clean, join and visualise geospatial datasets.

The population join initially matched 9 of 12 wards. After applying consistent name cleaning to both datasets, all 12 wards matched.

The health facility CSV contained 41 records. Standardising `PHC` and `Primary Health Centre` produced a consistent facility category.

The exercises also reinforced the importance of checking geometry types, CRS, spatial bounds and coordinate order before using geospatial data.

## 7. Limitations

The maps produced in this exercise are exploratory outputs rather than final cartographic products. The ward geometry should be independently checked against an authoritative administrative boundary source before using the resulting map for formal spatial analysis.

The EPSG:4326 CRS is geographic and uses angular coordinates. A suitable projected CRS should be selected for any distance or area calculations.

## 8. Conclusion

Week 10 provided practical experience in using pandas and GeoPandas to inspect tabular and vector data, create spatial points, validate geometries, join datasets and produce thematic maps.

Applying the techniques to my Ibadan North project data helped connect the Python exercises to an existing geospatial workflow.