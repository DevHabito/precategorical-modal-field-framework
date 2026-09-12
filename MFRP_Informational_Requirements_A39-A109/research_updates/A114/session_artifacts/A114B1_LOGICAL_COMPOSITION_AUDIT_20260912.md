# A114-B1 logical composition audit — 2026-09-12

## Verdict

**PASS — the `b+1` phase pivot theorem is logically closed under the frozen analytic-tail contract.**

The review was performed adversarially against the failure modes already seen in A94–A114: compressed/lifted conflation, circular determinant orientation, use of a strict-max hypothesis at the wrong contact, post-hoc architecture selection, and silent deletion of a degenerate boundary.

## 1. Determinant circularity

### Previous risk

A112-B derived `D_G>0` under adjacent positivity. That is sufficient for the original A112 implication but cannot be reversed to infer adjacent positivity from Cramer signs without circularity.

### A114-B1 repair

The new standalone symbolic certificate proves

\[
D_G=\det(C)A(s).
\]

A110 gives `det(C)<0` structurally and A112-G gives `A(s)<0` before adjacent positivity is assumed. Therefore `D_G>0` is now available independently.

**Gate: PASS.**

## 2. Does A112 require `j` itself to be the compressed maximizer?

The A112 composition audit is explicit:

- A112-A: no strict-compressed assumption;
- A112-B/C/E/F/G: adjacent positivity/localization and tail structure;
- A112-D: uses `E_j<0` for the active gamma dual;
- the audit states that A112-D is the only point in the KKT closure that needs the compressed sign.

Therefore the minimal inherited hypothesis is `E_j<0`, not `E_(j-1)>0>E_j`.

For a strict compressed `b+1` maximum, A113 gives `E_(b+1)<0`, and its proved central nesting

\[
E_{b+1}-2E_{b+2}>0
\]

forces `E_(b+2)<0`. Hence both candidate contacts satisfy the only compressed-sign hypothesis required by A112-D.

**Gate: PASS.**

## 3. Is the pivot rule derived or fitted?

It is derived from pre-existing exact identities:

\[
p_{j+1}=F_j^{up}/D_G,
\qquad
p_j=-F_{j+1}^{up}/D_G,
\]

and pre-existing uniform barriers

\[
F_{b+1}^{up}>0,
\qquad
F_{b+3}^{up}<0.
\]

Once `D_G>0` is independent, the only unfrozen adjacent sign for the two candidate contacts is exactly `F_(b+2)^up`.

The theorem was not obtained by fitting the M=561 counterexample; that counterexample was used to reject the stronger false claim first.

**Gate: PASS.**

## 4. Competing architectures

The proof does not enumerate two-band, q0/q1, gamma-minus, or endpoint-released competitors. This is legitimate here because for `F_(b+2)^up != 0` one of the two gamma-plus bases satisfies the complete **strict** KKT system. Complete strict KKT, including strict reduced costs for every nonbasic atom, certifies the unique global optimum of the full declared LP. Therefore a different architecture cannot represent a distinct competing optimum in the strict cases.

At `F_(b+2)^up=0`, no uniqueness claim is made.

**Gate: PASS.**

## 5. Degenerate pivot

The zero case is not deleted. Both adjacent gamma-plus bases remain nonsingular as matrices but each has one zero basic P coefficient. Their seven common columns are linearly independent, so after deleting the zero pivot variable both give the same primal point.

Continuity from a neighboring strict gamma-plus KKT branch proves global optimality at the zero with non-strict KKT inequalities. The theorem does not claim a unique basis, strict complementarity or a unique primal optimum there.

**Gate: PASS.**

## 6. Independent exact controls

The standalone cross-check uses direct exact matrix solves and scans every unused atom. It does not import the symbolic orientation certificate.

- even, negative pivot: `M=522, s=131/1000`; predicted contact passes 1053/1053 strict conditions; alternate fails one adjacent basic mass;
- odd, negative pivot: `M=561, s=53/400`; predicted contact passes 1131/1131; alternate fails one adjacent basic mass;
- odd, positive pivot: `M=561, s=13277/100000`; predicted contact passes 1131/1131; alternate fails one adjacent basic mass.

Both pivot signs are represented. The positive-pivot case is the previously found exact counterexample to same-contact lifting.

**Gate: PASS.**

## 7. Claims explicitly rejected

The following statements remain false or unproved and are not promoted:

1. `compressed b+1 max => lift contact b+1` — **false**; exact counterexample at `M=561, s=13277/100000`.
2. `F_(b+2)^up classifies every lifted tail phase` — **not proved**.
3. `A114-B1 closes the b+2 phase` — **false**.
4. `the pivot point is a unique strict optimum` — **not claimed**.
5. `compressed maximizer contact must equal lifted adjacent contact` — **false**.

## 8. Remaining risk

The remaining mathematical target is genuinely different: in the strict compressed `b+2` phase, `E_(b+1)>0>E_(b+2)`. Therefore when `F_(b+2)^up<0`, the contact `b+1` gamma-plus branch may be primal-feasible but A112-D gives the wrong gamma-dual orientation. That is precisely where other A102 architecture classes can become necessary.

No statement about that regime is smuggled into A114-B1.

## Final status

\[
\boxed{\text{A114-B1: PROVED / CLOSED within the declared tail contract.}}
\]

with an explicit non-strict transition classification at `F_(b+2)^up=0`.
