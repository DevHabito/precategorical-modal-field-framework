# A115 — exact target-node deformation audit

**Date:** 2026-09-14  
**Status:** `PASS_WITH_REFUTATION`  
**Classification:** exact algebraic identities + exact finite evidence + exact refutation of a stronger universal extension.  
**Not a general asymptotic theorem.**

## 1. Purpose

A113 proves the compressed one-variation theorem under the frozen contract

\[
M\ge 521,\qquad \frac{129}{1000}\le s\le\frac{133}{1000},
\qquad \beta=\frac18,\qquad \tau=\frac12.
\]

A115 asks a narrower structural question:

> Which parts of the A84/A113 compressed mechanism survive when the target node
> \(\tau\) is deformed away from \(1/2\)?

The audit does **not** assume that the A113 threshold `521`, its remote-sign
bounds, or the A114 lifted active-set staircase remain valid after this
deformation.

The order of claims is deliberately separated into:

1. exact algebraic identities;
2. exact reproduction of the frozen contract;
3. finite exact evidence;
4. exact counterexamples;
5. open claims.

No physical or ontological interpretation is made.

---

## 2. Deformed central Q block

Let

\[
h=\left\lfloor\frac M2\right\rfloor,\qquad
u=\tau^h,\qquad 0<\tau<1.
\]

Keep the central support

\[
Q=\{1,h,h+1\}.
\]

The normalized central equations are

\[
q_1+q_h+q_{h+1}=t,
\]

\[
q_1+hq_h+(h+1)q_{h+1}=\frac M2\,t,
\]

\[
\tau q_1+\tau^h q_h+\tau^{h+1}q_{h+1}=1.
\]

Define

\[
\boxed{
D_\tau=\tau-hu+(h-1)\tau u.
}
\]

For \(M=2h\),

\[
\boxed{
q_1=\frac{1-ut}{D_\tau},
\qquad
q_h=t-hq_1,
\qquad
q_{h+1}=(h-1)q_1.
}
\]

For \(M=2h+1\),

\[
\boxed{
q_1=
\frac{1-\frac{1+\tau}{2}ut}{D_\tau},
}
\]

\[
\boxed{
q_h=\frac t2-hq_1,
\qquad
q_{h+1}=\frac t2+(h-1)q_1.
}
\]

The audit verifies all six normalization/mean/target equations symbolically.

### 2.1 Nonsingularity

Write

\[
D_\tau
=
\tau\left[
1-h\tau^{h-1}+(h-1)\tau^h
\right].
\]

For \(h\ge2\), set

\[
g_h(\tau)=1-h\tau^{h-1}+(h-1)\tau^h.
\]

Then

\[
g_h(1)=0
\]

and

\[
g_h'(\tau)
=
h(h-1)\tau^{h-2}(\tau-1)<0
\qquad(0<\tau<1).
\]

Hence

\[
g_h(\tau)>0
\]

and therefore

\[
\boxed{D_\tau>0\qquad(0<\tau<1).}
\]

No numerical determinant assumption is needed for this central block.

---

## 3. Exact deformed \(Q_r\) coefficient

Let

\[
L_r=r-hr^h+(h-1)r^{h+1}.
\]

Writing

\[
Q_r=C_r+D_r t,
\]

the coefficient of \(t\) is

\[
\boxed{
D_r=
r^h-u\frac{L_r}{D_\tau}
\qquad(M=2h),
}
\]

and

\[
\boxed{
D_r=
\frac{r^h+r^{h+1}}2
-
\frac{1+\tau}{2}u\frac{L_r}{D_\tau}
\qquad(M=2h+1).
}
\]

At

\[
\tau=\frac12
\]

these formulas reduce exactly to the A81/A84 parity formulas.

The independent audit reproduces the frozen `D_r` in

\[
\boxed{36/36}
\]

exact `Fraction` controls.

---

## 4. Scale-normalized error under target deformation

The A64 noise contract is scale-normalized by the sharp lower transform value
at the known mean.

For the function

\[
x\mapsto \tau^x,\qquad 0<\tau<1,
\]

and mean \(M/2\), the sharp discrete lower interpolation gives

\[
\ell_\tau(M,M/2)
=
\begin{cases}
\tau^h,&M=2h,\\[4pt]
\dfrac{1+\tau}{2}\tau^h,&M=2h+1.
\end{cases}
\]

With the existing

\[
\delta=\frac1{1875},
\]

the deformed absolute tolerance is therefore

\[
\boxed{
\varepsilon_\tau
=
\begin{cases}
\dfrac{\tau^h}{1875},&M=2h,\\[8pt]
\dfrac{1+\tau}{3750}\tau^h,&M=2h+1.
\end{cases}
}
\]

At \(\tau=1/2\),

\[
\varepsilon_{2h}=\frac{2^{-h}}{1875},
\qquad
\varepsilon_{2h+1}=\frac{2^{-h}}{2500},
\]

