# Fixed-Family Double Bifurcation and the Active Contact Reset

**Programme:** Modal Field Research Programme  
**Provisional audit:** A77  
**Author line:** Felipe Gianini Romero  
**Status:** exact all-\(M\) orientation theorem for one fixed contact family, exact \(M=23,24,25\) active-reset theorem on a corrected common interval, and complete declared one-pivot classification

## Technical abstract

A76 identified the actual late-stage family

\[
P=\{0,5,6,M\},
\qquad
Q=\{1,h,h+1\},
\qquad
h=\lfloor M/2\rfloor,
\]

and found an actual selected gamma-sign change:

\[
M=22:\gamma+,
\qquad
M=23:\gamma-.
\]

A77 asks two separate questions.

First:

> For the fixed \(\{5,6\}\) contact family, is the negative
> \(\gamma+\) orientation after \(M=23\) permanent?

Second:

> Does the actual optimizer remain on that family, or does it change
> contacts before the fixed-family orientation returns?

The answers are different.

For the fixed family, on

\[
I=
\left[
\frac{13}{100},
\frac{33}{250}
\right],
\]

the exact Cramer orientation is

\[
\boxed{
\lambda_{\gamma+}>0
\quad
(M=19,20,21,22),
}
\]

\[
\boxed{
\lambda_{\gamma+}<0
\quad
(23\le M\le34),
}
\]

and

\[
\boxed{
\lambda_{\gamma+}>0
\quad
\text{for every integer }M\ge35.
}
\]

Thus the fixed-family inversion is not permanent.

However, the optimizer does not wait until \(M=35\).

On the corrected common active-reset interval

\[
J=
\left[
\frac{131}{1000},
\frac{263}{2000}
\right],
\]

the exact selected sequence is

\[
\boxed{
M=23:
\quad
P=\{0,5,6,23\},
\quad
\gamma-,
}
\]

\[
\boxed{
M=24:
\quad
P=\{0,6,7,24\},
\quad
\gamma+,
}
\]

and

\[
\boxed{
M=25:
\quad
P=\{0,6,7,25\},
\quad
\gamma+.
}
\]

The actual negative gamma state therefore lasts only at \(M=23\) within this
three-support transition.

The contact reset is forced by primal feasibility:

- at \(M=23\), the future \(\{6,7\}\) family has a negative basic variable;
- at \(M=24,25\), the old \(\{5,6\}\) family has a negative basic variable.

The change is not a discretionary solver pivot.

All

\[
55+57+59
=
\boxed{171}
\]

selected-branch KKT conditions are strictly positive on \(J\).

At the exact probe

\[
s_0=\frac{131}{1000},
\]

all

\[
159+166+173
=
\boxed{498}
\]

declared one-pivot neighbors are rejected, and each selected reference is the
unique strict local KKT optimum.

---

## 1. Why two intervals are necessary

The wider interval \(I\) is appropriate for the fixed-family Cramer theorem.

It is not appropriate for one single active branch at \(M=24\) or \(M=25\),
because it crosses real phase transitions.

An initial attempt to certify one basis over all of \(I\) correctly failed:
some basic-variable Bernstein coefficients changed sign.

The active-reset theorem therefore uses the narrower rational interval \(J\),
which lies inside the stable selected branches for all three supports.

This restriction is not an ad hoc repair. It is required by the exact phase
structure.

---

## 2. Parity-reduced fixed-family theorem

For even supports:

\[
M=2h,
\qquad
U=2^{-h},
\qquad
V=s^h,
\qquad
\varepsilon=\frac{U}{1875}.
\]

For odd supports:

\[
M=2h+1,
\qquad
\varepsilon=\frac{U}{2500}.
\]

The fixed-family multiplier has exact parity forms:

\[
\lambda_{\gamma+}^{\rm even}
=
\frac{N_{\rm even}(h,U,V,s)}
{D_{\rm even}(h,U,V,s)},
\]

\[
\lambda_{\gamma+}^{\rm odd}
=
\frac{N_{\rm odd}(h,U,V,s)}
{D_{\rm odd}(h,U,V,s)}.
\]

The complete symbolic expressions are stored in:

- `a77_fixed_family_parity_formula_cache.json`;
- `a77_fixed_family_parity_results.json`.

Exact Bernstein certificates cover:

\[
19\le M\le47.
\]

Parity-specific asymptotic remainder bounds begin at:

\[
h=24,
\]

covering:

\[
M\ge48
\]

for even supports and:

\[
M\ge49
\]

for odd supports.

### Finite sign table

