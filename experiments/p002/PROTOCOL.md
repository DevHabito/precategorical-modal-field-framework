# P-002 — Prospective test of transition-law drift

**Protocol version:** 1.0  
**Frozen date:** 2026-10-03  
**Status:** preregistered before inspection of 2024 trip outcomes.

## 1. Question

Did P-001 fail because the transition law used in prediction was not temporally stable?

P-002 tests a narrower empirical proposition:

[
oxed{
	ext{a transition law estimated from the immediately preceding 8 weeks
predicts the next week better than an equally sized law estimated 8--16 weeks earlier.}
}
]

The equal-window comparison is designed to isolate **recency** rather than sample-size advantage.

This experiment does not test RZS as a physical theory and does not identify any repository primitive with a fundamental physical quantity.

## 2. Data source and untouched evaluation set

Source: NYC TLC Yellow Taxi Trip Records.

Permitted raw fields:

- `tpep_pickup_datetime`
- `PULocationID`
- `DOLocationID`

Taxi-zone metadata come from the official NYC/TLC zone lookup.

The evaluation set is the 52 complete Monday-to-Monday calendar weeks

[
2024	ext{-}01	ext{-}01 00{:}00
le t <
2024	ext{-}12	ext{-}30 00{:}00.
]

No 2024 outcome aggregate, model score, weekly gain, or target destination distribution was inspected before this protocol was frozen. Public metadata were checked only to confirm that 2024 Yellow Taxi Trip Data exist and expose the required fields.

The final two days of 2024, 2024-12-30 and 2024-12-31, are excluded solely so that every target unit is a complete seven-day week.

## 3. State definition

A microscopic source state is

[
(i,h),
]

where:

- (i) = TLC pickup zone;
- (hin{0,ldots,167}) = hour-of-week.

Only pickup zones mapped by the official lookup to one of the five NYC boroughs are included as sources.

The destination observable (B) is the official destination borough label. Destination IDs absent from the official lookup are retained as the explicit class `UNMAPPED`.

No target row is excluded because of its destination.

## 4. Three transition laws

For target week (w) beginning at time (t_w), define:

### RECENT

[
W_R(w)=[t_w-56	ext{ d},,t_w).
]

### STALE

[
W_S(w)=[t_w-112	ext{ d},,t_w-56	ext{ d}).
]

Both windows have exactly 56 days = 8 complete weekly cycles.

### FROZEN

The P-001 reference law is estimated once from

[
W_F=[2023	ext{-}01	ext{-}01,,2023	ext{-}07	ext{-}01).
]

The FROZEN law is not needed to establish drift itself. It is included to test whether a recency-updated law also improves over the specific old law implicated in P-001.

## 5. Estimator

For model window (W), source row ((i,h)), and destination class (B), let (c^W_{ihB}) be the number of training trips.

Every model uses the same symmetric Jeffreys smoothing:

[
widehat K^W_{ihB}
=
rac{c^W_{ihB}+alpha}
{sum_C c^W_{ihC}+alpha J},
qquad
alpha=rac12,
]

where (J) is the fixed number of destination classes.

No smoothing search is allowed.

If a source row ((i,h)) is absent from a training window, the estimator reduces to the symmetric uniform prior. Such rows are retained and their target-trip fraction is reported separately for RECENT, STALE, and FROZEN.

## 6. Weekly scoring

Let (y_{w,ihB}) be target-week trip counts and

[
n_{w,ih}=sum_B y_{w,ihB}.
]

For model (Min{R,S,F}),

[
L_M(w)
=
-rac{1}{N_w}
sum_{i,h,B}
y_{w,ihB}
logwidehat K^M_{ihB},
]

with

[
N_w=sum_{i,h,B} y_{w,ihB}.
]

Define the primary weekly gain

[
g_{RS}(w)=L_S(w)-L_R(w)
]

and the P-001 linkage gain

[
g_{RF}(w)=L_F(w)-L_R(w).
]

Trip-weighted aggregate gains are

[
G_{RS}
=
rac{sum_w N_w g_{RS}(w)}
{sum_w N_w},
]

[
G_{RF}
=
rac{sum_w N_w g_{RF}(w)}
{sum_w N_w}.
]

## 7. Primary prediction

The central P-002 prediction is

[
oxed{G_{RS}>0.}
]

RECENT and STALE have the same estimator and the same 56-day duration. A positive value therefore cannot be attributed merely to RECENT having a longer training window.

