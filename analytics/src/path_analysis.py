"""
DriveMaintenance
Path Analysis
"""

from collections import Counter


class PathAnalyzer:

    def __init__(self, repository):

        self.repository = repository


    def run(self):

        rows = self.repository.rows()

        blank_rows = []

        for row in rows:

            path = (
                row.get("Path") or ""
            ).strip()

            if not path:

                blank_rows.append(row)


        mime_distribution = Counter()

        for row in blank_rows:

            mime = (
                row.get("MIME Type") or ""
            ).strip()

            mime_distribution[mime] += 1


        samples = []

        for row in blank_rows[:20]:

            samples.append(
                {
                    "name": row.get("Name"),
                    "mime": row.get("MIME Type"),
                    "size": row.get("Size"),
                    "id": row.get("File ID")
                }
            )


        return {

            "blank_count": len(blank_rows),

            "mime_distribution": mime_distribution,

            "samples": samples

        }