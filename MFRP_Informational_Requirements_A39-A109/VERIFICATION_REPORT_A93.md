# Verification Report — A93

## A93 replay

Command:

```bash
python audits/a93_exact_continuum_global_one_variation_audit.py
```

Result:

- verdict: `PASS_EXACT_FULL_SEQUENCE_CONTINUUM_ONE_VARIATION_AND_25_GLOBAL_OFFSET_THREE_WINDOWS`
- gates: `18/18`
- selected exact algebraic cells: `25`
- non-decisive interval certificates: `5,426/5,426`
- complete factor classifications: `5,451`
- full-positive global cells: `14`
- simple global maximizer transitions: `11`
- independent sparse-versus-A84 exact regressions: `108/108`

All non-decisive signs close on the first rational monotone-monomial interval enclosure over an outer hull containing the exact algebraic cell. No floating-point number decides a theorem gate.

## Repository tests

Command:

```bash
python -m unittest discover -s tests -v
```

Result: `35/35` tests passed.

## Evidence boundary

A93 proves full adjacent-factor one-variation and global **compressed-objective** maximizer phases only on the twenty-five A92 selected cells, for `10<=M<=520` and `129/1000<=s<=133/1000`. It does not certify the other 833 A92 cells, lifted KKT feasibility, arbitrary supports, or any physical interpretation.
