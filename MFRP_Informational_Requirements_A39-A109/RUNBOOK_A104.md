# A104 runbook

## Exact continuum atlas for the seven exceptional q0/q1 segments

The computation is deterministic and seed-free. To avoid retaining all large exact-polynomial records in one process, replay each source record independently and then assemble the atlas.

From the repository root:

```bash
mkdir -p provenance/a104_exceptional_continuum_atlas
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 0
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 1
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 2
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 3
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 4
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 5
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index 6
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --assemble-from-records
python tools/generate_a104_figure.py
```

Expected verdict:

```text
PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_SEVEN_EXCEPTIONAL_Q0Q1_SEGMENTS_AS_TWO_SIDED_STRICT_SUBCOMPONENTS
```

Expected headline counts:

- 7 unique exceptional source segments;
- 3 q0/q1 gamma-inactive and 4 q0/q1 gamma-minus-active bases;
- 6,489 KKT conditions and 6,496 numerator/denominator obligations;
- 25 isolated candidate roots;
- 14 selected simple algebraic boundaries;
- 11 exact competing-bracket ordering checks;
- 14 exact negative outside counterexamples;
- zero witness, core, root, ordering, or boundary-hull failure.

## Outputs

```text
results/a104_exceptional_q0q1_continuum_segment_results.json
results/a104_exceptional_q0q1_continuum_segment_catalogue.json
figures/a104_exceptional_q0q1_continuum_segment_atlas.png
```
