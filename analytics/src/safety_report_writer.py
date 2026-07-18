"""
DriveMaintenance
Safety Report Writer
"""


import csv


class SafetyReportWriter:


    def __init__(self, output_file):

        self.output_file = output_file



    def write(self, rows):

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