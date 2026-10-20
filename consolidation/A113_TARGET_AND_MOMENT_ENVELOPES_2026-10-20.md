# A113 finite target and moment envelopes

**Date:** 2026-10-20  
**Review branch:** `audit/2026-10-19-trust-and-integrity`  
**Status:** the pinned Lean 4.33.1 `lake build` and seven selected theorem-axiom traces **passed** for formal commit `3dd0525f9bc9644f71be51e775aab3829cfb8562` in [Actions run 39466591437](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39466591437). All seven printed only `propext`, `Classical.choice`, and `Quot.sound`, with no native evaluation axioms. The dedicated module-level `leanchecker (PrecategoryFormal.A113MomentEnvelopes)` and the complete 26-job matrix subsequently **passed** for source commit `b77745052bbb716ae67cd69784cb702ebe168dea` in [Actions run 39467407162](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39467407162). The independent audit also passed in [run 39467407166](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39467407166).

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
independent small-left reconstruction. Their formalization passed the
complete Lean build and selected axiom trace, but the isolated checker
has since passed at the pinned revision cited above. There are no A113 sign assumptions in
the new module. The independently written standard-library rational
regression passed 30 exact size/node pairs in [audit run 39466979975](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39466979975), including the endpoint 0 and target 1/2. This sample is not the universal proof.

If certified, these target/slope envelopes join the already kernel-
checked ideal core, dyadic unit and denominator, actual even/odd defect,
and both H deviations. The ten-term affine, linear and constant
perturbation controls, followed by the single universal
`|E_(M,k)(s)-F_k(s)|<20U_M` conclusion, remain unproved in Lean.
Consequently neither the unconditional full small-left A113
positivity statement nor the other A113 sectors are certified.
The three damaged historical ZIPs remain a separate integrity block.
