"""
DriveMaintenance
Execution Manifest Writer
"""

import csv


class ExecutionManifestWriter:
    """
    Writes the execution manifest.

    This becomes the master execution ledger
    shared between Python and Google Apps Script.
    """

    def __init__(self, output_file):

        self.output_file = output_file

    def write(self, execution_plan):

        with open(
            self.output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                #
                # Human workflow
                #

                "Review Status",

                "Operation",

                "Resolution Mode",

                "File Name",

                "Current Path",

                "Canonical File Name",

                "Canonical Path",

                "Reason",

                #
                # Execution lifecycle
                #

                "Run ID",

                "Execution Status",

                "Executed At",

                #
                # Technical identifiers
                #

                "File ID",

                "Canonical File ID",

            ])

            for item in execution_plan:

                writer.writerow([

                    #
                    # Review
                    #

                    "PENDING",

                    item.get(
                        "Operation",
                        ""
                    ),

                    item.get(
                        "Resolution Mode",
                        ""
                    ),

                    item.get(
                        "File Name",
                        ""
                    ),

                    item.get(
                        "Path",
                        ""
                    ),

                    #
                    # Canonical information
                    #

                    "" if item.get("Operation") == "KEEP"
                    else item.get(
                        "Canonical File Name",
                        ""
                    ),

                    "" if item.get("Operation") == "KEEP"
                    else item.get(
                        "Canonical Path",
                        ""
                    ),

                    item.get(
                        "Reason",
                        ""
                    ),

                    #
                    # Filled later by Apps Script
                    #

                    "",

                    "",

                    "",

                    #
                    # Technical IDs
                    #

                    item.get(
                        "File ID",
                        ""
                    ),

                    "" if item.get("Operation") == "KEEP"
                    else item.get(
                        "Canonical File ID",
                        ""
                    ),

                ])