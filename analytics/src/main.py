"""
DriveMaintenance
Analytics Main Runner
"""

from pathlib import Path

from analytics.src.csv_loader import CsvLoader
from analytics.src.repository import DriveIndexRepository

from analytics.src.duplicate_detector import DuplicateDetector
from analytics.src.recommendation_engine import RecommendationEngine
from analytics.src.duplicate_report_writer import DuplicateReportWriter
from analytics.src.action_queue_writer import ActionQueueWriter
from analytics.src.cleanup_decision_resolver import CleanupDecisionResolver
from analytics.src.cleanup_plan_writer import CleanupPlanWriter

from analytics.src.execution_planner import ExecutionPlanner
from analytics.src.execution_manifest_writer import ExecutionManifestWriter
from analytics.src.execution_report_writer import ExecutionReportWriter
from analytics.src.approval_report_writer import ApprovalReportWriter


def main():

    csv_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "DriveIndex_RC2.csv"
    )

    reports_dir = (
        Path(__file__).resolve().parent.parent
        / "reports"
    )

    loader = CsvLoader(csv_file)

    rows = loader.load()

    repository = DriveIndexRepository(rows)

    print()
    print("=" * 60)
    print("REAL DUPLICATE ANALYSIS")
    print("=" * 60)

    detector = DuplicateDetector(repository)

    groups = detector.run()

    engine = RecommendationEngine()

    #
    # Duplicate Review Report
    #

    DuplicateReportWriter(
        reports_dir / "duplicate_review_report.csv"
    ).write(groups)

    #
    # Action Queue
    #

    ActionQueueWriter(
        reports_dir / "action_queue.csv"
    ).write(
        groups,
        engine
    )

    #
    # Cleanup Plan
    #

    resolver = CleanupDecisionResolver()

    cleanup_plan = resolver.resolve(
        groups,
        engine
    )

    CleanupPlanWriter(
        reports_dir / "cleanup_plan.csv"
    ).write(cleanup_plan)

    #
    # Execution Planning
    #

    planner = ExecutionPlanner(
        cleanup_plan
    )

    execution = planner.build()

    ExecutionManifestWriter(
        reports_dir / "execution_manifest.csv"
    ).write(
        execution["execution_plan"]
    )

    ExecutionReportWriter(
        reports_dir / "execution_report.csv"
    ).write(
        execution["validation"]
    )


    ApprovalReportWriter(
        reports_dir / "approval_summary.csv"
    ).write(
        execution
    )

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(
        f"Duplicate Groups : {len(groups)}"
    )

    print(
        f"Cleanup Records  : {len(cleanup_plan)}"
    )

    print(
        f"Execution Records: "
        f"{len(execution['execution_plan'])}"
    )

    print(
        f"Trash Operations : "
        f"{len(execution['cleanup_script'])}"
    )

    print(
        f"Rollback Records : "
        f"{len(execution['rollback'])}"
    )

    print()

    if execution["validation"]["valid"]:

        print(
            "Execution validation : PASSED"
        )

    else:

        print(
            "Execution validation : FAILED"
        )

        for error in execution["validation"]["errors"]:

            print(error)

    print()

    print(
        f"Reports written to:\n{reports_dir}"
    )


if __name__ == "__main__":

    main()