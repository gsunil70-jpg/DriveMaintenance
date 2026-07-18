"""
DriveMaintenance
Folder Priority Engine
"""


class FolderPriority:
    """
    Scores folder paths.

    Higher score means a better canonical location.
    """

    def score(self, path):

        path = (path or "").lower()

        score = 0

        #
        # Official backup
        #

        if "/backup/" in path:
            score += 100

        #
        # Mirror created by synchronization
        #

        if "gdrive:" in path:
            score -= 40

        #
        # Desktop copies
        #

        if "/desktop/" in path:
            score -= 30

        #
        # Downloads
        #

        if "/downloads/" in path:
            score -= 20

        #
        # Personal archive
        #

        if "/999_personal/" in path:
            score += 20

        #
        # Temporary copies
        #

        if "copy of" in path:
            score -= 15

        #
        # Trash-like folders
        #

        if "/temp/" in path:
            score -= 50

        return score