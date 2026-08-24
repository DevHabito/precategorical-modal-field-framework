# Reproducibility A96

Run from the repository root:

```bash
python audits/a96_full_lp_active_set_resolution_audit.py
python tools/generate_a96_figure.py
python -m unittest tests.test_audit_integrity.IntegrityTests.test_a96_full_lp_active_set_resolution
```

The theorem-producing audit uses SymPy exact rational arithmetic. The high-precision simplex record in `provenance/a96_high_precision_active_set_discovery.json` is discovery provenance only and is not used to establish the result.

The exact audit reconstructs the 7-by-7 basis, checks all 246 unrestricted atom reduced costs, checks all inactive band slacks, and verifies exact primal–dual objective equality.
