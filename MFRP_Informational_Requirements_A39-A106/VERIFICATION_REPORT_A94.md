# Verification Report — A94

## A94 replay

Command:

```bash
python audits/a94_exact_all_cell_continuum_one_variation_audit.py
```

Result:

- verdict: `PASS_EXACT_CONTINUUM_ALL_858_CELL_ONE_VARIATION_AND_205_GLOBAL_ADJACENT_TRANSITIONS`
- gates: `24/24`
- exact algebraic cells: `858/858`
- non-decisive factor classifications: `124,956`
- complete factor classifications: `125,814`
- fixed unique-global-maximizer cells: `653`
- simple adjacent global-transition cells: `205`
- strict-convexity fallback roots: `12`
- independent sparse-versus-A84 exact regressions: `48/48`

All theorem decisions use exact rational arithmetic. Direct rational outer-hull enclosures settle 119,984 factors; adaptive interval, derivative, and strict-convexity certificates settle the remaining 4,972.

## Repository tests

Command:

```bash
python -m unittest discover -s tests -v
```

Result: `37/37` tests passed.

## Evidence boundary

A94 proves one-variation and the resulting global **compressed-objective** phase classification only on the 858 A92 algebraic cells, for the declared finite support and probe interval. It does not certify lifted full-KKT feasibility, arbitrary support sizes, another probe interval, spacetime, matter, or pre-temporal physics.
