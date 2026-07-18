"""
DriveMaintenance
Cleanup Plan Writer
"""

import csv
from pathlib import Path



class CleanupPlanWriter:


    def __init__(self, output_file: Path):

        self.output_file = output_file



    def write(self, rows):

        self.output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        if not rows:

            return


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