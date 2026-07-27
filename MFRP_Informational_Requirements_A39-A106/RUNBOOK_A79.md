# A79 Reproduction Runbook

## Main audit

From the structured repository root:

```bash
python audits/a79_compression_interval_certificate_audit.py
```

The audit uses symbolic rational arithmetic, exact polynomial root isolation, complete root censuses, and exact rational KKT witnesses. It writes:

- `results/a79_compression_interval_results.json`;
- `results/a79_boundary_polynomials.json`.

## Flat runtime

```bash
python tools/materialize_runtime.py --clean
python tools/run_all_audits.py --from-audit 79 --to-audit 79
```

## Expected verdict

```text
PASS_EXACT_COMPRESSION_INTERVALS_AND_CONTACT_ENTRY_POLYNOMIALS
```

Expected top-level gates: `6/6`.  
Expected nested support gates: `48/48`.  
Expected supports: `40, 57, 74`.
