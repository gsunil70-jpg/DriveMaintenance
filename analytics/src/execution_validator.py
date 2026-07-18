"""
DriveMaintenance
Execution Validator
"""


class ExecutionValidator:
    """
    Validates the execution plan before any
    Drive operation is permitted.
    """

    ALLOWED_OPERATIONS = {
        "KEEP",
        "MANUAL_REVIEW",
        "REDIRECT_TO_CANONICAL",
    }

    ALLOWED_RESOLUTION_MODES = {
        "KEEP_CANONICAL",
        "MANUAL_REVIEW",
        "REDIRECT_TO_CANONICAL",
        "CONSOLIDATE",
    }

    ALLOWED_REVIEW_STATUS = {
        "PENDING",
        "APPROVED",
        "REJECTED",
        "EXECUTED",
        "FAILED",
    }

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def validate(self):

        errors = []

        seen_ids = set()

        for index, record in enumerate(
            self.execution_plan,
            start=1,
        ):

            file_id = (
                record.get("File ID") or ""
            ).strip()

            operation = (
                record.get("Operation") or ""
            ).strip()

            resolution = (
                record.get(
                    "Resolution Mode",
                    ""
                ) or ""
            ).strip()

            review_status = (
                record.get(
                    "Review Status",
                    "PENDING"
                ) or ""
            ).strip()

            canonical_id = (
                record.get(
                    "Canonical File ID",
                    ""
                ) or ""
            ).strip()

            canonical_path = (
                record.get(
                    "Canonical Path",
                    ""
                ) or ""
            ).strip()

            #
            # File ID
            #

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

            #
            # Operation
            #

            if operation not in self.ALLOWED_OPERATIONS:

                errors.append(
                    f"Row {index}: Invalid operation '{operation}'."
                )

            #
            # Resolution Mode
            #

            if resolution not in self.ALLOWED_RESOLUTION_MODES:

                errors.append(
                    f"Row {index}: Invalid resolution mode '{resolution}'."
                )

            #
            # Review Status
            #

            if review_status not in self.ALLOWED_REVIEW_STATUS:

                errors.append(
                    f"Row {index}: Invalid review status '{review_status}'."
                )

            #
            # KEEP
            #

            if operation == "KEEP":

                if canonical_id:

                    errors.append(
                        f"Row {index}: KEEP should not reference Canonical File ID."
                    )

                if canonical_path:

                    errors.append(
                        f"Row {index}: KEEP should not reference Canonical Path."
                    )

            #
            # REDIRECT
            #

            if operation == "REDIRECT_TO_CANONICAL":

                if not canonical_id:

                    errors.append(
                        f"Row {index}: Missing Canonical File ID."
                    )

                if not canonical_path:

                    errors.append(
                        f"Row {index}: Missing Canonical Path."
                    )

                if canonical_id == file_id:

                    errors.append(
                        f"Row {index}: Canonical File ID equals File ID."
                    )

                if resolution != "REDIRECT_TO_CANONICAL":

                    errors.append(
                        f"Row {index}: Resolution Mode mismatch."
                    )

            #
            # MANUAL REVIEW
            #

            if operation == "MANUAL_REVIEW":

                if resolution != "MANUAL_REVIEW":

                    errors.append(
                        f"Row {index}: Manual review resolution mismatch."
                    )

        return {

            "valid":

                len(errors) == 0,

            "errors":

                errors,

            "record_count":

                len(self.execution_plan),

        }