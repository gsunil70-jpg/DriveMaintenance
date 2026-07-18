"""
DriveMaintenance
Recommendation Engine
"""

from analytics.src.canonical_scorer import CanonicalScorer


class RecommendationEngine:

    def __init__(self):

        self.scorer = CanonicalScorer()

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

        #
        # Score every file
        #

        ranked = []

        for file in files:

            ranked.append(

                (
                    self.scorer.score(file),
                    file
                )

            )

        #
        # Highest score first
        #

        ranked.sort(

            key=lambda item: item[0],

            reverse=True

        )

        keep = ranked[0][1]

        review = [

            item[1]

            for item in ranked[1:]

        ]

        #
        # Backup detection
        #

        backup_exists = any(

            (

                f.get(
                    "Inside Backup",
                    ""
                ).upper()

                == "TRUE"

            )

            for _, f in ranked

        )

        #
        # Recommendation
        #

        if backup_exists:

            action = "KEEP_BACKUP_REMOVE_NON_BACKUP"

            reason = (

                "Canonical copy selected "

                "using scoring engine."

            )

        elif len(files) > 1:

            action = "REVIEW"

            reason = (

                "Canonical copy selected "

                "but no backup exists."

            )

        else:

            action = "IGNORE"

            reason = "Single file."

        return {

            "action": action,

            "reason": reason,

            "keep": [

                keep.get("File ID")

            ],

            "review": [

                f.get("File ID")

                for f in review

            ],

            "canonical_score":

                ranked[0][0]

        }