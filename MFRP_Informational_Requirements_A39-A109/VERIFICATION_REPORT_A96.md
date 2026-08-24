# Verification Report — A96

## Scope

This report verifies the A39–A96 repository after integrating the exact unrestricted full-LP resolution of the first A95 obstruction.

## A96 replay

Command:

```bash
python audits/a96_full_lp_active_set_resolution_audit.py
```

Result:

```text
PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M125
```

The replay reconstructed the exact basis

```text
P = [23, 24, 125]
Q = [1, 62, 63]
active bands = alpha+, beta-
```

and passed 22/22 gates. The exact certificate contains 259 strict KKT conditions, including all 246 unrestricted nonbasic atom reduced costs.

## Regression tests

```text
41/41 tests passed
```

## Repository totals

- 58 registered audits: A39–A96
- 801 registered gates: all passed
- 100 PNG figures
- exact JSON parsing: passed
- Python compilation for audits and tools: passed
- manifest hashes: passed after release materialization

## Evidence boundary

The high-precision simplex record is discovery provenance. The theorem is established independently by the exact rational KKT audit. A96 is a point theorem at `M=125`, `s=33/250`; it is not an interval theorem, an all-support theorem, or a physical result.
