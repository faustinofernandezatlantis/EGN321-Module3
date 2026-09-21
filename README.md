# Engineering Valve Selection Tool

This Python tool replaces hard-to-read spreadsheet lookup logic with a modular, fully tested lookup engine. It calculates temperature-dependent engineering coefficients using structured lookup tables and linear interpolation while strictly refusing extrapolation beyond supported temperature ranges.

## Engineering Rule
> **Interpolate inside the evidence. Refuse outside it.**

## Supported Valve Families & Temperature Ranges
| Valve Family | Minimum Temp (°C) | Maximum Temp (°C) |
| :--- | :--- | :--- |
| **VX-100** | 20°C | 100°C |
| **VX-200** | 10°C | 90°C |
| **VX-300** | 0°C | 100°C |

## Core Calculation Rules
1. **Exact Match:** If the requested temperature matches a table row, return the coefficient directly without interpolating.
2. **Linear Interpolation:** For temperatures falling strictly between known rows $x_1$ and $x_2$:
   $$y = y_1 + \frac{x - x_1}{x_2 - x_1} \times (y_2 - y_1)$$
3. **Extrapolation Refusal:** Raises a `ValueError` if requested temperature is below the minimum or above the maximum supported limit.
4. **Unsupported Family Refusal:** Raises a `ValueError` if an unrecognized valve family is requested.

## Running Tests
Run the test suite using `pytest`:
```bash
pytest -v