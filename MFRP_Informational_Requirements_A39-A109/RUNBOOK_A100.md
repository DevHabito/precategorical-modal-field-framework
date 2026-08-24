# A100 Runbook

From the repository root:

```bash
python provenance/a100_high_precision_active_set_discovery.py
python audits/a100_full_lp_active_set_resolution_audit.py
python tools/generate_a100_figure.py
```

Expected exact verdict:

```text
PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M443
```

The exact audit regenerates:

- `results/a100_full_lp_active_set_resolution_results.json`;
- `results/a100_full_lp_active_set_certificate.json`.
