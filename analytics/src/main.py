"""
DriveMaintenance
Unique Storage Runner
"""

from analytics.src.constants import CSV_FILE
from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository
from analytics.src.unique_storage_analysis import UniqueStorageAnalyzer


def main():

    loader = CsvLoader(CSV_FILE)

    rows = loader.load()

    repository = DriveIndexRepository(rows)

    analyzer = UniqueStorageAnalyzer(repository)

    result = analyzer.run()


    print()

    print("=" * 60)
    print("UNIQUE STORAGE ANALYSIS")
    print("=" * 60)


    print()

    print(
        f"Unique Files : {result['unique_count']:,}"
    )

    print(
        f"True Size MB : {result['total_size']/1024/1024:,.2f}"
    )


    print()

    print("Top MIME Types")

    for mime, size in result["mime_sizes"][:15]:

        print(
            f"{size/1024/1024:>12,.2f} MB  {mime}"
        )


    print()

    print("Largest Unique Files")


    for item in result["top_files"]:

        print(
            f"{item['size']/1024/1024:>10,.2f} MB  {item['name']}"
        )


if __name__ == "__main__":

    main()