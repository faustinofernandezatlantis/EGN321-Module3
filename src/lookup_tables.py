"""
Readable representation of engineering lookup tables and range checks.
"""

LOOKUP_TABLES = {
    "VX-100": [
        (20, 0.88),
        (40, 0.93),
        (60, 0.99),
        (80, 1.06),
        (100, 1.14),
    ],
    "VX-200": [
        (10, 1.12),
        (30, 1.18),
        (50, 1.27),
        (70, 1.39),
        (90, 1.55),
    ],
    "VX-300": [
        (0, 0.75),
        (25, 0.82),
        (50, 0.91),
        (75, 1.03),
        (100, 1.18),
    ],
}


def get_supported_range(valve_family: str) -> tuple[float, float]:
    """Returns the minimum and maximum supported temperatures for a given valve family."""
    if valve_family not in LOOKUP_TABLES:
        raise ValueError(f"Unsupported valve_family: {valve_family}")

    table = LOOKUP_TABLES[valve_family]
    min_temp = table[0][0]
    max_temp = table[-1][0]
    return min_temp, max_temp