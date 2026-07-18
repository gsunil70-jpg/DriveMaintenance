"""
DriveMaintenance
Execution Manifest Writer
"""

import csv


class ExecutionManifestWriter:
    """
    Writes execution manifest.
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

                "Operation",

                "File ID",

                "File Name",

                "Path",

                "Reason",

                "Canonical File ID",

                "Canonical File Name",

                "Canonical Path",

            ])



            for item in execution_plan:


                writer.writerow([

                    item["Operation"],

                    item["File ID"],

                    item["File Name"],

                    item["Path"],

                    item["Reason"],

                    item.get(
                        "Canonical File ID",
                        ""
                    ),

                    item.get(
                        "Canonical File Name",
                        ""
                    ),

                    item.get(
                        "Canonical Path",
                        ""
                    ),

                ])