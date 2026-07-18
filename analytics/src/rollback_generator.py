"""
DriveMaintenance
Rollback Generator
"""


class RollbackGenerator:
    """
    Generates rollback information for every
    execution operation that modifies Drive.

    Produces enough information for auditing
    and future recovery.
    """

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def generate(self):

        rollback = []

        for record in self.execution_plan:

            if record["Operation"] != "REDIRECT_TO_CANONICAL":
                continue

            rollback.append(

                {

                    "Operation":

                        record["Operation"],

                    "Resolution Mode":

                        record.get(
                            "Resolution Mode",
                            ""
                        ),

                    "File ID":

                        record["File ID"],

                    "File Name":

                        record["File Name"],

                    "Original Path":

                        record["Path"],

                    "Canonical File ID":

                        record.get(
                            "Canonical File ID",
                            ""
                        ),

                    "Canonical File Name":

                        record.get(
                            "Canonical File Name",
                            ""
                        ),

                    "Canonical Path":

                        record.get(
                            "Canonical Path",
                            ""
                        ),

                    "Reason":

                        record.get(
                            "Reason",
                            ""
                        )

                }

            )

        return rollback