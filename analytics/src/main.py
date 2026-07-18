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
from analytics.src.action_queue_writer import ActionQueueWriter
from analytics.src.cleanup_decision_resolver import CleanupDecisionResolver
from analytics.src.cleanup_plan_writer import CleanupPlanWriter



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


    resolver = CleanupDecisionResolver()

    cleanup_plan = resolver.resolve(
        groups,
        engine
    )


    cleanup_file = (
        Path(__file__).resolve().parent.parent
        / "reports"
        / "cleanup_plan.csv"
    )


    cleanup_writer = CleanupPlanWriter(
        cleanup_file
    )

    cleanup_writer.write(
        cleanup_plan
    )


    print()

    print("=" * 60)
    print("CLEANUP PLAN")
    print("=" * 60)

    print(
        f"Plan Records : {len(cleanup_plan)}"
    )

    print(
        f"Output       : {cleanup_file}"
    )


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


    report_writer = DuplicateReportWriter(
        report_file
    )

    report_writer.write(
        groups
    )


    action_queue_file = (
        Path(__file__).resolve().parent.parent
        / "reports"
        / "action_queue.csv"
    )


    queue_writer = ActionQueueWriter(
        action_queue_file
    )


    queue_writer.write(
        groups,
        engine
    )


    print()

    print(
        f"Action queue created: {action_queue_file}"
    )


    print()

    print(
        f"Duplicate Groups : {len(groups)}"
    )


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