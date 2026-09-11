# A110 — Rigorous replication review

## Verdict

**PASS — independent exhaustive replication of the finite structural closure.**

The finite A109 structural closure is now supported by two separately implemented
exact calculations: the original Stage 6 derivation and a new Fraction-based
replication that does not call the A109 full atlas and does not inspect any new
canonical full-KKT outcome after rank 430.

## Frozen scope

- parent repository commit: `533af49547d3a92f5153a2f752cea44504b16b90`
- `14 <= M <= 520`
- `129/1000 <= s <= 133/1000`
- all 1,870 distinct `(M,j)` pairs in the A94 `b+1,b+2,b+3` contact envelope
- Stage-5 preregistration SHA-256:
  `d9070d481309649bc4b2343f158e58008b31824865180fccc66b5276288d1a53`

The reconstructed preregistration bytes match the SHA announced before the
Stage-5 diagnostics.

## Exhaustive independent replication

All chunk ranges cover exactly 1..1870 with no gap or overlap.

The independent program obtained:

- 1,870 / 1,870 contact pairs completed;
- 11,220 / 11,220 residual-slope sign certificates;
- 9,350 / 9,350 threshold-order certificates;
- 67,022 exact interval boxes in those two reduced-cost tests;
- 1,870 / 1,870 positive dual-denominator certificates;
- 3,370 dual-denominator interval boxes;
- 1,870 / 1,870 exact `N_gamma = negative_constant * E_j` polynomial proportionalities;
- 1,870 / 1,870 negative proportionality factors;
- 1,870 / 1,870 conditional `E_(j-1)>0 and E_j<0 => RQ(2)>0` certificates;
- 11,402 conditional interval boxes;
- 1,870 / 1,870 primal affine-slope pairs with `dp_j/dt<0<dp_(j+1)/dt`;
- 1,870 / 1,870 `A(s)<0` certificates;
- 1,870 / 1,870 `B(s)>0` certificates;
- 1,870 / 1,870 `t'(s)>0` numerator certificates;
- 23,846 primal interval boxes;
- maximum adaptive depth: 5;
- mathematical failures: **0**.

These totals reproduce the Stage-6 announced counters exactly.

## Independent implementation-to-solver regression

On the already-inspected H19 ranks 415..430, the new implementation was compared
against the frozen direct gamma-plus solver.

- records: 16
- exact rational comparisons: 240
- mismatches: 0

The comparisons cover basic masses, `basic_t`, `active_dual_alpha_+1`,
`reduced_cost_p_1`, and the five Q checkpoints. Equality was checked as exact
rational equality, not floating-point closeness.

## Logic review

The finite closure uses the following chain.

1. The P nonbasic reduced-cost family collapses to `r_P(1)>0`.
2. The Q nonbasic reduced-cost family collapses to five checkpoints by the
   five-zero bound for the six-dimensional real exponential-polynomial system.
3. The new threshold ordering makes `R_Q(2)>0` sufficient for all six residual
   reduced-cost conditions.
4. Exact polynomial proportionality makes a strict compressed maximum
   (`E_j<0`) imply `y_gamma>0`; the earlier dual-threshold theorem then implies
   all three active dual multipliers are positive.
5. The strict compressed-maximizer pair
   `E_(j-1)>0, E_j<0` implies `R_Q(2)>0`.
6. The signed-generating-polynomial argument excludes `p_0`, `q_1`, and `p_M`
   as a first exit while the active gamma-plus equations and `t>0` hold.
7. Exact Q-block identities protect `q_(h+1)` and make `t` non-independent.
8. The finite q_h barrier proves `p_(j+1)>0 => q_h>0` on the A94 envelope.
9. All inactive slacks are identically `4*epsilon*t`.
10. `p_j(s)` is strictly decreasing and `p_(j+1)(s)` strictly increasing, so
    their common-positive set is one interval and has no hidden disconnected
    component.

Therefore, inside a strict A94 gamma-plus compressed phase, the complete strict
KKT component is exactly the region where

`p_j > 0` and `p_(j+1) > 0`.

Its only possible internal boundaries are left `p_(j+1)=0` and right `p_j=0`.

## Status change

The scientifically defensible status is now:

> **A109 is a finite structural theorem for the frozen A94/A95/A102 gamma-plus
> catalogue/parameter contract, independently replicated.**

This is stronger than the earlier statement that A109 merely survived 325
prospective mathematical resolutions.

## Remaining limits

This result does **not** establish:

- arbitrary `M`;
- source probes outside `[129/1000,133/1000]`;
- a different P/Q support family;
- a different active-band architecture;
- a universal statement about KKT systems;
- any spacetime, gravity, quantum, or empirical physical interpretation.

The next legitimate research problem is the analytic tail: determine which of
the finite-envelope inequalities admit uniform proofs for `M>=521`, and find an
exact counterexample if any one of them fails.
