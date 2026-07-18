"""
DriveMaintenance
Duplicate Timeline Analysis
"""

from collections import defaultdict


class DuplicateTimelineAnalyzer:

    def __init__(self, repository):

        self.repository = repository

    def run(self, limit=10):

        rows = self.repository.rows()

        occurrences = defaultdict(list)

        for index, row in enumerate(rows, start=1):

            file_id = (
                row.get("File ID") or ""
            ).strip()

            if file_id:

                occurrences[file_id].append(index)

        duplicated = {
            file_id: positions
            for file_id, positions in occurrences.items()
            if len(positions) > 1
        }

        result = []

        for file_id, positions in duplicated.items():

            gaps = []

            for i in range(1, len(positions)):

                gaps.append(
                    positions[i] - positions[i-1]
                )

            result.append(
                {
                    "file_id": file_id,
                    "copies": len(positions),
                    "positions": positions,
                    "gaps": gaps
                }
            )

        result.sort(
            key=lambda x: x["copies"],
            reverse=True
        )

        return result[:limit]