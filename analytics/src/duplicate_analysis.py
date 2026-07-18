"""
DriveMaintenance
Duplicate Analysis
"""

from collections import Counter


class DuplicateAnalyzer:

    def __init__(self, repository):

        self.repository = repository

    def run(self):

        rows = self.repository.rows()

        file_ids = []

        for row in rows:

            file_id = (row.get("File ID") or "").strip()

            if file_id:

                file_ids.append(file_id)

        counts = Counter(file_ids)

        distribution = Counter(counts.values())

        maximum = max(counts.values())

        average = len(file_ids) / len(counts)

        top20 = counts.most_common(20)

        return {

            "unique": len(counts),

            "maximum": maximum,

            "average": average,

            "distribution": distribution,

            "top20": top20

        }