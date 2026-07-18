"""
DriveMaintenance
Action Queue Writer

Creates a human-reviewable cleanup queue.

No Drive modification.
No deletion.
"""

import csv
from pathlib import Path


class ActionQueueWriter:

    def __init__(self, output_file: Path):

        self.output_file = output_file


    def write(self, groups, engine):

        self.output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        rows = []


        action_id = 1


        for group in groups:

            recommendation = engine.recommend(group)


            for file in group["files"]:

                rows.append(
                    {
                        "Action ID": f"A{action_id:04d}",
                        "Action": recommendation["action"],
                        "Reason": recommendation["reason"],
                        "File Name": file.get("Name"),
                        "File ID": file.get("File ID"),
                        "Path": file.get("Path"),
                        "Size": file.get("Size"),
                        "Inside Backup": file.get("Inside Backup"),
                        "Modified": file.get("Modified"),
                    }
                )

                action_id += 1



        with open(
            self.output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer = csv.DictWriter(
                file,
                fieldnames=rows[0].keys()
            )


            writer.writeheader()

            writer.writerows(rows)