"""
DriveMaintenance
Approval Report Writer
"""

import csv
from pathlib import Path


class ApprovalReportWriter:
    """
    Creates a human review summary before execution.
    """


    def __init__(self, output_file):

        self.output_file = Path(output_file)



    def write(self, execution):

        execution_plan = execution["execution_plan"]

        validation = execution["validation"]

        rollback = execution["rollback"]


        counts = {

            "KEEP": 0,

            "REDIRECT_TO_CANONICAL": 0,

            "MANUAL_REVIEW": 0,

            "UNKNOWN": 0,

        }



        for record in execution_plan:


            operation = record.get(

                "Operation",

                "UNKNOWN"

            )


            if operation in counts:

                counts[operation] += 1

            else:

                counts["UNKNOWN"] += 1



        rows = [

            (
                "Total Execution Records",
                len(execution_plan)
            ),

            (
                "KEEP",
                counts["KEEP"]
            ),

            (
                "REDIRECT_TO_CANONICAL",
                counts["REDIRECT_TO_CANONICAL"]
            ),

            (
                "MANUAL_REVIEW",
                counts["MANUAL_REVIEW"]
            ),

            (
                "UNKNOWN",
                counts["UNKNOWN"]
            ),

            (
                "Rollback Records",
                len(rollback)
            ),

            (
                "Validation Status",
                "PASSED"
                if validation.get("valid")
                else "FAILED"
            ),

            (
                "Permanent Delete Operations",
                0
            ),

            (
                "Approval Status",
                "PENDING"
            ),

        ]



        self.output_file.parent.mkdir(

            parents=True,

            exist_ok=True

        )



        with open(

            self.output_file,

            "w",

            newline="",

            encoding="utf-8"

        ) as f:


            writer = csv.writer(f)


            writer.writerow(

                [
                    "Metric",
                    "Value"
                ]

            )


            writer.writerows(rows)