"""
Linear interpolation helper function.
"""


def linear_interpolate(
    x: float, x1: float, y1: float, x2: float, y2: float
) -> float:
    """
    Calculates y using linear interpolation between (x1, y1) and (x2, y2).
    Formula: y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
    """
    if x1 == x2:
        return y1

    return y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)