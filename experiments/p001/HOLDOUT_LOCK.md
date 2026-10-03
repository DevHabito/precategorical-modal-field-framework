# P-001 — Holdout lock

**Locked:** 2026-10-03  
**Prevalidation implementation commit:** `40af45e108cd4682ad30577c7b04ccfe455ed652`  
**Prevalidation workflow run:** `37135318128`  
**Prevalidation artifact digest:** `sha256:a3e5bc682b59a157602a77359edde8bbb45509bec8ef009a57874672a7f23ec3`

This file records the state of P-001 immediately before opening the September–December 2023 holdout.

## What validation said

TRAIN was January–June 2023. VALIDATION was July–August 2023. The holdout was not loaded.

The validation artifact contained:

- trips scored: `5,670,974`;
- blocks: `6,247`;
- MICRO log-loss: `0.4330349013267722`;
- MACRO log-loss: `0.43304241315523884`;
- observed gain (L_macro-L_micro): `7.511828466608548e-06` nats/trip;
- weekly-bootstrap 95% interval for gain:
  `[-6.646566754958911e-05, 0.00010618816111392607]`;
- pre-outcome predicted KL separation:
  `0.0002710477359940815` nats/trip;
- weighted structural slope:
  `-0.3233895949329587`;
- weekly-bootstrap 95% interval for structural slope:
  `[-0.6620160736374743, -0.017756428081405075]`;
- composition-alignment permutation p-value: `0.001`;
- unseen zone/hour-of-week pickup fraction:
  `0.000308059955838274`.

The validation result is therefore **not reassuring**. The primary gain was tiny and its interval crossed zero; the preregistered structural direction was negative.

Post-run audit also found temporal and borough heterogeneity. Those observations are diagnostics only. They are not used to alter P-001.

## Independent arithmetic check

The exported `block_scores.csv` was recomputed independently outside the experiment script. The trip count, both aggregate log-losses, aggregate gain, aggregate predicted KL separation, weighted structural slope, and both weekly-bootstrap intervals reproduced the workflow values.

No arithmetic discrepancy was found.

## No rescue changes

After seeing validation, P-001 v1 will **not**:

- remove Bronx or Brooklyn;
- keep only Manhattan or Queens;
- change the one-hour window;
- change hour-of-week conditioning;
- change Jeffreys (alpha=1/2);
- change destination classes;
- change the unseen-row fallback;
- change log-loss;
- change bootstrap or permutation counts;
- change any PASS/FAIL/INCONCLUSIVE/ARTIFACT_SUSPECTED gate.

The holdout is opened because the preregistered protocol committed us to doing so regardless of whether validation looked promising, provided code and data-integrity checks passed.

## Holdout

The untouched evaluation period is:

[
oxed{	ext{2023-09-01 through 2023-12-31}}
]

The fitted transition rows remain based on January–June only. July–August are not added to training.

A negative result will be retained as a negative result.
