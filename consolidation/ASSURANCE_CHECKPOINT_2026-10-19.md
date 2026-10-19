# Scientific assurance checkpoint — 2026-10-19

**Repository:** `DevHabito/precategorical-modal-field-framework`  
**Baseline main commit:** `89e2668c3aef3fbff5a7f399f86de7d27e467da1`  
**Status:** partial independent audit, **not** repository-wide mathematical or software certification.

## Method and scope

This checkpoint separates inspected source, independently reproduced finite
claims, formal-assurance qualifications, and unresolved verification work.
A "PASS" in a script is evidence for the exact contract it checks, not for a
stronger theorem or for physical relevance.

The GitHub recursive tree was inventoried at the baseline commit. Selected
source proofs, Lean modules, audit scripts, claim ledgers, negative controls,
and literature notes were inspected. The full 3,552-file content corpus,
large binary artifacts, all historical result JSON files, and the full
mathematical proof chain **have not** been independently replayed.

An external mathematician's peer review **has not** been performed by this
checkpoint. Automated adversarial inspection is not a substitute for one.

## Finding F1 — Lean native-evaluation trust boundary

**Severity:** high for assurance wording; **not evidence of a false result**.

The pinned toolchain is Lean `v4.33.1`. At this version, `native_decide`
depends on native evaluation and introduces a computation-specific axiom.
A successful Lean elaboration, build, or `leanchecker` replay does not turn
such a native computation into kernel-only evaluation.

In particular:

- `PrecategoryFormal.PosetEnumeration` uses `native_decide` for its finite
  poset counts;
- `PrecategoryFormal.EdgeToggleSensitivity` uses `native_decide` for the
  five-vertex numerator and other finite counts;
- semantic equivalence and graph-realization lemmas may have a different
  trust boundary. Their transitive axiom dependencies must be inspected
  individually; do not infer them from a file-level "PASS".

For each published theorem, run `#print axioms` in the pinned Lean
environment and record the output. At minimum inspect:

- `PrecategoryFormal.encodedPosetCount_five`
- `PrecategoryFormal.natCard_literalRepresentativeCode_five`
- `PrecategoryFormal.changedPairCount_five`
- `PrecategoryFormal.edgeToggleProbability_five_crossmul`
- `PrecategoryFormal.mf_r009_graph_level_code_collision`

These are **commands to run**, not outputs claimed in this checkpoint.

**Required language:** Lean-checked semantic bridges and exact native
finite computations, with a disclosed compiler/axiom dependency. Reserve
"kernel-only" for statements with verified axiom dependencies and no
native-evaluation trust assumption.

Official references:

- Lean reference, *Validating a Lean Proof*:
  https://lean-lang.org/doc/reference/latest/ValidatingProofs/
- Lean API, *Init.Tactics* (`native_decide`):
  https://lean-lang.org/doc/api/Init/Tactics.html

## Finding F2 — stale root SHA-256 inventories

**Severity:** high for full-checkout reproducibility; **not mathematical falsification**.

The baseline recursive Git tree contains:

- 3,552 tracked blobs in 208 directories;
- 3,319 entries in `MANIFEST.csv`;
- 233 tracked blobs absent from the manifest;
- six manifest entries whose recorded size differs from the current Git blob
  size; the remaining 3,313 paths and sizes agree.

The six size-drift paths are:

1. `README.md`
2. `docs/CANONICAL_VERSIONS.md`
3. `docs/novelty/MF-R008_representative_code_count.md`
4. `docs/novelty/MF-R011_edge_flip_probability.md`
5. `docs/novelty/NOVELTY_AUDIT_C1_SUMMARY.md`
6. `docs/novelty/README.md`

This comparison uses Git blob metadata and manifest declarations. It does
**not** independently hash the 3,552 checkout files, and no such check is
claimed here.

The existing `tools/validate_repository.py` checks only paths that already
appear in the manifest and therefore does not detect all omissions. The
six size mismatches are sufficient to make its current full-checkout gate fail.

`SHA256SUMS.txt` also needs regeneration and byte-for-byte validation,
rather than being silently assumed current.

### Non-destructive remediation

Run from a clean checkout of the review branch:

```bash
python tools/refresh_integrity_indexes.py --check
python tools/refresh_integrity_indexes.py --write
python tools/refresh_integrity_indexes.py --check
python tools/validate_repository.py
git diff -- MANIFEST.csv SHA256SUMS.txt
```

The first check is **expected to fail until the indexes are regenerated**.
The write command hashes every Git-tracked regular file except the two root
indexes themselves. Do not update archival package-level manifests merely
because their data is old; historical snapshots have separate provenance.

After regeneration, review the diff before committing the two indexes.
No new root index hashes are invented in this checkpoint.

### Remediation subsequently executed on the audit branch

GitHub Actions [index-repair run 39336107630](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39336107630) regenerated root indexes from the checked-out bytes and committed them as `03822fb4c402e18873782e3b89a9ab032673709f`. The job logged `3560` indexed tracked files, a successful index readback, and `Repository validation passed.` These results belong to that exact commit state; editing any tracked file afterwards requires regenerating the root indexes again. The historical baseline mismatch recorded above remains a factual finding, not the status of that repaired commit.

### Lean axiom-dependency results from real CI

GitHub Actions [Lean run 39334714446](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39334714446) completed the Lean build and the selected axiom-printing step successfully. The printed declarations have been recorded in [LEAN_AXIOM_DEPENDENCIES_2026-10-19.md](LEAN_AXIOM_DEPENDENCIES_2026-10-19.md).

