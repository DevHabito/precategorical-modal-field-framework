# R-001 — External replication of the P-002 recency effect in Chicago taxi trips

**Protocol version:** 1.0  
**Frozen date:** 2026-10-03  
**Status:** preregistered before inspection of Chicago trip outcomes.

## 1. Purpose

R-001 is an external replication of the central empirical result that survived P-002:

[
oxed{
	ext{an 8-week RECENT transition law predicts the next week better than an equally sized 8-week STALE law.}
}
]

The purpose is to test whether that result transfers outside New York City.

R-001 is not a new search for a favorable timescale. It carries forward the P-002 values unchanged:

- RECENT window = 8 weeks;
- STALE window = the immediately preceding 8 weeks;
- Jeffreys smoothing (alpha=1/2) per destination class;
- multinomial log-loss;
- 8-week moving-block bootstrap;
- 10,000 bootstrap replicates;
- seed = `20261003`.

## 2. Data

Source: City of Chicago Data Portal, official **Taxi Trips - 2024** dataset.

Public metadata checked before preregistration established only that the dataset exists, contains 6,480,350 rows, and exposes the fields needed for this experiment. No outcome aggregate or model score was inspected.

Raw fields permitted:

- `Trip ID` — pagination/audit only; never enters a model;
- `Trip Start Timestamp`;
- `Pickup Community Area`;
- `Dropoff Community Area`.

No fare, company, census-tract, coordinate, duration, or payment field is used.

## 3. Evaluation calendar

The first 16 complete weeks of 2024 are used only as causal history required to construct STALE and RECENT windows.

The untouched target set is the 36 complete Monday-to-Monday weeks

[
2024	ext{-}04	ext{-}22 00{:}00
le t <
2024	ext{-}12	ext{-}30 00{:}00.
]

For target week (w) beginning at (t_w):

[
W_R(w)=[t_w-56	ext{ d},t_w),
]

[
W_S(w)=[t_w-112	ext{ d},t_w-56	ext{ d}).
]

Both windows contain exactly 8 complete weeks and end before the target begins.

The final two days of 2024 are not targets because they do not form a complete target week.

## 4. States

A source state is

[
(i,h),
]

where:

- (i) = Chicago Pickup Community Area;
- (hin{0,ldots,167}) = local hour-of-week.

Rows with missing Pickup Community Area are excluded because the declared source state is undefined. This exclusion uses only source information.

Destination class (B) is Dropoff Community Area.

Chicago community-area IDs 1 through 77 are retained as distinct destination classes.

A missing or non-1-through-77 Dropoff Community Area is retained as the explicit destination class `UNMAPPED`.

Thus

[
J=78.
]

Target trips are never dropped because of their destination.

## 5. Transition estimators

For training window (W), source state ((i,h)), and destination (B), let (c^W_{ihB}) denote the observed count.

The transferred P-002 estimator is

[
widehat K^W_{ihB}
=
rac{c^W_{ihB}+1/2}
{sum_C c^W_{ihC}+(1/2)J}.
]

No Chicago-specific smoothing search is permitted.

If ((i,h)) is absent from a training window, the corresponding row is the symmetric uniform prior over the 78 destination classes.

Unseen-row target fractions for RECENT and STALE are reported.

## 6. Primary replication statistic

For target week (w),

[
L_R(w)
=
-rac{1}{N_w}
sum_{i,h,B}
y_{w,ihB}log widehat K^R_{ihB},
]

[
L_S(w)
=
-rac{1}{N_w}
sum_{i,h,B}
y_{w,ihB}log widehat K^S_{ihB}.
]

Define

[
g_{RS}(w)=L_S(w)-L_R(w)
]

and

[
G_{RS}
=
rac{sum_wN_wg_{RS}(w)}
{sum_wN_w}.
]

The transferred prediction is

[
oxed{G_{RS}>0.}
]

## 7. Dependence-aware uncertainty

Because adjacent target weeks share most adaptive training observations, R-001 reuses the P-002 uncertainty contract:

