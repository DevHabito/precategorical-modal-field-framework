# P-001 — Occupancy-preserving coarse-graining on real mobility data

**Protocol version:** 1.0  
**Frozen date:** 2026-10-03  
**Status:** pre-registered empirical application test; holdout not opened.

## 1. Question

Does retaining the microscopic composition of a coarse source state improve out-of-sample prediction of macroscopic destination flow, exactly in the way implied by occupancy-weighted aggregation?

This experiment tests an empirical application of the repository's coarse-graining result. It does **not** test RZS as a physical theory and does not identify (q), (mu), (K), or (pi) with fundamental physical quantities.

## 2. Data and fixed split

Primary source: NYC TLC 2023 Yellow Taxi Trip Data.

Only these raw trip fields are permitted:

- `tpep_pickup_datetime`
- `PULocationID`
- `DOLocationID`

Taxi-zone metadata are taken from the official TLC taxi-zone lookup.

Calendar split:

- **TRAIN:** 2023-01-01 through 2023-06-30
- **VALIDATION:** 2023-07-01 through 2023-08-31
- **HOLDOUT:** 2023-09-01 through 2023-12-31

The prevalidation executable is hard-limited to months 1–8 and asserts that no timestamp on or after 2023-09-01 is loaded.

A schema-only sanity exposure occurred before this file was frozen: the public API preview displayed the first January records to verify field names and types. No aggregate result, model score, validation statistic, or holdout row was inspected or used to choose the protocol.

## 3. States and observable

A microscopic source state (i) is a TLC pickup zone.

A macroscopic source state (A) is one of the five NYC boroughs:

[
Ain{mathrm{Bronx, Brooklyn, Manhattan, Queens, Staten Island}}.
]

Pickup zones not mapped by the official lookup to one of these five source boroughs are excluded using source information only.

The destination observable (B) is the official lookup's borough label. Any destination ID not mapped by the lookup is retained as the explicit class `UNMAPPED`; target rows are not discarded because of their destination.

Time is partitioned into one-hour windows (t). The training transition law is additionally stratified by hour-of-week

[
hin{0,ldots,167},
]

so both competing models receive the same ordinary weekly-periodic temporal information.

## 4. Training quantities

For zone (i), hour-of-week (h), and destination macro-label (B), let the training count be

[
c_{ihB}.
]

Let (J) be the number of destination classes determined from the official zone lookup plus `UNMAPPED`.

The zone-level destination row is estimated with the same symmetric Jeffreys smoothing for every row:

[
widehat K_{ihB}
=
rac{c_{ihB}+alpha}
{sum_C c_{ihC}+alpha J},
qquad
alpha=rac12.
]

No alpha search is allowed in P-001.

For source borough (A) and hour-of-week (h), define the training pickup composition

[
w_{mathrm{train}}(imid A,h)
=
rac{n^{mathrm{train}}_{ih}}
{sum_{kin A}n^{mathrm{train}}_{kh}}.
]

The occupancy-erasing macro prediction is deliberately constructed from the **same** zone-level rows:

[
widehat p_{mathrm{macro}}(Bmid A,h)
=
sum_{iin A}
w_{mathrm{train}}(imid A,h)widehat K_{ihB}.
]

This prevents differences in estimator family from being mistaken for an occupancy effect.

## 5. Prediction made before destination outcomes are used

For a validation or holdout hour (t), pickup counts are observed before the destination labels are used for scoring:

[
ho_t(imid A)
=
rac{n_{it}}
{sum_{kin A}n_{kt}}.
]

The occupancy-preserving prediction is

[
oxed{
widehat p_{mathrm{micro}}(Bmid A,t)
=
sum_{iin A}
ho_t(imid A)widehat K_{i,h(t),B}
}
]

and the occupancy-erasing comparator is

[
oxed{
widehat p_{mathrm{macro}}(Bmid A,t)
=
widehat p_{mathrm{macro}}(Bmid A,h(t)).
}
]

Both models know (A), (h(t)), and the number of pickups in the block. Only MICRO retains the within-borough pickup composition.

If a zone/hour-of-week pair appears outside training, its zone row falls back to the symmetric uniform distribution induced by the declared Jeffreys prior. The fraction of such pickups is reported explicitly and cannot be hidden by dropping them.

## 6. Primary score

The primary score is multinomial log-loss per trip.

For a block ((A,t)) with observed destination counts (y_{AtB}) and (N_{At}=sum_B y_{AtB}),

[
L_m(A,t)
=
-rac1{N_{At}}
sum_B
y_{AtB}logwidehat p_m(Bmid A,t).
]

Define the observed gain

