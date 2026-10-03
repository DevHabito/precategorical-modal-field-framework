# P-002 — Frozen result and independent audit

**Evaluation date:** 2026-10-03  
**Protocol:** `experiments/p002/PROTOCOL.md`  
**Protocol commit:** `cb081a071c169356ca7cd5311784d0e6f68ac8eb`  
**Evaluation implementation commit:** `c96700219a3fce11b3a8e4f59a896290a91a6c07`  
**GitHub Actions run:** `37137258184`  
**Workflow artifact digest:** `sha256:28f641455f7c26a5c8f48ee7929dfe62631de1f889d76878541fad7dcad696ac`

## 1. Frozen verdict

[
oxed{	ext{P-002 = PARTIAL}}
]

The central RECENT-versus-STALE prediction passed strongly.

The proposed link back to P-001 did not.

Therefore P-002 supports a narrow empirical claim of temporally relevant transition-law change at the declared 8-week scale, but it does **not** establish that temporal drift explains the P-001 failure.

## 2. Untouched 2024 evaluation

The target set contained exactly 52 complete weeks:

[
2024	ext{-}01	ext{-}01
le t <
2024	ext{-}12	ext{-}30.
]

Scored trips:

[
N=40846699.
]

The three aggregate log-losses were

[
L_R=0.3809613488726864,
]

[
L_S=0.38287234743888654,
]

[
L_F=0.38052501926014964.
]

Thus the preregistered primary gain was

[
oxed{
G_{RS}
=
L_S-L_R
=
0.001910998566200111
}
]

nats per trip.

The 8-week moving-block-bootstrap 95% interval was

[
oxed{
[0.0010489932842793505,,
0.0027492503943091413]
}.
]

The entire interval is positive.

RECENT therefore predicted 2024 destinations better than the equally sized STALE model under the declared protocol.

## 3. Structural gate

The target-source-weighted RECENT-versus-STALE model separation was

[
D_{RS}=0.011723139961741657.
]

The preregistered through-origin coefficient was

[
eta_{RS}=0.16152493891391043
]

with moving-block-bootstrap interval

[
[0.08322804736546102,,
0.23459892466581173].
]

Under the literal preregistered contract, this gate passes.

### Important audit limitation

The protocol text informally motivated (eta_{RS}>0) by saying that weeks with larger (D_{RS}(w)) should tend to show a larger realized RECENT advantage.

The chosen through-origin coefficient is not sufficient to establish that stronger monotonic relationship.

If weekly gains are mostly positive regardless of the variation in (D_{RS}), the through-origin coefficient can be positive even with little or no positive association between drift magnitude and gain magnitude.

After the frozen result was opened, post-hoc diagnostics gave:

[
r_{m Pearson}(D_{RS},g_{RS})
=
-0.025292733029059176,
]

and

[
ho_{m Spearman}(D_{RS},g_{RS})
=
0.13890548962691027.
]

These post-hoc quantities do not change the frozen P-002 verdict. They do limit interpretation of the structural gate.

Accordingly, P-002 may claim that RECENT systematically outperformed STALE and that the preregistered through-origin statistic was positive. It must **not** claim that a calibrated monotonic drift-magnitude law was demonstrated.

Any future test of that stronger statement requires a new preregistration with a statistic that actually tests centered association or calibration.

## 4. Link to P-001

The P-001 FROZEN model was estimated from

[
2023	ext{-}01	ext{-}01
le t <
2023	ext{-}07	ext{-}01.
]

The preregistered RECENT-versus-FROZEN gain was

[
oxed{
G_{RF}
=
L_F-L_R
=
-0.0004363296125367647
}.
]

Its 8-week moving-block-bootstrap 95% interval was

[
[-0.001357723501356603,,
0.0005528735152803497].
]

Thus RECENT did not outperform FROZEN in the aggregate. In fact, the point estimate favored FROZEN.

The secondary drift quantity was

[
D_{RF}=0.013009135821578324,
]

with

[
eta_{RF}=-0.02983089078216639.
]

Therefore the simple explanation

> P-001 failed because its January-June 2023 transition law was too stale, and a recent 8-week law fixes the problem

is not supported by P-002.

## 5. Independent arithmetic audit

The compact workflow artifact was downloaded and `weekly_scores.csv` was recomputed independently from the experiment summary code.

The independent reconstruction gave:

