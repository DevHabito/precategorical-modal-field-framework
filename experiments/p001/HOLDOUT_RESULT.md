# P-001 — Frozen holdout result and independent audit

**Evaluation date:** 2026-10-03  
**Protocol:** `experiments/p001/PROTOCOL.md`  
**Holdout lock:** `experiments/p001/HOLDOUT_LOCK.md`  
**Successful holdout implementation commit:** `f59ae55cccdd44a913a1ab1d0eaec959afc0894f`  
**GitHub Actions run:** `37135812573`  
**Artifact digest:** `sha256:07a6cb74ebe7bbbb2fdb5e1fff46860ffaa4522ae6320b63b00970db7f294479`

## 1. Frozen verdict

[
oxed{	ext{P-001 = INCONCLUSIVE under the preregistered verdict contract}}
]

P-001 did **not** pass.

The primary directional gain was positive only by

[
G_{m obs}
=
1.4870565041931886	imes10^{-6}
quad	ext{nats/trip},
]

and its preregistered weekly-bootstrap interval crossed zero.

The preregistered structural prediction was not merely uncertain: it pointed in the opposite direction.

[
eta
=
-0.922424213659756,
]

with a 95% weekly-bootstrap interval entirely below zero.

The result therefore supplies no positive empirical support for the proposed P-001 bridge.

## 2. Exact holdout output

TRAIN remained January–June 2023.

VALIDATION July–August 2023 was not loaded by the holdout executable.

The untouched evaluation period was September–December 2023.

Exact summary emitted by the frozen run:

| Quantity | Holdout value |
|---|---:|
| scored trips | 12979407 |
| scored source-hour blocks | 11755 |
| calendar-week bootstrap units | 18 |
| unseen zone/hour-of-week pickups | 4379 |
| unseen pickup fraction | 0.0003373805906541031 |
| MICRO log-loss | 0.40364683782610206 |
| MACRO log-loss | 0.40364832488260627 |
| (G_{m obs}=L_{m macro}-L_{m micro}) | 1.4870565041931886e-06 |
| 95% weekly-bootstrap CI for (G_{m obs}) | [-5.771282139244516e-05, 6.066970491865039e-05] |
| weighted predicted (D_{m KL}(p_{m micro}|p_{m macro})) | 0.00029258436389281934 |
| structural slope (eta) | -0.922424213659756 |
| 95% weekly-bootstrap CI for (eta) | [-1.1388473270879926, -0.7470484009281131] |
| composition-alignment permutations | 999 |
| permutation-null mean gain | -0.0009157766388742871 |
| permutation-null 99th percentile | -0.0008252588892372212 |
| one-sided permutation p-value | 0.001 |

The automatic code-level verdict was `INCONCLUSIVE`, exactly as specified in the frozen contract: (G_{m obs}>0), but the lower endpoint of the primary bootstrap interval was not positive.

## 3. Why the permutation p-value is not a rescue

The permutation result does **not** make P-001 a success.

The null deliberately destroys the temporal alignment between current microscopic pickup composition and the MICRO prediction while keeping source borough, hour-of-week, macro prediction, and outcomes fixed. These deliberately mismatched MICRO predictions were strongly harmful on average:

[
G_{m null,mean}
=
-0.0009157766388742871.
]

The correctly aligned MICRO prediction was therefore much better than a wrongly aligned MICRO prediction.

That is compatible with microscopic composition carrying information.

It does **not** establish the preregistered claim that the frozen occupancy-preserving predictor improves over the occupancy-erasing MACRO comparator. Relative to MACRO, its observed gain was essentially zero at the declared sampling resolution.

## 4. Structural prediction

Before outcomes were used, each block had the predicted separation

[
S_{At}
=
D_{m KL}
left(
widehat p_{m micro}
middle|
widehat p_{m macro}
ight).
]

P-001 predicted that blocks with larger structural separation would, on average, show larger realized MICRO gain, summarized by the through-origin weighted coefficient

[
eta
=
rac{sum N_{At}S_{At}g_{At}}
{sum N_{At}S_{At}^{2}}.
]

The holdout instead gave

[
eta=-0.922424213659756
]

with

[
CI_{95%}
=
[-1.1388473270879926,-0.7470484009281131].
]

This preregistered structural subprediction is contradicted in the declared holdout.

The most conservative reading is not that the exact coarse-graining identity is false. The identity is conditional on the relevant transition rows. P-001 introduced an empirical bridge: transition rows estimated from January–June and conditioned only on zone and hour-of-week were assumed to transport well enough to September–December for current occupancy variation to yield the predicted advantage. The holdout does not support that bridge.

## 5. Independent arithmetic audit

After the successful workflow finished, the exported `block_scores.csv` was recomputed independently from the compact artifact rather than by reusing the experiment's summary function.

The independent calculation reproduced:

- scored trips: `12979407`;
- MICRO log-loss: `0.40364683782610206`;
- MACRO log-loss: `0.4036483248826062` (last decimal differs only from summation order);
- gain: `1.4870565041862648e-06`;
- weighted predicted KL separation: `0.000292584363892809`;
- structural slope: `-0.9224242136597579`;
- unseen fraction: `0.0003373805906541031`.

A second independent reconstruction of the 10000 weekly bootstraps using seed `20261003` reproduced:

