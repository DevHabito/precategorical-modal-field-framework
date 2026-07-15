# A11 — Order–Volume Correspondence and Manifoldlikeness Audit

## Design

- Confirmatory dimensions: 2 and 3.
- Train size: n=64.
- Prospective test size: n=96.
- Nulls: transitive percolation and random three-layer posets.
- Null matching: ordering fraction.
- Primary endpoint: balanced accuracy >= 0.75 with bootstrap lower bound > 0.50.
- 4D was diagnostic only because the feasibility pilot showed sparse large intervals.

## Results

- Mean absolute ordering-fraction mismatch: 0.014201
- Test balanced accuracy: 0.812500
- Test ROC AUC: 0.913125
- Bootstrap 95% CI: [0.7368238304093567, 0.8857142857142857]
- Ordering-fraction-only balanced accuracy: 0.500000
- Minimum grouped balanced accuracy: 0.500000
- 4D sufficient-interval fraction: 0.437500

## Verdict

FAIL_ORDER_VOLUME_DISCRIMINATION

## Boundary

This result is a discrimination result against two specified null families.
It is not a derivation of spacetime, gravity, a Lorentzian continuum, or a
fundamental law of selection.
