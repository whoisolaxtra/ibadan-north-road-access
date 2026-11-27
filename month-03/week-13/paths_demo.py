
from pathlib import Path

# Locate the folder containing the LGA facility CSV files
folder = Path("data/raw/lga_facilities")

print("Folder exists:", folder.exists())

# List all CSV files in alphabetical order
for path in sorted(folder.glob("*.csv")):
    print(
        path.name,
        "| stem:", path.stem,
        "| suffix:", path.suffix
    )

# Create the output folder
output = Path("data/processed") / "lga_points"
output.mkdir(parents=True, exist_ok=True)

print("Output folder ready:", output)
