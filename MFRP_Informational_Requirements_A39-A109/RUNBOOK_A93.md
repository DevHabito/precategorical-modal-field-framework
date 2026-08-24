# Runbook — A93

```bash
python audits/a93_exact_continuum_global_one_variation_audit.py
python tools/generate_a93_figure.py
python tools/verify_results.py
python -m unittest discover -s tests -v
```

Expected audit verdict:

```text
PASS_EXACT_FULL_SEQUENCE_CONTINUUM_ONE_VARIATION_AND_25_GLOBAL_OFFSET_THREE_WINDOWS
```

The audit normally completes in under a minute on a multicore machine. It generates a compact result JSON and a detailed catalogue containing 5,426 non-decisive factor certificates.
