
"""
Convert every facility CSV in a folder into a GeoPackage of points.

Run from the repository root:
    uv run month-03/week-13/batch_convert.py
"""

import logging
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd


# ============================================================
# SETTINGS
# ============================================================

INPUT_FOLDER = Path("data/raw/lga_facilities")
OUTPUT_FOLDER = Path("data/processed/lga_points")

SUMMARY_FILE = Path("month-03/week-13/batch_summary.csv")
LOG_FILE = Path("month-03/week-13/batch_run.log")

WORKING_CRS = "EPSG:32631"
OVERWRITE = False


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyogrio").setLevel(logging.WARNING)


# ============================================================
# FUNCTIONS
# ============================================================

def csv_to_points(csv_path):
    """Read a facility CSV, standardise columns and create point geometries."""

    table = pd.read_csv(csv_path)

    # Standardise inconsistent column names without editing source CSVs
    table = table.rename(
        columns={
            "lat": "latitude",
            "lon": "longitude",
            "facility": "name"
        }
    )

    # Check that the required coordinate columns exist
    missing = {"latitude", "longitude"} - set(table.columns)

    if missing:
        raise ValueError(
            f"missing columns: {sorted(missing)}"
        )

    # Convert coordinates to numeric values
    table["latitude"] = pd.to_numeric(
        table["latitude"],
        errors="raise"
    )

    table["longitude"] = pd.to_numeric(
        table["longitude"],
        errors="raise"
    )

    # Create point geometries in WGS 84
    points = gpd.GeoDataFrame(
        table,
        geometry=gpd.points_from_xy(
            table["longitude"],
            table["latitude"]
        ),
        crs="EPSG:4326"
    )

    # Reproject to the project's metric CRS
    return points.to_crs(WORKING_CRS)


def process_one(csv_path):
    """Convert one CSV file into a GeoPackage."""

    out_path = OUTPUT_FOLDER / f"{csv_path.stem}.gpkg"

    # Avoid overwriting existing outputs
    if out_path.exists() and not OVERWRITE:
        logging.info(
            "Skipping %s, output already exists",
            csv_path.name
        )

        return {
            "file": csv_path.name,
            "status": "skipped",
            "points": None
        }

    points = csv_to_points(csv_path)

    points.to_file(
        out_path,
        layer="facilities",
        driver="GPKG"
    )

    logging.info(
        "Converted %s: %d points",
        csv_path.name,
        len(points)
    )

    return {
        "file": csv_path.name,
        "status": "done",
        "points": len(points)
    }


def main():
    """Process all CSV files and save a batch summary."""

    start = time.perf_counter()

    # Ensure the output directory exists
    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    results = []

    # Process CSV files in alphabetical order
    for csv_path in sorted(INPUT_FOLDER.glob("*.csv")):

        try:
            result = process_one(csv_path)
            results.append(result)

        except Exception as error:
            logging.error(
                "Failed on %s: %s",
                csv_path.name,
                error
            )

            results.append(
                {
                    "file": csv_path.name,
                    "status": "failed",
                    "points": None
                }
            )

    # Create the batch summary
    summary = pd.DataFrame(results)

    # Use nullable integers so failed and skipped files remain <NA>
    summary["points"] = summary["points"].astype("Int64")

    summary.to_csv(
        SUMMARY_FILE,
        index=False
    )

    elapsed = time.perf_counter() - start

    logging.info(
        "Finished %d files in %.1f seconds",
        len(results),
        elapsed
    )

    print(summary)


# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
