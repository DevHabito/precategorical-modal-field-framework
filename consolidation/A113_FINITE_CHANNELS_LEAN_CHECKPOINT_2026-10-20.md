# A113 finite channels — parity-safe Lean bridge

**Date:** 2026-10-20  
**Source branch:** `audit/2026-10-19-trust-and-integrity`  
**Status:** exact definitions and scoped lemmas committed to Lean. Any
compilation or checker status must be taken from a pinned Actions run
for the exact revision, not inferred from this document.

## Exact historical normalization

For each integer `M>=521` write

```text
h = floor(M/2)
U = (1/2)^h
d = 1 - (h+1)*U
eps = U/1875   if M is even
      U/2500   if M is odd
```

The retained A84 expressions are, with `r` an arbitrary real:

```text
D_even(r) =
    -2*U*r/d
  + (1+2*h*U/d)*r^h
  - 2*(h-1)*U*r^(h+1)/d

D_odd(r) =
    -(3/2)*U*r/d
  + (1/2+(3/2)*h*U/d)*r^h
  + (1/2-(3/2)*(h-1)*U/d)*r^(h+1)

H_beta = (1+beta^M)/2 - D_M(beta) + 2*eps
H_s    = (1+s^M)/2 - D_M(s)       - 2*eps

A = (1+(1/2)^M)/2
a_M(r) = (1-r^M)/M
```

The Lean definitions are in
`formal/lean/PrecategoryFormal/A113FiniteChannels.lean`, including
`a113ActualFactor` defined by the original A83 cofactor combination.
They are full finite-`M` expressions; the ideal core is defined in
a separate module, and is never substituted as the actual factor.

An arbitrary-node comparison of the two H conventions proves

```text
H_M(r,beta_channel) - H_M(r,source_channel) = 4*eps_M.
```

This checks the signs independent of any bound or sign law.

## Proven-on-paper dyadic and denominator estimates

For `M>=521`, integer division gives `h>=260`. For any integer
`n>=5`, the sequence `(n+1)/2^n` is nonincreasing: at the base
`n=5`, its value is `6/32=3/16 <1/4`; the induction step uses

```text
(n+2)/2^(n+1) <= (n+1)/2^n
  because n+2 <= 2(n+1).
```

Therefore, in the frozen range,

```text
0 < U <= (1/2)^260 = 1/2^260,
0 < 3/4 <= d.
```

The Lean source includes named, universally quantified theorems for
these relations; certification must be checked against its final CI
log and an independent `leanchecker` module replay.

## What the final sign-transport theorem does and does not prove

The conditional Lean theorem
`a113ActualFactor_pos_of_uniform_error` consumes the
**explicitly assumed**, currently unverified quantitative premise

```text
abs(a113ActualFactor M k s - contactIdealCore k 1/8 1/2 s)
    < 20*a113Unit M.
```

It then uses the earlier fully proved ideal-core lower bound and
the dyadic unit estimate to infer positivity for `M>=521`,
`2<=k<=29`, `129/1000<=s<=133/1000`.

This is **not** an unconditional proof of finite-size positivity.
No hidden `axiom`, `sorry`, `admit`, or experimental inference is
used to replace the error premise.

## Next exact obligations

1. Derive `|D_M(r)| < U/2` for `r=beta` or
   `s in [129/1000,133/1000]`, for both parities, using the
   positive denominator and the geometric high-power bounds.
2. Derive `|H_beta-1/2|<U` and `|H_s-1/2|<U`, retaining
   opposite `2*eps` terms; prove matching bounds on
   `a_M(r)` and `A`.
3. Derive the actual factor's ten-term remainder bounds
   (affine channels, linear coefficients and the constant).
4. Combine them to prove `|E_(M,k)(s)-F_k(s)|<20U`
   **unconditionally** for the frozen small-left sector.

The other A113 sectors, lifted KKT, historical corrupt ZIPs and any
physical interpretation are still separate unresolved obligations.
