# A114-B2-W1 logical audit — 2026-09-12

## Verdict

**PASS for the exact pointwise result at `M=521, s=129/1000`.**

**A114-B2 remains OPEN as a phase-classification problem.**

## Contract

The promoted certificate uses the odd-tail contract

`M=521`, `h=260`, `s=129/1000`, `epsilon=1/(2500*2^260)`.

Exact integer-power inequalities certify `b=89`. The compressed objectives at contacts `90,91,92` are reconstructed with rational arithmetic and give the strict winner `91=b+2`.

## Full KKT certificate

The candidate is

`P={90,91,521}`, `Q={0,1,260,261}`,

with active bands `alpha+`, `beta-`, `gamma-`.

The primary exact certificate checks all `1051=2M+9` strict KKT conditions, all primal equations, and exact primal-dual objective equality. The smallest strict condition is `reduced_cost_p_520>0`.

A separate implementation based on Python `fractions.Fraction` repeats the full pointwise check and obtains the same result.

## Negative controls

Three exact controls are retained:

1. the same q0/q1 support with `gamma+` fails through `basic_q_0` and the gamma+ multiplier;
2. gamma-plus at contact `b+1` fails through `active_dual_gamma_+1<0`;
3. gamma-plus at contact `b+2` fails through `basic_p_92<0`.

## Discovery correction

The first exploratory M=521 simplex run used the wrong parity scale `1875` and is invalid. The corrected discovery uses `2500` and recovers the same candidate. Discovery is kept only as provenance; the promoted pointwise result is certified by the exact checks above.

## Quantifier boundary

Promoted:

`At M=521 and s=129/1000, the unique strict global lifted optimum is P={90,91,521}, Q={0,1,260,261}, with alpha+, beta-, gamma- active.`

Not promoted:

- `strict b+2 => q0/q1 gamma-minus`;
- `Phi<0 => q0/q1 gamma-minus` for every tail point;
- a complete architecture classification of the `b+2` phase.
