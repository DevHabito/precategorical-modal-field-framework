# A115–A122: explicit optimization contracts and proof gates

*7 November 2026 — normative research specification for this branch; not a claim about the intentions of historical authors.*

The main problem in the current research is no longer the polynomial algebra. It is the possibility of quietly switching between **different feasible sets** and calling all their maximizers “the optimum.” Below I write the actual finite problems in one notation, with a clear distinction between source-supported assumptions and proposed extensions.

## Shared definitions

Choose an integer `M≥4`, an observation source `s∈[129/1000,133/1000]`, a target `0<τ<1`, fixed `β=1/8`, `γ=1/16` (only where explicitly included), and `δ=1/1875`. Put `h=floor(M/2)` and

```
ell_(M,τ) = τ^h                     if M=2h,
            (1+τ)*τ^h/2            if M=2h+1;
ε=δ*ell_(M,τ).
G_r(p)=sum_(x=0)^M p_x*r^x.
```

The unknowns are `p_x≥0`, `q_x≥0`, `t≥0` for `0≤x≤M`, without any *a priori* restriction on support. A valid scaled primal point satisfies

```
sum p_x = sum q_x = t,
sum x*p_x = sum x*q_x = (M/2)*t,
G_τ(q) = 1.
```

These conditions imply `t>0`. The equivalent unscaled probability measures are `μ_x=p_x/t`, `ν_x=q_x/t`, with common mean `M/2`. The scaled target objective is

```
maximize F=G_τ(p)=G_τ(μ)/G_τ(ν).
```

Every observation band, when present, has **both** orientations:

```
-2*ε*t <= G_r(p)-G_r(q) <= 2*ε*t.
```

The scaling by `t` is essential: replacing `2 ε t` by `2 ε` changes the optimization problem. All quantities above are rational at rational nodes, so exact feasibility checking is possible.

## Model F3: full three-observation-band finite LP

Impose the two-sided bands at `R={s,β,γ}`. Allow all p/q support points and all band activities. The historical **frozen target** instance has `τ=1/2`. A100's exact finite LP at `M=443,s=13/100` uses `τ=1/2`, `β=1/8`, `γ=1/16`, and epsilon `1/(2500*2^221)`, in agreement with the frozen odd-scale formula.

**F3(τ) for variable target is a proposed continuation of the full contract**, not something A115's source script automatically verifies. If using F3(τ) to make a target-deformed claim, one must explicitly declare the inheritance of the third gamma band.

Original sources:
- [A81 gamma-band reduced system](../../MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py)
- [A100 unrestricted finite LP](../../MFRP_Informational_Requirements_A39-A109/audits/a100_full_lp_active_set_resolution_audit.py)
- [A100 exact contract note](../../MFRP_Informational_Requirements_A39-A109/docs/technical_notes/MFRP_next_step_third_unrestricted_full_lp_resolution.md)

## Model F2: two-observation-band finite LP

Keep exactly the same mass, mean, target, positivity and objective constraints, but impose only the two-sided bands at `R={s,β}`. This is a **different, relaxed LP**: every F3-feasible point is F2-feasible, but not conversely.

The special compressed architecture studied in A115 imposes an *additional support/active-set ansatz*:

```
P support subset {0,k,M},
Q support subset {1,h,h+1},
P_β-Q_β=-2 ε t,
P_s-Q_s=+2 ε t.
```

Call this restricted algebraic family **C2(k)**, not “the full F2 optimum.” Its two active equalities are imposed as exact equations. Even in F2, a C2(k) solution is only a candidate until all its weights and inactive/opposite band inequalities are checked and a global dual bound is proved.

The A115 Python script explicitly studies its reduced cofactor factor and **does not** verify a full F3(τ) primal or dual certificate. A119's interval proof applies to a transformed expression inherited from this family; it is not a shortcut to global F2 or F3 optimization.

Original:
- [A115 target deformation](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT_20260914.md)
- [Exact compressed objective derivation](../formal/A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md)

## Canonical acceptance gates

For any candidate pair `p,q`, acceptance as *F3(τ)-primal feasible* requires, independently:

