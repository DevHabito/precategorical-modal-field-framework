# Complete One-Pivot Neighborhood and the First \(M=13\) Grammar Break

**Programme:** Modal Field Research Programme  
**Provisional audit:** A73  
**Author line:** Felipe Gianini Romero  
**Status:** complete exact classification of a declared one-pivot signature neighborhood at one rational probe, plus an exact \(M=13\) global theorem; not a complete LP-basis enumeration

## Technical abstract

A72 established a four-signature terminal pivot diamond for \(M=10,11,12\).
It did not enumerate the complete local one-pivot neighborhood.

A73 performs that enumeration at the common exact probe

\[
\boxed{
s_0=\frac{33}{256}
}
\]

or

\[
\boxed{
\alpha_0
=
-\log_2\left(\frac{33}{256}\right)
=
2.9556058806415465623\ldots.
}
\]

The reference late-stage signature is

\[
S_M:
\begin{cases}
P=\{0,3,4,M\},\\
Q=\{1,h,h+1\},\\
h=\lfloor M/2\rfloor,\\
\text{active bands}=\{\alpha+,\beta-,\gamma+\}.
\end{cases}
\]

The same rational probe lies strictly inside:

- the exact \(S_{11}\) phase;
- the exact \(S_{12}\) phase;
- the exact \(M=13\) phase with the same contacts but
  \(\gamma-\) instead of \(\gamma+\).

The declared one-pivot neighborhood contains every signature obtained by
exactly one of the following operations:

1. exchange one active \(P\) contact with one inactive \(P\) contact;
2. exchange one active \(Q\) contact with one inactive \(Q\) contact;
3. flip the sign of the active \(\beta\) or \(\gamma\) band;
4. deactivate \(\beta\) or \(\gamma\) while one active \(P\) or \(Q\)
   contact leaves the reduced basis.

The scale variable is retained. The \(\alpha\) band is not flipped or
deactivated. Two-contact exchanges and combined contact/sign changes are
excluded.

The exact neighborhood sizes are

\[
75,\qquad82,\qquad89
\]

for \(M=11,12,13\), giving

\[
\boxed{246}
\]

single-pivot neighbors.

Including the three reference signatures, 249 exact rational bases were
evaluated.

Every basis was classified through the full KKT hierarchy:

1. primal basic-variable signs;
2. active observation multipliers;
3. nonbasic reduced costs;
4. inactive observation slacks;
5. local optimality.

No candidate was singular and no rank mismatch occurred.

The combined one-pivot classification is

\[
\boxed{
181\text{ primal infeasible},
}
\]

\[
\boxed{
25\text{ active-dual infeasible},
}
\]

\[
\boxed{
37\text{ reduced-cost infeasible},
}
\]

\[
\boxed{
2\text{ inactive-slack infeasible},
}
\]

and

\[
\boxed{
1\text{ locally optimal}.
}
\]

At \(M=11\) and \(M=12\), no one-pivot neighbor is locally optimal. The
reference \(S_M\) signature is the unique strict local KKT optimum.

At \(M=13\), the reference \(S_{13}\) signature is rejected by

\[
\boxed{
\lambda_{\gamma+}
=
-2417766079298191810149220362330917219631104/321825089367461621927536123652615519643349
<0.
}
\]

Among all 89 one-pivot neighbors, the unique strict local optimum is obtained
by the single row-sign pivot

\[
\boxed{
\gamma+\longrightarrow\gamma-.
}
\]

The contacts remain unchanged:

\[
P=\{0,3,4,13\},
\qquad
Q=\{1,6,7\}.
\]

Thus the first exact grammar break is not a hidden contact exchange, a
singular tie, or a numerical basis ambiguity. It is a pure completion-band
sign selection forced by dual feasibility.

A73 also extends the global first-boundary theorem to \(M=13\). The exact
integer catalogue has 84 designs and the unique winner remains

\[
\boxed{\{2,3,4\}.}
\]

The continuous completion

\[
\{\alpha,3,4\}
\]

has eight exact algebraic phases and seven simple finite transitions. Its
risk is strictly increasing on

\[
[2,3),
\]

so

\[
\boxed{\alpha^\star=2}
\]

remains the unique global first-anchor optimum.

---

## 1. Exact probe and phase membership

The probe is rational in \(s\), not an approximate \(\alpha\)-coordinate.

For \(M=11\) and \(M=12\), it lies in phase 4:

\[
S_M:
\quad
P=\{0,3,4,M\},
\quad
Q=\{1,h,h+1\},
\quad
\alpha+,\beta-,\gamma+.
\]

For \(M=13\), it lies in phase 7:

\[
B_{13}:
\quad
P=\{0,3,4,13\},
\quad
Q=\{1,6,7\},
\quad
\alpha+,\beta-,\gamma-.
\]

All three phase memberships were checked against exact rational isolating
intervals, not decimal transition approximations.

---

## 2. Declared neighborhood completeness

For a support with \(M+1\) states, the reference signature has four active
\(P\) contacts and three active \(Q\) contacts.

The number of \(P\)-exchange candidates is

\[
4\bigl((M+1)-4\bigr)=4(M-3).
\]

The number of \(Q\)-exchange candidates is

\[
3\bigl((M+1)-3\bigr)=3(M-2).
\]

There are two completion-band sign flips.

There are fourteen band-deactivation/contact-leaving candidates:

\[
2(4+3)=14.
\]

Therefore the declared one-pivot count is

\[
4(M-3)+3(M-2)+2+14
=
7M-2.
\]

This gives:

\[
75,\ 82,\ 89
\]

at \(M=11,12,13\).

---

## 3. Classification by support

