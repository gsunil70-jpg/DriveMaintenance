"""
DriveMaintenance
Unique Storage Analysis
"""

from collections import defaultdict


class UniqueStorageAnalyzer:

    def __init__(self, repository):

        self.repository = repository


    def run(self):

        rows = self.repository.rows()

        unique_files = {}

        for row in rows:

            file_id = (
                row.get("File ID") or ""
            ).strip()

            if not file_id:

                continue

            if file_id not in unique_files:

                try:

                    size = int(
                        row.get("Size") or 0
                    )

                except ValueError:

                    size = 0


                unique_files[file_id] = {

                    "name": row.get("Name"),

                    "size": size,

                    "mime": row.get("MIME Type")

                }


        total_size = 0

        mime_sizes = defaultdict(int)

        files = []


        for file_id, data in unique_files.items():

            size = data["size"]

            total_size += size

            mime_sizes[data["mime"]] += size


            files.append(
                {
                    "id": file_id,
                    "name": data["name"],
                    "size": size,
                    "mime": data["mime"]
                }
            )


        files.sort(
            key=lambda x: x["size"],
            reverse=True
        )


        return {

            "unique_count": len(unique_files),

            "total_size": total_size,

            "mime_sizes": sorted(
                mime_sizes.items(),
                key=lambda x: x[1],
                reverse=True
            ),

            "top_files": files[:20]

        }