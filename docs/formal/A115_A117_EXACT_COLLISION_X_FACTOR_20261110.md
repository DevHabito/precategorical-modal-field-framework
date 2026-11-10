# A115 source-to-A117 phase: an exact x-factor identity

**Date:** 2026-11-10. **Status:** exact algebra independently checked with SymPy; formal module kernel verified in CI run 42922256460 (51/51 SUCCESS).

The dominant K-independent normalized source factor reconstructed from A115 is

\[
\mathcal J=(1-s)(\tau-s)W/2+
x(1-\tau)(U_0-V_0)+
U_0(f_k/\tau)[(s-\tau)(s-1)(q-1)+x(s^2-2s+\tau)],
\]

where x=1/M, q=k/M=1/2-bx, b=sigma+r-1, tau=s(1+2alpha*x), W=s^(1-r) f_h, f_h=(s/tau)^h and f_k=(s/tau)^k. The exact leading central responses are U0=a_tau*(beta/tau+2delta) and V0=a_tau*(s/tau-2delta)-a_s*f_h.

**Exact identity:** for every nonzero tau, the expression is x times the bracket `collisionBracket` written explicitly in [A115CollisionCoreFactor.lean](../../formal/lean/PrecategoryFormal/A115CollisionCoreFactor.lean). No O notation or exponential approximation is necessary. This was independently checked by SymPy, with a zero polynomial difference after rational cancellation.

At x=0, setting a_tau=a_s=a, f_h=f_k=e, and z=s^(1-r), that bracket is exactly

\[
(1-s)[-a C+e(A+\alpha D)],
\]

where C=1-beta/s-4delta, A=a*(1-beta/s-2delta), D=s^(2-r)-a*(beta/s+2delta). This matches the published A117 phase numerator algebraically. The Lean theorem `collision_zero_matches_A117_phase` checks this **as a separate universal rational identity**, not by assuming A117's formula.

Why this matters: since `mathcal J=x*collisionBracket` exactly, a uniform second-order approximation of the bracket suffices for an O(x^3) remainder in the full normalized factor. The earlier draft expansion of the full core via a generic third derivative is stronger than necessary.

**Still open:** the exact real x->0 limit f_h=f_k=exp(-alpha); a uniform second-order expansion of the bracket for both exponent shifts sigma and sigma+r-1; the identification of the first derivative with A118's Xi; a final source-derived uniform bound in Lean. This says nothing about global F3 optimization or priority.


## CI failure and successful correction record

The first Lean build (42921508312) failed because the identifier 'at' is reserved; the second (42921821575) failed solely on the unused-variable linter applied to the nonzero-tau hypothesis. The final source retained this hypothesis, renamed identifiers, and used an underscore-prefixed hypothesis name to satisfy the linter. The exact mathematical statements were not weakened. [Run 42922256460](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42922256460) completed SUCCESS with all 51 jobs, including the individual kernel checker of A115CollisionCoreFactor.