| \(M\) | Neighbors | Primal | Active dual | Reduced cost | Inactive slack | Local optimum |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 75 | 57 | 4 | 13 | 1 | 0 |
| 12 | 82 | 60 | 8 | 13 | 1 | 0 |
| 13 | 89 | 64 | 13 | 11 | 0 | 1 |

At \(M=11\) and \(M=12\), the reference signature is strictly optimal and
all declared neighbors fail at least one exact KKT condition.

At \(M=13\), one neighbor is strictly optimal and the reference itself is
dual-infeasible.

---

## 4. Classification by pivot type

| Pivot type | Candidates | Primal | Active dual | Reduced cost | Inactive slack | Local optimum |
|---|---:|---:|---:|---:|---:|---:|
| `p_contact_exchange` | 108 | 83 | 6 | 19 | 0 | 0 |
| `q_contact_exchange` | 90 | 65 | 11 | 14 | 0 | 0 |
| `completion_band_sign_flip` | 6 | 3 | 2 | 0 | 0 | 1 |
| `deactivate_band_remove_p_contact` | 24 | 12 | 6 | 4 | 2 | 0 |
| `deactivate_band_remove_q_contact` | 18 | 18 | 0 | 0 | 0 | 0 |

Contact exchanges overwhelmingly fail primal feasibility.

Among the six sign-flip candidates across the three supports:

- three are primal infeasible;
- two are dual-multiplier infeasible;
- one is locally optimal.

The unique surviving sign flip is the \(M=13\) \(\gamma\)-band reversal.

---

## 5. Exact \(M=13\) selection

The reference \(S_{13}\) basis is primal feasible at the probe. It is not
discarded by a negative basic variable or a reduced cost.

It fails specifically because the active positive \(\gamma\)-band multiplier
is negative:

\[
\lambda_{\gamma+}
=
-2417766079298191810149220362330917219631104/321825089367461621927536123652615519643349.
\]

Active inequality multipliers must be nonnegative. Hence \(S_{13}\) cannot
be locally optimal.

Replacing only

\[
\gamma+
\quad\text{by}\quad
\gamma-
\]

produces a basis with:

- all basic variables strictly positive;
- all active multipliers strictly positive;
- all nonbasic reduced costs strictly positive;
- all inactive observation slacks strictly positive.

It is therefore a strict local KKT optimum.

The exact ratio at the probe is

\[
\boxed{
\rho_{13}(s_0)
=
18952358970362603204693358995617015511754371/5002976055488424213430705950605245596462416.
}
\]

---

## 6. Exact global \(M=13\) theorem

The integer catalogue winner is

\[
\{2,3,4\}
\]

with exact ratio

\[
\boxed{
64844289946255264972429/38856153250389533993590.
}
\]

The runner-up is

\[
\{2,3,5\}
\]

and the exact positive gap is

\[
\boxed{
50199975102649518151265765761694302741017337728/720623541454995515907174341873203220162084040095.
}
\]

The continuous phase transitions occur at

\[
\begin{aligned}
\alpha_1&\approx 2.782136871616065,\\
\alpha_2&\approx 2.795232533004783,\\
\alpha_3&\approx 2.871880270656817,\\
\alpha_4&\approx 2.901814422307968,\\
\alpha_5&\approx 2.909286149740939,\\
\alpha_6&\approx 2.918107171804178,\\
\alpha_7&\approx 2.978100451975272.
\end{aligned}
\]

Every exact phase satisfies primal and dual feasibility, positive derivative,
and finite transition denominators.

The boundary and coalescence risks are

\[
Q_{13}(2)
=
0.36941822889850663235787555113204609350433716957445,
\]

and

\[
Q_{13}(3^-)
=
1.0392211789066361911143621891809103601972514108701.
\]

---

## 7. What A73 proves

1. Complete enumeration of the explicitly declared one-pivot signature
   neighborhood at one exact rational probe.
2. Exact classification of all 246 neighbors.
3. Unique strict local optimality of \(S\) at \(M=11,12\).
4. Exact dual rejection of \(S\) at \(M=13\).
5. Unique strict local optimality of the \(\gamma\)-sign flip at \(M=13\).
6. No hidden contact-exchange competitor.
7. No singular or degenerate local tie.
8. An exact global continuous theorem for \(M=13\).
9. A unique exact integer-catalogue winner \(\{2,3,4\}\) at \(M=13\).

---

## 8. What A73 does not prove

A73 does not enumerate every possible LP basis.

In particular, it excludes:

- exchange of the scale variable;
- \(\alpha\)-band deactivation or sign reversal;
- two-contact pivots;
- combined contact and band-sign pivots;
- signatures requiring more than one adjacency move;
- behavior away from the single exact probe.

The phrase “complete one-pivot neighborhood” applies only to the declared
signature moves listed in Section 2.

---

## 9. Next rigorous target

The next target should lift the \(M=13\) sign selection from one point to a
parametric statement.

For the reference \(S_M\) signature, derive

\[
\lambda_{\gamma+}(M,s)
=
\frac{
N_\gamma(M,2^{-M},s,\varepsilon_M)
}{
D_\gamma(M,2^{-M},s,\varepsilon_M)
}.
\]

Then:

1. locate the exact support-size/sign bifurcation between \(M=12\) and
   \(M=13\);
2. determine whether \(\lambda_{\gamma+}<0\) on the complete \(M=13\)
   terminal interval;
3. classify the gamma-sign-flipped basis over that full interval;
4. test \(M=14\) without assuming the \(M=13\) phase grammar persists.

That would upgrade the exact pointwise selection theorem into an
interval-stable support-size bifurcation theorem.
