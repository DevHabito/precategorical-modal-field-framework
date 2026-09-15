# A116 — compact-uniform target-deformation nesting

A116 resolves the A115 open question of eventual positivity for fixed interior target deformations, while proving that no single tail threshold can hold uniformly up to the collision wall `tau=s`.

## Status

**PROVED under the inherited target-deformed reduced-factor contract; red-team verdict PASS WITH SCOPE.**

Main results:

- for every compact `K` inside the inherited A84 node-order domain, there exists `M0(K)` such that `J_(tau,b_tau+1)>0` uniformly for all `M>=M0(K)`;
- consequently every fixed interior pair has eventual positive central nesting;
- there is no global threshold valid up to `tau=s`;
- an explicit even-M boundary sequence `s=133/1000`, `tau_M=s+(5/2)/M` has `b=M/2-4` and `J<0` for all sufficiently large even `M`;
- the boundary-layer sign is certified analytically, with the transcendental sign reduced to exact rational Taylor bounds.

No minimal closed form for `M0(K)`, no target-deformed A114 staircase, and no physical or ontological interpretation are claimed.

## Files

- `A116_COMPACT_UNIFORM_NESTING_BOUNDARY_LAYER_THEOREM_20260915.md` — theorem and proof.
- `a116_compact_uniform_boundary_layer_audit.py` — standalone symbolic/exact audit.
- `A116_EXACT_AUDIT_RESULTS_20260915.json` — machine-readable exact audit output.
- `A116_RED_TEAM_AUDIT_20260915.md` — adversarial review and preserved proof hardening.
