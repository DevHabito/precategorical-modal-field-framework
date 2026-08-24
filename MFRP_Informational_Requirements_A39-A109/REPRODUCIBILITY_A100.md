# A100 Reproducibility Contract

- Python with SymPy, mpmath, and Matplotlib.
- No random seeds are used.
- `provenance/a100_high_precision_active_set_discovery.py` is discovery-only and runs a complete-standard-form two-phase revised simplex at 180 decimal digits.
- `audits/a100_full_lp_active_set_resolution_audit.py` is the promoted exact audit.
- The promoted proof uses exact rational matrix inversion and exact rational sign comparisons.
- Every unused P/Q atom is checked; no reduced-cost sampling is used.
- All inactive band directions are checked.
- The high-precision active set and exact certificate must match, but no scientific conclusion depends on floating-point or high-precision sign decisions.
- The claim is restricted to `M=443`, `s=13/100`, and the declared finite LP contract.
