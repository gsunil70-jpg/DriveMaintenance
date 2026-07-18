"""
DriveMaintenance
Canonical Scorer
"""

from analytics.src.folder_priority import FolderPriority
from analytics.src.version_detector import VersionDetector

from analytics.src.constants import (
    BACKUP_BONUS,
    MIRROR_PENALTY,
    VERSION_WEIGHT,
    FOLDER_WEIGHT,
)


class CanonicalScorer:
    """
    Produces one overall score
    for every duplicate candidate.
    """

    def __init__(self):

        self.folder = FolderPriority()
        self.version = VersionDetector()

    def score(self, file):

        score = 0

        #
        # Folder quality
        #

        score += (
            self.folder.score(
                file.get("Path", "")
            )
            * FOLDER_WEIGHT
        )

        #
        # Filename quality
        #

        score += (
            self.version.score(
                file.get("File Name", "")
            )
            * VERSION_WEIGHT
        )

        #
        # Backup bonus
        #

        if (
            file.get(
                "Inside Backup",
                ""
            ).upper()
            == "TRUE"
        ):

            score += BACKUP_BONUS

        #
        # Mirror penalty
        #

        path = (
            file.get("Path", "")
            .lower()
        )

        if "gdrive:" in path:

            score -= MIRROR_PENALTY

        return score