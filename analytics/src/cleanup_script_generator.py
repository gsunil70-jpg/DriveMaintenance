"""
DriveMaintenance
Cleanup Script Generator
"""


class CleanupScriptGenerator:
    """
    Generates execution instructions.

    No Google Drive operations are performed.
    """

    def __init__(self, execution_plan):

        self.execution_plan = execution_plan

    def generate(self):

        commands = []

        for record in self.execution_plan:

            if record["Operation"] != "MOVE_TO_TRASH":
                continue

            commands.append(
                {
                    "Operation": "MOVE_TO_TRASH",
                    "File ID": record["File ID"],
                    "File Name": record["File Name"],
                    "Reason": record["Reason"],
                }
            )

        return commands