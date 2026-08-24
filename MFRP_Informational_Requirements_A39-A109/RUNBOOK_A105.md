# A105 runbook

## Exact continuum atlas for the 40 legacy two-band segments

A105 is deterministic and seed-free. Each record is best replayed in a separate process because the exact sparse-polynomial certificates become large for the highest supports.

From the repository root:

```bash
mkdir -p provenance/a105_legacy_two_band_continuum_atlas/records
for i in $(seq 0 39); do
  python audits/a105_legacy_two_band_continuum_segment_atlas_audit.py \
    --record-index "$i"
done
python audits/a105_legacy_two_band_continuum_segment_atlas_audit.py \
  --assemble-from-record-dir
python tools/generate_a105_figure.py
```

The record loop may be parallelized safely because every index writes a distinct file:

```bash
seq 0 39 | xargs -I{} -P8 \
  python audits/a105_legacy_two_band_continuum_segment_atlas_audit.py \
  --record-index {}
python audits/a105_legacy_two_band_continuum_segment_atlas_audit.py \
  --assemble-from-record-dir
```

Expected verdict:

```text
PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_40_LEGACY_TWO_BAND_SEGMENTS_WITH_0_FULL_AND_40_PARTIAL_COMPONENTS
```

Expected headline counts:

- 40 unique legacy two-band source segments;
- 24,312 exact KKT conditions;
- 24,352 numerator/denominator sign obligations;
- 181 sign-changing candidate roots;
- 80 selected locally unique simple boundaries;
- 101 exact competing-bracket ordering checks;
- 80 exact negative outside counterexamples;
- 0 complete source-segment certificates;
- 40 proper strict subcomponents;
- zero witness, core, root, ordering, hull, or unresolved failure.

## Outputs

```text
results/a105_legacy_two_band_continuum_segment_results.json
results/a105_legacy_two_band_continuum_segment_catalogue.json
figures/a105_legacy_two_band_continuum_segment_atlas.png
provenance/a105_legacy_two_band_continuum_atlas/records/a105_record_000.json
...
provenance/a105_legacy_two_band_continuum_atlas/records/a105_record_039.json
```
