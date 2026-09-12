# A114-B2-W1 — exact tail witness at `M=521, s=129/1000`

## Status

**PROVED POINTWISE.**

This note proves one exact full-LP statement inside the still-open strict compressed `b+2` phase. It is **not** an all-`M` classification theorem for A114-B2.

## Contract

Fix

\[
M=521,\qquad s=\frac{129}{1000},\qquad h=260,
\]

with the frozen A112/A113 conventions

\[
\tau=\frac12,\qquad \beta=\frac18,\qquad \gamma=\frac1{16},
\]

and, because `M` is odd,

\[
\varepsilon=\frac{1}{2500\,2^{260}}.
\]

Let

\[
c(s)=\frac{\log2}{-2\log s},\qquad b=\lceil Mc(s)\rceil.
\]

The exact rational power gates

\[
2^{521}s^{176}>1,
\qquad
2^{521}s^{178}\le1
\]

certify

\[
\boxed{b=89}.
\]

## Compressed phase

The exact compressed objectives at the three A113-tail candidates satisfy

\[
V_{91}>V_{90},\qquad V_{91}>V_{92}.
\]

Therefore the strict compressed maximizer is

\[
\boxed{j=91=b+2}.
\]

The A112 upper-gamma boundary reconstruction also gives

\[
D_G>0,
\qquad
F_{b+2}^{\rm up}=F_{91}^{\rm up}<0.
\]

This is precisely the side of B2 on which the direct gamma-plus lifting argument does not close.

## Lifted candidate

Consider the full lifted basis

\[
P=\{90,91,521\},
\qquad
Q=\{0,1,260,261\},
\]

with active bands

\[
\alpha+,
\qquad
\beta-,
\qquad
\gamma-.
\]

Equivalently, this is the q0/q1 four-atom Q topology with gamma-minus active.

## Theorem

At the declared rational contract, this basis satisfies every strict KKT condition of the complete finite lifted LP:

- all eight basic variables are strictly positive;
- the three active-band dual multipliers are strictly positive;
- all `1037` nonbasic P/Q atom reduced costs are strictly positive;
- all three opposite inactive-band slacks are strictly positive;
- all primal equations hold exactly;
- the primal and dual objective values are exactly equal.

The strict-condition count is therefore

\[
8+3+1037+3=1051=2M+9.
\]

The smallest strict condition is

`reduced_cost_p_520`,

with positive decimal value approximately

\[
8.001525988146702\times10^{-31}.
\]

Hence

\[
\boxed{
P=\{90,91,521\},\ Q=\{0,1,260,261\},\
(\alpha+,\beta-,\gamma-)
}
\]

is the **unique strict global optimum** of the declared finite lifted LP at

\[
\boxed{M=521,\ s=129/1000}.
\]

## Exact negative controls

Three natural gamma-plus alternatives were reconstructed exactly rather than merely rejected numerically.

### Same P/Q support with gamma-plus

Keeping

\[
P=\{90,91,521\},\qquad Q=\{0,1,260,261\}
\]

but switching to `gamma+` fails through

- `basic_q_0<0`, and
- `active_dual_gamma_+1<0`.

### Gamma-plus at contact `b+1`

The basis

\[
P=\{0,90,91,521\},\qquad Q=\{1,260,261\}
\]

is primal-feasible but fails exactly through

\[
\boxed{y_{\gamma+}<0}.
\]

This is the clean pointwise obstruction showing why the B1 proof cannot simply be copied into B2.

### Gamma-plus at contact `b+2`

The basis

\[
P=\{0,91,92,521\},\qquad Q=\{1,260,261\}
\]

fails through

\[
\boxed{p_{92}<0}.
\]

Thus the two adjacent gamma-plus branches fail for distinct structural reasons.

## Independent replication

The main certificate uses exact SymPy rational arithmetic. A second implementation uses only Python `fractions.Fraction`, with an independent Gauss-Jordan solver and independent KKT reconstruction.

It reproduces:

- `1051/1051` strict KKT conditions for the q0/q1 gamma-minus candidate;
- the same smallest strict condition `reduced_cost_p_520`;
- rejection of gamma-plus contact `b+1` by the active gamma multiplier;
- rejection of gamma-plus contact `b+2` by `basic_p_92`;
- exact primal equations and exact primal-dual equality.

## Scientific consequence

This point establishes that non-gamma-plus lifted structure does **not** disappear merely because the analytic tail has begun at `M>=521`.

In particular, the proposition

`all strict compressed b+2 tail points lift to gamma-plus`

is false.

What is proved here is only one exact counterexample/witness and its unique full-LP optimum. The classification of the complete strict compressed `b+2` phase remains open.

## Reproducibility files

- `a114b2_w1_m521_exact_kkt_certificate.py`
- `A114B2_W1_M521_EXACT_KKT_CERTIFICATE_20260912.json`
- `a114b2_w1_m521_fraction_crosscheck.py`
- `A114B2_W1_M521_FRACTION_CROSSCHECK_20260912.json`
- `a114b2_w1_corrected_discovery.py`
- `A114B2_W1_CORRECTED_DISCOVERY_20260912.json`

The corrected high-precision simplex file is provenance/discovery only; the theorem does not depend on it.

## Claim boundary

Not proved by A114-B2-W1:

- an all-`M` B2 architecture law;
- that `F_(b+2)^up<0` always selects q0/q1 gamma-minus;
- that the other finite-atlas B2 architectures disappear in the tail;
- a complete classification of transition sets;
- any statement outside `129/1000<=s<=133/1000`;
- any physical interpretation.
