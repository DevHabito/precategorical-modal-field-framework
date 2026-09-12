# A114-B2-A logical composition audit — 2026-09-12

## Verdict

**PASS — the positive-pivot subphase of the strict compressed `b+2` analytic tail is closed.**

The audit was performed specifically against the failure modes already encountered in A112–A114: determinant circularity, compressed/lifted conflation, using a compressed sign at the wrong contact, extrapolating a finite atlas to all M, and silently absorbing the zero-pivot boundary.

## 1. Determinant orientation

A112-B originally obtained `D_G>0` under adjacent primal positivity, so that route cannot be reversed to infer primal positivity.

A114-B1 independently repaired this by proving

\[
D_G=\det(C)A(s)>0
\]

through A110 `det(C)<0` and A112-G `A(s)<0`, neither of which assumes adjacent positivity.

A114-B2-A imports only this independent orientation theorem.

**Gate: PASS.**

## 2. Primal positivity is derived, not assumed

At contact `j=b+2`, A112-A gives

\[
p_{b+3}=F_{b+2}^{up}/D_G,
\qquad
p_{b+2}=-F_{b+3}^{up}/D_G.
\]

The B2-A premise supplies `F_(b+2)^up>0`; the proved A112-A barrier supplies `F_(b+3)^up<0`; and the independent orientation supplies `D_G>0`.

Therefore both adjacent masses are strictly positive with no circular step.

**Gate: PASS.**

## 3. The compressed sign is used at the correct contact

The candidate contact is `j=b+2`, which is itself the assumed strict compressed maximizer. Hence A113 gives directly

\[
E_{b+2}<0.
\]

A112-D is the only inherited KKT step that needs a compressed-factor sign, and it needs exactly `E_j<0` at the candidate contact.

No use is made of the wrong-sign neighboring factor `E_(b+1)>0`.

**Gate: PASS.**

## 4. Full LP versus restricted architecture comparison

A112 closes every nonbasic P/Q reduced cost and all band slacks for the full declared finite LP once adjacent positivity and `E_j<0` hold.

Thus the conclusion is not merely “best gamma-plus candidate”. It is a full strict KKT certificate and therefore a unique strict global basic optimum.

Competing architecture enumeration is unnecessary on this subphase.

**Gate: PASS.**

## 5. Zero and negative pivot are not smuggled into the theorem

The theorem assumes strict `Phi>0`.

- `Phi=0` gives `p_(b+3)=0`, so strictness is lost and no architecture classification is promoted.
- `Phi<0` makes the contact-`b+2` gamma-plus basis primal-infeasible. A114-B2-W1 proves that a different architecture can occur there.

Therefore B2-A does not close all of B2.

**Gate: PASS.**

## 6. Independent exact replication

A standalone exact-rational script scans every full-LP KKT condition for positive-pivot witnesses of both parities:

- `M=522, s=129/1000`: 1053/1053 pass;
- `M=523, s=132/1000`: 1055/1055 pass;
- `M=521, s=131/1000`: 1051/1051 pass.

The premise-negative control `M=521,s=129/1000` has strict compressed `b+2` but `Phi<0`; gamma-plus at `b+2` fails.

**Gate: PASS.**

## 7. Finite atlas is only a consistency check

The exact A102 census finds 404 positive-pivot `b+2` witnesses, all gamma-plus, and 40 negative-pivot witnesses, none gamma-plus.

This is not used as an all-M inference. The analytic theorem follows from A112/A113 identities and signs.

**Gate: PASS.**

## 8. Remaining open problem

The global A114-B2 problem is reduced to

\[
F_{b+2}^{up}\le0.
\]

The negative side already contains multiple finite-atlas architecture classes and one exact tail q0/q1 gamma-minus witness. Any next theorem must derive the architecture partition there rather than postulate a single replacement family.

## Final status

\[
\boxed{\text{A114-B2-A: PROVED / CLOSED for strict `b+2` with }F_{b+2}^{up}>0.}
\]

\[
\boxed{\text{A114-B2 complete classification: still OPEN.}}
\]
