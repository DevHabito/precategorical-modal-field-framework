# A99 Runbook

From the repository root:

```bash
python audits/a99_q0q1_interval_and_residual_atlas_audit.py
python tools/generate_a99_figure.py
```

Expected exact verdict:

```text
PASS_Q0Q1_M396_INTERVAL_AND_TWO_OF_SIX_REMAINING_RESIDUAL_RESOLUTIONS
```

The first command regenerates:

- the main A99 result;
- the full M396 interval certificate;
- the six-witness residual atlas.
