# A103 runbook

## Exact continuum atlas for the 76 endpoint-released segments

The full computation is deterministic and seed-free. It can be replayed in independent exact chunks to control memory and wall-clock use.

From the repository root:

```bash
mkdir -p provenance/a103_continuum_atlas
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py --chunk-start 0  --chunk-end 16 --workers 8 --chunk-output provenance/a103_continuum_atlas/a103_chunk_000_016.json
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py --chunk-start 16 --chunk-end 32 --workers 8 --chunk-output provenance/a103_continuum_atlas/a103_chunk_016_032.json
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py --chunk-start 32 --chunk-end 48 --workers 8 --chunk-output provenance/a103_continuum_atlas/a103_chunk_032_048.json
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py --chunk-start 48 --chunk-end 64 --workers 8 --chunk-output provenance/a103_continuum_atlas/a103_chunk_048_064.json
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py --chunk-start 64 --chunk-end 76 --workers 8 --chunk-output provenance/a103_continuum_atlas/a103_chunk_064_076.json
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py
python tools/generate_a103_figure.py
```

Expected verdict:

```text
PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS
```

Expected headline counts:

- 76 unique source segments;
- 25 complete-segment certificates;
- 51 proper witness-containing strict components;
- 54,944 KKT conditions and 55,020 numerator/denominator sign obligations;
- 55 selected algebraic boundaries, all locally unique and simple;
- 55 exact negative outside counterexamples;
- zero core, root, hull, or routing failure.

## Outputs

```text
results/a103_endpoint_released_continuum_segment_results.json
results/a103_endpoint_released_continuum_segment_catalogue.json
figures/a103_endpoint_released_continuum_segment_atlas.png
```
