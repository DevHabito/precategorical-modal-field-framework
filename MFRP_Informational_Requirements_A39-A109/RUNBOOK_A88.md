# Runbook A88

From the repository root:

```bash
python audits/a88_nine_term_secant_positivity_audit.py
python tools/generate_a88_figure.py
python -m unittest tests.test_audit_integrity
python tools/verify_results.py
```

Expected A88 verdict:

```text
PASS_NINE_TERM_SECANT_REDUCTION_EXTENDED_EXACT_POSITIVITY_AND_POSITIVE_PARITY_PHASE_LIMIT
```

The exact audit can take tens of seconds because it evaluates 8,019 rational cells through `M=900`.
