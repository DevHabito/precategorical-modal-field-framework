# A101 Runbook

From the repository root:

```bash
python audits/a101_gamma_active_interval_and_residual_closure_audit.py
python tools/generate_a101_figure.py
```

Expected exact verdict:

```text
PASS_GAMMA_ACTIVE_M443_INTERVAL_AND_THREE_OF_THREE_FINAL_RESIDUAL_RESOLUTIONS
```

The audit regenerates:

- the main A101 result;
- the complete M443 interval certificate;
- the full three-witness residual certificate atlas.

The promoted calculation is deterministic and seed-free. It normally completes in seconds on a modern desktop, but JSON serialization of the full 2,873-condition residual atlas may take longer on slower disks.
