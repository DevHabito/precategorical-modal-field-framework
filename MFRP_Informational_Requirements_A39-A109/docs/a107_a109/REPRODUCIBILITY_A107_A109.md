# Reproducibility guide for A107-A109

## Environment

Use Python 3 with the repository requirements installed:

```bash
python -m pip install -r requirements.txt
```

The late gamma-plus audits also use SymPy, which is already part of the repository dependency set.

## Verify the historical A39-A106 baseline

```bash
python tools/verify_results.py
```

The package was rebuilt from the supplied A39-A106 repository archive. Before the A107-A109 files were added, the historical verifier returned 68 audit results, 1,013 gates, 110 figures, zero failures, status `PASS`.

## Verify the A107-A109 update

```bash
python tools/verify_a107_a109_update.py
python -m unittest tests.test_a109_update
```

These tests check the stored rank-105 counterexample, the current cumulative accounting through rank 414, the frozen/unexecuted H19 preregistration hash and prediction counts, and the sign-classifier truth table.

## Re-run a frozen H19 shard manually

H19 is not executed by this package. To run a single already-frozen rank, for example rank 415:

```bash
python audits/a109_gamma_plus_holdout_runner.py   --preregistration preregistrations/a107_a109/A109_H19_PREREGISTRATION.json   --expected-sha256 abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d   --start 415 --end 415   --output results/a107_a109/h19/full_atlas/A109_H19_R415_RESULT.json
```

The frozen execution policy uses a 55-second wall-clock limit and at most two identical attempts. The repository tool applies that policy across all sixteen H19 ranks:

```bash
python tools/run_a109_h19.py
```

If a rank times out twice, do **not** reinterpret the timeout as support or refutation. A separate exact sufficient-certificate protocol must be preregistered before any fallback computation is run.

## Historical artifacts

The directory `research_updates/A107_A109/raw_packages/` contains the detailed package contents used during the research session, including per-rank full-atlas results, certificate blocks, logs, original scripts, preregistrations, and aggregate outputs. These are preserved as provenance and are not rewritten to make them prettier.

## Hash discipline

Frozen preregistrations are checked by SHA-256 before execution. Never edit a frozen preregistration in place. If a protocol must change, create a new preregistration with a new name and hash, and state why the prior protocol was insufficient or refuted.
