# A83 Runbook

From the repository root:

```bash
python audits/a83_seven_term_adjacent_sign_atlas_audit.py
python tools/generate_a83_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected A83 verdict:

```text
PASS_SEVEN_TERM_ADJACENT_DIFFERENCE_FACTORIZATION_AND_COMPLETE_LOCAL_SIGN_ATLAS
```

The audit uses exact SymPy rational arithmetic. No floating-point value is used to decide a gate.
