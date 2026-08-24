# A102 runbook

## Complete exact rational-witness lift atlas

From the repository root:

```bash
python audits/a102_complete_rational_witness_lift_atlas_audit.py --workers 8
python tools/generate_a102_figure.py
```

Expected verdict:

```text
PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS
```

Expected headline counts:

- 1,063 unique rational witness keys;
- 980 legacy natural lifts;
- 76 endpoint-released gamma-inactive lifts;
- 3 q0/q1 gamma-inactive lifts;
- 4 q0/q1 gamma-active lifts;
- 676,847 exact KKT conditions in the merged source atlas;
- 183 independent A102 replays;
- zero replay failure and zero source/replay mismatch.

The audit imports the A78, A97, A99, and A101 exact evaluators. Eight workers are a practical default; lower worker counts reduce memory pressure.

## Outputs

```text
results/a102_complete_rational_witness_lift_atlas_results.json
results/a102_complete_rational_witness_lift_atlas_catalogue.json
provenance/a102_complete_atlas/a102_source_certificate_hashes.json
figures/a102_complete_rational_witness_lift_atlas.png
```
