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

            if record["Operation"] != "REDIRECT_TO_CANONICAL":
                continue

            commands.append(
                {
                    "Operation": "REDIRECT_TO_CANONICAL",
                    "File ID": record["File ID"],
                    "File Name": record["File Name"],
                    "Reason": record["Reason"],
                }
            )

        return commands