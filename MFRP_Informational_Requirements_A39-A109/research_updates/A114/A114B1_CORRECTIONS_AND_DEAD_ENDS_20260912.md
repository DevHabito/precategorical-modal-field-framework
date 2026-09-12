# A114-B1 — corrections, rejected stronger claims, and dead ends

This note records the paths that were deliberately rejected while proving A114-B1. They are preserved because the final theorem is narrower than several initially tempting statements.

## 1. Same-contact lifting is false

The first candidate statement was

`strict compressed maximizer b+1 => gamma-plus lift at contact b+1`.

It is false.

At the exact rational point

\[
M=561,\qquad s=\frac{13277}{100000},\qquad b=97,
\]

the compressed objective has strict maximizer `j=98=b+1`, but the gamma-plus basis at contact 98 has

\[
p_{98}<0.
\]

An unrestricted high-precision simplex run was used only to discover the replacement candidate. It selected the gamma-plus support

\[
P=\{0,99,100,561\},\qquad Q=\{1,280,281\}.
\]

That discovery is not the proof. The independent exact-rational A114-B1 cross-check reconstructs the candidate and verifies all

\[
2M+9=1131
\]

strict KKT conditions. The contact-98 alternative is rejected exactly through `basic_p_98`.

The corrected lesson is that the compressed maximizing contact and the lifted adjacent P contact need not coincide.

## 2. The pivot is not a universal A114 classifier

A second tempting overstatement was that `F_(b+2)^up` classifies the entire lifted tail problem. That is not proved.

A114-B1 proves only that, **conditional on the strict compressed maximizer being `b+1`**, the sign of

\[
F_{b+2}^{up}
\]

selects between the two neighboring gamma-plus contacts `b+1` and `b+2`.

The strict compressed `b+2` phase is different: there

\[
E_{b+1}>0>E_{b+2},
\]

so a primal-feasible contact-`b+1` gamma-plus branch can have the wrong active-gamma dual orientation. A114-B2 remains open.

## 3. A determinant-orientation reversal would have been circular

A112-B proved `D_G>0` under adjacent primal positivity. That implication is sufficient for A112, but it cannot be reversed to infer primal positivity from the Cramer signs.

Using it that way would be circular.

A114-B1 repairs this independently. The new symbolic certificate proves

\[
D_G=\det(C)A(s),
\]

where A110 supplies `det(C)<0` by generalized Vandermonde and A112-G supplies `A(s)<0` on the localization strip. Therefore

\[
D_G>0
\]

without assuming either adjacent mass is positive.

Only after this repair is the Cramer bridge a legitimate sufficient sign test.

## 4. The old `R_Q(2)` limiting-core route is not the A114-B1 bottleneck

An earlier A112 snapshot left `R_Q(2)>0` open and isolated a positive limiting core. Later A112-B/C already closed the required implication

\[
p_j>0,\ p_{j+1}>0\Longrightarrow R_Q(2)>0
\]

uniformly on the frozen tail gamma-plus architecture.

Reopening the old limiting-core remainder calculation as though it were the next A114-B1 task would mix chronological snapshots and duplicate already-closed work.

A114-B1 instead uses the completed A112 composition.

## 5. The zero pivot is not strict

At

\[
F_{b+2}^{up}=0
\]

the two adjacent gamma-plus bases are both degenerate: one pivot mass is zero in each representation. The theorem therefore does not call this point a strict KKT basis and does not claim a unique basis or unique primal optimum.

The two nonsingular basis matrices share seven columns; after deleting the zero pivot coefficient they represent the same primal point. Global optimality follows as the limit of a neighboring strict KKT branch, with non-strict KKT inequalities at the pivot.

Deleting this equality case from the theorem would hide a genuine transition and would be scientifically incorrect.

## 6. Why competing architectures are not enumerated in B1

The finite A102 atlas contains gamma-plus, gamma-minus, compressed two-band, endpoint-released and q0/q1 architectures. A114-B1 does not claim these families never occur elsewhere.

For `F_(b+2)^up != 0` inside the strict compressed `b+1` phase, however, the selected gamma-plus candidate satisfies the complete **strict** KKT system of the full declared LP. This already certifies the unique global optimum, so enumerating every alternative architecture is unnecessary for this phase.

At the zero pivot no uniqueness claim is made.

## Final correction boundary

Promoted:

\[
\boxed{\text{strict compressed }b+1\text{ phase }\Longrightarrow
\operatorname{sgn}F_{b+2}^{up}\text{ gives the gamma-plus lift pivot rule}}
\]

Not promoted:

- same-contact lifting;
- a universal all-phase `F_(b+2)^up` classifier;
- closure of the strict compressed `b+2` phase;
- strictness or uniqueness at the zero pivot;
- any statement outside the frozen tail/source contract;
- any physical interpretation.
