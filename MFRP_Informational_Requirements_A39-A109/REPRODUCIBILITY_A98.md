# A98 Reproducibility Contract

- Python with SymPy, mpmath, and Matplotlib.
- No random seeds are used.
- `provenance/a98_high_precision_active_set_discovery.py` performs discovery at 180 decimal digits only.
- The discovery result is not used as a proof.
- `audits/a98_full_lp_active_set_resolution_audit.py` reconstructs the full certificate with exact rational arithmetic.
- All 788 unused P/Q atom reduced costs are checked explicitly.
- All primal equations, active multipliers, inactive band slacks, probability constraints, and primal-dual equality are exact.
- The claim is restricted to `M=396`, `s=13/100` under the declared finite LP contract.
