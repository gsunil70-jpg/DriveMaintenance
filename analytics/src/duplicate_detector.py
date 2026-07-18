"""
DriveMaintenance
Real Duplicate Detector

Detects possible true duplicates.

Rules:
1. Same File ID repeated = index duplication (ignored)
2. Different File IDs:
      - same checksum OR
      - same name + size
   = duplicate candidate

Analysis only.
No deletion.
"""

from collections import defaultdict


class DuplicateDetector:

    def __init__(self, repository):
        self.repository = repository


    def run(self):
        return self.analyze()


    def analyze(self):

        groups = defaultdict(list)

        files = self.repository.unique_rows()


        for file in files:

            file_id = file.get("File ID")
            name = file.get("Name", "")
            size = file.get("Size", "")
            checksum = file.get("Checksum", "")


            if checksum:

                key = (
                    "CHECKSUM",
                    checksum
                )

            else:

                key = (
                    "NAME_SIZE",
                    name,
                    size
                )


            groups[key].append(file)



        duplicates = []


        for key, items in groups.items():

            unique_ids = {
                item.get("File ID")
                for item in items
            }


            # Ignore repeated index entries
            if len(unique_ids) <= 1:
                continue


            duplicates.append(
                {
                    "key": key,
                    "count": len(unique_ids),
                    "files": items
                }
            )


        return duplicates