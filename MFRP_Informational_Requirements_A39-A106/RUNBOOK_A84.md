# A84 Runbook

From the repository root:

```bash
python audits/a84_k_space_exponential_polynomial_stress_audit.py
python tools/generate_a84_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected A84 verdict:

```text
PASS_K_SPACE_EXPONENTIAL_POLYNOMIAL_REDUCTION_AND_FINITE_ONE_VARIATION_STRESS
```

Typical runtime for the A84 audit is tens of seconds. All finite gates use exact rational arithmetic.