[
g_{At}=L_{mathrm{macro}}(A,t)-L_{mathrm{micro}}(A,t)
]

and the trip-weighted total gain

[
G_{mathrm{obs}}
=
rac{sum_{A,t}N_{At}g_{At}}
{sum_{A,t}N_{At}}.
]

The directional prediction is

[
oxed{G_{mathrm{obs}}>0.}
]

No minimum percentage improvement is invented.

## 7. Structural prediction independent of destination outcomes

Before reading the destinations for a block, the two predicted distributions imply

[
S_{At}
=
D_{mathrm{KL}}!left(
widehat p_{mathrm{micro}}(cdotmid A,t)
middle|
widehat p_{mathrm{macro}}(cdotmid A,t)
ight).
]

When the occupancy change does not change the predicted macro row, (S_{At}=0), and no occupancy-derived gain is predicted. Larger (S_{At}) represents a larger pre-outcome structural separation.

The reported structural slope is the trip-weighted through-origin coefficient

[
eta
=
rac{sum_{A,t}N_{At}S_{At}g_{At}}
{sum_{A,t}N_{At}S_{At}^2}.
]

The directional structural prediction is (eta>0).

## 8. Inferential controls fixed before validation execution

Random seed:

[
20261003.
]

### Weekly block bootstrap

Calendar weeks are the resampling units. Exactly 10,000 bootstrap replicates are used. The 2.5% and 97.5% percentiles form the reported 95% interval for (G_{mathrm{obs}}) and for (eta).

### Composition-alignment null

Within each fixed pair ((A,h)), the MICRO prediction vectors generated by observed pickup compositions are permuted across validation/holdout hours. Macro predictions and destination outcomes are held fixed.

Exactly 999 permutations are used. The one-sided Monte Carlo p-value is

[
p
=
rac{1+#{G_{mathrm{null}}ge G_{mathrm{obs}}}}
{1000}.
]

This asks whether correct temporal alignment of microscopic composition contains information beyond the distribution of compositions itself.

The threshold (ple0.01) is a conventional inferential gate fixed here before validation execution; it is not a theoretical constant of the framework.

## 9. Holdout verdict contract

The holdout will be opened regardless of whether validation performance is encouraging or disappointing, provided only that code and data-integrity checks pass.

**PASS** requires all of:

1. (G_{mathrm{obs}}>0);
2. the lower endpoint of the weekly-bootstrap 95% interval for (G_{mathrm{obs}}) is (>0);
3. the composition-alignment permutation test gives (ple0.01);
4. (eta>0) and the lower endpoint of its weekly-bootstrap 95% interval is (>0).

**FAIL** if (G_{mathrm{obs}}le0): the central directional empirical prediction is wrong on the untouched holdout.

**INCONCLUSIVE** if (G_{mathrm{obs}}>0) but sampling uncertainty prevents the PASS gates from being met.

**ARTIFACT_SUSPECTED** if the apparent primary gain is well separated from zero but the permutation or structural controls fail.

Validation cannot itself confer PASS or FAIL on P-001.

## 10. Validation governance

July–August are for implementation verification and pre-holdout red-team checks.

Performance on validation may not be used to:

- select alpha;
- select another time-window size;
- select another source/destination grouping;
- remove inconvenient boroughs or hours;
- change the primary metric;
- choose a more favorable temporal stratum;
- cancel the holdout because validation looks bad.

A genuine code or data-integrity defect may be corrected. Any substantive mathematical/statistical change after validation has been inspected requires a new protocol version, an explicit changelog, and a new commit **before** the holdout is opened.

## 11. Reproducibility and audit trail

The executable records SHA-256 hashes of every downloaded input file, monthly raw/retained row counts, unseen zone/hour-of-week coverage, block scores, bootstrap results, and the permutation-null result.

Raw TLC files are not committed to the repository. Only compact audit outputs may be retained.

Two deterministic synthetic tests run before any real-data analysis:

1. a non-lumpable two-zone example must produce positive MICRO gain under a shifted occupancy;
2. a lumpable two-zone example must make MICRO and MACRO identical up to floating-point roundoff.

## 12. What P-001 can and cannot establish

A PASS would establish only that this occupancy-preserving relational aggregation rule has preregistered out-of-sample predictive value in the declared mobility problem.

It would **not** establish:

- RZS as a physical theory;
- a Modal Field ontology;
- physical meaning for (q,mu,K,pi);
- novelty over the general literature on Markov aggregation, lumpability, mobility prediction, or mixture models;
- universality across domains.

A FAIL is retained as evidence that this proposed empirical bridge did not survive its declared test. The mathematical occupancy identity remains a conditional theorem; the failed empirical application is not repaired after the fact.
