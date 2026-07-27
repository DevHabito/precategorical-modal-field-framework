# A81 Runbook

From the repository root:

```bash
python audits/a81_reduced_boundary_system_audit.py
```

The audit writes:

- `results/a81_reduced_boundary_system_results.json`
- `results/a81_all_contact_positive_gap_certificates.json`
- `results/a81_selected_contact_coefficient_formulas.json`

The computation uses exact SymPy rational arithmetic. It reconstructs all 142 A80 selected-contact boundary polynomials, evaluates the reduced/full symbolic identities on eight declared witnesses, and certifies positive interval enclosures for `T` and `Delta` over all 1,438 admissible `(M,k)` pairs.

A normal replay takes roughly one minute on the packaged environment. A PASS verdict requires all 17 top-level gates.
