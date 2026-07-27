# A87 Runbook

From the repository root:

```bash
python audits/a87_exact_secant_offset_classifier_audit.py
python tools/generate_a87_figure.py
python -m unittest tests.test_audit_integrity
python tools/verify_results.py
```

Primary outputs:

- `results/a87_exact_secant_offset_classifier_results.json`
- `results/a87_exact_secant_offset_classifier_catalogue.json`
- `figures/a87_exact_secant_offset_classifier.png`

A87 reads the committed A84, A85, and A86 result layers. All theorem gates use exact `Fraction` arithmetic.
