# A112 field notes — corrections, dead ends, and why they matter

This is intentionally not a polished theorem note. It records the places where the research changed direction, where an attractive stronger statement failed, and where the final audit found missing assumptions.

The purpose is provenance. A future reader should not have to guess which formulas were abandoned or why the final proof has the shape it does.

## 1. The stronger contact-only q2 claim is false

A tempting shortcut was:

`j in {b+1,b+2} => RQ(2)>0`.

It is false.

Exact counterexample:

- `M=600`;
- `s=133/1000`;
- `b=104`;
- `j=106=b+2`;
- `p_j>0`;
- `p_(j+1)<0`;
- `RQ(2)<0`.

Lesson: localization alone is not enough. The primal antecedent `p_j,p_(j+1)>0` is essential.

## 2. Two intermediate tail-T corrections were discarded

During the q2 expansion, two formulas were derived and then rejected after checking that gamma-contact terms had been zeroed too early.

They must not be reused:

- the first provisional `-16(s-1/8)YT` correction;
- the later provisional `TY(512s^2-96s-31)/(40(2s-1))` correction.

The corrected full first contact-tail correction is

\[
\Delta_T=TY\frac{(8s-1)(16s-1)}{10(2s-1)}<0.
\]

The later determinant-resultant proof supersedes the need to lean on these asymptotic formulas, but the correction history is preserved because it explains why the determinant route was chosen.

## 3. Direct inverse propagation was abandoned

An early plan was to propagate all tail perturbations through a large symbolic inverse. This created unnecessary conditioning constants and enormous algebra.

The successful route used affine determinant boundaries in

\[
R=s^j/U
\]

and their linear resultant. This removed the large inverse completely and made the sign problem auditable.

## 4. A112-F initially had an implicit regularity gap

The first monotonicity certificate established:

- `partial p_j / partial t < 0`;
- `partial p_(j+1) / partial t > 0`;
- `BA' - B'A > 0` for `t=-B/A`.

But that does not by itself prove `t'(s)>0` if `A(s)` could vanish.

The logical composition audit caught this.

A112-G then proved uniformly on the entire localization strip

\[
A(s)<0<B(s).
\]

Only after that regularity certificate is it legitimate to conclude

\[
t'(s)>0.
\]

## 5. “Cannot be the first zero” was not enough

The old sign-variation results for `q_1,p_0,p_M` were continuation statements: starting from a strict witness, those variables cannot be the first obstruction.

For a tail theorem without a historical witness, that is weaker than the needed pointwise implication.

The repair was direct:

- at `q_1=0`, prove `p_j<0`;
- since `partial p_j/partial t<0`, deduce `p_j>0 => q_1>0`;
- combine with `p_(j+1)>0 => q_h>0`;
- use exact Q formulas for `q_(h+1)>0`;
- then use Descartes pointwise to force `p_0,p_M>0`.

This removes the anchor dependency entirely.

## 6. Partial certificates remain historical, not authoritative

The early `A112B_INTERLACING_PARTIAL_CERTIFICATE_20260911.json` closed the core, first contact tail and a finite-U model, but explicitly left raw tails unpropagated.

It is preserved as a historical waypoint. It is not the theorem certificate.

The authoritative q2 result is `A112B_EXACT_DETERMINANT_INTERLACING_CERTIFICATE_20260911.json` together with its script and cross-check.

## 7. Current discipline

When a later file contradicts or supersedes an earlier one:

- keep the earlier file;
- mark it historical/superseded in the human index;
- never silently rewrite a failed derivation into a successful one;
- preserve exact counterexamples;
- distinguish exploration scripts from theorem certificates.

That is the standard this update is trying to make explicit.