| \(M\) | Parity | Numerator | Determinant | Multiplier |
|---:|---:|---:|---:|---:|
| 19 | odd | +1 | +1 | +1 |
| 20 | even | +1 | +1 | +1 |
| 21 | odd | +1 | +1 | +1 |
| 22 | even | +1 | +1 | +1 |
| 23 | odd | -1 | +1 | -1 |
| 24 | even | -1 | +1 | -1 |
| 25 | odd | -1 | +1 | -1 |
| 26 | even | -1 | +1 | -1 |
| 27 | odd | -1 | +1 | -1 |
| 28 | even | -1 | +1 | -1 |
| 29 | odd | -1 | +1 | -1 |
| 30 | even | -1 | +1 | -1 |
| 31 | odd | -1 | +1 | -1 |
| 32 | even | -1 | +1 | -1 |
| 33 | odd | -1 | +1 | -1 |
| 34 | even | -1 | +1 | -1 |
| 35 | odd | -1 | -1 | +1 |
| 36 | even | -1 | -1 | +1 |
| 37 | odd | -1 | -1 | +1 |
| 38 | even | -1 | -1 | +1 |
| 39 | odd | -1 | -1 | +1 |
| 40 | even | -1 | -1 | +1 |
| 41 | odd | -1 | -1 | +1 |
| 42 | even | -1 | -1 | +1 |
| 43 | odd | -1 | -1 | +1 |
| 44 | even | -1 | -1 | +1 |
| 45 | odd | -1 | -1 | +1 |
| 46 | even | -1 | -1 | +1 |
| 47 | odd | -1 | -1 | +1 |

The sign changes are:

\[
22\to23:
\quad
N:+\to-,
\qquad
D:+,
\]

and:

\[
34\to35:
\quad
N:-,
\qquad
D:+\to-.
\]

Therefore:

- the first bifurcation is numerator-driven;
- the second is determinant-driven.

---

## 3. Exact active-reset interval

The active-reset interval is:

\[
J=
\left[
\frac{131}{1000},
\frac{263}{2000}
\right].
\]

In first-anchor coordinates:

\[
2.926865295369785\ldots
\le
\alpha
\le
2.932361283124637\ldots.
\]

The exact selected signatures are:

| \(M\) | Active \(P\)-support | Active \(Q\)-support | Bands | KKT conditions |
|---:|---:|---:|---:|---:|
| 23 | [0, 5, 6, 23] | [1, 11, 12] | alpha+, beta-, gamma- | 55 |
| 24 | [0, 6, 7, 24] | [1, 12, 13] | alpha+, beta-, gamma+ | 57 |
| 25 | [0, 6, 7, 25] | [1, 12, 13] | alpha+, beta-, gamma+ | 59 |

For every support:

1. all selected KKT conditions are positive;
2. the opposite gamma sign has a negative active multiplier;
3. the selected gamma-plus Cramer orientation has the declared sign;
4. the adjacent contact family is primal-infeasible.

Thus:

\[
\boxed{
\{5,6\},\gamma-
\quad\longrightarrow\quad
\{6,7\},\gamma+
}
\]

is an exact support-size/contact reset between \(M=23\) and \(M=24\).

---

## 4. Complete declared one-pivot neighborhood

The declared neighborhood contains:

- one \(P\)-contact exchange;
- one \(Q\)-contact exchange;
- a beta or gamma sign flip;
- beta or gamma deactivation with one contact leaving the reduced basis.

The exact classification is:

| \(M\) | Neighbors | Primal | Active dual | Reduced cost | Inactive slack |
|---:|---:|---:|---:|---:|---:|
| 23 | 159 | 114 | 39 | 4 | 2 |
| 24 | 166 | 125 | 6 | 34 | 1 |
| 25 | 173 | 127 | 6 | 39 | 1 |

Combined:

\[
\boxed{366\text{ primal infeasible}},
\]

\[
\boxed{51\text{ active-dual infeasible}},
\]

\[
\boxed{77\text{ reduced-cost infeasible}},
\]

and

\[
\boxed{4\text{ inactive-slack infeasible}}.
\]

No neighbor is locally optimal.

No basis is singular.

Each reference is the unique strict local optimum.

---

## 5. What A77 proves

1. Exact even and odd Cramer formulas for the fixed \(\{5,6\}\) family.
2. A complete support-size sign theorem for every integer \(M\ge19\) on \(I\).
3. A negative fixed-family window exactly covering \(23\le M\le34\).
4. Positive fixed-family orientation re-entry for every \(M\ge35\).
5. Exact active gamma-minus selection at \(M=23\) on \(J\).
6. Exact contact reset to \(\{6,7\}\) at \(M=24\).
7. Exact gamma-plus selection at \(M=24,25\).
8. Exact primal exclusion of the family on the wrong side of the reset.
9. Exact rejection of all 498 declared one-pivot neighbors.

---

## 6. What A77 does not prove

A77 does not establish a universal rule such as:

\[
\text{the active contact pair advances every five supports}.
\]

The observed sequence suggests structured blocks, but that recurrence has not
been proved.

A77 also does not prove:

1. the global full-\(\alpha\) phase atlas for \(M=24,25\);
2. the selected family for arbitrary \(M\);
3. a universal relation between contact resets and gamma-sign flips;
4. complete enumeration of every LP basis.

---

## 7. Next rigorous target

The next structural family is:

\[
P=\{0,k,k+1,M\}.
\]

The next audit should treat \(k\) as a discrete structural variable and ask:

1. for which \((M,k)\) is the family primal feasible on a fixed interval?
2. where does the selected \(k\) change?
3. are the observed blocks
   \[
   k=3,\ 4,\ 5,\ 6,\ldots
   \]
   governed by an exact inequality?
4. does each contact reset occur before the fixed-family gamma orientation
   re-enters?
5. can the primal feasibility boundary be expressed by one Cramer minor?

That would move from support-specific contact resets to a genuine contact
selection theorem.
