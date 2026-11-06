# A115 — exact feasible parameter interval for the central Q block

**Date:** 2026-11-06  
**Scope:** the three-site central Q solution, not the complete coupled probability-measure optimization problem.  
**Novelty status:** elementary algebra; **not a new theorem claim**.

## 1. Original equations

For `M >= 4`, put `h=floor(M/2)>=2`, `u=tau^h`, and

```
D = tau - h*u + (h-1)*tau*u.
```

For `0<tau<1`, `D>0`; an equivalent expression is

```
D = tau*(1-tau)^2 * sum_{j=0}^{h-2} (j+1)*tau^j.
```

The three weights obey normalization, prescribed mean `M*t/2`, and target transform 1. The A115 system gives (with `v` defined in each case):

### Even M = 2h

```
v = 1-u*t
q1 = v/D
qh = t-h*q1
qh1 = (h-1)*q1
```

All three weights are nonnegative **if and only if**

```
h/(D+h*u) <= t <= 1/u.
```

Indeed `q1>=0` is equivalent to `u*t<=1`; `qh>=0` is equivalent to `h<=t(D+h*u)`; the remaining weight is automatically nonnegative once `q1>=0`, since `h>=2`.

### Odd M = 2h+1

Put `a=(1+tau)/2`, and

```
v = 1-a*u*t
q1 = v/D
qh = t/2-h*q1
qh1 = t/2+(h-1)*q1
```

All three weights are nonnegative **if and only if**

```
2*h/(D+2*h*a*u) <= t <= 1/(a*u).
```

Here `q1>=0` gives the upper bound, `qh>=0` gives the lower bound, and `qh1>=0` follows from `t>=0`, `h>=2`, and `q1>=0`. Conversely, if all three weights are nonnegative, their sum `t` is nonnegative, and the first two conditions imply the bounds.

The denominators simplify without approximation:

```
D+h*u       = tau*(1+(h-1)*u),
D+2*h*a*u   = tau*(1+(2*h-1)*u), where a=(1+tau)/2.
```

Consequently, the exact feasible intervals can also be displayed in the publication-friendly form

```
even: h/[tau*(1+(h-1)*tau^h)] <= t <= tau^(-h)
odd:  2h/[tau*(1+(2h-1)*tau^h)] <= t <= 2/[(1+tau)*tau^h].
```

The intervals are nonempty, with strict separation of endpoints, since `D>0`.

**Important:** this is the exact condition for the **three Q weights only**. It is not by itself sufficient for feasibility of all transform-band constraints, the other measure, KKT inequalities, or global optimality.

## 2. Independent rational falsification gate

The standalone script `audits/a115_independent_feasibility_bounds_20261106.py` checks integers `M=4,...,59`, five rational targets `tau in {1/7,1/3,1/2,4/5,9/10}`, and five values of `t` for each pair: one below the lower endpoint, each endpoint, one interior midpoint, and one above the upper endpoint.

For each of 1,400 cases, direct `Fraction` evaluation confirms:

```
(q1>=0 and qh>=0 and qh1>=0) == (lower<=t<=upper)
```

Observed output:

```
PASS: 1400 exact feasibility comparisons, including both interval boundaries and outside points
```

These are finite consistency controls. The exact formulas above can be proved algebraically for all `M>=4`.

## 3. Lean 4 formal status

The module `formal/lean/PrecategoryFormal/TargetDeformationAudit.lean` received two new **sufficiency** lemmas:
- `even_central_weights_nonnegative`
- `odd_central_weights_nonnegative`

Both specify the bound hypotheses explicitly and prove nonnegativity of all three weights. Their successful compilation and kernel replay must be checked against the GitHub Actions run for commit `5b85174b934dd9e8b41aa67d122eb2396411b23f`. The full **if and only if**, written above, is an elementary mathematical consequence but is **not yet certified by these two Lean lemmas**.

## 4. Next gates

1. Upgrade the Lean statements from sufficient criteria to equivalences and derive the precise fractional interval endpoints with positive denominators.
2. Connect the block to the **full** primal feasibility conditions, especially the second distribution and bilateral transform bands. No extension by assumption.
3. Derive the reduced factor `E_M,k` from original primal/dual definitions, then verify the ten-term identity and its relation to the local sign theorem.
4. Revisit novelty only after a complete self-contained formulation. Do not claim general moment-space discoveries from this straightforward normalization algebra.

**Verdict:** explicit feasibility interval identified, subjected to exact finite falsification tests and partially encoded in Lean; global LP feasibility and originality are still open.

## 5. Formal compilation failure and corrective step

The first Lean compilation of the sufficiency lemmas at commit `5b85174b934dd9e8b41aa67d122eb2396411b23f` **FAILED** in GitHub Actions run [42305718215](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42305718215). The two logged failures were `linarith failed to find a contradiction` at lines 210 and 239 of the then-current module. The missing step was explicitly associating `h * (v/D)` with `(h*v)/D` before applying the established divided inequality. No mathematical assertion was refuted by these logs.

A subsequent commit `86b6eb36aafef1a10abcfd9aa625d45ea02751d3` replaced both opaque `nlinarith` conclusions with the explicit ring identity followed by the proven bound. It triggered GitHub Actions run [42305941974](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42305941974). The repaired version must **not** be labeled PASS until that run completes successfully.
