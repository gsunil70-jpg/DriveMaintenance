"""
DriveMaintenance
Execution Report Writer
"""

import csv


class ExecutionReportWriter:
    """
    Writes execution summary.
    """

    def __init__(self, output_file):

        self.output_file = output_file

    def write(self, validation_result):

        with open(
            self.output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Metric",
                "Value"
            ])

            writer.writerow([
                "Valid",
                validation_result["valid"]
            ])

            writer.writerow([
                "Record Count",
                validation_result["record_count"]
            ])

            writer.writerow([])

            writer.writerow([
                "Errors"
            ])

            for error in validation_result["errors"]:

                writer.writerow([error])