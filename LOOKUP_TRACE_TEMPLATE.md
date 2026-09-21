# Spreadsheet Lookup Trace Analysis

## Criteria Identification
- **First Lookup Criterion:** Valve Family (e.g., VX-100, VX-200, VX-300)
- **Second Lookup Criterion:** Operating Temperature (°C)

## Legacy Workbook Audit
- **Location of Engineering Data:** Engineering tables reside in dedicated sheets grouped by valve family inside `VALVE_SELECTION_rev3.xlsx`.
- **Workbook Selection Logic:** Uses nested lookup functions (`INDEX`, `MATCH`, `VLOOKUP`) or chained `IF` statements to route queries.
- **Exact Match Behavior:** Directly pulls the matched temperature row's coefficient.
- **In-between Rows Behavior:** Evaluates linear interpolation formulas inline within spreadsheet cell calculations.
- **Out-of-range Behavior:** Silently computes extrapolated values beyond validated laboratory testing limits.

## Pain Points of Legacy Spreadsheet
1. Deeply nested cell logic makes verification difficult.
2. High potential for silent engineering errors when operating beyond bounds.
3. Automated testing and edge-case testing cannot be implemented cleanly.