- trips: `40846699`;
- RECENT log-loss: `0.3809613488726864`;
- STALE log-loss: `0.3828723474388865`;
- FROZEN log-loss: `0.38052501926014953`;
- (G_{RS}): `0.0019109985662000594`;
- (G_{RF}): `-0.0004363296125367654`;
- weighted (D_{RS}): `0.011723139961741602`;
- weighted (D_{RF}): `0.013009135821578277`;
- (eta_{RS}): `0.16152493891390687`;
- (eta_{RF}): `-0.029830890782166684`;
- RECENT unseen-row fraction: `0.0009800547162942103`;
- STALE unseen-row fraction: `0.0012214940551254828`;
- FROZEN unseen-row fraction: `0.0007358244542600615`.

The final-decimal differences relative to the workflow summary are consistent with floating-point summation order.

A separate reimplementation of the preregistered 10000-replicate moving-block bootstrap with seed `20261003` reproduced:

[
CI_{95%}(G_{RS})
=
[0.0010489932842793117,,
0.0027492503943090806],
]

[
CI_{95%}(G_{RF})
=
[-0.0013577235013565725,,
0.0005528735152803218],
]

and

[
CI_{95%}(eta_{RS})
=
[0.08322804736545819,,
0.2345989246658077].
]

No arithmetic discrepancy relevant to the verdict was found.

## 6. Post-hoc sign diagnostics

These diagnostics were computed only after the frozen evaluation and do not redefine P-002.

Of the 52 target weeks:

- (g_{RS}>0) in **49** weeks;
- (g_{RS}le0) in **3** weeks;
- (g_{RF}>0) in **26** weeks;
- (g_{RF}le0) in **26** weeks.

The three non-positive RECENT-versus-STALE weeks began:

- 2024-08-26;
- 2024-09-09;
- 2024-09-16.

This is consistent with a broad recency advantage relative to an equally sized older window, while the FROZEN comparison is much less uniform.

## 7. Post-hoc aggregation by target-week start month

The following aggregation groups each seven-day target week by the month in which that week begins. It is diagnostic only.

| start month | weeks | trips | (G_{RS}) | (G_{RF}) | (D_{RS}) | through-origin (eta_{RS}) |
|---|---:|---:|---:|---:|---:|---:|
| 2024-01 | 5 | 3364956 | 0.0009005115734990039 | -0.0038990876995993852 | 0.010641947467382873 | 0.08543561349839023 |
| 2024-02 | 4 | 2919338 | 0.0008803957173108961 | -0.0032479167171840114 | 0.011243487798108092 | 0.07944447236871632 |
| 2024-03 | 4 | 3232679 | 0.0022813145852400283 | -0.002208385087400916 | 0.01193163069876786 | 0.19117726015185463 |
| 2024-04 | 5 | 4135516 | 0.003971479672703554 | -0.0003036905953614822 | 0.01171191216860424 | 0.3404988066663683 |
| 2024-05 | 4 | 3311436 | 0.0031581220102370354 | 0.0001187290154954395 | 0.011629336413054353 | 0.2705525791593744 |
| 2024-06 | 4 | 3288384 | 0.0016450730385557792 | 0.0005734818783140422 | 0.011139622298249378 | 0.14896551414864864 |
| 2024-07 | 5 | 3488676 | 0.001222814387019821 | 0.0009568838695570772 | 0.011253335049875973 | 0.11113107454736057 |
| 2024-08 | 4 | 2633177 | 0.0000662473871298243 | 0.00013992669092020672 | 0.01302351052964397 | -0.00043413418120936633 |
| 2024-09 | 5 | 4211399 | 0.0000569885915023247 | -0.0002974692784573064 | 0.012442928178676885 | 0.00203898376376414 |
| 2024-10 | 4 | 3537201 | 0.003438929094493867 | 0.0006642356904664593 | 0.012514687177906374 | 0.27752186025117465 |
| 2024-11 | 4 | 3333387 | 0.0022724326071324147 | 0.0011600395350925268 | 0.012308795576778477 | 0.18462591317707233 |
| 2024-12 | 4 | 3390550 | 0.0024691202693306663 | 0.0006562305733097695 | 0.010859514031145349 | 0.2242702194110024 |

Every start-month aggregate has (G_{RS}>0), but the magnitude varies substantially.

The RECENT-versus-FROZEN contrast changes sign across the year: FROZEN is strongly favored early in 2024, while RECENT is often favored later.

This pattern was not a preregistered seasonal hypothesis and must not be promoted to a confirmed seasonal law.

## 8. Input provenance

The official zone lookup hash was

`2b51bd2e40f6a1f74d0986abd39b5286451874277b1ebad9e2ec38d8043bb450`.

### Frozen 2023 inputs

