# A85 Runbook

From the repository root:

```bash
python audits/a85_parity_dominant_balance_contact_localization_audit.py
python tools/generate_a85_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected A85 verdict:

```text
PASS_PARITY_DOMINANT_BALANCE_AND_ASYMPTOTIC_CONTACT_LOCALIZATION
```

The exact audit evaluates 1,746 transition-bracket factors with rational arithmetic and also performs a small high-precision logarithmic diagnostic. Typical runtime is well below the full A84 scan because A85 reuses the committed A84 maximizer catalogue.
