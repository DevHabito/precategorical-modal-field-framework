# MF-R049 — rational witness and F3 proof checkpoint

**Status:** exact mathematical derivation; Lean finite-algebra module submitted
for verification. The complete analytic score/transport bridge is **not yet**
claimed as a proved Lean theorem.

**Provenance:** This is an independently derived alternative to the historical
four-point witness at `lambda = log 2`. It does not replace that witness or
amend its historical result files.

## Definitions and normalization

For a four-point probability vector `p = (p0,p1,p2,p3)` on marked support
`q = (0,1,2,3)`, define the moment polynomial

```text
M_p(t) = p0 + p1*t + p2*t^2 + p3*t^3.
```

At `lambda > 0`, its exponential moment is exactly
`M_p(exp(-lambda))`. The mean is `M_p'(1)` and the total mass is
`M_p(1)`.

The centered contraction `q'_k = (1-a)*mean + a*k` has transformed moment

```text
E_p[exp(-lambda*q')] =
    exp(-lambda*(1-a)*mean) * M_p(exp(-a*lambda)).
```

This identity follows term by term from `exp(x+y)=exp(x)exp(y)`.
For positive moments and nonzero `lambda`, the score is
`Q_lambda(p) = -log(M_p(exp(-lambda))) / lambda`.

## Construct the difference without fitting

To produce two distinct distributions with equal total mass, mean, and
moment at `t0=1/4`, their signed difference polynomial must satisfy

```text
D(1) = 0; D'(1) = 0; D(1/4) = 0.
```

Among polynomials of degree at most three, these conditions force
`D(t) = c*(t-1)^2*(t-1/4)`. Choose the rational nonzero scaling
`c=1/8` around the uniform probability vector and verify all resulting
weights are strictly positive:

```text
p+ = (15,22, 7,20) / 64
p- = (17,10,25,12) / 64
D(t) = M_p+(t)-M_p-(t)
     = (t-1)^2*(t-1/4)/8.
```

The scale `1/8` is not estimated from data: it gives a convenient exact
positive pair. The nonclosure argument works for every sufficiently small
nonzero rational scale, so no result depends on this particular numerator.

Direct exact arithmetic gives:

| Quantity | p+ | p- |
|---|---:|---:|
| Total mass | 1 | 1 |
| Mean | 3/2 | 3/2 |
| `M(1/4)` | 85/256 | 85/256 |
| `M(1/2)` | 121/256 | 119/256 |

For `lambda = 2*log(2)`, `exp(-lambda)=1/4`. Under `a=1/2`,
`exp(-a*lambda)=1/2`. Hence the next exponential moments equal

```text
exp(-3*lambda/4) * 121/256
exp(-3*lambda/4) * 119/256.
```

Their difference is `exp(-3*lambda/4)/128 > 0`. Both moments are
positive. The real logarithm is injective on positive reals, and division
by the nonzero `lambda` preserves inequality. Thus the two systems have
equal original `(mean,Q_lambda)` and different next `Q_lambda`.

This proves that the declared macrostate does **not generally** determine
the next score on the unrestricted finite-distribution class. It neither
excludes special invariant families nor establishes physical dynamics.

## Established prior literature: no priority inference

The construction belongs to the existing setting of finite exponential
moments and moment non-identifiability. The following sources support
background concepts, not novelty of our particular rational coefficients:

- Kuehn (2016), *Moment Closure—A Brief Review*, Springer, pp. 253–271:
  surveys the general closure problem and unresolved higher moments.
  https://arxiv.org/abs/1505.02190
- Lin and Dou (2021), *Statistics* 55(2), 367–385:
  studies uniqueness of distributions from sufficiently rich families of
  Laplace–Stieltjes transform values.
  https://doi.org/10.1080/02331888.2021.1893728
- Föllmer and Schied (2002), *Finance and Stochastics* 6(4), 429–447:
  precedes this project on convex risk measures. Its exact relationship
  to the score and affine update requires theorem-level comparison rather
  than inference from the article abstract.
  https://doi.org/10.1007/s007800200072

The project-specific four-point construction is not asserted to be a
new general closure theorem, a unique minimal representation, or a
priority claim. No full-text theorem comparison has been completed.

## Verification layers

1. The exact polynomial, positivity, mass, mean, and two point evaluations
   are encoded without `native_decide` in
   `formal/lean/PrecategoryFormal/DynamicNonclosure.lean`.
2. `tools/independent_c2_rational_witness.py` rechecks the rational
   equalities without historical audit imports or floating tolerances.
3. The generic exponential-moment transport identity, centered-contraction
   moment transformation, and logarithmic injectivity bridge are now
   **submitted for Lean verification** in
   `formal/lean/PrecategoryFormal/DynamicNonclosureTransport.lean`.
   Successful compiler and axiom-report evidence must be inspected before
   F3 can receive an end-to-end formal assurance label.
4. The new Lean claims require successful pinned build and `#print axioms`
   evidence, not merely the absence of `sorry` in their source.
5. Classical exponential-utility and moment-closure antecedents remain
   relevant; this exact example is not a general novelty or priority claim.

**Failed build recorded:** the first CI runs for the finite module failed
because two real-valued rational constant definitions were not declared
`noncomputable`. The corrected revision marks these constants and the real
exponential/logarithmic constructions appropriately. The failure was a Lean
definition/elaboration problem, not evidence of a false rational equality.
The corrected build is a separate verification gate, not an assumed PASS.

**Failure policy:** preserve the original witness, the alternate exact
construction, the tested source revision, and any Lean CI failure logs.
Do not narrow hypotheses, change coefficients, or label computations as
proofs to recover a preferred outcome.
