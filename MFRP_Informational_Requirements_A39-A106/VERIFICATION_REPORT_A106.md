# Verification Report — A106

## Scope

This report verifies the integrated A106 exact continuum atlas for the eighteen A102 records classified as `legacy_three_band_gamma_minus`.

## Exact audit result

- Verdict: `PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_18_LEGACY_GAMMA_MINUS_SEGMENTS_WITH_1_FULL_AND_17_PARTIAL_COMPONENTS`
- Gates: **19/19**
- Source segments: **18/18**, all unique
- Complete source-segment certificates: **1**
- Proper witness-containing strict subcomponents: **17**
- Exact KKT conditions: **2,410**
- Direct-matrix versus rank-one exact comparisons: **2,410/2,410**
- KKT numerators plus common denominators: **2,428**
- Sign-changing candidate roots: **22**
- Selected nearest algebraic boundaries: **17**
- Exact competing-bracket ordering checks: **5/5**
- Exact negative outside counterexamples: **17**
- Witness, direct-regression, core, root, ordering, hull, and unresolved failures: **0**

## Boundary census

The only complete segment is the left side of the inverse compressed exchange at `M=28`.

Every partial record has no internal left boundary and one internal right boundary. In all seventeen cases, the boundary occurs when the lower adjacent basic support mass `p_{j-1}` reaches zero. Every selected root is isolated by an exact rational bracket with opposite endpoint signs and a fixed nonzero derivative sign. All competing brackets are ordered using exact rational inequalities. Every selected boundary has a rational point beyond it where the responsible KKT condition is strictly negative.

## Full standalone replay

A separate standalone package independently recomputed all eighteen record files, reassembled the result and catalogue, and regenerated the figure.

- Recomputed records: **18/18**
- SHA-256 comparisons: **21/21 identical**
  - 18 record JSON files;
  - consolidated result JSON;
  - consolidated catalogue JSON;
  - generated figure.

Replay verdict: `PASS_FULL_18_RECORD_EXACT_STANDALONE_REPLAY_MATCH`.

## Repository-wide verification

- Registered main audits: **68**
- Registered gates: **1,013/1,013**
- Unit and integrity tests: **64/64**
- English PNG figures: **110**
- Python audit/tool compilation: **PASS**
- JSON parsing: **PASS**
- Manifest verification: **PASS**

## Claim boundary

A106 proves exact witness-containing continuum components only for the eighteen A95/A102 legacy gamma-minus source segments. It does not establish continuum lifting for the 922 legacy gamma-plus witnesses, coverage of complete A92 cells, an all-`M` theorem, a universal active-support law, or a physical interpretation.
