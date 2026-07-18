"""
DriveMaintenance
Duplicate Report Writer

Creates a CSV review report from duplicate candidates.

No deletion.
No Drive modification.
Review only.
"""

import csv
from pathlib import Path


class DuplicateReportWriter:
    """
    Writes duplicate detection results
    into a human reviewable CSV file.
    """

    def __init__(self, output_file: Path):

        self.output_file = output_file


    def write(self, duplicate_groups):

        self.output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        headers = [
            "Group Key",
            "Detection Rule",
            "File Name",
            "Size",
            "File ID",
            "Path",
            "Inside Backup",
            "Modified"
        ]


        rows = []


        for group in duplicate_groups:

            key = group.get("key")

            rule = key[0] if key else ""


            for file in group.get("files", []):

                rows.append(
                    [
                        str(key),
                        rule,
                        file.get("Name", ""),
                        file.get("Size", ""),
                        file.get("File ID", ""),
                        file.get("Path", ""),
                        file.get("Inside Backup", ""),
                        file.get("Modified", "")
                    ]
                )


        with open(
            self.output_file,
            "w",
            encoding="utf-8",
            newline=""
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(headers)

            writer.writerows(rows)


        print(
            "\nDuplicate report written:"
        )

        print(
            self.output_file
        )