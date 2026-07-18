"""
DriveMaintenance
Confidence Engine
"""


class ConfidenceEngine:
    """
    Assigns confidence to recommendations.

    Score range:
        0 - 100
    """

    def score(
        self,
        backup=False,
        folder_priority=0,
        newest=False,
        checksum=False,
        mirror=False
    ):

        score = 50

        #
        # Exact checksum match
        #

        if checksum:
            score += 20

        #
        # Backup location
        #

        if backup:
            score += 20

        #
        # Preferred folder
        #

        score += max(
            0,
            min(
                folder_priority // 5,
                10
            )
        )

        #
        # Most recent copy
        #

        if newest:
            score += 10

        #
        # Mirror penalty
        #

        if mirror:
            score -= 15

        return max(
            0,
            min(score, 100)
        )