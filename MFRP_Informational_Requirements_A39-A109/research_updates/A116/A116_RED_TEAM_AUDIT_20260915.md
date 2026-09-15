# A116 — independent red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH SCOPE.**

The red-team target was the proposed compact-uniform eventual positivity theorem and its claimed boundary-layer obstruction.

## Attacks performed

### 1. Hidden use of the collision wall

A uniform proof over the full open domain would be invalid because `tau-s` can shrink with `M`. The theorem was therefore restricted to arbitrary compact subsets of the inherited A84 node-order domain. Compactness supplies a strictly positive distance from `tau=s` and from the other domain walls.

**Result:** scope is explicit; no global uniform threshold is claimed.

### 2. Contact-domain failure

A115 previously caught an exploratory negative point whose second factor lay outside the A84 adjacent-factor domain. A116 checks admissibility analytically:

- on a compact interior set, `c_tau(s)` is uniformly below `1/2`, hence `h-k -> infinity` uniformly;
- on the negative boundary sequence, `b=h-4`, so `b+2=h-2` is exactly the last valid adjacent-factor contact.

**Result:** PASS.

### 3. Parity leakage

The compact theorem uses both A115 parity formulas through `a_p(tau)=1` (even) and `(1+tau)/2` (odd). The explicit negative boundary sequence is deliberately claimed only for even `M`.

**Result:** PASS; no odd-parity extrapolation is made.

### 4. Constant-channel underbound

A tempting but insufficient estimate is

`c1 = O(tau^h/M)`.

After normalization by `tau^h tau^k`, that estimate does not prove decay. The proof was hardened using the exact grouping

`c1=A(a_beta-a_s)+H_beta(a_s-a_tau)+H_s(a_tau-a_beta)`,

which yields the sharper

`c1 = O(tau^M/M)`.

Because `M-h-k` grows linearly on every compact interior set, the normalized constant channel then decays exponentially.

**Result:** a real proof gap was identified and closed before promotion.

### 5. Treating finite stress as proof

The exact 30-point compact regression and four boundary-sequence controls are not premises. The compact theorem is proved by uniform asymptotic bounds; the boundary obstruction is proved by an analytic limit with a rational sign certificate.

**Result:** PASS.

### 6. Floating-point sign in the boundary limit

The negative boundary limit contains `exp(-1250/133)`. No decimal approximation is used to certify its sign. The audit proves `exp(1250/133)>10000` from a finite positive Taylor partial sum, hence `exp(-1250/133)<1/10000`, and then closes the sign with an exact rational margin.

**Result:** PASS.

### 7. Rounding in `b=ceil(M c_tau)`

The boundary proof needs the exact eventual identity `b=h-4`. The audit separately certifies `2 < -log(133/1000) < 2.1`, which places the limiting offset strictly between 4 and 5. Since the inequalities are strict, the ceiling stabilizes for all sufficiently large even `M`.

**Result:** PASS.

### 8. Node-order drift

The algebraic A115 identity itself is meaningful more broadly, but A116 does not silently enlarge the structural A84 contract. It retains `s tau < beta`, ensuring the declared A84 node order.

**Result:** PASS WITH SCOPE.

## Preserved failed/insufficient routes

1. A global constant threshold is impossible: the boundary sequence gives negative `J` arbitrarily deep in the tail.
2. The estimate `c1=O(tau^h/M)` is insufficient after normalization and must not be reused.
3. A coarse finite grid cannot establish compact-uniform positivity.
4. Fixed-gap asymptotics cannot be applied when `tau-s=O(1/M)`; the source-affine channel then survives in the scaled limit.

## Verdict

**PASS WITH SCOPE.**

A116 closes the A115 open question of eventual positivity for every fixed interior target deformation in the inherited A84 node-order domain, and explains why no one-size-fits-all tail threshold can hold up to the collision wall.

Reopen the result if any of the following is retracted:

- the A115 exact deformed Q-block;
- the generic A84 ten-term identity;
- the A115 scale-normalized error law;
- the exact `J` transform identity.

No claim about the lifted A114 architecture or physical ontology is certified here.
