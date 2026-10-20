# A113 — uniform finite-size H-channel envelopes

**Date:** 2026-10-20  
**Branch:** `audit/2026-10-19-trust-and-integrity`  
**Scope:** finite-size A83/A84 beta and source normalization; **not** the full A113 sign theorem.

## Definitions retained without asymptotic substitution

For each integer `M>=521`, set `h=floor(M/2)`, `U=(1/2)^h`, and
`d=1-(h+1)*U`. The exact historical quantities are

```text
epsilon_M = U/1875  (even M), or U/2500  (odd M)

H_beta(M) = (1+beta^M)/2 - D_M(beta) + 2*epsilon_M
H_s(M)    = (1+s^M)/2    - D_M(s)    - 2*epsilon_M

beta=1/8; 129/1000 <= s <= 133/1000.
```

The Lean definitions in `PrecategoryFormal/A113FiniteChannels.lean`
retain the two parity cases and both opposite signs. The independent
`PrecategoryFormal/A113DefectSigns.lean` theorem has already established

```text
|D_M(r)| < U/2
```

for all integers `M>=521` and all real `0<=r<=1/6`.

## Derivation of the two H bounds

For any `0<=r<=1/6`, the full-size node power is bounded by the
already checked half-size geometric power envelope:

```text
0 <= r^M <= r^h <= U/128.
```

Here `h<=M`; because `0<=r<=1`, the omitted exponent contributes
a factor at most one. The parity-independent epsilon cap is

```text
0 < epsilon_M <= U/1875.
```

Consequently, for either correction sign,

```text
|H_M(r,channel)-1/2|
  <= r^M/2 + |D_M(r)| + 2*epsilon_M
  < (1/256 + 1/2 + 2/1875)*U
  < U.
```

This gives the strict, uniform beta-channel and source-channel
deviations. All endpoint constants are exact rationals, without
floating-point rounding.

## Formal assurance boundary

The new source `formal/lean/PrecategoryFormal/A113HEnvelopes.lean`
defines and proves the full-size power comparison, the exact epsilon
cap, an elementary real-algebra bound for either Boolean channel, and
the two specialized H theorems.

**The mathematical statements may be called kernel-certified only
after the pinned Lean 4.33.1 `lake build`, selected axiom trace,
and module-specific `leanchecker` succeed for the exact source
revision.** A passing rational regression is not a substitute for
the universally quantified theorem.

The ten-term actual-versus-ideal remainder `|E_(M,k)(s)-F_k(s)|<20U`
is still open in Lean. Its remaining component estimates include
the A83 target normalization and the moment slopes, then the linear,
affine and constant A84 channels. The historical archives and
the other A113 sectors remain separate unresolved obligations.
