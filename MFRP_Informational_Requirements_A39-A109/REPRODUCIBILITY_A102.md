# Reproducibility notes — A102

## Claim class

A102 is an exact finite database-closure audit. It merges the 1,063 rational phase-segment witnesses introduced by A95 and assigns one strict finite-LP KKT certificate to every key.

It is not a continuum lift theorem.

## Inputs

A102 freezes 18 source files from A95, A97, A98, A99, A100, and A101. Their SHA-256 hashes are written to:

```text
provenance/a102_complete_atlas/a102_source_certificate_hashes.json
```

## Exact layers

1. The complete A95 witness key set is read and checked for uniqueness.
2. The 980 natural A95 passes are validated against the exact source verdict, unique branch classification, and fixed finite-LP KKT census `2*M+9`.
3. The 83 A95 obstructions are matched exactly to the A97 catalogue.
4. The A97, A98/A99, and A100/A101 resolution sets are checked for disjointness and exact union with the 83 obstruction keys.
5. The full A98 and A100 rational certificates are parsed condition by condition.
6. All 83 post-A95 resolutions are independently recomputed.
7. A deterministic stratified set of 100 natural lifts is independently recomputed: all 40 compressed, all 18 gamma-minus, and 42 support-spread gamma-plus cases.

The independent replay layer contains 183 branches and is seed-free.

## Commands

```bash
python audits/a102_complete_rational_witness_lift_atlas_audit.py --workers 8
python tools/generate_a102_figure.py
```

The audit should return:

```text
PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS
```

with 23/23 gates.

## Determinism

The replay uses multiprocessing only to distribute independent exact rational KKT evaluations. Output rows are sorted by the frozen A95 key before serialization.

## Boundaries

A102 establishes pointwise closure only. It does not certify that a witness basis remains valid on the entire parent A94 phase segment. Only A97, A99, and A101 currently provide interval persistence for representative bases.
