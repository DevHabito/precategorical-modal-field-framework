# Runbook — A95

From the repository root:

```bash
python audits/a95_rational_witness_lift_obstruction_audit.py --workers 16
python tools/generate_a95_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected audit verdict:

```text
PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION
```

A95 evaluates 3,189 natural-lift branches and additionally exhausts 19,421 restricted-family candidates in the obstruction prefix through `M=325`. Runtime depends strongly on exact-integer size and available worker processes. A full replay can take several minutes.
