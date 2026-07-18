"""
DriveMaintenance
CSV Loader
"""

import csv
from pathlib import Path


class CsvLoader:
    """
    Loads the Drive Index CSV into memory.
    Automatically tries common encodings.
    """

    def __init__(self, csv_file: Path):

        self.csv_file = csv_file

    def load(self):

        if not self.csv_file.exists():

            raise FileNotFoundError(
                f"CSV file not found:\n{self.csv_file}"
            )

        print(
            f"Loading:\n{self.csv_file}\n"
        )

        encodings = [
            "utf-8-sig",
            "utf-8",
            "cp1252",
            "latin1"
        ]

        last_error = None

        for encoding in encodings:

            try:

                with open(
                    self.csv_file,
                    mode="r",
                    encoding=encoding,
                    newline=""
                ) as file:

                    reader = csv.DictReader(file)

                    rows = list(reader)

                print(
                    f"Encoding    : {encoding}"
                )

                print(
                    f"Rows loaded : {len(rows):,}"
                )

                print(
                    f"Columns     : {len(reader.fieldnames)}"
                )

                return rows

            except UnicodeDecodeError as error:

                last_error = error

        raise last_error