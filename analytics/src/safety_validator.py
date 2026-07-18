"""
DriveMaintenance
Safety Validator
"""


class SafetyValidator:
    """
    Applies hard safety rules before execution.

    Returns a validated execution plan.
    """

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def validate(self):

        validated = []

        for record in self.execution_plan:

            operation = record["Operation"]
            path = (record["Path"] or "").lower()

            safe = True
            message = "OK"

            #
            # Never delete anything inside Backup
            #
            if (
                operation == "MOVE_TO_TRASH"
                and "/backup/" in path
            ):

                safe = False
                message = (
                    "Backup copy cannot be deleted."
                )

            #
            # Unknown operations are never allowed
            #
            if operation == "UNKNOWN":

                safe = False
                message = (
                    "Unknown operation."
                )

            validated.append(
                {
                    **record,
                    "Safe": safe,
                    "Validation": message,
                }
            )

        return validated