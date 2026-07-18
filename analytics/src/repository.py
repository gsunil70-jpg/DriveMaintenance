"""
DriveMaintenance
Drive Index Repository
"""


class DriveIndexRepository:
    """
    Repository over the loaded Drive Index.

    Owns dataset access and normalization.
    """

    def __init__(self, rows):

        self._rows = rows


    def rows(self):

        """
        Return raw rows.
        """

        return self._rows


    def unique_rows(self):

        """
        Remove duplicate index records.

        Google Drive File ID is the identity key.
        """

        seen = set()
        unique = []

        for row in self._rows:

            file_id = row.get("File ID")

            if not file_id:
                continue

            if file_id in seen:
                continue

            seen.add(file_id)
            unique.append(row)

        return unique


    def row_count(self):

        """
        Return raw row count.
        """

        return len(self._rows)


    def unique_row_count(self):

        """
        Return unique file count.
        """

        return len(self.unique_rows())


    def column_names(self):

        """
        Return CSV column names.
        """

        if not self._rows:
            return []

        return list(self._rows[0].keys())