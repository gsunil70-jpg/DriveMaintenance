"""
DriveMaintenance
Audit Engine
"""

from collections import Counter


class AuditEngine:
    """
    Computes statistics for the Drive Index.
    """

    def __init__(self, repository):

        self.repository = repository

    def run(self):

        rows = self.repository.rows()

        file_ids = []
        blank_paths = 0
        blank_names = 0
        blank_mime = 0
        blank_sizes = 0
        inside_backup = 0
        outside_backup = 0

        for row in rows:

            file_id = (row.get("File ID") or "").strip()

            if file_id:
                file_ids.append(file_id)

            if not (row.get("Path") or "").strip():
                blank_paths += 1

            if not (row.get("Name") or "").strip():
                blank_names += 1

            if not (row.get("MIME Type") or "").strip():
                blank_mime += 1

            if not (row.get("Size") or "").strip():
                blank_sizes += 1

            inside = (row.get("Inside Backup") or "").strip().lower()

            if inside == "true":
                inside_backup += 1
            else:
                outside_backup += 1

        counter = Counter(file_ids)

        duplicate_file_ids = sum(
            1 for count in counter.values()
            if count > 1
        )

        duplicate_rows = sum(
            count - 1
            for count in counter.values()
            if count > 1
        )

        return {

            "rows": len(rows),

            "unique_file_ids": len(counter),

            "duplicate_file_ids": duplicate_file_ids,

            "duplicate_rows": duplicate_rows,

            "blank_paths": blank_paths,

            "blank_names": blank_names,

            "blank_mime_types": blank_mime,

            "blank_sizes": blank_sizes,

            "inside_backup": inside_backup,

            "outside_backup": outside_backup

        }