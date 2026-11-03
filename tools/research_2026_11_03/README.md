# Independent exact regression checkpoint — 2026-11-03

These scripts preserve the calculations I actually ran for C2/F3 and the frozen A113 small-left case. They are separate from the historical project test modules. They do **not** constitute a Lean or general-theorem certification.

Environment used: Python 3.13.5; SymPy 1.14.0 (consistent with the repository's pinned \`requirements.txt\`); \`fractions.Fraction\` from Python's standard library. No floating-point tolerance determines a pass. The A113 all-contact script **reuses** definitions from the 60-case script, so the two finite suites do not count as independent numerical models.

Run from the repository root:

~~~bash
python -m py_compile tools/research_2026_11_03/*.py
python tools/research_2026_11_03/pmff_independent_audit_2026-11-03.py
python tools/research_2026_11_03/pmff_a113_independent_remainder_2026-11-03.py
python tools/research_2026_11_03/pmff_a113_all_contacts_2026-11-03.py
~~~

The first and second scripts import \`sympy\`; the third requires only standard-library packages plus the adjacent second script. Exact outputs from the November 3 re-execution are in \`results/\`, captured as evidence rather than generated source of mathematical assumptions.

| Script | Executed scope | Observed outcome |
| --- | --- | --- |
| pmff_independent_audit_2026-11-03.py | four-point F3 witness, cubic identity, nullspace, negative control, A113 generating function and margin | PASS |
| pmff_a113_independent_remainder_2026-11-03.py | symbolic A83/A84 identity, sign-mutation negative control, 60 rational M/s/k cases | PASS |
| pmff_a113_all_contacts_2026-11-03.py | 336 exact rational cases, all contacts 2..29 over four M and three s values | PASS |

The 60 configurations are a subset of the 336 configurations. None of these scripts runs Lean. Refer to \`../../consolidation/A113_SMALL_LEFT_CLOSURE_CHECKPOINT_2026-11-03.md\` for the mathematical derivation and unresolved assurance gates.

## A113 beta/source gap (next analytic obligation)

`pmff_a113_delta_channels.py` independently checks the original finite-M parity-sensitive H definitions and the exact source-minus-beta normalized gap in 21 rational test cases, with a deliberate sign-orientation negative control. The continuous uniform gap bound is **not** proven by these samples. See `../../consolidation/A113_DELTA_CHANNEL_AUDIT_2026-11-03.md`.

The exact central-pair symbolic checks also completed successfully in GitHub Actions [41721969226](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41721969226). The extended finite Delta regression completed successfully in [41722823626](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41722823626). Neither finite result proves the entire A113 sign theorem. The central-pair **algebraic** result is separately Lean-certified in [41721969228](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41721969228).
