"""
Main valve coefficient selection tool with boundary validation and extrapolation refusal.
"""

from src.interpolation import linear_interpolate
from src.lookup_tables import LOOKUP_TABLES, get_supported_range


def select_coefficient(valve_family: str, temperature_c: float) -> dict:
    """
    Selects and calculates the valve coefficient based on valve family and temperature.

    Engineering Rules:
    1. Unsupported valve family -> Raise ValueError.
    2. Temperature out of supported range -> Raise ValueError (Refuse extrapolation).
    3. Exact temperature match -> Return exact table coefficient.
    4. In-range between rows -> Apply linear interpolation.
    """
    if valve_family not in LOOKUP_TABLES:
        raise ValueError(f"Unsupported valve_family: {valve_family}")

    table = LOOKUP_TABLES[valve_family]
    min_temp, max_temp = get_supported_range(valve_family)

    # Validate temperature bounds (Refuse extrapolation)
    if temperature_c < min_temp:
        raise ValueError(
            f"temperature_c {temperature_c} is below the supported minimum {min_temp}"
        )
    if temperature_c > max_temp:
        raise ValueError(
            f"temperature_c {temperature_c} exceeds the supported maximum {max_temp}"
        )

    # 1. Exact match lookup
    for row_temp, coeff in table:
        if temperature_c == row_temp:
            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": coeff,
                "method": "exact",
                "lower_point": (row_temp, coeff),
                "upper_point": (row_temp, coeff),
                "supported_range": (min_temp, max_temp),
            }

    # 2. Find surrounding rows for linear interpolation
    for i in range(len(table) - 1):
        x1, y1 = table[i]
        x2, y2 = table[i + 1]

        if x1 < temperature_c < x2:
            coeff = linear_interpolate(temperature_c, x1, y1, x2, y2)
            return {
                "valve_family": valve_family,
                "temperature_c": temperature_c,
                "coefficient": round(coeff, 4),
                "method": "interpolation",
                "lower_point": (x1, y1),
                "upper_point": (x2, y2),
                "supported_range": (min_temp, max_temp),
            }

    raise RuntimeError("Unexpected state processing table rows.")