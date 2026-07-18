"""
DriveMaintenance
Safety Policy

Defines rules for cleanup protection.
"""


PROTECTED_KEYWORDS = [
    "phd",
    "thesis",
    "viva",
    "legal",
    "agreement",
    "finance",
    "tax",
    "medical",
    "report"
]


def contains_protected_keyword(name):

    if not name:
        return False

    name = name.lower()

    for keyword in PROTECTED_KEYWORDS:

        if keyword in name:
            return True

    return False