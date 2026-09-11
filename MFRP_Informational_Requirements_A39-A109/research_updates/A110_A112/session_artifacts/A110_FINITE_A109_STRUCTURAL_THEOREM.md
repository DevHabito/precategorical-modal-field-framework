# A110 — Finite structural closure of A109

## Verdict

Within the frozen finite A94/A102 contract

\[
14\le M\le520,\qquad
129/1000\le s\le133/1000,
\]

and the gamma-plus architecture

\[
P=\{0,j,j+1,M\},\qquad
Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

the A109 two-adjacent-boundary mechanism can now be closed structurally.

No new full-atlas outcome for canonical ranks 431..922 was used.

---

## 1. Reduced costs collapse to `reduced_cost_q_2`

Earlier exact work reduced all P-type nonbasic reduced costs to

\[
r_P(1)>0
\]

and all Q-type nonbasic reduced costs to the five checkpoints

\[
R_Q(0),R_Q(2),R_Q(h-1),R_Q(h+2),R_Q(M).
\]

The new exact continuum audit covers every one of the 1,870 distinct
\((M,j)\) pairs in the A94 contact envelope.

For each pair and every \(s\) in the complete source window, all six quantities

\[
r_P(1),R_Q(0),R_Q(2),R_Q(h-1),R_Q(h+2),R_Q(M)
\]

are affine functions of the same dual coordinate \(y_\alpha\), with strictly
negative slope.

Their zero thresholds satisfy

\[
T_{Q,2}
<
T_{P,1},\,
T_{Q,0},\,
T_{Q,h-1},\,
T_{Q,h+2},\,
T_{Q,M}.
\]

This was certified by 11,220 exact slope-sign certificates and 9,350 exact
threshold-order certificates on the full rational source interval, with zero
failures.

Therefore

\[
\boxed{
R_Q(2)>0
\Longrightarrow
\text{every nonbasic P and Q reduced cost is positive}.
}
\]

---

## 2. The compressed maximizer forces the active duals

Let

\[
E_j(s)=V_{j+1}(s)-V_j(s)
\]

be the exact A94 adjacent compressed-objective factor.

For all 1,870 finite-envelope pairs, coefficient-by-coefficient exact rational
comparison gives

\[
N_\gamma(s)=-K_{M,j}E_j(s),
\qquad K_{M,j}>0,
\]

where \(N_\gamma\) is the numerator of the gamma-plus active multiplier.
The common dual denominator is strictly positive throughout the source window.

Hence

\[
\boxed{
E_j(s)<0\Longrightarrow y_\gamma(s)>0.
}
\]

The previously proved active-dual threshold ordering then gives

\[
y_\gamma>0
\Longrightarrow
y_\alpha>0,\qquad y_\beta>0.
\]

So a strict compressed maximum automatically protects all three active dual
multipliers.

---

## 3. A strict compressed maximum also forces `RQ(2)>0`

For a strict interior compressed maximizer \(j\),

\[
E_{j-1}(s)>0,\qquad E_j(s)<0.
\]

An exact conditional interval audit over the same 1,870-pair envelope proves

\[
\boxed{
E_{j-1}>0,\ E_j<0
\Longrightarrow
R_Q(2)>0.
}
\]

The proof audit visited 11,402 exact rational interval boxes, required maximum
adaptive depth 5, and left zero unresolved boxes.

Combining Sections 1–3:

\[
\boxed{
j\text{ strict compressed maximizer}
\Longrightarrow
\text{all active duals and all nonbasic reduced costs are positive}.
}
\]

---

## 4. Remaining basic variables

Previous structural reductions give:

- `basic_p_0`, `basic_q_1`, and `basic_p_M` cannot be the first basic
  obstruction by Descartes/sign-variation of the signed generating polynomial;
- `basic_q_(h+1)` is controlled by the exact Q-block identities;
- `basic_t` is the sum of the Q masses and is not an independent first
  obstruction;
- on the finite A94 contact envelope,
  \[
  p_{j+1}>0\Longrightarrow q_h>0;
  \]
- all three inactive slacks are identically
  \[
  4\varepsilon t>0.
  \]

Thus, inside a strict compressed-maximizer phase, the only basic variables
that can terminate the strict KKT component are

\[
\boxed{p_j,\quad p_{j+1}.}
\]

---

## 5. No hidden roots: the adjacent masses are monotone

Write the seven source-independent primal equations using `basic_t=t` as the
affine coordinate.

For every finite-envelope pair,

\[
\frac{\partial p_j}{\partial t}<0,
\qquad
\frac{\partial p_{j+1}}{\partial t}>0.
\]

The alpha equation gives

\[
t(s)=-\frac{B(s)}{A(s)}.
\]

Exact interval certificates over the complete source window establish

\[
A(s)<0,\qquad B(s)>0,
\]

and

\[
B(s)A'(s)-B'(s)A(s)>0.
\]

Therefore

\[
t'(s)>0.
\]

Consequently

\[
\boxed{
p_j(s)\text{ is strictly decreasing},
\qquad
p_{j+1}(s)\text{ is strictly increasing}.
}
\]

Each can cross zero at most once.

So the strict KKT component cannot split into hidden disconnected pieces.

---

## 6. Finite A109 theorem

Let a frozen A102 gamma-plus source record lie inside a strict A94 compressed
phase.

Because the source witness is strict and the results above exclude every
non-adjacent KKT obstruction, the complete strict KKT component is exactly

\[
\{s:\ p_j(s)>0,\ p_{j+1}(s)>0\}
\]

inside that source phase.

Because the two functions are monotone in opposite directions, this set is a
single interval.

Its only possible internal boundaries are:

\[
\boxed{
\text{left: }p_{j+1}=0,
\qquad
\text{right: }p_j=0.
}
\]

Thus the A109 endpoint-sign classifier is structurally valid for the frozen
finite A102 gamma-plus catalogue:

- both endpoint target signs positive: full coverage;
- only \(p_{j+1}\) fails at the left endpoint: left partial;
- only \(p_j\) fails at the right endpoint: right partial;
- both fail at their respective outer endpoints: two-sided partial, with the
  strict witness between the unique roots.

This is no longer merely a pattern inferred from the 325 prospectively
resolved ranks.

It is a **finite structural theorem** under the already-frozen A94/A95/A102
architecture and finite parameter contract.

---

## 7. What this does not prove

It does not establish:

- arbitrary \(M\);
- a different source interval;
- a different P/Q support family;
- a different active-band architecture;
- a general theorem for all relational models;
- any physical, spacetime, gravitational, quantum, or experimental claim.

The next mathematically meaningful question is whether the finite proof can be
lifted to an analytic all-\(M\) theorem, or whether one of its finite-envelope
inequalities eventually fails outside the declared contract.
