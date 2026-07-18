"""
DriveMaintenance
Storage Analysis
"""

from collections import defaultdict


class StorageAnalyzer:

    def __init__(self, repository):

        self.repository = repository


    def run(self):

        rows = self.repository.rows()

        total_size = 0

        mime_sizes = defaultdict(int)

        backup_size = 0

        outside_backup_size = 0

        files = []


        for row in rows:

            try:

                size = int(
                    row.get("Size") or 0
                )

            except ValueError:

                size = 0


            total_size += size


            mime = (
                row.get("MIME Type") or "unknown"
            )

            mime_sizes[mime] += size


            inside = (
                row.get("Inside Backup") or ""
            ).upper()


            if inside == "TRUE":

                backup_size += size

            else:

                outside_backup_size += size


            files.append(
                {
                    "name": row.get("Name"),
                    "size": size,
                    "mime": mime,
                    "id": row.get("File ID")
                }
            )


        files.sort(
            key=lambda x: x["size"],
            reverse=True
        )


        top_files = files[:20]


        top_mime = sorted(
            mime_sizes.items(),
            key=lambda x: x[1],
            reverse=True
        )


        return {

            "total_size": total_size,

            "backup_size": backup_size,

            "outside_backup_size": outside_backup_size,

            "mime_sizes": top_mime,

            "top_files": top_files

        }