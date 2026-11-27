
"""
Batch reproject GeoPackage datasets to a common projected CRS.

The script processes every GeoPackage in data/processed,
saves reprojected copies in data/processed/reprojected,
skips existing outputs unless OVERWRITE is enabled,
and records processing results in a CSV summary and log file.

Run from the repository root:
    uv run month-03/week-13/my_batch.py
"""

import logging
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd


# ============================================================
# SETTINGS
# ============================================================

INPUT_FOLDER = Path("data/processed")
OUTPUT_FOLDER = Path("data/processed/reprojected")

SUMMARY_FILE = Path("month-03/week-13/my_batch_summary.csv")
LOG_FILE = Path("month-03/week-13/my_batch_run.log")

TARGET_CRS = "EPSG:32631"
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

def validate_layer(layer, layer_name):
    """
    Validate that a GeoDataFrame has a CRS and contains features.

    Parameters
    ----------
    layer : GeoDataFrame
        Spatial dataset to validate.
    layer_name : str
        Name used in validation messages.
    """

    if layer.crs is None:
        raise ValueError(f"Missing CRS: {layer_name}")

    if layer.empty:
        raise ValueError(
            f"Dataset contains no features: {layer_name}"
        )


def reproject_layer(input_path):
    """
    Read a GeoPackage and reproject it to the target CRS.

    Parameters
    ----------
    input_path : Path
        Path to the input GeoPackage.

    Returns
    -------
    tuple
        Reprojected GeoDataFrame and original CRS.
    """

    layer = gpd.read_file(input_path)

    validate_layer(layer, input_path.name)

    source_crs = layer.crs.to_string()

    if layer.crs.to_string() == TARGET_CRS:
        logging.info(
            "%s is already in %s",
            input_path.name,
            TARGET_CRS
        )
        return layer, source_crs

    reprojected = layer.to_crs(TARGET_CRS)

    return reprojected, source_crs


def process_one(input_path):
    """
    Reproject one GeoPackage and save the output.

    Parameters
    ----------
    input_path : Path
        Path to the input GeoPackage.

    Returns
    -------
    dict
        Processing details for the batch summary.
    """

    output_path = OUTPUT_FOLDER / input_path.name

    if output_path.exists() and not OVERWRITE:
        logging.info(
            "Skipping %s, output already exists",
            input_path.name
        )

        return {
            "file": input_path.name,
            "status": "skipped",
            "features": None,
            "source_crs": None,
            "output_crs": None
        }

    layer, source_crs = reproject_layer(input_path)

    layer.to_file(
        output_path,
        driver="GPKG"
    )

    # Reopen the saved file to validate the actual output.
    saved_layer = gpd.read_file(output_path)

    validate_layer(saved_layer, output_path.name)

    output_crs = saved_layer.crs.to_string()

    if output_crs != TARGET_CRS:
        raise ValueError(
            f"CRS validation failed for {input_path.name}: "
            f"expected {TARGET_CRS}, found {output_crs}"
        )

    logging.info(
        "Reprojected %s: %d features, %s to %s",
        input_path.name,
        len(saved_layer),
        source_crs,
        output_crs
    )

    return {
        "file": input_path.name,
        "status": "done",
        "features": len(saved_layer),
        "source_crs": source_crs,
        "output_crs": output_crs
    }


# ============================================================
# DELIBERATE FAILURE TEST
# ============================================================

def test_missing_crs():
    """
    Test how the validation function handles a dataset without a CRS.
    """

    test_data = gpd.GeoDataFrame(
        {"facility": ["Test Facility"]},
        geometry=gpd.points_from_xy(
            [3.9],
            [7.4]
        )
    )

    try:
        validate_layer(
            test_data,
            "deliberate_test_dataset"
        )

    except ValueError as error:
        logging.warning(
            "Deliberate failure test: %s",
            error
        )


# ============================================================
# MAIN BATCH PROCESS
# ============================================================

def main():
    """Process all GeoPackages and create a batch summary."""

    start = time.perf_counter()

    if not INPUT_FOLDER.exists():
        raise FileNotFoundError(
            f"Input folder does not exist: {INPUT_FOLDER}"
        )

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    SUMMARY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    results = []

    input_files = sorted(
        INPUT_FOLDER.glob("*.gpkg")
    )

    logging.info(
        "Found %d GeoPackage files",
        len(input_files)
    )

    for input_path in input_files:

        try:
            result = process_one(input_path)
            results.append(result)

        except Exception as error:
            logging.error(
                "Failed on %s: %s",
                input_path.name,
                error
            )

            results.append({
                "file": input_path.name,
                "status": "failed",
                "features": None,
                "source_crs": None,
                "output_crs": None
            })

    summary = pd.DataFrame(results)

    summary["features"] = summary["features"].astype("Int64")

    summary.to_csv(
        SUMMARY_FILE,
        index=False
    )

    elapsed = time.perf_counter() - start

    logging.info(
        "Finished %d files in %.2f seconds",
        len(results),
        elapsed
    )

    print("\nBATCH PROCESSING SUMMARY")
    print(summary.to_string(index=False))


# ============================================================
# SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()

    test_missing_crs()