[
CI_{95%}(G)
=
[-5.771282139244516	imes10^{-5},
6.066970491865039	imes10^{-5}]
]

and

[
CI_{95%}(eta)
=
[-1.1388473270879926,
-0.7470484009281131].
]

No arithmetic discrepancy relevant to the verdict was found.

## 6. Post-hoc diagnostics — not part of the verdict

These diagnostics were computed only **after** the frozen holdout result and cannot be used to redefine P-001.

### By calendar month

| Month | Trips | Gain | Predicted KL | Structural slope |
|---|---:|---:|---:|---:|
| 2023-09 | 2817305 | -1.829347626122e-06 | 0.000329747... | -0.757855... |
| 2023-10 | 3489925 | -7.115016613e-05 | 0.0002138... | -1.177157... |
| 2023-11 | 3311889 | 4.64e-05 approximately | 0.000261... | -0.898357... |
| 2023-12 | 3360288 | 3.6e-05 approximately | 0.000374... | -0.953330... |

The primary gain changes sign across months. The structural slope remains negative in every month.

The approximate month-level display above is diagnostic only; the canonical exact aggregate values are those in Sections 2 and 5.

### By source borough

The post-hoc decomposition shows substantial heterogeneity:

- Bronx: MICRO worse overall; high unseen-row fraction relative to the aggregate.
- Brooklyn: MICRO worse overall.
- Manhattan: small positive MICRO gain.
- Queens: positive MICRO gain.
- Staten Island: very sparse and dominated by unseen zone/hour-of-week rows; not a stable standalone diagnostic.

No borough is removed or promoted after seeing these results.

### Seen versus unseen rows

Blocks with no unseen zone/hour-of-week pickup contribution still did not restore the preregistered structural direction. Therefore the negative aggregate structural result cannot be dismissed solely as an unseen-row fallback artifact.

## 7. Provenance of implementation failures before the successful run

Two implementation problems occurred and are retained in the audit trail.

1. An automatically generated holdout file initially contained a literal escaped newline in source. It was detected by source inspection before holdout execution and corrected without changing any scientific quantity.
2. The first holdout workflow attempt compiled and passed the synthetic self-test, then immediately hit the inherited prevalidation assertion
   `ALLOWED_MONTHS == tuple(range(1, 9))`.
   That assertion executes before the data directory and download loop, so the attempt stopped before downloading or reading any September–December file.

The month guard was then changed only to the already frozen holdout set

[
(1,2,3,4,5,6,9,10,11,12),
]

with July and August explicitly excluded.

The successful holdout run followed.

## 8. Input hashes for the successful holdout run

### Zone lookup

`nyc_taxi_zones.json`

`2b51bd2e40f6a1f74d0986abd39b5286451874277b1ebad9e2ec38d8043bb450`

### TRAIN

- 2023-01: `32df6f67578fa86c484a6b5ef23a5281992ff085521082340b0f9e5889e9a572`
- 2023-02: `4809e6aaac64f05a62d16a25d55713be1537ad64fc261e895eaf2d2120fe750a`
- 2023-03: `e7d44943111b007bf0e7084863511886e0db29f862f9a96239383a1f86c6c26e`
- 2023-04: `95c01c53c865e06489179bdecce3a59603697a1557c4d5d183c20ae13a144dc6`
- 2023-05: `9bd7d1c557bb9d0413619ba296b4828b884852a70bd07f2230b83f080d9a8591`
- 2023-06: `3e60e29b5df45683948b68acbfb503aa459d14162c610622585c6580fdbfc73a`

### HOLDOUT

- 2023-09: `091bf156bea5bb10bd217f5f12375f966f8789349af45d5ee4153e3e1e077a87`
- 2023-10: `dc5f069476d350df802ed8120f3b39ec321c34cfa905381e87f608c78ca0c645`
- 2023-11: `af203de0e73a92d640121f02a34326f25037d62380fc406237c87c2a4231ae58`
- 2023-12: `ab4f4db11cb31484747f62eb507c13fcfaff290aaf59c13e6465dea0b1166b9c`

## 9. Scientific conclusion

P-001 asked whether preserving current within-borough pickup composition, combined with transition rows learned from the frozen training period, would yield a preregistered out-of-sample improvement in macroscopic destination prediction.

It did not establish that claim.

The aggregate gain was indistinguishable from zero under the declared weekly resampling, and the structural calibration prediction had the opposite sign.

This is a result about the proposed empirical bridge, not a refutation of the underlying algebraic identity.

Accordingly:

[
oxed{
	ext{P-001 provides no positive empirical evidence for RZS or a Modal Field interpretation.}
}
]

It also does not show that occupancy is irrelevant in real mobility systems. The permutation diagnostic in fact shows that deliberately misaligning composition is substantially harmful. What failed is the stronger frozen predictive construction as specified.

No post-hoc change is permitted to turn P-001 into a positive result.

## 10. What may legitimately happen next

Any follow-up must receive a new identifier and a new preregistration.

A scientifically justified next question is why the exact conditional aggregation principle failed to become a calibrated out-of-sample predictor under a fixed transition law estimated months earlier.

Candidate explanations include transition-law drift, omitted time/context variables, estimator error in sparse microscopic rows, or the fact that the declared state representation is insufficient for transport across months.

Those are hypotheses for a future P-002, not repairs to P-001.
