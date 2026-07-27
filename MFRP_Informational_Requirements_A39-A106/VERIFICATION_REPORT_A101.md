# A101 Verification Report

A101 was verified as a deterministic exact replay.

## M443 symbolic interval replay

`audits/a101_gamma_active_interval_and_residual_closure_audit.py` reconstructed the A100 basis through an exact rank-one row update around `s=13/100`.

Verified interval conditions:

- 895 symbolic KKT conditions;
- one seven-term common denominator, strictly positive on the complete boundary hull;
- lower boundary: active `gamma-` dual multiplier;
- upper boundary: basic `p77` mass;
- both boundary roots isolated in rational intervals of width `1e-24`;
- both roots unique and simple by exact endpoint and derivative signs;
- 893/893 nonboundary numerators strictly positive on the full hull.

The certified component is the open interval between the two isolated roots.

## Final residual replay

The same gamma-active family was rebuilt exactly at the final three A99 residual witnesses.

| M | P support | Q support | Strict KKT conditions |
|---:|---|---|---:|
| 449 | `{78,79,449}` | `{0,1,224,225}` | 907/907 |
| 484 | `{84,85,484}` | `{0,1,242,243}` | 977/977 |
| 490 | `{85,86,490}` | `{0,1,245,246}` | 989/989 |

Across the three witnesses:

```text
2873/2873 strict conditions
```

Every primal system closes exactly and every primal objective equals its dual objective exactly.

## Repository verification

The integrated archive passed:

- 63/63 registered audit verdicts;
- 909/909 gates;
- 50/50 integrity tests;
- Python compilation for all audit and tool programs;
- JSON validation for all committed results;
- 105 committed PNG figures.

Exact verdict:

```text
PASS_GAMMA_ACTIVE_M443_INTERVAL_AND_THREE_OF_THREE_FINAL_RESIDUAL_RESOLUTIONS
```

## Scientific boundary

A101 closes the 83 selected A95 rational obstruction witnesses pointwise. It is not a continuous lifted-KKT theorem over all 858 cells, an all-M support law, or a physical interpretation.

## Independent standalone replay

The standalone A101 package was assembled with only the required upstream result summaries and replayed from its own root. The three promoted outputs match the integrated repository byte-for-byte:

```text
main result:          7585036b70b06b7b1bd12c9b4af23d76bcc46063967bb6e4b0494e7a7221f59a
interval certificate: ec773fee7483b31dbad520095664bdaa236071f1cb2c57a0cc5719a15e68d03b
residual atlas:       d6813d2524856862a30bae95901417e5e44aed229ea0cb2c7eedfcfc7466f716
```
