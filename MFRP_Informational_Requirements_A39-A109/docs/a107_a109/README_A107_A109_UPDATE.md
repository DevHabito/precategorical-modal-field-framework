# A107-A109 research update

This update records the gamma-plus continuum work that followed A106. The most important point is not that many tests passed. The important point is that an early structural claim **failed exactly**, and the replacement rule has since been tested prospectively without being repaired after outcomes.

## What changed

A107 opened the legacy three-band gamma-plus family and established exact local continuum stability on the first canonical records. A structural endpoint pattern then emerged: partial components were repeatedly terminated on the left by the upper adjacent basic variable, `basic_p_{j+1}`.

A108 tried to promote that observation into a one-sided rule. That rule is false. Canonical rank 105 is an exact counterexample: `basic_p_{j+1}` remains positive, while `basic_p_j` reaches zero on the **right**. The full exact atlas identifies `basic_p_22` as the selected right boundary, and an independent direct-matrix regression gives 988 exact comparisons with zero mismatch.

The current A109 candidate is therefore two-sided and local:

- `basic_p_{j+1}` is the candidate left boundary;
- `basic_p_j` is the candidate right boundary.

The development fit on ranks 1-105 is post-hoc and is kept separate from prospective evidence. The prospective sequence currently resolved is ranks 106-414. According to the stored cumulative status artifact, 309 records are mathematically resolved, 308 count as strict-clean prospective cases because rank 295 has a documented protocol-ordering exception, and the resolved sequence contains 215 full segments and 94 partial components. Among the partial components, 88 terminate on the left and 6 on the right. No two-sided case and no non-adjacent selected KKT boundary has been observed in that sequence. The direct symbolic-versus-matrix regression count is 475,782 exact comparisons with zero mismatch; the strict-clean comparison count is 473,770.

These are finite computational statements. They are **not** an all-922 theorem and they are **not** a physical claim.

## Why the result is interesting

The full KKT system contains many conditions that could, in principle, become the first obstruction along a source segment. The current evidence suggests that, inside this declared gamma-plus family, the first obstruction may be controlled by only the two basic variables adjacent to the compressed contact. If that can be proved, the result would be a structural compression: a high-dimensional feasibility question would reduce to two local numerator sign tests plus monotonicity and positivity conditions.

The evidence is not yet enough to state that theorem. A single future record with a non-adjacent KKT condition becoming the first boundary would refute the universal form of the conjecture.

## Current frozen holdout

A109-H19 is frozen and has **not** been full-atlas executed in this package. It covers canonical ranks 415-430. The frozen prediction is 11 full records and 5 partial records: four left boundaries and one right boundary. The right-branch case is rank 428, predicted in advance to terminate at `basic_p_56` on the right.

H19 preregistration SHA-256:

`abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d`

Target-only snapshot SHA-256:

`25825c8638b869429e02f90cbac174da7b4d0590389efcb3b8a1490a7dfc6236`

## Where the files are

- `docs/a107_a109/` — readable technical documentation and equations.
- `preregistrations/a107_a109/` — frozen preregistrations, target-only snapshots, and execution manifests.
- `results/a107_a109/` — curated aggregate/status/counterexample results.
- `research_updates/A107_A109/raw_packages/` — original extracted run packages, including detailed full-atlas outputs, certificates, logs, and historical scripts.
- `research_updates/A107_A109/session_artifacts/` — every currently available A107/A108/A109 non-ZIP session artifact.
- `research_updates/A107_A109/archives/` — the original ZIP packages.
- `audits/a109_gamma_plus_holdout_runner.py` — repository-portable runner for already-frozen holdouts.
- `tools/run_a109_h19.py` — H19 full-atlas orchestrator with the frozen two-attempt 55-second policy.
- `tests/test_a109_update.py` — integrity and accounting tests for this update.

## Historical-source caution

Two historical source scripts referenced in the research log are not present in the currently available file set: the A108-P5 shard script and the post-hoc two-sided development scan script. Their result artifacts are preserved. They were **not reconstructed**, because silently recreating missing historical code would weaken provenance. See `docs/a107_a109/PROVENANCE_GAPS.md`.
