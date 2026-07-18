"""
DriveMaintenance
Execution Plan Builder
"""


class ExecutionPlanBuilder:
    """
    Converts cleanup decisions into executable operations.
    """

    def __init__(self, cleanup_plan):

        self.cleanup_plan = cleanup_plan

    def build(self):

        plan = []

        for record in self.cleanup_plan:

            decision = record["Decision"]

            if decision == "KEEP":
                operation = "KEEP"

            elif decision == "REVIEW":
                operation = "MANUAL_REVIEW"

            elif decision == "REVIEW_REMOVE":
                operation = "MOVE_TO_TRASH"

            else:
                operation = "UNKNOWN"

            plan.append(
                {
                    "Operation": operation,
                    "File ID": record["File ID"],
                    "File Name": record["File Name"],
                    "Path": record["Path"],
                    "Reason": record["Reason"],
                }
            )

        return plan