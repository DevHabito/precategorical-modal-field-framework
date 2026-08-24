# Verification Report — A105

## Scope

This report verifies the integrated A105 exact continuum atlas for the forty A102 records classified as `legacy_two_band_compressed`.

## Exact audit result

- Verdict: `PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_40_LEGACY_TWO_BAND_SEGMENTS_WITH_0_FULL_AND_40_PARTIAL_COMPONENTS`
- Gates: **17/17**
- Source segments: **40/40**, all unique
- `unique_b_plus_2` segments: **14**
- right-side `b_plus_1_to_b_plus_2` segments: **26**
- Complete source-segment certificates: **0**
- Proper two-sided strict subcomponents: **40**
- Exact KKT conditions: **24,312**
- KKT numerators plus common denominators: **24,352**
- Sign-changing candidate roots: **181**
- Selected nearest algebraic boundaries: **80**
- Exact competing-bracket ordering checks: **101/101**
- Exact negative outside counterexamples: **80**
- Witness, core, root, ordering, hull, and unresolved failures: **0**

## Boundary census

The lower boundaries split into two mechanisms:

- inactive `gamma-` slack reaches zero for `M = 40, 41, 57, 74, 97, 120`;
- basic endpoint mass `p0` reaches zero for the other **34** records.

For every one of the forty records, the upper boundary occurs when the inactive `gamma+` slack reaches zero.

Every selected root is isolated by an exact rational bracket with opposite endpoint signs and a fixed nonzero derivative sign. All competing brackets are ordered using exact rational inequalities. Every selected boundary has a rational point beyond it where the responsible KKT condition is strictly negative.

## Full standalone replay

A separate standalone package independently recomputed all forty record files, reassembled the result and catalogue, and regenerated the figure.

- Recomputed records: **40/40**
- SHA-256 comparisons: **43/43 identical**
  - 40 record JSON files;
  - consolidated result JSON;
  - consolidated catalogue JSON;
  - generated figure.

Replay verdict: `PASS_FULL_40_RECORD_EXACT_STANDALONE_REPLAY_MATCH`.

## Repository-wide verification

- Registered main audits: **67**
- Registered gates: **994/994**
- Unit/integrity tests: **61/61**
- English PNG figures: **109**
- Python compilation: **PASS**
- JSON parsing: **PASS**
- Manifest verification: recorded after final manifest generation

## Claim boundary

A105 proves exact witness-containing continuum components only for the forty A95/A102 source segments in the legacy two-band family. It does not establish continuum lifting for the 940 legacy three-band witnesses, coverage of complete A92 cells, an all-`M` theorem, a universal active-support law, or a physical interpretation.
