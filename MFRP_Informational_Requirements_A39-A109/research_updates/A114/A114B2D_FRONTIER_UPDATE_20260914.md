# A114-B2 frontier update after D — 2026-09-14

A114-B2-D closes the three **internal zero-discriminant boundaries** of the already-classified strict compressed `b+2`, `Phi<0` analytic tail.

Under

`M>=521`, `129/1000<=s<=133/1000`, strict compressed maximizer `j=b+2`, and `Phi=F_j^up<0`, the complete promoted/staging classification is now:

| Conditions | Optimal structure | Primal uniqueness |
|---|---|---|
| `p0^C>0` | strict `C` | unique |
| `p0^C=0` | degenerate `C/E/QI` coalescence | unique primal point |
| `p0^C<0`, `r_E(q0)>0` | strict `E` | unique |
| `p0^C<0`, `r_E(q0)=0`, `Gamma>0` | optimal face `conv{E,QI}` | non-unique |
| `p0^C<0`, `r_E(q0)=0`, `Gamma=0` | optimal face `conv{E,QI}`, with `QI=QA` at the far endpoint | non-unique |
| `p0^C<0`, `r_E(q0)=0`, `Gamma<0` | optimal face `conv{E,QA}` | non-unique |
| `p0^C<0`, `r_E(q0)<0`, `Gamma>0` | strict `QI` | unique |
| `p0^C<0`, `r_E(q0)<0`, `Gamma=0` | degenerate `QI/QA` coalescence | unique primal point |
| `p0^C<0`, `r_E(q0)<0`, `Gamma<0` | strict `QA` | unique |

where

`Gamma=S_(gamma-)^QI`.

The important structural correction is that the three equality sets are **not all the same kind of simplex degeneracy**:

- `p0^C=0` is a primal-degenerate but primal-unique transition;
- `r_E(q0)=0` is a genuine one-dimensional primal optimal face because a nonbasic reduced cost vanishes;
- `Gamma=0` (under the residual `r_E(q0)<0` premises) is a constraint-activation degeneracy with a unique primal point.

The D proof does not infer these statements from finite scans. It composes the promoted C1/C2/C3 determinant/pivot identities and ECT reduced-cost closure. The new exact boundary certificate protects the nonzero C masses directly on `p0^C=0`; the hardening note proves that the displayed D2 segment is the **entire** primal optimal face.

## Reproducibility package

- `A114B2D_INTERNAL_ZERO_BOUNDARY_THEOREM_20260914.md`
- `A114B2D_BOUNDARY_HARDENING_NOTE_20260914.md`
- `a114b2d_boundary_analytic_certificate.py`
- `A114B2D_BOUNDARY_ANALYTIC_CERTIFICATE_20260914.json` — 13/13 exact rational gates PASS
- `a114b2d_exact_boundary_regression.py`
- `A114B2D_EXACT_BOUNDARY_REGRESSION_20260914.json` — 30/30 gates PASS on ten exact-rational full-KKT controls
- `a114b2d_logical_audit.py`
- `A114B2D_LOGICAL_AUDIT_20260914.json` — 28/28 checks PASS

The first hardened logical-audit run exposed a matcher bug in the audit itself (27/28). The theorem was not changed to hide it; the pattern was corrected and the rerun passed 28/28. This provenance is retained in the logical-audit JSON.

## Falsification controls

The exact rational regression contains one even and one odd tail cell exhibiting all five strict architectures on neighboring rational controls:

`E -> QA -> QI -> C -> G+`.

This is evidence that the discriminants correspond to real LP transitions. It is **not** promoted to a universal monotone ordering in `s`; other cells can skip regions or place a zero outside the active branch.

## Remaining A114-B2 frontier

The outer pivot set

`Phi=0`

remains open in the strict compressed `b+2` phase. A114-B1 already classifies a different `Phi=0` degeneracy inside the strict compressed `b+1` phase, but that result must not be imported automatically into `b+2`.

Accordingly, the next target should be a separate boundary package for `b+2, Phi=0`, with no assumption that it is the same degeneracy as B1.

No physical interpretation is claimed.