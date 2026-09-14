# A114-B2 frontier update after E — 2026-09-14

A114-B2-E closes the outer `Phi=0` boundary **inside the strict compressed `b+2` phase**.

Under

- `M>=521`,
- `129/1000<=s<=133/1000`,
- strict compressed maximizer `j=b+2`,
- `Phi=F_j^up=0`,

E proves that the compressed two-band point C is primal-optimal and unique as a primal solution, while the adjacent gamma-plus basis G+ has zero pivot mass and represents the same primal point.

The new analytic certificate proves **22/22** gates, including the stronger equality-surface source box and the uniform separation

`p0^C > 0.0029407...`

on `Phi=0`. The exact near-boundary Fraction crosscheck passes **24/24**, the section-scoped logical audit passes **32/32**, and the multi-cell red-team scan passes **79/79** across 13 strict-b+2 cells from `M=521` through `M=1000`.

The independent red-team audit records **PASS WITH SCOPE**.

## Strict compressed `b+2` status

The complete strict-`b+2` phase is now classified under the frozen tail contract:

- `Phi>0` -> unique strict gamma-plus lift at contact `b+2` (B2-A);
- `Phi=0` -> unique primal optimum with degenerate C/G+ coalescence (B2-E);
- `Phi<0`, `p0^C>0` -> unique strict C (C2);
- `Phi<0`, `p0^C=0` -> unique primal optimum with degenerate C/E/QI coalescence (D);
- `Phi<0`, `p0^C<0`, `r_E(q0)>0` -> unique strict E (C1);
- `Phi<0`, `p0^C<0`, `r_E(q0)=0` -> exact one-dimensional optimal face (D);
- `Phi<0`, `p0^C<0`, `r_E(q0)<0`, `Gamma>0` -> unique strict QI (C3);
- the same residual branch with `Gamma=0` -> unique primal optimum with degenerate QI/QA coalescence (D);
- the same residual branch with `Gamma<0` -> unique strict QA (C3).

## What is still not closed

This does **not** mean all of A114 is closed.

A114-A, B1 and B2 classify **strict compressed phases**. The remaining natural A114 boundary problem is the set where the compressed maximizer itself is non-strict, i.e. adjacent compressed objectives tie. In A113 notation the principal candidates are

- `E_(b+1)=0` — the `b+1` / `b+2` compressed tie;
- `E_(b+2)=0` — the `b+2` / `b+3` compressed tie.

No theorem is promoted here for those tie surfaces.

The next rigorous target should therefore be a separate compressed-tie closure package, with no assumption that the lifted optimum is obtained by naively taking a limit from either neighboring strict compressed phase.

No physical interpretation is claimed.
