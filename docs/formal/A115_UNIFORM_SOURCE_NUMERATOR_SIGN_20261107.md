# A115 — an analytic sign lemma for the common Cramer numerator

**Date:** 7 November 2026  
**Scope:** the three-site compressed P/Q family, not the full lifted linear program.  
**Status:** a self-contained calculus proof of a *specific* uniform sign statement; exact rational regression on published code; a separate Lean 4 proof of the key algebraic cancellation and a conditional sign lemma. See the CI run before labeling the latter kernel-checked.  
**Priority:** no claim of historical novelty.

## The question

The preceding [adjacent objective comparison](A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md) shows that

```
(V_(k+1)-V_k) * Delta_k * Delta_(k+1) = -Z * E_(M,k).
```

A key open assumption was `Z<0`. Earlier audits such as A83 had proved positivity of their *oppositely oriented* source numerator on a finite support range. Can its sign be established **uniformly**, without checking a growing sequence of integers?

The answer is yes for the A115 central block and nodes `0<beta<s<1/4`. This sign lemma is narrower than a global optimality theorem but stronger than a finite-grid observation. The argument below keeps `M`, the target `tau`, and the parity explicit.

## Definitions and hypotheses

Let `M>=4`, `h=floor(M/2)>=2` and `0<tau<1`. Define

```
L_h(r) = r - h*r^h + (h-1)*r^(h+1)
       = r*(1-r)^2*sum_{j=0}^{h-2} (j+1)*r^j.

D_tau = L_h(tau).

R_(M,h)(r) = (1-r^h)*(1-r^(M-h))/2.
```

Both `L_h(r)` and `R_(M,h)(r)` are strictly positive for `0<r<1` under these assumptions. The finite factorization of `L_h` is the same exact algebra as the already Lean-checked positive central denominator identity.

For the parity-dependent coefficient put

```
a_r = 1                  when M = 2h,
a_r = (1+r)/2            when M = 2h+1,
u = tau^h,   K = a_tau*u,  epsilon = delta*K.
```

The original target-deformed Q block has the exact transform decomposition

```
Q_r = C_r + D_r*t,
C_r = L_h(r)/D_tau,
D_r = a_r*r^h - K*C_r.
```

For the P baseline `A_r=(1+r^M)/2`, note the exact identity

```
A_r - a_r*r^h = R_(M,h)(r)
```

in **both parities** (the factor `M-h` equals `h` or `h+1`).

Take `0<beta<s<1/4` and `delta>=0`. The two active bands have coefficients

```
H_beta = A_beta-D_beta+2*epsilon
       = R_beta+K*C_beta+2*epsilon,

H_s = A_s-D_s-2*epsilon
    = R_s+K*C_s-2*epsilon.
```

The common Cramer numerator, using the **new** orientation, is `Z=C_beta*H_s-C_s*H_beta`. A81/A83 use its negative: `Z_source=-Z`.

## Exact cancellation

Expanding both H coefficients gives

```
Z = C_beta*R_s-C_s*R_beta
    -2*epsilon*(C_beta+C_s),
```

because `K*C_beta*C_s` cancels identically.

Multiplying by `D_tau>0`:

```
D_tau*Z = L_h(beta)*R_s
          - L_h(s)*R_beta
          - 2*epsilon*(L_h(beta)+L_h(s)).
```

**This is exact, for either parity, for every tau in (0,1).** The cancellation eliminates the shared `K` contribution, but epsilon still contains `tau`. It would be incorrect to say that the entire numerator is independent of the target deformation.

## An elementary uniform monotonicity proof

The key lemma is that `L_h` is strictly increasing on `(0,1/4)` for every integer `h>=2`. Differentiation gives

```
L_h'(r) = 1 - h^2*r^(h-1) + (h^2-1)*r^h.
```

For `0<r<=1/4` and `h>=2`, we claim

```
h^2*r^(h-1) <= 4*r.
```

Here is the entire induction, rather than an appeal to plots or sample counts. At `h=2`, both sides equal `4r`. If the claim holds for `h`, then

```
(h+1)^2*r^h
  = ((h+1)/h)^2 * r * [h^2*r^(h-1)]
  <= (9/4)*(1/4)*[h^2*r^(h-1)]
  <= h^2*r^(h-1)
  <= 4r,
```

since `(h+1)/h <= 3/2` for `h>=2`. Thus, for `0<r<1/4`,

