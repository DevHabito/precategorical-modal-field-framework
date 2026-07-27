# A78 Reproduction Runbook

## Main audit

From the structured repository root:

```bash
python audits/a78_rational_probe_contact_selection_audit.py
```

The audit uses exact rational arithmetic and normally takes tens of seconds on a current desktop-class CPU. It writes:

- `results/a78_rational_probe_contact_selection_results.json`;
- `results/a78_rational_probe_branch_catalogue.json`.

## Flat runtime

The standard materializer also supports A78:

```bash
python tools/materialize_runtime.py --clean
python tools/run_all_audits.py --from-audit 78 --to-audit 78
```

## Expected verdict

```text
PASS_EXACT_RATIONAL_PROBE_CONTACT_SELECTION_AND_COMPRESSION_RESETS
```

Expected branch count: `9230`.  
Expected gates: `12/12`.  
Expected compressed supports: `40, 57, 74`.