The link back to P-001 predicts additionally

[
oxed{G_{RF}>0.}
]

If RECENT beats STALE but not FROZEN, temporal drift may exist without explaining the P-001 failure in the proposed way.

## 8. Pre-outcome structural drift prediction

For each target week, use only target **source** counts (n_{w,ih}), not target destinations, to define

[
D_{RS}(w)
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

If RECENT is a better approximation to the current transition law, weeks where RECENT and STALE differ more should tend to show a larger realized RECENT advantage.

The preregistered through-origin weighted slope is

[
eta_{RS}
=
rac{
sum_w N_w D_{RS}(w)g_{RS}(w)
}{
sum_w N_w D_{RS}(w)^2
}.
]

The directional prediction is

[
oxed{eta_{RS}>0.}
]

No prediction of slope magnitude is made.

For connection to P-001, the analogous (D_{RF}) and (eta_{RF}) are reported as secondary diagnostics and are not additional PASS gates.

## 9. Dependence-aware uncertainty

Adjacent target weeks share most of their RECENT and STALE training windows, so treating all 52 weekly gains as independent would be unjustified.

The primary uncertainty estimate is therefore a moving-block bootstrap with:

- block length: exactly 8 consecutive target weeks;
- justification: the adaptive transition law has an 8-week memory;
- 10,000 bootstrap replicates;
- seed: `20261003`;
- blocks sampled from all non-wrapping consecutive 8-week segments;
- sampled blocks concatenated until at least 52 weeks are obtained, then truncated to 52.

The 2.5% and 97.5% percentiles give the reported 95% intervals for:

- (G_{RS});
- (G_{RF});
- (eta_{RS}).

The block length is frozen here and will not be selected from the result.

## 10. Verdict contract

### PASS

All of the following must hold on untouched 2024 data:

1. (G_{RS}>0);
2. the lower 95% moving-block-bootstrap bound for (G_{RS}) is (>0);
3. (eta_{RS}>0);
4. the lower 95% moving-block-bootstrap bound for (eta_{RS}) is (>0);
5. (G_{RF}>0);
6. the lower 95% moving-block-bootstrap bound for (G_{RF}) is (>0).

A PASS supports the limited statement that transition-law recency has preregistered predictive value and is consistent with temporal instability contributing to P-001.

It does not prove that drift was the only cause of P-001.

### FAIL

If

[
G_{RS}le0,
]

the central drift prediction is wrong on the declared evaluation set.

### INCONCLUSIVE

If (G_{RS}>0) but its lower bootstrap bound is not positive, the data do not separate the central prediction from zero under the declared uncertainty procedure.

### PARTIAL

If the primary RECENT-vs-STALE gain is robustly positive but either the structural slope or the RECENT-vs-FROZEN linkage fails its corresponding positive-interval gate, temporal recency has predictive value but the full P-001 explanation is not established.

No other verdict label may replace these after the result is known.

## 11. Synthetic logic checks before real evaluation

The executable must pass deterministic tests before downloading 2024 data:

1. **stationary case:** identical RECENT and STALE rows give exactly zero drift and zero model difference up to numerical roundoff;
2. **drift case:** target outcomes generated from a RECENT row distinct from STALE produce positive RECENT-vs-STALE log-score gain and positive (D_{mathrm{KL}}(R|S));
3. **causal-window check:** for every target week, both adaptive training windows end strictly before the target begins and have exactly 56 days.

A failure of these checks stops the workflow before 2024 scoring.

## 12. Governance

No 2024 result may be used to:

- change 56 days to another recency window;
- change the weekly target unit;
- change (alpha=1/2);
- remove inconvenient weeks, zones, boroughs, or hours;
- change destination classes;
- change log-loss;
- change the 8-week bootstrap block length;
- replace the FROZEN interval;
- redefine PASS/FAIL/INCONCLUSIVE/PARTIAL.

A genuine code or source-integrity defect may be corrected only with an explicit audit note describing whether any 2024 target outcomes had already been exposed.

## 13. Scope

P-002 tests a standard empirical nonstationarity question for a transition kernel.

A PASS would not establish:

- RZS;
- Modal Field ontology;
- a fundamental physical (K);
- novelty over time-varying Markov, concept-drift, adaptive forecasting, or mobility literature;
- universality across domains.

A FAIL would leave the exact conditional coarse-graining mathematics intact while rejecting this particular temporal-drift explanation.
