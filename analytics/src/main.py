"""
DriveMaintenance
Path Analysis Runner
"""

from analytics.src.constants import CSV_FILE
from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository
from analytics.src.path_analysis import PathAnalyzer


def main():

    loader = CsvLoader(CSV_FILE)

    rows = loader.load()

    repository = DriveIndexRepository(rows)

    analyzer = PathAnalyzer(repository)

    result = analyzer.run()

    print()

    print("=" * 50)
    print("BLANK PATH ANALYSIS")
    print("=" * 50)

    print(
        f"Blank Paths : {result['blank_count']:,}"
    )

    print()

    print("MIME Distribution")

    for mime, count in result["mime_distribution"].items():

        print(
            f"{count:>8,}  {mime}"
        )

    print()

    print("Sample Files")

    for item in result["samples"]:

        print(item)


if __name__ == "__main__":

    main()