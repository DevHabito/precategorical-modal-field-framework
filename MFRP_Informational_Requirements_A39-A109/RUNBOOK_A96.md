# Runbook A96

```bash
python audits/a96_full_lp_active_set_resolution_audit.py
python tools/generate_a96_figure.py
```

Expected verdict:

```text
PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M125
```

Expected active set:

```text
P = [23, 24, 125]
Q = [1, 62, 63]
active bands = alpha+, beta-
```

The audit should report 22/22 gates and 259 strict KKT conditions.
