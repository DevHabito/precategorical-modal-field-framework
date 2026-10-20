# A113 A84 bilinear coefficient envelopes — partial formal checkpoint

**Date:** 2026-10-20  
**Branch:** `audit/2026-10-19-trust-and-integrity`  
**Status:** proof source submitted; the pinned Lean primary build succeeded for the initial module commit `ee45908c9ec43975c20f59be3a89289583308457` in [run 39487083634](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39487083634). The later root axiom trace and independent module `leanchecker` must be checked on their corresponding exact revision before promoting the four new declarations to full formal-assurance status.

## Goal and contract

For integers `M>=521`, with `U_M=2^(-floor(M/2))`, and real sources `129/1000<=s<=133/1000`, preserve exactly the historical A83/A84 finite channels:

```text
A = (1+(1/2)^M)/2;
H_beta = (1+beta^M)/2 - D_M(beta) + 2*epsilon_M;
H_s = (1+s^M)/2 - D_M(s) - 2*epsilon_M;
a_r = (1-r^M)/M;
beta = 1/8; tau = 1/2.
```

The first new bounded expressions are

```text
v_beta = A*a_s - H_s*a_tau;
v_s = A*a_beta - H_beta*a_tau;
v_tau = H_beta*a_s - H_s*a_beta.
```

The module `formal/lean/PrecategoryFormal/A113BilinearEnvelopes.lean`
formalizes the intended three conclusions

```text
|v_beta| <= 3*U_M/M;
|v_s|    <= 3*U_M/M;
|v_tau|  <= 3*U_M/M.
```

These bounds matter because each linear channel is a fixed factor of
one of the same three products. The affine channels add simple
differences of the already bounded A/H values. No A113 full-error
estimate or factor-sign assumption occurs in the new lemmas.

## Independent algebraic derivation

For any two channels `x,y` with `|x-1/2|<=U`,
`|y-1/2|<=U`, and two slopes `a,b` with
`0<=a,b<=t`, `|a-t|<=U*t`, `|b-t|<=U*t`:

```text
x*a-y*b = (x-1/2)*a + (a-b)/2 + (1/2-y)*b.
```

The three absolute contributions are bounded, respectively, by
`U*t`, `U*t`, and `U*t`, since
`|a-b|<=2*U*t`. Therefore

```text
|x*a-y*b| <= 3*U*t.
```

The actual finite-size theorem substitutes `t=1/M` and the
previously verified A113 bounds for target mass, H and moment slopes.
This applies separately to each of `v_beta,v_s,v_tau` without
special cases on the parity of `M` or sampling the source interval.

## Independent regression

A new standalone standard-library Python `fractions.Fraction`
checker, `tools/independent_a113_bilinear_coefficients.py`,
reconstructs both parity defects, both opposite-sign H channels,
the exact three A84 bilinear expressions, three affine coefficients,
three linear coefficients, the constant coefficient, the A84 ten-term
factor, and the ideal core. It samples six historical-size points
and three rational source values, including both interval endpoints.

Pre-push independent exact arithmetic completed without failure:

- 18 size/source cases;
- 54 bilinear, 54 affine, 54 linear and 18 constant controls;
- 90 actual-versus-ideal factor controls.

**This finite rational regression does not establish the universal
`|E-F|<20U` theorem**. The checker is included in
`.github/workflows/independent-audit.yml` and its GitHub job status
must be verified separately.

## Remaining formal obligations

To complete the ten-term error bound, formalize
`|A-H_r|<3U_M/2` and `|H_beta-H_s|<2U_M`,
transfer the three bilinear estimates to all affine and linear
coefficients, prove the constant coefficient bound and product
perturbation bound, and sum the resulting rational estimates at
`2<=k<=29`. Only then can the already certified ideal-core lower
bound yield unconditional small-left factor positivity.

The other A113 sectors, A112/A114 lifted KKT obligations,
comparative novelty and three invalid historical ZIPs remain open.
