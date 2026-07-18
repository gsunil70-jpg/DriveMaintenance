"""
DriveMaintenance
Safety Rules Engine

Converts cleanup decisions into
safe execution recommendations.

No Drive modification.
"""


from analytics.src.safety_policy import (
    contains_protected_keyword
)



class SafetyRulesEngine:


    def evaluate(self, item):

        file_name = item.get(
            "File Name",
            ""
        )

        decision = item.get(
            "Decision",
            ""
        )

        inside_backup = (
            str(
                item.get(
                    "Inside Backup",
                    ""
                )
            ).upper()
            == "TRUE"
        )


        if contains_protected_keyword(
            file_name
        ):

            return {
                "Safety Level": "BLOCKED",
                "Safety Reason":
                    "Protected keyword detected",
                "Allowed Action":
                    "Manual review"
            }


        if decision == "REVIEW":

            return {
                "Safety Level": "BLOCKED",
                "Safety Reason":
                    "No confirmed safe cleanup path",
                "Allowed Action":
                    "Manual review"
            }


        if (
            decision == "REVIEW_REMOVE"
            and not inside_backup
        ):

            return {
                "Safety Level": "APPROVED_CANDIDATE",
                "Safety Reason":
                    "Backup copy exists",
                "Allowed Action":
                    "Move to trash after approval"
            }


        if decision == "KEEP":

            return {
                "Safety Level": "PROTECTED",
                "Safety Reason":
                    "Backup copy selected",
                "Allowed Action":
                    "Keep"
            }


        return {
            "Safety Level": "REVIEW",
            "Safety Reason":
                "Unknown condition",
            "Allowed Action":
                "Manual review"
        }