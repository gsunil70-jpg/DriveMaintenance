"""
DriveMaintenance
Execution Validator
"""


class ExecutionValidator:
    """
    Validates the complete execution batch before
    any execution artifacts are produced.
    """

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def validate(self):

        errors = []

        seen_ids = set()

        allowed_operations = {
            "KEEP",
            "MANUAL_REVIEW",
            "MOVE_TO_TRASH",
        }

        for index, record in enumerate(
            self.execution_plan,
            start=1,
        ):

            file_id = (
                record.get("File ID") or ""
            ).strip()

            operation = record.get(
                "Operation",
                ""
            )

            if not file_id:

                errors.append(
                    f"Row {index}: Missing File ID."
                )

            elif file_id in seen_ids:

                errors.append(
                    f"Duplicate File ID: {file_id}"
                )

            else:

                seen_ids.add(file_id)

            if operation not in allowed_operations:

                errors.append(
                    f"Invalid operation '{operation}' "
                    f"for {file_id}"
                )

        return {

            "valid": len(errors) == 0,

            "errors": errors,

            "record_count": len(
                self.execution_plan
            ),

        }