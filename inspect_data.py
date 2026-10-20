
import csv
from pathlib import Path
from statistics import mean

DATA_FILE = Path("ibadan_north_analysis.csv")


def read_data(file_path):
    """Read settlement records from a CSV file."""
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return rows


def numeric_values(rows, column):
    """Return valid numeric values, skipping empty or invalid cells."""
    values = []

    for row in rows:
        raw_value = row.get(column, "").strip()

        if not raw_value:
            continue

        try:
            values.append(float(raw_value))
        except ValueError:
            continue

    return values


def summarise(rows, column, label):
    values = numeric_values(rows, column)

    print(f"\n{label}")
    print("-" * len(label))

    if not values:
        print("No valid numeric values found.")
        return

    print(f"Valid records: {len(values)}")
    print(f"Missing or invalid records: {len(rows) - len(values)}")
    print(f"Minimum: {min(values):,.2f}")
    print(f"Maximum: {max(values):,.2f}")
    print(f"Mean: {mean(values):,.2f}")


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_FILE}. "
            "Place the CSV beside this script."
        )

    rows = read_data(DATA_FILE)

    print("IBADAN NORTH SETTLEMENT DATA INSPECTION")
    print("=" * 40)
    print(f"Dataset: {DATA_FILE}")
    print(f"Total records: {len(rows)}")

    if rows:
        print(f"Available columns: {', '.join(rows[0].keys())}")

    summarise(rows, "distance", "Nearest mapped road distance (m)")
    summarise(rows, "block_area_sqm", "Settlement block area (m²)")


if __name__ == "__main__":
    main()
