
import csv


def read_rows(filename):
    with open(filename, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def clean_values(rows, column):
    values = []

    for row in rows:
        raw = row[column].strip()

        if raw == "" or raw.upper() == "NA":
            continue

        try:
            values.append(float(raw.replace(",", "")))
        except ValueError:
            continue

    return values


def summarise(values):
    if len(values) == 0:
        return {
            "count": 0,
            "smallest": None,
            "largest": None,
            "average": None,
        }

    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }


def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}

    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)

    return report


if __name__ == "__main__":
    report = summarise_all(
        "ibadan_north_analysis.csv",
        ["distance", "block_area_sqm"],
    )

    for column, stats in report.items():
        print(column, "->", stats)
