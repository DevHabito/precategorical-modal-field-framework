# Verification Report — A104

## Scope

This report verifies the integrated A104 exact continuum atlas for the seven exceptional q0/q1 rational source segments routed by A102.

## Exact audit result

- Verdict: `PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_SEVEN_EXCEPTIONAL_Q0Q1_SEGMENTS_AS_TWO_SIDED_STRICT_SUBCOMPONENTS`
- Gates: **22/22**
- Source segments: **7/7**, all unique
- Architecture partition: **3** q0/q1 gamma-inactive and **4** q0/q1 gamma-minus-active
- Proper two-sided strict subcomponents: **7**
- Complete source-segment certificates: **0**
- Exact KKT conditions: **6,489**
- KKT numerators plus common denominators: **6,496**
- Sign-changing candidate roots: **25**
- Selected nearest algebraic boundaries: **14**
- Exact competing-bracket ordering checks: **11/11**
- Exact negative outside counterexamples: **14**
- Witness, core, root, ordering, and hull failures: **0**

## Boundary census

For the three gamma-inactive bases:

- lower boundary: inactive `gamma-` slack reaches zero;
- upper boundary: basic `q0` mass reaches zero.

For the four gamma-minus-active bases:

- lower boundary: active `gamma-` dual multiplier reaches zero;
- upper boundary: the lower adjacent basic `P` mass reaches zero.

Every selected root is isolated by an exact rational bracket with opposite endpoint signs and a fixed nonzero derivative sign. Competing brackets are ordered by exact rational inequalities, not decimal midpoint comparisons.

## Deterministic record replay

The seven exact records were computed in seven memory-isolated processes and stored under:

```text
provenance/a104_exceptional_continuum_atlas/
```

The final assembly loads those seven files, verifies source routing, condition counts, boundary mechanisms, root ordering, core positivity, boundary-hull positivity, and outside counterexamples.

The standalone package independently recomputed all seven records and reassembled the atlas. The consolidated result JSON, catalogue JSON, and figure are byte-identical to the integrated repository outputs.

## Repository-wide verification

- Registered main audits: **66**
- Registered gates: **977/977**
- Unit/integrity tests: **58/58**
- English PNG figures: **108**
- Python compilation: **PASS**
- JSON parsing: **PASS**
- Manifest verification: recorded after final manifest generation

## Claim boundary

A104 proves continuum persistence only for the seven exceptional A95 rational source segments. It does not establish continuum lifting for the remaining 1,056 A102 witnesses, complete A92-cell coverage, an all-`M` theorem, a universal active-support law, or a physical interpretation.