so the frozen A75/A84 contract is recovered exactly.

---

## 5. Deformed contact locator without floating-point logs

For

\[
0<s<\tau<1,
\]

define

\[
c_\tau(s)=\frac{\log\tau}{2\log s}
=
\frac{\log(1/\tau)}{-2\log s}.
\]

The integer locator

\[
b_\tau=\lceil M c_\tau(s)\rceil
\]

is evaluated in the audit without logarithms:

\[
\boxed{
b_\tau=
\min\{n\in\mathbb Z_{\ge0}:s^{2n}\le\tau^M\}.
}
\]

For every declared counterexample, the two exact inequalities

\[
s^{2b_\tau}\le\tau^M
\]

and

\[
s^{2(b_\tau-1)}>\tau^M
\]

are checked.

---

## 6. Exact deformed A84 factor and k-space reconstruction

The deformed compressed adjacent factor is reconstructed from the original
cofactor form

\[
E_k
=
X\,\Delta B_s
+
Y\,B_s
+
W\,H_s
\]

using the deformed central \(D_r\) and deformed
\(\varepsilon_\tau\).

Independently, the generic A84 ten-term expansion is verified symbolically
with beta, target and source left algebraically independent.

The audit then checks equality of the cofactor and k-space reconstructions in

\[
\boxed{204/204}
\]

exact deformed controls.

No floating-point equality is used.

---

## 7. Generalized central transform

Define

\[
\boxed{
J_{\tau,k}
=
E_k-\tau^{-1}E_{k+1}.
}
\]

For the target-affine channel

\[
(c_\tau+k c_{k\tau})\tau^k,
\]

one has identically

\[
(c_\tau+k c_{k\tau})\tau^k
-
\tau^{-1}
(c_\tau+(k+1)c_{k\tau})\tau^{k+1}
=
\boxed{-c_{k\tau}\tau^k}.
\]

Thus the nonconfluent target coefficient cancels for every
\(\tau>0\).

The factor `2` in the frozen A113 quantity

\[
E_k-2E_{k+1}
\]

is therefore the specialization

\[
\tau^{-1}=2
\]

at \(\tau=1/2\).

This identity is proved symbolically by the audit.

---

## 8. Frozen-contract reproduction gates

Before using the deformation, the implementation is required to return to the
existing \(\tau=1/2\) contract.

Exact gates:

- deformed \(D_r\) equals frozen A84 \(D_r\): `36/36`;
- deformed cofactor \(E_k\) equals frozen A84 \(E_k\): `90/90`;
- deformed cofactor and deformed k-space form agree: `204/204`;
- A113 sentinel controls reproduce \(E_b>0\), \(E_{b+3}<0\), \(J>0\): `21/21`.

The A113 sentinel set includes both parities, the declared source probes,
deep-tail controls, and the preserved \(M=561,s=129/1000\) case where
\(E_{b+2}>0\).

---

## 9. Finite exact deformation stress

### 9.1 Coarse predeclared grid

The exact grid is

\[
s\in
\left\{
\frac{129}{1000},
\frac{131}{1000},
\frac{133}{1000}
\right\},
\]

\[
M\in\{521,522,600,760\},
\]

and

\[
\tau\in
\left\{
\frac3{20},\frac15,\frac14,\frac3{10},
\frac7{20},\ldots,\frac9{10}
\right\},
\]

i.e. rational increments of \(1/20\) from \(0.15\) through \(0.90\).

All 192 central controls are inside the A84 adjacent-factor contact domain.

Result:

\[
\boxed{
J_{\tau,b_\tau+1}>0
\quad\text{in }192/192\text{ controls}.
}
\]

This is **finite exact evidence only**.

The stronger package

\[
E_{b_\tau}>0,\qquad
E_{b_\tau+3}<0,\qquad
J_{\tau,b_\tau+1}>0
\]

passes only

\[
170/192
\]

controls.

By target value:

- \(\tau=3/20\): `0/12`;
- \(\tau=1/5\): `6/12`;
- \(\tau=1/4\): `8/12`;
- each declared coarse value \(\tau\ge3/10\): `12/12`.

This does **not** establish a threshold at \(3/10\). It only records the
predeclared finite grid.

---

## 10. Near-wall stress and exact refutation

A second grid was declared specifically to attack the region near
\(\tau=s\):

\[
\tau=s+\Delta,
\]

with

\[
\Delta\in
\left\{
10^{-4},2\cdot10^{-4},5\cdot10^{-4},
10^{-3},2\cdot10^{-3},5\cdot10^{-3},
10^{-2},2\cdot10^{-2}
\right\},
\]

and

\[
M\in\{521,600,800,1000,1500,2000\}.
\]

After enforcing the actual A84 adjacent-factor domain

\[
2\le k\le h-2,
\]

60 central controls remain admissible.

Results:

\[
\boxed{58\text{ positive},\qquad2\text{ negative}.}
\]

