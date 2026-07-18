"""
DriveMaintenance
Analytics Constants
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
REPORT_DIR = PROJECT_ROOT / "reports"
OUTPUT_DIR = PROJECT_ROOT / "output"

CSV_FILE = DATA_DIR / "DriveIndex_RC2.csv"

REPORT_FILE = REPORT_DIR / "RC2_Index_Audit.md"

#
# Decision Scoring
#

BACKUP_BONUS = 40

MIRROR_PENALTY = 25

NEWEST_BONUS = 15

CHECKSUM_BONUS = 30

VERSION_WEIGHT = 1

FOLDER_WEIGHT = 1