Among nine declarations, eight include native evaluation axioms. The general `addDirectedEdge_preserves_reachability_iff` theorem reported no axioms. The historical five-vertex count and edge-toggle proofs still depend on native evaluation. No `sorryAx` appeared in the selected traces; this is not a full-corpus axiom audit.

## Finding F3 — finite independent cross-checks

`tools/independent_finite_crosscheck.py` was written without importing the
historical Python audit implementations. A local Python 3.13 execution of the
same mathematical checks reproduced:

| Claim | Independently reproduced exact output | Boundary |
|---|---|---|
| MF-R008 | `p(1..5) = 1,3,19,219,4231` and five-vertex code count `5234` | finite enumeration only |
| MF-R011 | `P2=1`, `P3=3/4`, `P4=1/2`, `P5=75/256`, `P6=313/2048` | uniform loopless digraph ensemble |
| MF-R049 | mean `3/2`, initial moment `15/32`, differing half-scale moments | fixed four-point witness |

MF-R011 was checked by both reachable-set decomposition and directed-cut
inclusion-exclusion. These are distinct counting decompositions, though
they share the same mathematical definitions and were implemented in the same
review workflow. They are not blind independent peer reviews.

An additional depth-first-search oracle, `tools/independent_graph_toggle_oracle.py`,
independently computes full vertex-level reachability for every loopless
digraph on `n=2,3,4` vertices and toggles every directed edge. It reproduced
the exact sensitive ordered graph-edge pair counts `8`, `288`, and
`24576`, respectively. Negative controls require a redundant edge to
preserve reachability and a first edge to change it. The script also verifies
the exact finite insertion criterion for every absent edge. The GitHub Actions
[independent-audit run 39336360343](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39336360343)
completed this DFS step, the A119 interval replay, and the other finite
checks successfully. This does not prove the all-`n` probability identity
or eliminate the native-computation dependencies in Lean.


### A119 rational interval replay

A separate script, `tools/independent_a119_interval_replay.py`, reconstructed
A119's exact critical substitution and the positive natural-interval
covering calculation with `Fraction` arithmetic. The local execution found:

- `2,304` positive even-parity boxes, with worst exact lower bound
  `7962094616280060340361057850523941099377/4460543890481278214239707910840320000000`;
- `4,096` positive odd-parity boxes, with worst exact lower bound
  `3296636265099577642233577213168576496429665038806348563/2438741833785351580293579578096010608476160000000000000`;
- positive exact cutoff bounds for the excluded deep even/odd cells;
- independent rational Taylor enclosures establishing
  `2 < -log(s) < 21/10` on the full source interval.

Those exact lower endpoints agree with the preserved A119 artifact. The
replay supplies independent implementation-level evidence for the interval
arithmetic and finite covering **conditional on the displayed A118/A119
formula**. It is not a blind derivation of that formula, a Lean theorem, or a
new certificate for the entire A115–A122 dependency chain.


No conclusion about all graph sizes, global optimization, physical geometry,
or bibliographic priority follows from these checks.

## Finding F4 — historical statuses remain scoped

- A108's universal one-sided boundary claim was refuted. A110 does not make
  A108 true retroactively.
- A112/A113 are conditional on their frozen source, target, and optimization
  contracts. Compressed maxima are not automatically full lifted KKT optima.
- A115 preserves exact counterexamples to a universal target-deformation
  threshold.
- A119's published 6,400 interval-box sign certificates and deep-cell cutoff
  bounds were reproduced with a separately written exact `Fraction` interval
  evaluator. Its two worst certified lower endpoints match the archived values
  exactly. This independently replays the **published critical-substitution
  formula**, not the upstream A115–A118 derivations or the full theorem chain.
- A120–A122 study fixed-interior rounding phases; their local-maximizer
  statements do not establish global target-deformed maximizers.
- The foundational pre-submission manuscript has open independent-review
  and reference-precision gates.

Older manuscript blueprints and cumulative A39 directories may use earlier
status language. They are historical artifacts, not the authority over the
current Consolidation 1.0 claim ledger.

## Literature: verified scope and attribution

- Uno, Y. and Ibaraki, T. (1998), *Reachability Problems of Random
  Digraphs*, IEICE Transactions on Fundamentals, E81-A(12), 2694–2702.
  The paper treats fixed-pair reachability probabilities in independent-edge
  random digraphs and an exact computation method.
  https://globals.ieice.org/en_transactions/fundamentals/E81-A_12
- Qin, Y., Sheng, Q. Z., Parkinson, S. and Falkner, N. J. G. (2017),
  *Edge Influence Computation in Dynamic Graphs*, DASFAA, 649–660.
  DOI: https://doi.org/10.1007/978-3-319-55699-4_41

These works predate the repository and prohibit an original-discovery claim
about fixed-pair random-digraph reachability or reachability-based edge
influence as general subjects. Neither this checkpoint nor a negative search
certifies priority of the particular finite fraction `75/256`.

## Release gate: still open

Before merging a broad scientific-integrity claim:

1. Rebuild the project from a clean checkout with the pinned toolchains.
2. Run the exact finite cross-check and both integrity-index checks.
3. Inspect `#print axioms` for every promoted Lean theorem.
4. Rerun independent interval certificates and compare exact outputs/hashes.
5. Check source hypotheses against every theorem header and imported lemma.
6. Test known failed variants as negative controls; retain counterexamples.
7. Reconcile historical novelty labels with verified primary literature.
8. Obtain genuine independent mathematical review for submission claims.

The current checkpoint closes none of these release-level obligations merely
by documenting them. It records concrete partial evidence and a reproducible
repair path without changing mathematical data or the historical archive.
