# Changelog — A95

## Added

- `audits/a95_rational_witness_lift_obstruction_audit.py`
- `results/a95_rational_witness_lift_results.json`
- `results/a95_rational_witness_lift_catalogue.json`
- `docs/technical_notes/MFRP_next_step_rational_witness_lift_obstruction.md`
- `tools/generate_a95_figure.py`
- `figures/a95_rational_witness_lift_atlas.png`
- `RUNBOOK_A95.md`
- `REPRODUCIBILITY_A95.md`
- `VERIFICATION_REPORT_A95.md`

## Result

A95 classifies 1,063 exact open phase-segment witnesses from A94. The natural lift triad passes uniquely on 980 segments and fails on 83. At the first obstruction, `M=125`, `s=33/250`, all 370 previously declared F2/F3 candidates fail the complete strict KKT system. The exhaustive obstruction prefix through `M=325` contains 19,421 candidate evaluations and zero strict passes.

## Boundary

The result is a rational-witness and restricted-family obstruction theorem. It is not a continuum lifted-KKT atlas and does not identify the missing full-LP active set.
