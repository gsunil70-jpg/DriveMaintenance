"""
DriveMaintenance
Analytics
"""

from constants import CSV_FILE
from csv_loader import CsvLoader


def main():

    loader = CsvLoader(CSV_FILE)

    dataframe = loader.load()

    print()

    print("Dataset successfully loaded.")


if __name__ == "__main__":

    main()