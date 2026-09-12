# A114-A — Analytic-tail endpoint-released lift theorem

## Status

**PROVED under the frozen reduced/lifted contract, conditional on the compressed maximizer being `j=b+3`.**

The proof is exact. No floating-point sign decision enters the theorem certificate.

## Contract

Let

\[
M\ge 521,\qquad \frac{129}{1000}\le s\le\frac{133}{1000},
\]

with

\[
\beta=\frac18,\qquad \tau=\frac12,\qquad \gamma=\frac1{16},\qquad h=\lfloor M/2\rfloor,
\]

and

\[
c(s)=\frac{\log 2}{-2\log s},\qquad b=\lceil Mc(s)\rceil.
\]

Assume the compressed objective has strict maximizer

\[
\boxed{j=b+3}.
\]

Equivalently in the adjacent-factor notation,

\[
E_{j-1}>0>E_j.
\]

A113 already proves that every compressed maximizer in the tail belongs to
`{b+1,b+2,b+3}` and that all remote factors after `b+2` are negative.

## The lifted architecture

Consider the endpoint-released basis

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,
\qquad
\beta-,
\]

and gamma inactive in both orientations.

## Theorem

Under the contract and hypothesis above, every strict KKT condition of the full declared finite lifted LP is satisfied:

- all basic variables are strictly positive;
- the two active multipliers are strictly positive;
- every unused P-atom reduced cost is strictly positive;
- every unused Q-atom reduced cost is strictly positive;
- both inactive gamma slacks are strictly positive;
- the opposite alpha/beta slacks are strictly positive.

Therefore the endpoint-released basis is the unique strict global basic optimum of the declared lifted LP.

In compact form,

\[
\boxed{
 j=b+3\text{ strict compressed maximizer}
 \Longrightarrow
 \text{endpoint-released strict global KKT optimum}.
}
\]

## Proof map

### 1. The strict `b+3` phase forces a quantitative source lower bound

Write

\[
U=2^{-h},\qquad Q=\frac{s^{b+2}}{U}.
\]

The A113 exponential-polynomial decomposition is rebuilt locally in the A114-A certificate. The inherited coefficient caps are re-derived rather than copied:

- the D-block remainder cap;
- `H<0.51`;
- `Delta/U>0.0043`;
- `M|X|/U<0.271`;
- the affine-channel cap `<0.36`.

Assuming `Q<=0.009` gives the exact upper bound

\[
\frac{E_{b+2}}{U\tau^{b+2}}
< -5.7106602687140\times 10^{-5}<0.
\]

Hence

\[
\boxed{E_{b+2}>0\Longrightarrow Q>0.009.}
\]

### 2. Endpoint primal signs

After eliminating normalization, mean and the central Q block, the endpoint family reduces to a 2x2 system. Both parity cases are treated exactly.

The easy interval gates prove positivity of:

- the reduced determinant;
- the scale numerator;
- `q1` and `qh` numerators;
- the active dual numerators;
- the two neighboring compressed determinants.

The cancellation-prone quantities are written as exact symbolic numerators and decomposed as

\[
\text{numerator}=\text{core}+\text{remainder}.
\]

The final absolute core-minus-remainder margins are strictly positive. The smallest reported hard margins are still comfortably positive:

- even gamma-minus conservative numerator: about `0.0423`;
- odd gamma-plus conservative numerator: about `0.0120`.

The endpoint masses `p_(j-1)` and `p_j` are therefore positive. Positivity of `p_M` follows from the exact mean identity once `t>0`, `p_(j-1)>0` and `j/M<1/2` are known.

The remaining Q mass `q_(h+1)` follows from the exact parity formulas for the central Q block.

### 3. Exact straddling and `reduced_cost_p0`

The certificate proves the exact numerator identities linking the endpoint masses to the two adjacent compressed `p0` numerators. They imply

\[
p_0^{j-1}>0>p_0^j.
\]

The simplex exchange identity is

\[
V_j-V_{j-1}
=
 r_E(p_0)\bigl(p_0^{j-1}-p_0^j\bigr).
\]

