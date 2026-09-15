# Lean formalization pilot — MF-R009

This directory begins Consolidation 1.0's proof-kernel track.

## Current scope

`PrecategoryFormal/RepresentativeCode.lean` formalizes the encoding-level core of MF-R009:

- a five-vertex minimum-block representation;
- the two explicit A8.1 witness partitions;
- validity of both minimum-representative maps;
- exact reproduction of historical representative code `100663296`;
- inequality of the two full block assignments;
- non-injectivity of the historical representative-code map.

The witness is reconstructed from definitions inside Lean. No result from the Python A8.1 audit is imported as an axiom.

## Deliberate limitation

This first pilot does **not** yet derive the two block maps from the original directed graphs by formal reachability/SCC computation. Therefore it is an encoding-level theorem, not yet the full graph-to-code formalization of MF-R009.

The next formal obligation is to define finite directed reachability and SCCs, compute the two explicit graph witnesses, and prove that their SCC minimum maps are exactly `blockMinA` and `blockMinB`.

## Build

Pinned toolchain: Lean `v4.33.1`, mathlib `v4.33.1`.

```bash
cd formal/lean
lake update
lake build
```

The repository CI additionally runs `leanchecker` and rejects `sorry`/`admit` placeholders in Lean source files.
