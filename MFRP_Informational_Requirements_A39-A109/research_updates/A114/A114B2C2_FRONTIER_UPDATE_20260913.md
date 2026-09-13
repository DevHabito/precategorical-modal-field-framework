# A114-B2 frontier update after C2 — 2026-09-13

A114-B2-C2 closes the compressed branch inside the strict compressed `b+2`, negative-pivot analytic tail.

Under `M>=521`, `129/1000<=s<=133/1000`, strict compressed maximizer `j=b+2`, and `Phi=F_j^up<0`, let `C: P={0,j,M}, Q={1,h,h+1}` with `alpha+`, `beta-` active and gamma inactive.

C2 proves `p0^C>0 => C satisfies the complete strict KKT system and is the unique strict global basic optimum.`

The proof is analytic. It uses the C1 source box, the exact A81 two-variable reduction, an exact bordered gamma-plus pivot identity, positive neighboring compressed determinants/masses, exact simplex exchange identities, and the previously validated five-dimensional ECT zero budgets. The dedicated certificate reports `49/49` exact rational gates PASS. The pre-existing independent full-LP Fraction controls for three C points also pass completely but remain regression evidence only.

Combining C2 with C1, the strict negative-pivot frontier is now:

- `p0^C>0` -> `C` (closed by C2);
- `p0^C<0, r_E(q0)>0` -> `E` (closed by C1);
- `p0^C<0, r_E(q0)<0` -> `QI` versus `QA` (open).

The zero sets `p0^C=0`, `r_E(q0)=0`, and `Phi=0` remain outside the strict theorems.

The next efficient target is therefore the QI/QA edge. The finite exact chain suggests the inactive `gamma-` slack of QI and the active `gamma-` multiplier of QA are opposite-orientation versions of the same pivot discriminant, but that identity must be derived and audited before any universal classifier is promoted.
