# A114-C1 — frontier update after the first compressed tie

**Date:** 2026-09-14

A114-C1 closes the first non-strict compressed boundary

\[
E_{b+1}=0
\]

under the frozen analytic-tail contract

\[
M\ge521,\qquad 129/1000\le s\le133/1000.
\]

A113 forces `E_(b+2)<0`, so this is exactly the `b+1 / b+2` compressed tie.

The lifted classification is:

- `Phi>0`: unique strict gamma-plus optimum at contact `b+2`;
- `Phi=0`: unique primal optimum with degenerate `C/G1+/G2+` coalescence;
- `Phi<0, p0^C>0`: exact one-dimensional optimal face `conv{G1+,C}`;
- `Phi<0, p0^C=0`: exact one-dimensional optimal face `conv{G1+,C=E}`;
- `Phi<0, p0^C<0`: exact one-dimensional optimal face `conv{G1+,E}`.

The theorem is backed by:

- exact rational near-tie regression: 24/24 PASS;
- independent symbolic boundary certificate: 5/5 PASS;
- hardened logical-composition audit: 32/32 PASS;
- independent red-team audit: PASS WITH SCOPE.

The red-team found and repaired one proof-exposition gap: the optimal line cannot continue through `G1+` away from C/E because the gamma-plus slack is affine, zero at `G1+`, positive at the C/E endpoint, and therefore negative immediately beyond `G1+` in the opposite direction.

## Remaining frontier

The only compressed-tie surface still unresolved in A114 is

\[
\boxed{E_{b+2}=0},
\]

the `b+2 / b+3` tie.

Exploratory exact controls suggest `Phi>0` and a `G2+ / ER3` zero-cost transition, but neither statement is promoted here. In particular the implication

\[
E_{b+2}=0\Longrightarrow\Phi>0
\]

remains to be proved or refuted.

No physical or ontological interpretation is asserted.