# Runbook A90

From the repository root:

```bash
python audits/a90_prethreshold_all_k_one_variation_audit.py
python tools/generate_a90_figure.py
```

Expected audit verdict:

```text
PASS_EXACT_PRETHRESHOLD_NINE_PROBE_ALL_K_ONE_VARIATION_AND_FOUR_CONTACT_STRIP
```

Typical execution is substantially faster than direct `Fraction` evaluation of every factor because the ten rational nodes are converted once per support/probe cell into integer bases.