Since strict compressed maximality gives `V_j-V_(j-1)>0`, the straddling gives

\[
\boxed{r_E(p_0)>0.}
\]

The negative-control case `M=521, s=0.129, j=b+3` but **not** a compressed maximum fails exactly through `basic_p_j<0` and `reduced_cost_p0<0`. Thus the compressed-maximizer hypothesis is genuinely necessary and is not decorative.

### 4. P reduced-cost collapse

The P reduced-cost function belongs to the five-dimensional extended-Chebyshev space

\[
\operatorname{span}\{1,x,\beta^x,s^x,\tau^x\}.
\]

Its basic zeros are

\[
j-1,\quad j,\quad M.
\]

The theorem certificate proves positivity at

\[
0,\quad j-2,\quad j+1,\quad M-1.
\]

A hypothetical negative nonbasic integer on either populated side would force two additional real zeros by continuity. Together with the three existing roots this would exceed the four-zero budget of the ECT space. Therefore every nonbasic P reduced cost is positive.

### 5. Q reduced-cost collapse

The Q reduced-cost function belongs to the same ECT space and has basic roots

\[
1,\quad h,\quad h+1.
\]

The certificate proves

\[
r_Q(0)>0,\qquad r_Q(2)>0.
\]

Because the values at 0 and 2 are both positive while `r_Q(1)=0`, the root at 1 has even multiplicity at least two. Together with the distinct roots `h,h+1`, this exhausts the four-zero budget. Hence there is no room for an additional sign-changing zero at an integer nonbasic Q atom, and all Q reduced costs are positive.

### 6. Inactive slacks

The opposite alpha/beta slacks reduce exactly to

\[
4\varepsilon t>0.
\]

For gamma, the proof avoids cancellation by bounding the two orientations separately:

\[
2\varepsilon t-P_\gamma>0,
\qquad
2\varepsilon t-Q_\gamma>0.
\]

The exact core-plus-remainder margins remain positive in both parities.

## Independent replication

A separate `Fraction`-only LP implementation, which does not import the theorem certificate, reconstructs the original seven equality rows, solves the basis, solves the dual, and scans every unused P/Q atom.

It reproduces:

- the historical A96 endpoint-released witness at `M=125`;
- an odd tail case `M=561, s=129/1000, b=95, j=98`;
- an even tail case `M=1282, s=129/1000, b=217, j=220`.

Both tail cases are independently confirmed to satisfy

\[
E_{j-1}>0>E_j
\]

and the complete endpoint KKT system.

The same independent solver rejects the negative control

\[
M=521,\ s=129/1000,\ b=89,\ j=92=b+3,
\]

because it is not a compressed maximum.

## Corrections made during proof construction

Several stronger or intermediate statements were deliberately rejected or corrected:

1. `j=b+3` by itself is insufficient; strict compressed maximality is necessary.
2. The common-denominator numerator of `r_P(M-1)` is **not** globally divisible by `m`; only its core is. The final proof bounds remainder/m termwise using certified tail/m envelopes.
3. An early `RQ(2)` core bound mixed `s_max` and `s_min` inside one increasing quadratic. The final proof uses the true common endpoint.
4. The first corrected `RQ(2)` lower bound still used `w_min` in a subtractive term `-wA`; the valid lower bound uses `w_max`.
5. The first `p_j` core lower bound used `a_min` where a subtractive product requires `max(a+m)`. The final margin uses the correct extremum.

All corrected margins remain strictly positive.

## Claim boundary

A114-A does **not** prove a universal lifted architecture theorem.

It proves only the `b+3` strict compressed phase in the frozen tail window.

Still open:

- global lifted architecture classification inside `b+1` phases;
- global lifted architecture classification inside `b+2` phases;
- how the gamma-plus, two-band, q0/q1 and gamma-minus architectures partition those phases;
- any extension outside the declared source window;
- any physical interpretation.

The next rigorous target is therefore the lifted architecture selection inside the remaining `b+1` and `b+2` compressed phases.
