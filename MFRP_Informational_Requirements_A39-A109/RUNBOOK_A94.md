# Runbook — A94

```bash
python audits/a94_exact_all_cell_continuum_one_variation_audit.py
python tools/generate_a94_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected audit verdict:

```text
PASS_EXACT_CONTINUUM_ALL_858_CELL_ONE_VARIATION_AND_205_GLOBAL_ADJACENT_TRANSITIONS
```

A94 is substantially heavier than A93. It classifies 125,814 factor/cell pairs and uses up to twelve worker processes. On the packaged reference environment it normally completes in several minutes.
