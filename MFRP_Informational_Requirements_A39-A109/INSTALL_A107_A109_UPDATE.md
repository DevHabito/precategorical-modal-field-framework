# Installing the A107-A109 update into an existing repository

This package was built as an additive update to the supplied A39-A106 repository. Historical A39-A106 files, `audit_registry.json`, and `MANIFEST.sha256` are intentionally left unchanged so the old baseline remains independently reproducible.

## If you use the full repository ZIP

Extract it and use the enclosed repository as your working tree.

## If you use the patch-only ZIP

Extract the patch at the root of your existing A39-A106 repository. The patch adds new files and directories; it is not supposed to replace the historical A39-A106 manifest or audit registry.

Then run:

```bash
python tools/verify_results.py
python -m unittest tests.test_a109_update
python tools/verify_a107_a109_update.py
```

Expected high-level outcome:

- historical A39-A106 verifier: `PASS`;
- A107-A109 update verifier: `PASS_A107_A109_UPDATE_VERIFICATION`;
- A109 update unit tests: all tests pass.

## Suggested Git workflow

```bash
git checkout -b a107-a109-gamma-plus-update
git status
git add .
git commit -m "Add A107-A109 gamma-plus continuum audits"
git push -u origin a107-a109-gamma-plus-update
```

Review the diff before merging. In particular, confirm that H19 remains preregistered but unexecuted if you have not intentionally run `tools/run_a109_h19.py`.