```
L_h'(r) >= 1-4r > 0.
```

This proves strict increase without restricting `h` to a finite range.

Meanwhile, `R_(M,h)(r)` is strictly decreasing on `(0,1)`: both factors `1-r^h` and `1-r^(M-h)` are positive and strictly decreasing, because `h>=2` and `M-h>=2`. Their positive product is strictly decreasing.

Therefore, for `0<beta<s<1/4`,

```
0 < L_h(beta) < L_h(s),
0 < R_s < R_beta.
```

It follows that

```
L_h(beta)*R_s < L_h(s)*R_s < L_h(s)*R_beta.
```

Finally `epsilon>=0` and both L values are positive, so the cancellation identity implies

```
D_tau*Z < 0.
```

As `D_tau>0`, **Z<0**. Equivalently, **A81/A83's opposite-orientation interior-mass numerator is strictly positive**.

### Precise theorem

For every integer `M>=4`, every `0<tau<1`, every `0<beta<s<1/4`, and every `delta>=0`, the common Cramer numerator `Z=C_beta*H_s-C_s*H_beta` of the beta-lower/s-upper compressed active-band family is strictly **negative**, under the original parity-specific target normalization.

The proof uses only exact identities, elementary inequalities, an induction and a derivative sign. This theorem proves neither that a given active-band candidate has positive masses nor that it satisfies the remaining LP constraints.

## Formal Lean 4 boundary

The [`CompressedSourceNumerator.lean`](../../formal/lean/PrecategoryFormal/CompressedSourceNumerator.lean) module proves:
- `central_source_numerator_cancellation`: exact universal rational-algebra identity;
- `central_source_numerator_negative`: exact sign of the reduced expression *given* `0<L_beta<L_s`, `0<R_s<R_beta`, `epsilon>=0`;
- `central_Z_negative_of_monotonicity`: the corresponding negativity of `Z` when `D_tau>0`.

The parity-dependent identities and **uniform derivative monotonicity proof for all natural h are written out above, but are not yet separately formalized as a full theorem about `L_h` in Lean 4**. It is important to retain that distinction.

The initial compilation [run 42358760783](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358760783) failed because the strict style checker objected to the use of `<;>` where an ordinary sequenced tactic was sufficient. The mathematical formula was not modified. The correction is commit `97f71f50c44544e80be4512fa0c43cf3b542164b` and the next CI run is [42358976869](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358976869). Its status must be read before labeling these Lean declarations verified.

The earlier [`CompressedPrimalFeasibility.lean`](../../formal/lean/PrecategoryFormal/CompressedPrimalFeasibility.lean) has already passed its [23-job Lean + Leanchecker run 42358308334](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358308334). It proves the exact three-site P nonnegativity iff, and that positive interior masses at two active-band solutions **plus Z<0** force both determinants negative. Combined with the analytic proof above, this removes an otherwise independent determinant-orientation hypothesis whenever both interior weights are strictly positive.

This is still a comparison of compressed candidates, not global LP optimality.

## Independent exact rational regression

Two new scripts use the standard library's `Fraction` class and are run by the repository [exact-audit CI workflow](../../.github/workflows/a115-a122-exact-audits.yml):

- [`a115_independent_primal_feasibility_and_orientation_20261107.py`](../../audits/a115_independent_primal_feasibility_and_orientation_20261107.py): **142,740** exact P-weight, mass, mean, and interval-equivalence checks (of which **57,096** deliberately violate feasibility); and **345** determinant-orientation checks including both `Z<0` and `Z>0`.
- [`a115_source_numerator_sign_20261107.py`](../../audits/a115_source_numerator_sign_20261107.py): **2,370** exact Q-block parity controls for `2<=h<=80`, three rational sources `s` and five rational targets `tau`. It independently reconstructs the original Q weights, checks the exact cancellation `D_tau*Z`, the strict sign, and the power inequality used in the derivative argument.

These test grids are not the uniform proof. The **analytical argument above** is the step that covers all positive integers `h>=2`; the rational code is a falsification/reproducibility tool. Clean GitHub [run 42358910281](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358910281) completed **SUCCESS**, logging all three numerical counts.

## Literature, attribution and open gates