1. `M`, `s`, `τ`, `δ` and `ε` lie in the declared domain and the parity formula is correct.
2. Every atom mass is nonnegative and lies on support `{0,...,M}`.
3. Both totals equal the **same** `t>0`.
4. Both means equal `M*t/2`.
5. `G_τ(q)=1`.
6. Every included observation node has both band inequalities checked **without floating-point tolerance**.
7. The objective is computed from actual P weights as `G_τ(p)`, not substituted from an unverified expression.

F2 uses the same gates but without gamma. A C2(k) *exact* algebraic solution is not automatically admitted to either LP.

Acceptance as a **global optimum** adds a verified upper-bound certificate (dual feasibility) with the correct maximize-direction and complementary slackness at the candidate, or another complete global proof. A value comparison between consecutive C2(k) candidates is insufficient.

## A sound general dual upper-bound template

These are the dual multipliers for the full two-measure LP, written without choosing an active set. This is an **algebraic certificate specification**, not a claim that a tight dual has been found for A115.

Take unrestricted real multipliers `a_p,a_q,b_p,b_q,v` for P mass, Q mass, P centered mean, Q centered mean, and `G_τ(q)=1`, respectively. For every band `r∈R`, let `u_r≥0` weight `G_r(p)-G_r(q)-2εt≤0`, and `w_r≥0` weight `-G_r(p)+G_r(q)-2εt≤0`.

A sufficient dual-feasibility system for the upper bound `F≤v` is:

```
for each 0<=x<=M:
  τ^x <= a_p + b_p*(x-M/2) + sum_r (u_r-w_r)*r^x;       [P]
       0 <= a_q + b_q*(x-M/2) + v*τ^x
                 - sum_r (u_r-w_r)*r^x;                  [Q]

0 <= -a_p-a_q-2*ε*sum_r(u_r+w_r).                          [t]
u_r>=0, w_r>=0.
```

Then multiply the P/Q pointwise inequalities by nonnegative masses, and the t row by `t≥0`. Summing gives `F≤v` because all mass/mean equalities cancel, `G_τ(q)=1`, and each weighted band lhs is ≤0. The sign of the t row is important; reversing it would not give an upper bound.

The template is *deliberately complete*: it covers every atom and both sides of every band. Complementary slackness, equality of primal and dual values, and strict reduced costs must be checked separately. An old certificate for `τ=1/2` cannot be recycled for `τ≠1/2` without verification.

As a **sanity check**, `a_p=1,a_q=-1,b_p=b_q=0,v=τ^{-M},u=w=0` satisfies the rows for `0<τ<1`; this proves the loose universal bound `F≤τ^{-M}`. It is not a tight bound for the A115 optimization and must not be presented as its optimality proof.

## Explicit counterexamples to shortcut reasoning

- The exact A115 compressed adjacent factor is **not** numerically equal to the adjacent difference in target objectives; see [the A113 erratum](../../MFRP_Informational_Requirements_A39-A109/research_updates/A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md).
- A strictly increasing C2(k) objective can point to a **negative endpoint mass** (M=24, k=5→6): sign improvement does not imply primal feasibility.
- Under the *inherited* gamma band, 0/213 sampled adjacent C2 pairs had both contacts gamma-feasible. This is not a proof that F3 is empty.
- For any 0<τ<1, the centered equal-measure construction P=Q is F3-feasible and has objective 1, provided coincident measures are permitted. Its finite exact regression uses 40 rational cases.

## Status and required next proof

**Contract status:** the F3 and F2 mathematical programs are specified here, but whether the deformed-target paper intends F2 or F3 is a research decision that must be stated in the theorem; no silent inheritance is accepted.

**Computational status:** the complete explicit feasibility verifier for these contracts belongs in [`audits/a115_explicit_full_primal_and_dual_gate_20261107.py`](../../audits/a115_explicit_full_primal_and_dual_gate_20261107.py). It is a test harness, not the underlying proof.

**Formal status:** the current Lean files prove the basis and adjacent-factor bridge, conditional sign transfers, and Q/P nonnegativity pieces. This document does not assert an end-to-end Lean proof of F3 dual optimality.

**Priority:** none of the LP formulation, dual weak bound, moment constraints or fractional homogenization methods is novel in isolation; these are classical mathematical tools. Do not imply affiliation with any institution or a peer-reviewed acceptance.

