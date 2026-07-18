"""
DriveMaintenance
Analytics Main Runner
"""

from pathlib import Path

from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository
from analytics.src.duplicate_detector import DuplicateDetector
from analytics.src.duplicate_report_writer import DuplicateReportWriter
from analytics.src.recommendation_engine import RecommendationEngine


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


    engine = RecommendationEngine()

    print()

    print("=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)


    for group in groups[:20]:

        recommendation = engine.recommend(group)

        print()

        print(group["key"])

        print(
            recommendation["action"]
        )

        print(
            recommendation["reason"]
        )


    report_file = (
        Path(__file__).resolve().parent.parent
        / "reports"
        / "duplicate_review_report.csv"
    )


    writer = DuplicateReportWriter(
        report_file
    )

    writer.write(groups)


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