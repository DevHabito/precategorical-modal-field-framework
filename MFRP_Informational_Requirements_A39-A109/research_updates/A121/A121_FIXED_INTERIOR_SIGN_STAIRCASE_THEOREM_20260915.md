# A121 — fixed-interior sign staircase and two-site local-peak theorem

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A120 fixed-interior reduced-factor contract.**  
**Classification:** analytic corollary of A120 + exact finite regression/hardening.  
**No target-deformed global-maximizer theorem and no physical or ontological interpretation are claimed.**

---

## 1. Scope

Retain the A120 contract

\[
\beta=\frac18,\qquad \delta=\frac1{1875},\qquad
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

with a fixed target satisfying

\[
s<\tau<\frac{\beta}{s}<1.
\]

Fix one parity \(p\). Let

\[
h=\left\lfloor \frac M2\right\rfloor,
\qquad
u_M=\tau^h,
\qquad
c=c_\tau(s)=\frac{\log\tau}{2\log s},
\]

\[
b_M=\lceil Mc\rceil,
\qquad
\rho_M=b_M-Mc\in[0,1).
\]

A120 proves, for every fixed integer offset \(j\),

\[
\frac{E_{M,b_M+j}}
     {u_M\tau^{b_M+j}}
=
\Psi_{p,j}(\rho_M)+o(1),
\]

where

\[
\Psi_{p,j}(\rho)
=
P_p\,s^{j+\rho}-Q_p,
\]

with

\[
P_p=
\frac{\tau-s}{2}\tau^{\sigma_p}>0,
\]

\[
\sigma_{\rm even}=0,
\qquad
\sigma_{\rm odd}=\frac12,
\]

and

\[
Q_p=
a_p(\tau)(1-\tau)
\left(\frac{s-\beta}{\tau}-4\delta\right)(1-c)>0,
\]

\[
a_{\rm even}=1,
\qquad
a_{\rm odd}=\frac{1+\tau}{2}.
\]

A121 extracts the sign geometry that is already implicit in this A120 asymptotic.

---

# 2. The phase-front coordinate

Define

\[
\boxed{
\xi_p(s,\tau)
=
\frac{\log(Q_p/P_p)}{\log s}.
}
\]

Because \(P_p,Q_p>0\) and \(0<s<1\), this is well-defined.

By definition,

\[
Q_p=P_p s^{\xi_p},
\]

so

\[
\boxed{
\Psi_{p,j}(\rho)
=
P_p\left(s^{j+\rho}-s^{\xi_p}\right).
}
\]

Hence the two variables \(j\) and \(\rho\) enter only through their sum

\[
x=j+\rho.
\]

Define

\[
\Phi_p(x)=P_p s^x-Q_p.
\]

Then

\[
\Psi_{p,j}(\rho)=\Phi_p(j+\rho).
\]

Since \(0<s<1\),

\[
\Phi_p'(x)=P_p s^x\log s<0.
\]

Thus the entire limiting fixed-interior sign landscape is a single strictly decreasing front.

---

# 3. Theorem A — exact limiting sign staircase

For every fixed parity and fixed interior pair,

\[
\boxed{
\Psi_{p,j}(\rho)>0
\iff
j+\rho<\xi_p,
}
\]

\[
\boxed{
\Psi_{p,j}(\rho)=0
\iff
j+\rho=\xi_p,
}
\]

and

\[
\boxed{
\Psi_{p,j}(\rho)<0
\iff
j+\rho>\xi_p.
}
\]

Therefore, if

\[
\xi_p-\rho\notin\mathbb Z,
\]

and

\[
n_p(\rho)=\left\lceil \xi_p-\rho\right\rceil,
\]

then

\[
\Psi_{p,j}(\rho)>0
\quad\text{for }j<n_p(\rho),
\]

while

\[
\Psi_{p,j}(\rho)<0
\quad\text{for }j\ge n_p(\rho).
\]

So the limiting factor sequence has exactly one possible \(+\to-\) transition and no later reversal.

At a resonance

\[
\xi_p-\rho=m\in\mathbb Z,
\]

the leading term satisfies

\[
\Psi_{p,m}(\rho)=0,
\]

with positive leading signs for \(j<m\) and negative leading signs for \(j>m\). A121 does not decide the finite sign of the resonant marginal factor; that requires the next asymptotic order.

---

# 4. Cell gluing and the two-site rule

The phase family satisfies

\[
\boxed{
\Psi_{p,j+1}(\rho)
=
\Psi_{p,j}(\rho+1).
}
\]

Equivalently, adjacent integer offsets glue continuously into the single coordinate \(x=j+\rho\).

Write

\[
\xi_p=m+\theta,
\qquad
m=\lfloor \xi_p\rfloor,
\qquad
0\le\theta<1.
\]

If \(0<\theta<1\), then away from the critical phase \(\rho=\theta\),

\[
n_p(\rho)=
\begin{cases}
m+1,&0\le\rho<\theta,\\[4pt]
m,&\theta<\rho<1.
\end{cases}
\]

Hence the limiting transition can occupy only two adjacent offsets.

This is the origin of the two-site local-peak motion.

---

# 5. Theorem B — eventual adjacent nesting for every fixed offset

Define the A120-style adjacent nesting factor at offset \(j\),

\[
J^{(j)}_M
=
E_{M,b_M+j}
-
\tau^{-1}E_{M,b_M+j+1}.
\]

Using the A120 asymptotic for offsets \(j\) and \(j+1\),

\[
\frac{J^{(j)}_M}
{u_M\tau^{b_M+j}}
=
\Psi_{p,j}(\rho_M)
-
\Psi_{p,j+1}(\rho_M)
+
o(1).
\]

But

\[
\Psi_{p,j}(\rho)-\Psi_{p,j+1}(\rho)
=
P_p s^{j+\rho}(1-s).
\]

Therefore

\[
\boxed{
\frac{J^{(j)}_M}
{u_M\tau^{b_M+j}}
=
P_p s^{j+\rho_M}(1-s)+o(1).
}
\]

Because

\[
s^{\rho_M}\ge s
\qquad(0\le\rho_M<1),
\]

the leading term has the uniform-in-phase lower bound

\[
P_p s^{j+1}(1-s)>0.
\]

Thus, for every fixed interior pair, fixed parity and fixed integer \(j\),

\[
\boxed{
J^{(j)}_M>0
}
\]

for all sufficiently large \(M\) of that parity.

This theorem is **eventual**. It supplies no small or universal finite threshold.

---

# 6. Exact finite-window one-variation consequence

Fix any finite integer window

\[
j_-\le j\le j_+.
\]

Applying Theorem B to each adjacent offset and taking the maximum of the finitely many realization thresholds gives an \(M_0\) such that, for all later \(M\) of the chosen parity,

\[
J^{(j)}_M>0
\qquad
(j_-\le j<j_+).
\]

Since

\[
E_{b+j}>\tau^{-1}E_{b+j+1},
\]

a negative factor forces the next factor to be negative:

\[
E_{b+j}<0
\Longrightarrow
E_{b+j+1}<\tau E_{b+j}<0.
\]

Likewise,

\[
E_{b+j+1}>0
\Longrightarrow
E_{b+j}>\tau^{-1}E_{b+j+1}>0.
\]

Therefore the **exact finite-\(M\)** sign sequence in every fixed offset window is eventually one-variation:

\[
\boxed{
+\cdots +\;[0]\;-\cdots-
}
\]

with no \(-\to+\) reversal.

This is a local/fixed-offset result. It is not a theorem over all contacts simultaneously.

---

# 7. Nonresonant local compressed peak

Recall

\[
E_k=V_{k+1}-V_k.
\]

Suppose a subsequence of fixed parity satisfies

\[
\rho_M\to\rho
\]

with

\[
\xi_p-\rho\notin\mathbb Z.
\]

Let

\[
n=\left\lceil\xi_p-\rho\right\rceil.
\]

Then Theorem A and A120 imply eventually

\[
E_{b_M+n-1}>0,
\qquad
E_{b_M+n}<0.
\]

Hence

\[
V_{b_M+n}>V_{b_M+n-1},
\qquad
V_{b_M+n}>V_{b_M+n+1}.
\]

Therefore

\[
\boxed{
V_{b_M+n}
}
\]

is eventually a strict **local** compressed maximum.

No global compressed-maximizer statement is made.

---

# 8. Infinite two-site local-peak alternation in the A120 examples

A120 already proves two mixed-phase examples using exact endpoint margins plus irrationality/density.

## 8.1 Pair A

Take

\[
s=\frac{131}{1000},
\qquad
\tau=\frac15.
\]

A120 proves, for even parity and offset \(j=0\),

\[
\Psi_{\rm even,0}(0)>0,
\qquad
\Psi_{\rm even,0}(1)<0,
\]

and proves \(c_\tau(s)\) irrational.

Hence there is a unique

\[
\theta\in(0,1)
\]

with

\[
\xi_{\rm even}=0+\theta.
\]

Because the even rounding phases are dense, infinitely many even \(M\) fall on both sides of \(\theta\).

Moreover,

\[
\Psi_{\rm even,-1}(1)
=
\Psi_{\rm even,0}(0)>0,
\]

and

\[
\Psi_{\rm even,1}(0)
=
\Psi_{\rm even,0}(1)<0.
\]

Thus eventually

\[
E_{b_M-1}>0,
\qquad
E_{b_M+1}<0
\]

uniformly in the phase, while \(E_{b_M}\) changes sign infinitely often.

Therefore the strict local compressed peak alternates infinitely often between

\[
\boxed{V_{b_M}}
\]

and

\[
\boxed{V_{b_M+1}}.
\]

## 8.2 Pair B

Take

\[
s=\frac{129}{1000},
\qquad
\tau=\frac9{10}.
\]

A120 proves, for even parity and offset \(j=3\),

\[
\Psi_{\rm even,3}(0)>0,
\qquad
\Psi_{\rm even,3}(1)<0,
\]

and again proves irrationality of \(c_\tau(s)\).

Therefore there is a unique critical phase in this cell, and the strict local peak alternates infinitely often between

\[
\boxed{V_{b_M+3}}
\]

and

\[
\boxed{V_{b_M+4}}.
\]

This is a local phase-arithmetic phenomenon, not a finite-\(M\) accident.

---

# 9. Exact computational hardening

The accompanying exact `Fraction` audit performs three independent checks.

### 9.1 Frozen A113 regression

For

\[
M\in\{521,522,561,600,760,1000,2049\}
\]

and

\[
s\in\left\{\frac{129}{1000},\frac{131}{1000},\frac{133}{1000}\right\},
\]

all 21 frozen \(\tau=1/2\) controls have:

- positive \(E_b\);
- negative \(E_{b+3}\);
- no \(-\to+\) reversal across \(j=0,1,2,3\).

These are regression checks only; A113 remains the theorem source for the frozen case.

### 9.2 Exact two-site sentinels

For

\[
\left(s,\tau\right)
=
\left(\frac{131}{1000},\frac15\right),
\]

the audit exhibits both local sign patterns

\[
(+,+,-)
\]

and

\[
(+,-,-)
\]

on offsets

\[
j=-1,0,1
\]

for both even and odd finite controls.

For

\[
\left(s,\tau\right)
=
\left(\frac{129}{1000},\frac9{10}\right),
\]

it likewise exhibits

\[
(+,+,-)
\]

and

\[
(+,-,-)
\]

on offsets

\[
j=2,3,4
\]

for both parities.

All adjacent \(J^{(j)}\) values in these sentinels are exactly positive.

### 9.3 Explicit finite-\(M\) warning

At

\[
M=1200,
\qquad
s=\frac{129}{1000},
\qquad
\tau=\frac3{20},
\qquad
j=3,
\]

exact arithmetic gives

\[
\boxed{
J^{(3)}_M<0.
}
\]

Thus Theorem B must not be misread as a practical small-\(M\) bound.

---

# 10. What A121 establishes

A121 proves, within the inherited A120 contract:

1. the limiting remote-factor landscape depends only on \(j+\rho\);
2. it has one strictly decreasing sign front at \(j+\rho=\xi_p\);
3. each phase has at most one \(+\to-\) limiting transition across offsets;
4. each fixed finite offset window becomes exactly one-variation for sufficiently large \(M\);
5. every fixed adjacent nesting factor \(J^{(j)}\) is eventually positive;
6. away from a leading-order resonance, the strict local compressed peak is at
   \[
   b_M+\left\lceil\xi_p-\rho\right\rceil;
   \]
7. if \(\xi_p=m+\theta\) with \(0<\theta<1\), the local peak can move only between the two adjacent sites \(b_M+m\) and \(b_M+m+1\);
8. the two A120 irrational examples realize such two-site motion infinitely often.

---

# 11. Nonclaims

A121 does **not** prove:

- a global compressed maximizer under arbitrary target deformation;
- a full target-deformed A113 all-contact one-variation theorem;
- a target-deformed A114 lifted active-set theorem;
- a uniform finite threshold in \((s,\tau,j)\);
- a theorem uniform over infinitely many offsets at once;
- the resonant marginal factor when \(\xi_p-\rho\in\mathbb Z\);
- the separate collision regime \(\tau-s=O(1/M)\);
- novelty or priority relative to the literature;
- any RZS, modal-field, physical, spacetime, gravity, matter, or ontological interpretation.