Therefore the universal extension

\[
M\ge521,\quad\beta<s<\tau<1
\Longrightarrow
J_{\tau,b_\tau+1}>0
\]

is false.

### 10.1 First exact in-domain counterexample

\[
\boxed{
M=521,\quad
s=\frac{131}{1000},\quad
\tau=\frac{141}{1000}.
}
\]

Here

\[
h=260,\qquad b_\tau=252,
\]

so

\[
b_\tau+2=254\le258=h-2.
\]

Thus both central factors used by \(J\) are valid A84 adjacent factors.

Exact arithmetic gives

\[
\boxed{
J_{\tau,b_\tau+1}<0.
}
\]

The full reduced `Fraction` is frozen by SHA-256

`dc0efb5b23581db2a5c4983e87097884582dddee1fd68d5ec28d9b459bef8bac`.

The numerator has 3447 decimal digits and the denominator 3889.

An independent direct \(3\times3\) rational solve of the Q block reconstructs
the same two \(E\)-factors and the same sign.

### 10.2 Second exact in-domain counterexample

\[
\boxed{
M=521,\quad
s=\frac{133}{1000},\quad
\tau=\frac{143}{1000}.
}
\]

Again

\[
h=260,\qquad b_\tau=252,\qquad b_\tau+2=254\le258.
\]

Exact arithmetic gives

\[
\boxed{
J_{\tau,b_\tau+1}<0.
}
\]

Fraction SHA-256:

`e60c0f4b4bf1ef74867c3d80cebb5fb805364b7d542114fe2f858b6aeea7e34f`.

This counterexample also survives the independent direct-matrix
reconstruction.

---

## 11. Preserved correction: rejected out-of-domain counterexample

An earlier exploratory point was

\[
M=521,\qquad
s=\frac{129}{1000},\qquad
\tau=\frac{667}{5000}.
\]

It gives

\[
b_\tau=257,\qquad h=260.
\]

Although the algebraic value of the proposed \(J\) is negative, it uses

\[
b_\tau+2=259.
\]

But A84 adjacent factors only exist through

\[
h-2=258.
\]

Therefore this point is **not a valid counterexample to an in-domain A84
central-nesting claim**.

It is explicitly classified as

`REJECTED_AS_COUNTEREXAMPLE_OUTSIDE_A84_ADJACENT_FACTOR_DOMAIN`.

The point is preserved rather than deleted because the failure exposed a real
domain-checking weakness in the exploratory stage.

---

## 12. What is proved, refuted, evidenced, and open

### Proved algebraically

1. The deformed central-Q mass formulas.
2. Positivity of \(D_\tau\) for \(0<\tau<1\), \(h\ge2\).
3. The deformed \(D_r\) formulas.
4. The scale-normalized \(\varepsilon_\tau\) formula under the same A64
   dimensionless-noise rule.
5. The exact log-free characterization of \(b_\tau\).
6. The generic A84 ten-term expansion identity.
7. The exact target-affine cancellation in
   \(J_{\tau,k}=E_k-\tau^{-1}E_{k+1}\).

### Refuted

The stronger statement

\[
\boxed{
M\ge521,\quad\beta<s<\tau<1
\Longrightarrow
J_{\tau,b_\tau+1}>0
}
\]

is refuted by exact in-domain counterexamples.

Therefore `521` is **not** a universal target-deformation threshold.

### Finite exact evidence

The coarse rational grid gives

\[
192/192
\]

positive \(J\)-controls.

This evidence cannot override the exact near-wall counterexamples and is not
promoted to a theorem.

### Open

The following remain open:

\[
\forall\text{ fixed }\beta<s<\tau<1,\quad
\exists M_0(s,\tau)
\]

such that \(J_{\tau,b_\tau+1}>0\) for all sufficiently large admissible \(M\);

and the stronger compact-uniform version

\[
\forall K\Subset\{\beta<s<\tau<1\},\quad
\exists M_0(K)
\]

with eventual positivity uniform on \(K\).

This audit supplies motivation for those questions but **does not prove
either**.

---

## 13. Nonclaims

A115 does not establish:

- a deformed global one-variation theorem;
- a universal remote-sign theorem;
- a universal target-deformation threshold;
- a deformed A114 active-set staircase;
- any physical, spacetime, gravity, quantum, or ontological interpretation.

The result is currently mathematical: an exact target-deformation identity,
a reproducible finite stress audit, and an exact refutation of one stronger
universal extension.

---

## 14. Reproducibility

Run

```bash
python research_updates/A115/a115_target_deformation_exact_audit.py
```

The script writes

`A115_TARGET_DEFORMATION_EXACT_RESULTS_20260914.json`.

All sign decisions in the finite audit use Python `Fraction` arithmetic.
SymPy is used only for symbolic identity gates.

The two counterexamples are independently reconstructed by solving the
central \(3\times3\) rational system directly instead of using the closed
\(D_r\) formula.
