"""
DriveMaintenance
Recommendation Engine

Converts duplicate groups into
safe cleanup recommendations.

No file operations.
No deletion.
Analysis only.
"""


class RecommendationEngine:

    def __init__(self):
        pass


    def recommend(self, duplicate_group):

        files = duplicate_group.get(
            "files",
            []
        )

        if not files:

            return {
                "action": "IGNORE",
                "reason": "No files found"
            }


        backup_files = []
        normal_files = []


        for file in files:

            inside_backup = (
                file.get("Inside Backup", "")
                .upper()
                == "TRUE"
            )

            if inside_backup:

                backup_files.append(file)

            else:

                normal_files.append(file)



        # Case 1:
        # Backup copy exists
        if backup_files and normal_files:

            return {

                "action":
                    "KEEP_BACKUP_REMOVE_NON_BACKUP",

                "reason":
                    "Backup copy exists; "
                    "non-backup duplicate requires review",

                "keep":
                    [
                        f.get("File ID")
                        for f in backup_files
                    ],

                "review":
                    [
                        f.get("File ID")
                        for f in normal_files
                    ]

            }



        # Case 2:
        # Multiple copies but no backup
        if len(files) > 1:

            return {

                "action":
                    "REVIEW",

                "reason":
                    "Multiple copies exist but "
                    "no backup copy identified"

            }



        # Case 3:
        # Nothing actionable

        return {

            "action":
                "IGNORE",

            "reason":
                "No cleanup recommendation"

        }