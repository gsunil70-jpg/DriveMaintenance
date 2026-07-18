"""
DriveMaintenance
Analytics Main Runner
"""

from pathlib import Path

from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository
from analytics.src.duplicate_detector import DuplicateDetector


def main():

    csv_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "DriveIndex_RC2.csv"
    )

    loader = CsvLoader(csv_file)

    rows = loader.load()

    repository = DriveIndexRepository(rows)

    print()

    print("=" * 60)
    print("REAL DUPLICATE ANALYSIS")
    print("=" * 60)

    detector = DuplicateDetector(
        repository
    )

    groups = detector.run()

    print()

    print(
        f"Duplicate Groups : {len(groups)}"
    )

    print()

    for group in groups[:20]:

        print("-" * 60)

        print(
            f"Copies: {group['count']}"
        )

        seen_ids = set()

        for file in group["files"]:

            file_id = file.get("File ID")

            if file_id in seen_ids:
                continue

            seen_ids.add(file_id)

            print(
                f"{file.get('Name')} | "
                f"{file.get('Size')} | "
                f"{file_id}"
            )


if __name__ == "__main__":

    main()