- 2023-01: `32df6f67578fa86c484a6b5ef23a5281992ff085521082340b0f9e5889e9a572`
- 2023-02: `4809e6aaac64f05a62d16a25d55713be1537ad64fc261e895eaf2d2120fe750a`
- 2023-03: `e7d44943111b007bf0e7084863511886e0db29f862f9a96239383a1f86c6c26e`
- 2023-04: `95c01c53c865e06489179bdecce3a59603697a1557c4d5d183c20ae13a144dc6`
- 2023-05: `9bd7d1c557bb9d0413619ba296b4828b884852a70bd07f2230b83f080d9a8591`
- 2023-06: `3e60e29b5df45683948b68acbfb503aa459d14162c610622585c6580fdbfc73a`

### Adaptive history 2023

- 2023-09: `091bf156bea5bb10bd217f5f12375f966f8789349af45d5ee4153e3e1e077a87`
- 2023-10: `dc5f069476d350df802ed8120f3b39ec321c34cfa905381e87f608c78ca0c645`
- 2023-11: `af203de0e73a92d640121f02a34326f25037d62380fc406237c87c2a4231ae58`
- 2023-12: `ab4f4db11cb31484747f62eb507c13fcfaff290aaf59c13e6465dea0b1166b9c`

### Untouched 2024 files

- 2024-01: `c4d59da7bbc8abaeeeb1727947ee93d9891a71acb42854bd80db1571b2030510`
- 2024-02: `c76c43c18c6c6664080dd920baab4928988d5786a6b65980792ca7cd796f9f20`
- 2024-03: `2d4cdc8fb96726cdd3803b13b02d2e61e71d45720aff0ebc693a8bdd1f249823`
- 2024-04: `ce37f736c7cf9e92164c850ef2b502a8f7bb590fc1804b6edbcb80293da01b89`
- 2024-05: `1974230be2b5a3ea92e47b5eb77f32dbf1de896d81ad8df4ab6faba52749ad23`
- 2024-06: `677cf14c8347f745b583f012fbdba072334c6c4efa17bfd6a64369f2ba30329c`
- 2024-07: `af12d6b04daeb78550799ae99933d495b27d715b6dbb0fad9bb750a4537d3070`
- 2024-08: `7315643dd16bafc03e27d9903edbfd35404c2550a695d0da0a3e73852d940cfb`
- 2024-09: `2f42e4a383a6635de803001462848d0aee2b47f6ce899126805d2d05361fb843`
- 2024-10: `d19fe05aa0b259af24eb47051735293287f1e6dc263ba04030ec1ab4c6ec2650`
- 2024-11: `5ef321876de5007a7c147a347389133fc94fd7ac28f82eb1d57d8f2cf05cfd3b`
- 2024-12: `41ebf7db80bebde60c58e5143c14cdf38ad04a0f3e3ff44215b3e240d55f6c78`

## 9. Scientific interpretation

P-002 answers two different questions differently.

### Does temporal recency matter?

Within the declared equal-window comparison, yes.

An 8-week RECENT transition law systematically outperformed the immediately preceding 8-week STALE law on the untouched 2024 target set.

The gain survived an 8-week moving-block bootstrap and appeared in 49 of 52 individual target weeks.

This is evidence against treating the empirically estimated transition law as completely stationary at this temporal resolution.

It does not distinguish secular drift from seasonality, policy changes, changing demand composition, estimation effects coupled to time, or other forms of temporal nonstationarity.

### Does that explain P-001?

Not under the proposed P-002 mechanism.

The broad FROZEN January-June 2023 law had lower aggregate 2024 log-loss than the 8-week RECENT law.

Therefore the statement

[
	ext{“P-001 failed simply because its }K	ext{ was old”}
]

is not supported.

A plausible interpretation is a bias-variance / multi-timescale problem: short recent windows can beat equally short stale windows while still losing to a much larger older training sample. Seasonality or other temporal structure may also matter.

Those explanations were not preregistered and remain hypotheses.

## 10. Relationship to the framework

P-002 supplies no positive evidence for RZS, a Modal Field ontology, or fundamental physics.

It does provide a real-data demonstration relevant to the repository's broader informational theme:

[
oxed{
	ext{the predictive adequacy of a coarse transition description depends on the state and timescale carried forward.}
}
]

That sentence must remain an empirical observation about this mobility dataset unless independently replicated elsewhere.

## 11. Next admissible question

P-002 suggests that the next experiment should not tune the 8-week window after the fact.

A new P-003 may instead preregister a genuinely new prediction about **multi-timescale state**:

> combining a long-term transition estimate with a causally recent correction should outperform either the long-term or short-term estimate alone on a new untouched dataset.

That is a new hypothesis and would require a new dataset/time period, frozen combination rule, and independent baselines before execution.
