# A101 Reproducibility Contract

- Python with SymPy and Matplotlib.
- No random seeds, web access, or external datasets are used.
- `audits/a101_gamma_active_interval_and_residual_closure_audit.py` performs every promoted calculation.
- The M443 symbolic layer uses the exact Sherman–Morrison formula for a one-row matrix update around `s=13/100`.
- All basic variables, dual variables, reduced costs, and inactive slacks share one seven-term rational denominator.
- Both boundary roots are isolated in exact rational brackets of width `1/10^24`.
- Root uniqueness and simplicity use exact endpoint signs and exact derivative interval signs.
- The common denominator and 893 nonboundary numerators are enclosed by integer-only termwise interval arithmetic on the complete boundary hull.
- The M449, M484, and M490 residual certificates use exact rational matrix inversion and check every unused P/Q atom reduced cost.
- The claim is pointwise at the three residual witnesses and interval-valued only at M443.
- No universal support law or physical interpretation is promoted.
