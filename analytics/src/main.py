"""
DriveMaintenance
Analytics
"""

from analytics.src.constants import CSV_FILE
from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository


def main():

    loader = CsvLoader(CSV_FILE)

    rows = loader.load()

    repository = DriveIndexRepository(rows)

    print()

    print("=" * 40)
    print("Repository Summary")
    print("=" * 40)

    print(f"Rows    : {repository.row_count():,}")
    print(f"Columns : {len(repository.column_names())}")

    print()
    print(repository.column_names())


if __name__ == "__main__":

    main()