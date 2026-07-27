# A97 Reproducibility Contract

- Python with SymPy and Matplotlib.
- No random seeds are used.
- All KKT decisions are exact rational comparisons.
- The M=125 interval certificate uses exact polynomial endpoint signs, exact derivative intervals, and exact rational interval Horner enclosures.
- The obstruction atlas uses all 83 A95 obstruction witnesses as committed inputs.
- A97 is intentionally executed in two memory-isolated phases; see `RUNBOOK_A97.md`.
