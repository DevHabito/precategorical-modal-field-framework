# Verification Report — A95

## Audit

`A95_EXACT_RATIONAL_WITNESS_LIFT_AND_RESTRICTED_FAMILY_OBSTRUCTION`

## Verdict

```text
PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION
```

## Exact replay method

The packaging environment imposes a short per-command execution cap. The exact A95 replay was therefore executed in deterministic, disjoint chunks rather than promoted from a partial single-shot run.

The committed provenance contains:

- 30 nonoverlapping natural-lift fragments;
- 1,063 total records and 1,063 unique merge keys;
- 5 nonoverlapping exhaustive-prefix fragments;
- 29 obstruction witnesses;
- 19,421 exhaustive candidate evaluations;
- zero strict passes in the exhaustive prefix.

The provenance verdict is:

```text
PASS_CHUNKED_EXACT_REPLAY_PROVENANCE
```

## Result checks

The merged exact result reports:

- 858 source A94 cells;
- 1,063 open phase-segment witnesses;
- 3,189 natural-lift candidate KKT evaluations;
- 980 segments with exactly one strict natural lift;
- 83 segments with no strict natural lift;
- zero segments with multiple strict lifts;
- 75 support sizes containing at least one obstruction;
- first obstruction at `M=125`, `s=33/250`;
- 370/370 old-family candidates rejected at the first obstruction;
- 19,421/19,421 old-family candidates rejected in the declared prefix through `M=325`.

All A95 gates pass:

```text
22/22
```

## Independent integrity checks

The repository unit suite verifies the A39–A95 registry, all JSON outputs, all technical notes, the A95 result counts, the A95 catalogue, and the chunked replay provenance.

The standalone A95 package includes a separate two-test integrity suite for the committed result and catalogue.

No floating-point quantity decides a KKT status. The plotted coordinates are presentation-only.

## SHA-256 reference hashes

```text
005aefe165635744e57f78e49189cbf7acbe19c57c9080aaeeb967ec77e35b3a  results/a95_rational_witness_lift_results.json
326edd554a3e4b0b3a74e2f985aef462c826910d5f708cefa1cfe5d011e96b85  results/a95_rational_witness_lift_catalogue.json
c544592f87f60835f86a04b094d5d99bbe9bbf54acd465f58c1043107c404b9e  provenance/a95_chunked_replay/a95_chunked_replay_manifest.json
830bb66faceba99974ee000c228972d22eb0f29605ae764b9792bc4d5dc44b5a  figures/a95_rational_witness_lift_atlas.png
```

## Claim boundary

The verification supports a rational-witness lift atlas and a restricted-family obstruction theorem. It does not support a continuum lifted-KKT theorem, a complete LP-basis classification, a universal support-size law, or a physical interpretation.

## Final package verification

```text
repository audit results: 57
registered gates: 779/779
English figures: 99
unit tests: 40/40
tracked files excluding manifests: 493
status: PASS
```

The standalone package integrity suite passes `3/3` tests.
