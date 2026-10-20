# A113 — exact ideal-core recurrence and uniform small-left bound

**Date:** 2026-10-20  
**Scope:** the ideal A83/A84 comparison factor, **not** the full finite-`M` adjacent factor.  
**Status:** the universal ideal-core lower bound compiled in Lean 4.33.1, passed the selected axiom trace, and passed its dedicated `leanchecker` job in [formal run 39403579662](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39403579662). Other independent checker jobs in the same matrix encountered unrelated Lean-download TLS errors; the full matrix should not be labeled green until their retries complete.

## Definitions

Fix three real nodes `0 < beta < s < tau`, and define

```text
F_k = 1/2 * [
    (s-beta)*(beta*s)^k
  + (beta-tau)*(beta*tau)^k
  + (tau-s)*(s*tau)^k
].
```

This is the idealized core `contactIdealCore k beta tau s` already proved
algebraically to agree with the equal-half-moment, common-slope A83
cofactor expression. It is not the actual `E_(M,k)(s)` at finite `M`.

## Exact recurrence

Expanding the three terms and collecting powers gives, for every
natural `k`,

```text
F_(k+1) - (s*tau)*F_k
  = (1/2)*(s-beta)*(tau-beta) *
      [tau*(beta*tau)^k - s*(beta*s)^k].
```

The right-hand bracket is nonnegative because

```text
0 <= beta*s <= beta*tau
0 <= s <= tau,
s*(beta*s)^k <= tau*(beta*s)^k <= tau*(beta*tau)^k.
```

Thus `F_(k+1) >= s*tau*F_k`. The first-contact value factors exactly:

```text
F_1 = (1/2)*(s-beta)*(tau-beta)*(tau-s) > 0.
```

Induction yields an unrestricted ideal-core theorem:

```text
F_k >= F_1*(s*tau)^(k-1) > 0, for every integer k >= 1.
```

No numerical scan, A113 certificate, `native_decide`, or
homogeneous-polynomial identity is used in this argument. The recurrence
supplies the desired lower bound directly and is simpler to formalize
than a general three-node complete-homogeneous-polynomial identity.

## Frozen small-left uniform inequality

For `beta=1/8`, `tau=1/2`, `129/1000 <= s <= 133/1000`,
and `2 <= k <= 29`, define the exact rational constant

```text
L = (1/2)*(129/1000-1/8)*(1/2-1/8)
        *(1/2-133/1000)*(129/2000)^28.
```

Each factor in `F_1` has its declared lower bound, and

```text
129/2000 <= s*tau < 1,
k-1 <= 28,
(s*tau)^(k-1) >= (s*tau)^28 >= (129/2000)^28.
```

Hence `F_k >= L > 0`. A separately checked exact rational gate
confirms `L > 20/2^260`. This is the ideal-core premise needed by the
earlier conditional small-left transport theorem.

## Code and assurance boundary

The new module
`formal/lean/PrecategoryFormal/A113IdealCoreUniform.lean` encodes:

- the exact recurrence;
- the order-theoretic nonnegative correction;
- an all-contact inductive power lower bound;
- monotonicity of real powers of bases in `[0,1]`;
- the frozen uniform lower bound for `2<=k<=29`;
- the resulting *conditional* transport theorem retaining the actual
  remainder and unit bounds as explicit hypotheses.

`tools/independent_a113_ideal_core.py` is a separate standard-library
rational regression. It evaluates **87 distinct** source/contact pairs
(3 source values times 29 contacts) and two boundary-equality controls.
Because `F_k` has no `M` dependence, multiplying this count by
several `M` values would be misleading. These controls are not the
proof of a continuum statement.

**What remains open in Lean:** the actual `D_M(r)` and parity-dependent
`H_r` definitions, the bound `|E_(M,k)-F_k|<20*2^(-floor(M/2))`,
and the dyadic size implication `M>=521 => U<=2^(-260)`.
The other A113 sectors, lifted KKT, historical ZIP integrity, and
literature priority are also outside this checkpoint. A PR merge must
not be based on this ideal-core result alone.
