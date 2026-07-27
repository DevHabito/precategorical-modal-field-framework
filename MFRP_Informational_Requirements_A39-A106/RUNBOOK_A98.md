# A98 Runbook

From the repository root:

```bash
python provenance/a98_high_precision_active_set_discovery.py
python audits/a98_full_lp_active_set_resolution_audit.py
python tools/generate_a98_figure.py
```

Expected exact verdict:

```text
PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M396
```

The first command is discovery only.  The second command is the exact proof-producing audit.
