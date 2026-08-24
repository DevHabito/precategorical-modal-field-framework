# Provenance gaps

The update preserves every A107/A108/A109 file that is currently available in the session artifact set. Two historical scripts referenced in the research log are not present among those files:

- `A108_P5_SHARD_AUDIT.py`
- `a108_two_sided_dev_check.py`

Their result artifacts are present, including the rank-105 counterexample and the post-hoc two-sided development output. The missing scripts were deliberately **not reconstructed**. Reconstructing historical code after seeing its outcomes could accidentally change implementation details while giving the appearance of original provenance.

If the original scripts are recovered later, add them as historical artifacts and record their SHA-256 hashes. Do not overwrite the preserved results.
