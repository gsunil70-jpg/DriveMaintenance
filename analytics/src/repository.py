"""
DriveMaintenance
Drive Index Repository
"""


class DriveIndexRepository:
    """
    Repository over the loaded Drive Index.

    This class owns the dataset and provides
    common access methods used by all analytics.
    """

    def __init__(self, rows):

        self._rows = rows

    def rows(self):

        """
        Return all rows.
        """

        return self._rows

    def row_count(self):

        """
        Return total number of rows.
        """

        return len(self._rows)

    def column_names(self):

        """
        Return CSV column names.
        """

        if not self._rows:

            return []

        return list(self._rows[0].keys())