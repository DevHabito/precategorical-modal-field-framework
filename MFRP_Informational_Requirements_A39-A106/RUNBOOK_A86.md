# A86 Runbook

From the repository root:

```bash
python audits/a86_exact_rational_contact_strip_audit.py
python tools/generate_a86_figure.py
python -m unittest tests.test_audit_integrity
python tools/verify_results.py
```

Primary outputs:

- `results/a86_exact_rational_contact_strip_results.json`
- `results/a86_exact_rational_contact_strip_catalogue.json`
- `figures/a86_exact_three_contact_localizer.png`

A86 depends on the committed exact A84 support records. It does not rerun the full A84 scan internally.
