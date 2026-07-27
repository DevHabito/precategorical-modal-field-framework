# Verification Report — A39–A92

## A92 replay

Command:

```bash
python audits/a92_exact_continuum_offset_three_window_audit.py
```

Result:

- verdict: `PASS_EXACT_CONTINUUM_DECISIVE_FACTOR_ATLAS_AND_25_LOCAL_OFFSET_THREE_WINDOWS`
- gates: `18/18`
- exact algebraic cells: `858`
- classifications: `833 negative`, `14 positive`, `11 single-root`
- strict local windows: `25`
- additional between-probe supports: `10`

## Repository tests

Command:

```bash
python -m unittest discover -s tests -v
```

Result: `33/33` tests passed.

## Evidence boundary

The A92 result is a complete continuum atlas for the decisive adjacent factor under the declared finite contract. It certifies strict local compressed maxima on twenty-five windows. It is not a continuum proof of global one-variation or global optimality over every contact.
