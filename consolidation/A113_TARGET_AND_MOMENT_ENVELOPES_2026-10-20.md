# A113 finite target and moment envelopes

**Date:** 2026-10-20  
**Review branch:** `audit/2026-10-19-trust-and-integrity`  
**Status:** proof source submitted to the pinned Lean 4.33.1 workflow. Do not treat the statements as certified until the exact-code build, selected axiom trace and dedicated `leanchecker` have passed.

## Frozen quantities

Use the historically defined normalization and slopes without limiting approximations:

```text
M >= 521; h = floor(M/2); U_M = 2^(-h); tau = 1/2
A_M = (1 + tau^M)/2
a_M(r) = (1-r^M)/M
beta = 1/8; 129/1000 <= s <= 133/1000
```

The new `formal/lean/PrecategoryFormal/A113MomentEnvelopes.lean`
contains the following uniformly quantified proof objectives.

### Target mass

Since `M>=h`, `0<tau<1`, and powers of `tau` are at most one,

```text
0 <= tau^M <= tau^h = U_M.
A_M - 1/2 = tau^M/2.
|A_M - 1/2| <= U_M/2.
1/2 <= A_M <= 1.
```

The proof uses a witness `M=h+offset` in the natural numbers. The
rewriting is scoped to the target power and does **not** substitute
`M=h+offset` throughout the definition of `U_M`.

### Moment slopes

For every real `0<=r<=tau`,

```text
0 <= r^M <= tau^M <= U_M,
a_M(r) - 1/M = -r^M/M,
0 <= a_M(r) <= 1/M,
|a_M(r)-1/M| <= U_M/M.
```

At the two small nodes `r=beta` and `r=s`, because `r<=1/6`,
the independently checked geometric envelope gives the stronger
estimate

```text
|a_M(r)-1/M| <= U_M/(128*M).
```

The target node keeps the general `U_M/M` bound. All statements use
real powers with natural exponents, and ordinary real division by
the strictly positive integer size. The exact identity for the slope
residual is algebraic, not a floating-point limit.

## Assurance and open obligations

These inequalities were previously used as *analytic estimates* in the
independent small-left reconstruction. Their new formalization is a
distinct verification step. There are no A113 sign assumptions in the
new module. The dedicated GitHub Actions checks must be read before
updating this document to `verified`.

If certified, these target/slope envelopes join the already kernel-
checked ideal core, dyadic unit and denominator, actual even/odd defect,
and both H deviations. The ten-term affine, linear and constant
perturbation controls, followed by the single universal
`|E_(M,k)(s)-F_k(s)|<20U_M` conclusion, remain unproved in Lean.
Consequently neither the unconditional full small-left A113
positivity statement nor the other A113 sectors are certified.
The three damaged historical ZIPs remain a separate integrity block.
