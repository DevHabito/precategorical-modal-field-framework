# A82 Reproducibility Contract

A82 is exact relative to the committed A78 and A81 contracts.

## Command

```bash
python audits/a82_adjacent_contact_locator_audit.py
python tools/generate_a82_figure.py
```

## Required committed inputs

- `audits/a78_rational_probe_contact_selection_audit.py`
- `audits/a80_local_compression_window_atlas_audit.py`
- `audits/a81_reduced_boundary_system_audit.py`
- `results/a78_rational_probe_contact_selection_results.json`

## Expected outputs

- `results/a82_adjacent_contact_locator_results.json`
- `results/a82_adjacent_difference_catalogue.json`
- `figures/a82_compressed_contact_locator.png`

## Arithmetic contract

All probe values, objective differences, KKT conditions, polynomial coefficients, root brackets, and side witnesses are computed with exact SymPy rational/integer arithmetic. Decimal root values are presentation-only.

## Scope

The complete locator theorem is restricted to `s=131/1000` and `10<=M<=80`. The local endpoint scan is restricted to `[129/1000,133/1000]` and is not represented as a complete root atlas for same-endpoint-sign polynomials.
