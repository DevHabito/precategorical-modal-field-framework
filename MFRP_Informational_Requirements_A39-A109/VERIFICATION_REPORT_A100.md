# A100 Verification Report

A100 was verified in two independent stages.

## Discovery replay

`provenance/a100_high_precision_active_set_discovery.py` was executed at 180 decimal digits on the complete standard-form LP. Phase one reached zero artificial objective, and phase two selected:

- `P={77,78,443}`;
- `Q={0,1,221,222}`;
- active `alpha+`, `beta-`, `gamma-`.

This stage is discovery-only.

## Exact promoted replay

`audits/a100_full_lp_active_set_resolution_audit.py` independently reconstructed the candidate with exact rational arithmetic.

Verified conditions:

- 8/8 basic variables strictly positive;
- 3/3 active multipliers strictly positive;
- 881/881 unused-atom reduced costs strictly positive;
- 3/3 opposite-band slacks strictly positive;
- all exact primal residuals zero;
- exact equality of primal and dual objective values.

Total strict KKT conditions:

```text
895/895
```

Exact verdict:

```text
PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M443
```

## Independent package replay

The standalone A100 package was extracted and both discovery and exact audit were rerun. The main result and full certificate hashes match the integrated repository copies exactly:

```text
results:     65b2ae8820523d4103a6a151fdda17b56aa06769ba75ad8fe5e82836ec725ecc
certificate: 92abdf14fb21f85a96e42eb9571429b1aa5850dc9dcb41045e73d4e0cd84eca7
```

## Scientific boundary

A100 is a pointwise exact theorem for one declared finite LP contract. It is not an interval theorem, an all-support theorem, or a physical interpretation.