- moving-block bootstrap;
- block length = 8 target weeks;
- 10,000 replicates;
- seed = `20261003`;
- all non-wrapping consecutive 8-week blocks eligible;
- concatenate sampled blocks until 36 target weeks are obtained, then truncate to 36;
- 2.5th and 97.5th percentiles form the 95% interval.

No alternative block length will be selected after seeing Chicago results.

## 8. Primary replication verdict

### REPLICATED

Requires both:

[
G_{RS}>0
]

and

[
CI_{95%,mathrm{lower}}(G_{RS})>0.
]

### FAILED_REPLICATION

If

[
G_{RS}le0.
]

### INCONCLUSIVE

If (G_{RS}>0) but the lower 95% bootstrap bound is not positive.

These are the only primary replication verdicts.

## 9. Secondary structural extension

P-002 used a through-origin slope that was discovered during post-result audit to be insufficient for the stronger verbal claim “larger model drift predicts larger realized gain.”

R-001 therefore does **not** reuse that statistic as a replication gate.

For each target week define, using only target source counts,

[
D_w
=
rac{1}{N_w}
sum_{i,h}
n_{w,ih}
D_{mathrm{KL}}
left(
widehat K^R_{ih}
middle|
widehat K^S_{ih}
ight).
]

Let the trip-weighted means be

[
ar D
=
rac{sum_wN_wD_w}{sum_wN_w},
qquad
ar g
=
rac{sum_wN_w g_{RS}(w)}{sum_wN_w}.
]

The corrected centered weighted slope is

[
b_c
=
rac{
sum_wN_w(D_w-ar D)(g_{RS}(w)-ar g)
}{
sum_wN_w(D_w-ar D)^2
}.
]

Secondary prediction:

[
b_c>0.
]

An 8-week moving-block-bootstrap interval for (b_c) is reported.

This extension is explicitly **not** part of the REPLICATED / FAILED_REPLICATION / INCONCLUSIVE verdict.

## 10. Synthetic checks before real scoring

Before the Chicago target set is evaluated, code must verify:

1. identical RECENT and STALE rows yield zero gain and zero KL drift up to numerical roundoff;
2. if outcomes are generated from a RECENT row different from STALE, RECENT has positive log-score gain;
3. the centered slope implementation returns a positive value on a deterministic synthetic series with increasing drift and increasing gain;
4. all 36 target weeks have exactly 8 RECENT and 8 STALE training weeks strictly before target;
5. target weeks begin at 2024-04-22 and end at the week beginning 2024-12-23.

## 11. API and pagination integrity

The Chicago dataset is accessed through the official public data endpoint.

`Trip ID` may be retrieved only to make pagination ordering deterministic.

The executable must:

- request only the four permitted fields;
- order pages deterministically by Trip Start Timestamp and Trip ID;
- cover 2024-01-01 through 2024-12-30 exclusive;
- record page count and accepted/excluded row counts;
- record a SHA-256 digest over the canonical sequence of accepted four-field rows, so reruns can detect source changes.

If the API schema differs from the documented field names, a schema-only correction may be made before outcome scoring. Any such correction must be recorded.

## 12. Governance

After Chicago outcomes are opened, R-001 may not:

- change 8-week windows;
- change target start date;
- change source/destination state definitions;
- change (alpha=1/2);
- pool destination areas after seeing sparsity;
- remove inconvenient areas or weeks;
- change log-loss;
- change bootstrap block length;
- promote the secondary structural extension into a rescue criterion.

A code or API integrity defect may be repaired only with explicit documentation of whether target outcome aggregates had already been exposed.

## 13. Scope

A successful R-001 would replicate the **empirical recency effect** in a second city and a different taxi system.

It would not establish:

- a new general theorem of nonstationary Markov processes;
- RZS;
- Modal Field ontology;
- fundamental physics;
- universality across arbitrary relational systems;
- novelty over concept drift, adaptive Markov models, or mobility forecasting.

A failed replication would materially weaken any attempt to present the P-002 recency effect as a broad practical property rather than a New York-specific observation.