Cramer's rule, polynomial monotonicity, parametric LP, and classical moment problems are not new mathematical methods. The earlier [A115–A122 literature record](../research/A115_A122_LITERATURE_AND_ATTRIBUTION_20261106.md) covers Charnes–Cooper, Gal–Nedoma, Prékopa and Karr; the original [A81 reduced system](../../MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py) and [A83 compressed sign atlas](../../MFRP_Informational_Requirements_A39-A109/docs/technical_notes/MFRP_next_step_seven_term_adjacent_sign_atlas.md) are the immediate internal predecessors.

The new argument improves the **scope of the project's source-numerator sign claim**, from previously documented finite evidence to a uniform analytical proof for the stated source window. This is **not** a claim that no earlier published result implies the same conclusion.

The next requirements are:
1. Encode the parity identities and uniform L/R monotonicity as a complete, standalone Lean 4 theorem; do not equate the three conditional sign lemmas with that complete formalization.
2. Prove the exact nonnegative P/Q weights and *all* remaining transform bands for candidate contacts in the intended theorem domain.
3. Derive and check the actual dual-reduced-cost/KKT inequalities for the whole LP, not just the two active equations.
4. Only then extend sign information to global support selection and the later A116–A122 layers.

## Formal expansion beyond the conditional sign lemma

The original [run 42358976869](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358976869) finished **24/24 SUCCESS** (Lean build and 23 individual Leanchecker jobs), including `PrecategoryFormal.CompressedSourceNumerator`. The exact cancellation and the conditional negative-sign implication are therefore verified by Lean's kernel at commit `97f71f50c44544e80be4512fa0c43cf3b542164b`.

To formalize the analytical step rather than simply citing the handwritten derivative inequality, a second module was added:

[`CompressedSourcePowerBound.lean`](../../formal/lean/PrecategoryFormal/CompressedSourcePowerBound.lean).

It encodes the induction `((n:Real)+2)^2 * r^(n+1) <= 4*r` for all `n:Nat`, `0<=r<=1/4`, derives the strict positivity of the derivative's explicit polynomial expression for `0<r<1/4`, and proves the even/odd factorizations of the centered baseline. The module's source commit `2cb8754dae581f4685a39cfec3a1f29dae776bc8` has passed a Lean project build. The individual Leanchecker replay of the imported module is tracked by [run 42359321885](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359321885); do not label that specific job PASS until it completes.

[`CompressedSourceMonotonicity.lean`](../../formal/lean/PrecategoryFormal/CompressedSourceMonotonicity.lean) is a separate attempt to connect the already-positive polynomial expression to the actual derivative and to Mathlib's strict monotonicity theorem on `(0,1/4)`. It is tracked by [run 42359621482](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359621482), which was **queued** at the latest observation. Its kernel verification is **not yet claimed**. The monotonicity of the other factor `R` still needs a formal statement if we want an end-to-end Lean-certified sign theorem.

These gates are intentionally separated. A paper proof can be mathematically complete while its mechanization remains incomplete; the evidence ledger must not collapse those two statuses.

## Kernel confirmation of the all-natural-index power bound

GitHub Actions [run 42359321885](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359321885) has now completed with **25/25 SUCCESS**, including individual Leanchecker replay of `PrecategoryFormal.CompressedSourcePowerBound`, at source commit `8ae4984d132f17d58501e5113d539ff400d8d71b`.

Therefore the inequality `(n+2)^2*r^(n+1)<=4*r` for **all natural n** on `0<=r<=1/4`, strict positivity of the formal derivative polynomial for `0<r<1/4`, and both parity factorization identities are kernel-certified. This is not just a finite enumeration.

A separate source `CompressedSourceMonotonicity.lean` attempts the remaining connection to the actual derivative and the Mathlib strict-monotonicity theorem. Its CI run [42359621482](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359621482) was in progress at the last observation. Do not call this final monotonicity theorem Lean-certified until the new module passes.

## Boundary test: why the strict source separation matters

There is a simple exact equality case outside the theorem's strict `beta<s` hypothesis. If `beta=s` and `delta=0`, both source transforms and both `R` factors coincide, while `epsilon=0). The cancelled expression is therefore exactly `D_tau*Z=0`. As `D_tau>0` for `0<tau<1`, `Z=0`, not `Z<0`.

This is not a counterexample to the stated strict-source theorem. It falsifies the tempting stronger version with only `beta<=s` and `delta>=0`. The open endpoints in the analytic statement are deliberate.
