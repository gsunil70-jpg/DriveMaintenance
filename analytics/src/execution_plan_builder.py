"""
DriveMaintenance
Execution Plan Builder
"""


class ExecutionPlanBuilder:
    """
    Converts cleanup decisions into executable operations.

    Produces the canonical execution plan used by
    validation, reporting and execution.
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

                operation = "REDIRECT_TO_CANONICAL"

            else:

                operation = "UNKNOWN"

            #
            # Canonical reference policy
            #

            if operation == "KEEP":

                canonical_file_id = ""
                canonical_file_name = ""
                canonical_path = ""

            else:

                canonical_file_id = record.get(
                    "Canonical File ID",
                    ""
                )

                canonical_file_name = record.get(
                    "Canonical File Name",
                    ""
                )

                canonical_path = record.get(
                    "Canonical Path",
                    ""
                )

            plan.append(

                {

                    "Review Status":

                        "PENDING",

                    "Operation":

                        operation,

                    "Resolution Mode":

                        record.get(
                            "Resolution Mode",
                            ""
                        ),

                    "File ID":

                        record["File ID"],

                    "File Name":

                        record["File Name"],

                    "Path":

                        record["Path"],

                    "Reason":

                        record["Reason"],

                    #
                    # Canonical reference
                    #

                    "Canonical File ID":

                        canonical_file_id,

                    "Canonical File Name":

                        canonical_file_name,

                    "Canonical Path":

                        canonical_path,

                }

            )

        return plan