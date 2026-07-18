"""
DriveMaintenance
Rollback Generator
"""


class RollbackGenerator:
    """
    Generates rollback information for every
    planned destructive operation.
    """

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def generate(self):

        rollback = []

        for record in self.execution_plan:

            if record["Operation"] != "MOVE_TO_TRASH":
                continue

            rollback.append(
                {
                    "File ID": record["File ID"],
                    "File Name": record["File Name"],
                    "Original Path": record["Path"],
                }
            )

        return rollback