# A114-A field notes — corrections, failed stronger claims, and proof hygiene

This file records the parts of the A114-A search that should **not** disappear from the history.

## False stronger claim: `j=b+3` alone is sufficient

False.

At

`M=521, s=129/1000, b=89, j=92=b+3`,

the exact compressed factors satisfy

`E_91<0` and `E_92<0`.

So `j=92` is not a compressed maximum. The endpoint-released lift fails exactly: `basic_p_92<0` and `reduced_cost_p_0<0`.

The final theorem therefore requires **strict compressed maximality**, not just the arithmetic offset `b+3`.

## Incorrect implementation assumption: whole `r_P(M-1)` numerator divisible by `m`

An early certificate attempted to form `num/m` after putting the expression over a common denominator.

That is not algebraically valid: the **core** is divisible by `m`, but some tail terms in the common-denominator numerator are not.

The final certificate never introduces `1/m`. Instead:

- core/m is handled exactly;
- any remainder monomial already containing `m` loses one factor normally;
- any m-free remainder monomial necessarily contains an exponentially small tail factor;
- one such factor is bounded as `tail/m` using derived monotone envelopes such as `U/m=MU`, `W_s/m=M W_s`, etc.

## Overly coarse `RQ(2)` source-window bound

An intermediate bound replaced

`60256 s^2 - 7628 s - 12`

by a mixed-endpoint expression using `s_max` in the positive quadratic term and `s_min` in the negative linear term.

That combination does not correspond to any common source value.

The polynomial is strictly increasing on the entire source interval, so the correct upper value is obtained by evaluating **all terms at `s_max`**.

## Wrong extremum in the subtractive `RQ(2)` term

After the previous correction, the bound still used `w_min` in a term of the form

`-w A(s)` with `A(s)>0`.

For a lower bound, the subtractive product must use `w_max`, not `w_min`.

Replacing it by the valid upper bound `w<=1-c_lower` reduces the numerical margin but leaves it positive.

## Wrong extremum in the `p_j` core bound

The `p_j` core contains a subtractive product proportional to

`-(a+m)(8s+1)`.

A lower bound must use the **maximum** of `a+m`, not a lower bound for `a`.

The corrected margins are approximately:

- even: `18.05239...`;
- odd: `7.16324...`.

Both remain far above their exponential remainders.

## Operational dead end: full exact scan at `M=4000`

A standalone `Fraction` solver can in principle scan every unused atom at `M=4000`, but doing so is needlessly expensive because the rational numerators and denominators have thousands of digits.

This was not converted into a theorem shortcut. The final independent full-KKT replication uses `M=561` and `M=1282` to cover both parities. The theorem itself remains the analytic certificate, not the finite regression.

## Discipline preserved

No failed stronger claim is silently removed. No finite scan is promoted into an all-M theorem. No proof gate is repaired by numerical tolerance.
