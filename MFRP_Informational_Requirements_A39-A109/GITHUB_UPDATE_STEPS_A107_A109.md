# GitHub update steps for A107-A109

1. Read `README_A107_A109_UPDATE.md` and `docs/a107_a109/CLAIMS_AND_LIMITS_A107_A109.md` before committing.
2. Run `python tools/verify_results.py` to confirm the untouched A39-A106 baseline.
3. Run `python tools/verify_a107_a109_update.py` to verify the new checksum manifest, stored accounting, H19 preregistration hash, and unit tests.
4. Inspect `git diff --stat` and `git status`.
5. Commit the update on a branch.
6. Do not describe A109 as an all-922 theorem. Do not describe the adjacent-boundary rule as a physical law.
7. Do not mark H19 as executed unless you intentionally run it after the frozen preregistration.

Suggested commit message:

`Add A107-A109 exact gamma-plus continuum audit update`
