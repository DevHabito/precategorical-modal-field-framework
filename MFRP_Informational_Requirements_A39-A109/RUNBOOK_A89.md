# Runbook A89

From the repository root:

```bash
python audits/a89_uniform_secant_threshold_audit.py
python tools/generate_a89_figure.py
python -m unittest tests.test_audit_integrity
python tools/verify_results.py
```

Expected A89 verdict:

```text
PASS_EXPLICIT_UNIFORM_LOCAL_SECANT_POSITIVITY_THRESHOLD_M521
```

The theorem gates use exact integer and `Fraction` arithmetic. The 45 regression cells are exact but are not used to establish the continuum theorem.
