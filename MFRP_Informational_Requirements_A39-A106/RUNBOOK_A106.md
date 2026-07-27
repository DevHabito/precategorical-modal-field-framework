# A106 runbook

## Exact continuum atlas for the 18 legacy gamma-minus segments

A106 is deterministic and seed-free. From the repository root:

```bash
mkdir -p provenance/a106_legacy_gamma_minus_continuum_atlas/records
for i in $(seq 0 17); do
  PYTHONPATH=audits python audits/a106_legacy_gamma_minus_continuum_segment_atlas_audit.py \
    --record-index "$i"
done
PYTHONPATH=audits python audits/a106_legacy_gamma_minus_continuum_segment_atlas_audit.py \
  --assemble-from-record-dir
python tools/generate_a106_figure.py
```

Expected verdict:

```text
PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_18_LEGACY_GAMMA_MINUS_SEGMENTS_WITH_1_FULL_AND_17_PARTIAL_COMPONENTS
```

Expected headline counts:

- 18 unique source segments;
- 2,410 exact KKT conditions;
- 2,410/2,410 direct-matrix versus rank-one witness equalities;
- 2,428 numerator/denominator sign obligations;
- 22 sign-changing candidate roots;
- 17 selected simple right boundaries;
- 5 exact competing-bracket ordering checks;
- 17 exact negative outside counterexamples;
- 1 complete source-segment certificate;
- 17 proper strict subcomponents;
- zero witness, core, root, ordering, hull, direct-regression, or unresolved failure.

## Outputs

```text
results/a106_legacy_gamma_minus_continuum_segment_results.json
results/a106_legacy_gamma_minus_continuum_segment_catalogue.json
figures/a106_legacy_gamma_minus_continuum_segment_atlas.png
provenance/a106_legacy_gamma_minus_continuum_atlas/records/a106_record_000.json
...
provenance/a106_legacy_gamma_minus_continuum_atlas/records/a106_record_017.json
```
