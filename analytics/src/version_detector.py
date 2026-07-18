"""
DriveMaintenance
Version Detector
"""

import re


class VersionDetector:
    """
    Estimates version quality from filenames.

    Higher score = preferred version.
    """

    def score(self, filename):

        name = (filename or "").lower()

        score = 0

        #
        # Penalize copied files
        #

        if name.startswith("copy of"):
            score -= 30

        #
        # Version indicators
        #

        if re.search(r"v\d+", name):
            score += 10

        #
        # Final
        #

        if "final" in name:
            score += 20

        #
        # Draft
        #

        if "draft" in name:
            score -= 15

        #
        # Temporary
        #

        if "temp" in name:
            score -= 20

        #
        # Old
        #

        if "old" in name:
            score -= 15

        return score