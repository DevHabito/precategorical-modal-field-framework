# A82 Runbook

From the repository root:

```bash
python audits/a82_adjacent_contact_locator_audit.py
```

Expected terminal summary:

- compressed contacts: `1438`
- adjacent comparisons: `1367`
- strictly unimodal support sizes: `71`
- gamma classes: `57 plus / 11 minus / 3 compressed`
- A78 selections reproduced: `71`
- local endpoint-crossing pairs: `(28,6,7)` and `(79,15,16)`
- gates: `18/18`
- verdict: `PASS_EXACT_ADJACENT_CONTACT_LOCATOR_AND_LOCAL_ORIENTATION_SWITCHES`

Generate the figure with:

```bash
python tools/generate_a82_figure.py
```

Run integrity checks with:

```bash
python tools/verify_results.py
python -m unittest tests.test_audit_integrity
```
