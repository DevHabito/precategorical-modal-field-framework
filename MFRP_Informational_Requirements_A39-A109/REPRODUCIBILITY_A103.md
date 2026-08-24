# Reproducibility notes — A103

## Claim class

A103 is an exact continuum classification for the 76 A95 rational inner phase segments assigned by A102 to the endpoint-released, gamma-inactive architecture. It is not a continuous theorem for the other 987 witnesses and not a theorem on complete A92 cells.

## Exact symbolic layer

Only the active alpha row depends on the probe `s`. The audit applies an exact Sherman–Morrison rank-one row update around the dyadic reference `s=1/8`. Basic variables, active multipliers, unused-atom reduced costs, inactive-band slacks, and the common basis denominator are represented as sparse integer polynomials after exact orientation.

The complete census contains 54,944 KKT conditions plus 76 common denominators, hence 55,020 exact sign obligations. Integer interval arithmetic, derivative signs, and concavity certificates are used; no floating-point tolerance controls a gate.

## Chunked replay

The 76 independent records are stored in five deterministic chunks:

```text
provenance/a103_continuum_atlas/a103_chunk_000_016.json
provenance/a103_continuum_atlas/a103_chunk_016_032.json
provenance/a103_continuum_atlas/a103_chunk_032_048.json
provenance/a103_continuum_atlas/a103_chunk_048_064.json
provenance/a103_continuum_atlas/a103_chunk_064_076.json
```

Recompute a chunk with:

```bash
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py \
  --chunk-start 0 --chunk-end 16 --workers 8 \
  --chunk-output provenance/a103_continuum_atlas/a103_chunk_000_016.json
```

After all chunks exist, assemble and verify the committed atlas:

```bash
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py
python tools/generate_a103_figure.py
```

Expected verdict:

```text
PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS
```

with 23/23 gates.

## Boundary meaning

A selected algebraic boundary is certified by opposite exact endpoint signs and a fixed nonzero derivative sign on its isolating bracket. Every nonselected condition is certified positive on the complete relevant boundary hull. Every proper component has an exact rational point outside at which the selected condition is negative.

## Scope

The certified objects are the A95 rational inner source segments. Excluded algebraic root brackets, larger A92 cells, arbitrary `M`, different target/mean/noise contracts, and physical interpretations are outside the theorem.
