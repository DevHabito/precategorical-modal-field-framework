# Poisson limit for isolated vertices in a 3+1 Minkowski causal-comparability graph

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** project theorem — proof complete in the Poisson sprinkling ensemble; independent/external review pending  
**Scope:** fixed finite Alexandrov interval in flat \(3+1\)-dimensional Minkowski spacetime  
**Novelty status:** targeted review located general Poisson-approximation theory and causal-set discussions of isolated points, but no prior statement of the \(3\pi\) limit for this Lorentzian comparability graph. Absolute priority is not certified.

## 1. Theorem

Let \(A=I(p,q)\) be a fixed flat Alexandrov interval in \(3+1\)-dimensional Minkowski spacetime.

Normalize its spacetime volume measure to a probability measure \(\mu\).

Let

\[
\eta_\lambda
\]

be a Poisson point process on \(A\) with intensity measure

\[
\lambda\mu.
\]

Construct the undirected causal-comparability graph \(G_\lambda\) on \(\eta_\lambda\):

\[
\{x,y\}\in E(G_\lambda)
\quad\Longleftrightarrow\quad
x\prec y
\ \text{or}\
y\prec x.
\]

Let

\[
I_\lambda
\]

be the number of isolated vertices of \(G_\lambda\).

Then

\[
\boxed{
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(3\pi)
\right)
=
O(\lambda^{-1/2})
}
\]

as

\[
\lambda\to\infty.
\]

In particular,

\[
\boxed{
I_\lambda
\xrightarrow{d}
\operatorname{Poisson}(3\pi)
}
\]

and

\[
\boxed{
P(I_\lambda=0)
\longrightarrow
e^{-3\pi}.
}
\]

Numerically,

\[
3\pi
\approx
9.4247779608,
\]

and

\[
e^{-3\pi}
\approx
8.06995\times10^{-5}.
\]

The theorem concerns the **Poisson sprinkling ensemble**.

A fixed-cardinality/binomial version is not asserted here.

---

## 2. Coordinates and exact comparable volume

Use the standard interval

\[
p=(-1,\mathbf 0),
\qquad
q=(1,\mathbf 0).
\]

For

\[
x=(t,\mathbf x),
\qquad
r=\|\mathbf x\|,
\]

set

\[
a=1+t-r,
\qquad
b=1-t-r.
\]

The diamond is

\[
a\ge0,
\qquad
b\ge0,
\qquad
a+b\le2.
\]

Let \(d\sigma\) denote normalized area measure on \(S^2\).

The normalized spacetime measure is

\[
\boxed{
d\mu
=
3
\left(
1-\frac{a+b}{2}
\right)^2
da\,db\,d\sigma.
}
\]

For \(x\in A\), let

\[
S_x
=
\{y\in A:y\sim x\}
\]

be its continuum comparability region and set

\[
Q(x)=\mu(S_x).
\]

The exact comparable fraction is

\[
\boxed{
Q(a,b)
=
\frac{
a^2(2-b)^2+b^2(2-a)^2
}{16}.
}
\]

The unique zero of \(Q\) is the null waist

\[
a=b=0.
\]

---

## 3. Mean number of isolated vertices

For an inserted point \(x\), Poisson independence gives

\[
P(
x\text{ is isolated}
)
=
e^{-\lambda Q(x)}.
\]

By Campbell–Mecke,

\[
\boxed{
\alpha_\lambda
:=
E[I_\lambda]
=
\lambda
\int_A
e^{-\lambda Q(x)}
\,\mu(dx).
}
\]

Rescale the null-waist coordinates by

\[
a=\frac{2A}{\sqrt\lambda},
\qquad
b=\frac{2B}{\sqrt\lambda}.
\]

Then the exact integral becomes

\[
\alpha_\lambda
=
12
\int_{\substack{A,B\ge0\\A+B\le\sqrt\lambda}}
\left(
1-\frac{A+B}{\sqrt\lambda}
\right)^2
\exp\left[
-A^2
\left(
1-\frac{B}{\sqrt\lambda}
\right)^2
-B^2
\left(
1-\frac{A}{\sqrt\lambda}
\right)^2
\right]
dA\,dB.
\]

On the triangular domain, at least one of

\[
A,\ B
\]

is at most

\[
\frac{\sqrt\lambda}{2}.
\]

Hence the exponent is bounded below by

\[
c(A^2+B^2)
\]

for an absolute

\[
c>0
\]

(for example \(c=1/8\) suffices).

Taylor expansion of the prefactor and exponent on bounded sets, together with this Gaussian domination and an exponentially small tail, gives

\[
\boxed{
\alpha_\lambda
=
3\pi
+
O(\lambda^{-1/2}).
}
\]

Indeed,

\[
12
\int_0^\infty
\int_0^\infty
e^{-(A^2+B^2)}
\,dA\,dB
=
12
\left(
\frac{\sqrt\pi}{2}
\right)^2
=
3\pi.
\]

---

## 4. Stein–Palm coupling

The proof uses the general Poisson-functional coupling theorem of Penrose (2018), Theorem 3.1.

For \(k=1\), that theorem gives a total-variation Poisson bound once, for almost every candidate point \(x\), one constructs a coupling

\[
U_x,V_x
\]

such that

\[
U_x\overset d=I_\lambda,
\]

\[
1+V_x
\]

has the law of the isolated count after inserting \(x\), conditioned on \(x\) being isolated, and

\[
E|U_x-V_x|
\]

is controlled.

The conditioning is especially simple for the deterministic causal kernel.

Split

\[
\eta_\lambda
=
\eta_{\mathrm{in}}
\cup
\eta_{\mathrm{out}},
\]

where

\[
\eta_{\mathrm{in}}
=
\eta_\lambda\cap S_x
\]

and

\[
\eta_{\mathrm{out}}
=
\eta_\lambda\cap S_x^c.
\]

The inserted point \(x\) is isolated exactly when

\[
\eta_{\mathrm{in}}=\varnothing.
\]

The two restrictions are independent Poisson processes, so conditioning on this event leaves

\[
\eta_{\mathrm{out}}
\]

unchanged.

Choose

\[
U_x
=
\text{isolated count in }\eta_\lambda
\]

and

\[
V_x
=
\text{isolated count in }\eta_{\mathrm{out}}.
\]

This is an exact Palm coupling.

---

## 5. Two ways the coupling can change the count

Deleting all process points in \(S_x\) can change the isolated count in only two ways.

### 5.1 Removed isolated vertices

An originally isolated point lying in \(S_x\) is deleted.

Its expected number is

\[
\boxed{
a_\lambda(x)
=
\lambda
\int_{S_x}
e^{-\lambda Q(y)}
\,\mu(dy).
}
\]

### 5.2 Newly isolated vertices

A point

\[
y\notin S_x
\]

becomes isolated after deleting \(S_x\) exactly when

- no point lies in
  \[
  S_y\setminus S_x,
  \]
- at least one point lies in
  \[
  S_y\cap S_x.
  \]

Set

\[
R(x,y)
=
\mu(S_x\cap S_y).
\]

Poisson independence on the two disjoint regions gives

\[
\boxed{
b_\lambda(x)
=
\lambda
\int_{S_x^c}
e^{-\lambda(Q(y)-R(x,y))}
\left(
1-e^{-\lambda R(x,y)}
\right)
\mu(dy).
}
\]

Therefore

\[
E|U_x-V_x|
\le
a_\lambda(x)+b_\lambda(x).
\]

Penrose's bound yields

\[
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(\alpha_\lambda)
\right)
\le
(1\wedge\alpha_\lambda^{-1})
\left(
A_\lambda+B_\lambda
\right),
\]

where

\[
\boxed{
A_\lambda
=
\lambda^2
\int_A
\int_{S_x}
e^{-\lambda(Q(x)+Q(y))}
\,\mu(dy)\mu(dx)
}
\]

and

\[
\boxed{
B_\lambda
=
\lambda^2
\int_A
e^{-\lambda Q(x)}
\int_{S_x^c}
e^{-\lambda(Q(y)-R(x,y))}
\left(
1-e^{-\lambda R(x,y)}
\right)
\mu(dy)\mu(dx).
}
\]

It remains to prove

\[
A_\lambda=O(\lambda^{-1})
\]

and

\[
B_\lambda=O(\lambda^{-1/2}).
\]

---

## 6. Waist localization

Fix a sufficiently small waist neighborhood

\[
W_\varepsilon
=
\{a\le\varepsilon,\ b\le\varepsilon\}.
\]

Since \(Q\) is continuous and vanishes only at

\[
a=b=0,
\]

there is

\[
q_\varepsilon>0
\]

such that

\[
Q(x)\ge q_\varepsilon
\]

outside \(W_\varepsilon\).

All portions of \(A_\lambda\) and \(B_\lambda\) with at least one exponentially weighted point outside this neighborhood are therefore

\[
O(\lambda^m e^{-c\lambda})
\]

for a fixed integer \(m\).

Only the waist neighborhood can contribute at power-law order.

Inside \(W_\varepsilon\),

\[
Q(a,b)
\ge
\frac{a^2+b^2}{16}.
\]

Thus after

\[
a=\frac{2A}{\sqrt\lambda},
\qquad
b=\frac{2B}{\sqrt\lambda},
\]

all radial integrals are dominated by Gaussian functions times fixed polynomials.

---

## 7. The \(A_\lambda\) term

Inside the waist, write two points as

\[
x=(t_x,r_x\sigma_x),
\qquad
y=(t_y,r_y\sigma_y).
\]

Let

\[
\theta
=
\angle(\sigma_x,\sigma_y)
\]

and

\[
v=\sin(\theta/2).
\]

For sufficiently small fixed \(\varepsilon\), the radii satisfy

\[
r_x,r_y\ge r_0>0.
\]

If \(x\) and \(y\) are causally comparable, then

\[
(t_x-t_y)^2
>
(r_x-r_y)^2
+
4r_xr_yv^2.
\]

Therefore

\[
v^2
\le
C
\left(
a_x+b_x+a_y+b_y
\right)^2.
\]

For a fixed direction \(\sigma_x\), normalized spherical measure gives

\[
d\sigma_y
=
2v\,dv
\]

after integrating the azimuthal symmetry.

Under waist scaling, the allowed angular cap consequently has measure

\[
O\left(
\frac{
(A+B+C+D)^2
}{\lambda}
\right).
\]

The remaining rescaled radial integral is finite under the Gaussian domination from the previous section.

Hence

\[
\boxed{
A_\lambda
=
O(\lambda^{-1}).
}
\]

A sharper local calculation gives the candidate first term

\[
A_\lambda
\sim
\frac{
18\pi(3-2\sqrt2)
}{\lambda},
\]

but this coefficient is not needed for the theorem.

---

## 8. Endpoint-overlap lemma

The difficult term is \(B_\lambda\).

For incomparable points \(x,y\), the cross intersections

\[
I(p,x)\cap I(y,q)
\]

and

\[
I(p,y)\cap I(x,q)
\]

are empty by transitivity.

Therefore

\[
S_x\cap S_y
=
\left[
I(p,x)\cap I(p,y)
\right]
\cup
\left[
I(x,q)\cap I(y,q)
\right]
\]

up to measure-zero boundaries.

We now bound the two endpoint overlaps.

### Lemma

For \(x,y\) in a fixed sufficiently small waist neighborhood, with angular separation

\[
\theta
\]

and

\[
v=\sin(\theta/2),
\]

there exists a constant \(C\) independent of \(x,y\) such that

\[
\boxed{
\mu(
I(p,x)\cap I(p,y)
)
\le
C
\frac{
a_x^2a_y^2
}{
v^4
}
}
\]

and, by time reversal,

\[
\boxed{
\mu(
I(x,q)\cap I(y,q)
)
\le
C
\frac{
b_x^2b_y^2
}{
v^4
}.
}
\]

The right-hand side is interpreted as \(+\infty\) at \(v=0\), where the bound is trivial.

### Proof

Shift the past endpoint \(p\) to time zero.

Write

\[
x=(T,r\,u),
\qquad
r=T-a,
\]

with \(u\in S^2\).

For a point

\[
z=(s,w)\in I(p,x),
\]

write

\[
\rho=\|w\|,
\qquad
\delta=s-\rho\ge0,
\]

and let \(\beta\) be the angle between \(w\) and \(u\).

The conditions

\[
\|w\|\le s
\]

and

\[
\|ru-w\|\le T-s
\]

give

\[
(T-s-a+\delta)^2
+
2r\rho(1-\cos\beta)
\le
(T-s)^2.
\]

It follows that

\[
0\le\delta\le a
\]

and

\[
r\rho(1-\cos\beta)
\le
a(T-s).
\]

Because \(r\) is bounded below and \(\rho\le s\),

\[
(\rho\sin\beta)^2
\le
C\,a\,s(T-s).
\]

Moreover,

\[
|s-\rho\cos\beta|
\le
C a.
\]

Thus at fixed time \(s\), the spatial section of \(I(p,x)\) is contained in a tube around the null ray

\[
s\,u
\]

with longitudinal thickness

\[
O(a)
\]

and transverse radius

\[
O\left(
\sqrt{a\,s(T-s)}
\right).
\]

Its spatial volume is therefore bounded by

\[
C a^2 s(T-s).
\]

Now let \(x,y\) have null directions \(u_x,u_y\), deficits \(a_x,a_y\), and angular separation \(\theta\).

If the two time-\(s\) tubes intersect, then

\[
2sv
=
s\|u_x-u_y\|
\le
C
\left[
a_x+a_y
+
\sqrt{(a_x+a_y)s}
\right].
\]

Solving this quadratic inequality in \(\sqrt s\) gives

\[
s
\le
C
\frac{
a_x+a_y
}{
v^2
}.
\]

The intersection section is bounded by the smaller of the two tube-section volumes.

Integrating over \(s\), and using

\[
\min(a_x^2,a_y^2)
(a_x+a_y)^2
\le
4a_x^2a_y^2,
\]

gives

\[
\operatorname{vol}
\left(
I(p,x)\cap I(p,y)
\right)
\le
C
\frac{
a_x^2a_y^2
}{
v^4
}.
\]

Normalization by the fixed volume of \(A\) only changes \(C\).

The future estimate follows by time reversal.

\(\square\)

Consequently, for incomparable waist points,

\[
\boxed{
R(x,y)
\le
C
\frac{
a_x^2a_y^2+b_x^2b_y^2
}{
v^4
}.
}
\]

---

## 9. The \(B_\lambda\) term

Because

\[
R(x,y)
\le
\min(Q(x),Q(y)),
\]

we have

\[
Q(x)+Q(y)-R(x,y)
\ge
\max(Q(x),Q(y)).
\]

Also

\[
1-e^{-u}
\le
\min(1,u).
\]

Therefore

\[
B_\lambda
\le
\lambda^2
\iint
e^{-\lambda\max(Q(x),Q(y))}
\min(
1,\lambda R(x,y)
)
\,\mu(dx)\mu(dy),
\]

where the integral may be enlarged from incomparable pairs to the whole waist domain.

Apply the waist scaling

\[
a_x=\frac{2A}{\sqrt\lambda},
\quad
b_x=\frac{2B}{\sqrt\lambda},
\]

\[
a_y=\frac{2C}{\sqrt\lambda},
\quad
b_y=\frac{2D}{\sqrt\lambda}.
\]

The measure factor

\[
\lambda^2\,\mu(dx)\mu(dy)
\]

becomes a bounded multiple of

\[
dA\,dB\,dC\,dD\,d\sigma_x\,d\sigma_y.
\]

The overlap lemma gives

\[
\lambda R(x,y)
\le
C
\frac{
A^2C^2+B^2D^2
}{
\lambda v^4
}.
\]

Set

\[
H=A^2C^2+B^2D^2.
\]

For fixed \(\sigma_x\), normalized spherical measure gives exactly

\[
d\sigma_y=2v\,dv.
\]

For every

\[
k\ge0,
\]

\[
\int_0^1
2v
\min\left(
1,\frac{k}{v^4}
\right)
dv
\le
2\sqrt{k}.
\]

For \(0\le k\le1\), split at

\[
v=k^{1/4};
\]

for \(k\ge1\), the integral is at most \(1\le\sqrt k\).

Taking

\[
k=
\frac{C H}{\lambda}
\]

gives an angular factor

\[
O\left(
\lambda^{-1/2}\sqrt H
\right).
\]

Finally,

\[
\sqrt H
\le
AC+BD,
\]

and

\[
e^{-c\max(A^2+B^2,C^2+D^2)}
\le
e^{-\frac c2(A^2+B^2+C^2+D^2)}.
\]

The remaining radial integral is therefore finite.

Hence

\[
\boxed{
B_\lambda
=
O(\lambda^{-1/2}).
}
\]

---

## 10. Completion of the proof

We have shown

\[
A_\lambda
=
O(\lambda^{-1})
\]

and

\[
B_\lambda
=
O(\lambda^{-1/2}).
\]

Since

\[
\alpha_\lambda
\to
3\pi,
\]

the prefactor

\[
1\wedge\alpha_\lambda^{-1}
\]

is bounded.

Penrose's coupling theorem therefore gives

\[
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(\alpha_\lambda)
\right)
=
O(\lambda^{-1/2}).
\]

For Poisson laws,

\[
d_{\mathrm{TV}}
\left(
\operatorname{Poisson}(\alpha_\lambda),
\operatorname{Poisson}(3\pi)
\right)
\le
|\alpha_\lambda-3\pi|.
\]

From Section 3,

\[
|\alpha_\lambda-3\pi|
=
O(\lambda^{-1/2}).
\]

The triangle inequality gives

\[
\boxed{
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(3\pi)
\right)
=
O(\lambda^{-1/2}).
}
\]

This proves the theorem.

\(\square\)

---

## 11. Corollaries and limits of interpretation

The theorem gives

\[
P(I_\lambda=0)
\to
e^{-3\pi}.
\]

Since graph connectedness requires the absence of isolated vertices,

\[
\boxed{
\limsup_{\lambda\to\infty}
P(
G_\lambda
\text{ is connected}
)
\le
e^{-3\pi}.
}
\]

Equality is **not** claimed.

Other disconnected nontrivial components may also occur.

The theorem also does not obstruct UPO orientation recovery.

An isolated vertex has no comparability edge, so it contributes no independent transitive-orientation choice.

The theorem therefore separates two notions:

- full graph connectedness can remain extremely rare;
- logical recovery of all existing causal arrows can still become common.

---

## 12. Relation to existing literature

### Penrose

Mathew D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, **Journal of Applied Probability 55(1)**, 112–136 (2018), DOI 10.1017/jpr.2018.9.

The present proof uses Penrose's general Poisson-functional coupling theorem.

The convenient homogeneous isolated-vertex theorem in the same paper does not apply directly here because the Lorentzian connection kernel is deterministic \(0/1\) and the comparable-volume function degenerates to zero at the null waist.

The project-specific work is therefore the explicit Palm coupling for this causal kernel and the Lorentzian overlap estimate that verifies the general theorem despite that degeneracy.

### Causal-set isolated points

Causal-set literature has previously discussed isolated points, including their effect on small-cardinality dimension estimators.

That establishes the physical relevance of the object but does not, in the sources located in the targeted review, supply the present \(3\pi\) Poisson law.

### Priority boundary

Targeted searches did not locate a prior statement equivalent to

\[
I_\lambda
\Rightarrow
\operatorname{Poisson}(3\pi)
\]

for isolated vertices of the undirected causal-comparability graph of a \(3+1\)-dimensional Minkowski Alexandrov sprinkling.

This is limited negative evidence only.

Absolute novelty and priority are not certified.

---

## 13. What is still open

This theorem closes the **Poisson-sprinkling isolated-vertex distribution** in the fixed \(3+1\) diamond, subject to independent review of the project proof.

It does not yet close:

1. the fixed-cardinality/binomial limit
   \[
   I_n
   \Rightarrow
   \operatorname{Poisson}(3\pi);
   \]
2. the adjacent-twin asymptotic theorem;
3. the residual larger-module UPO obstruction;
4. the limit of
   \[
   p_4^{\mathrm{UPO}}(n);
   \]
5. any preferred temporal polarity, metric duration, or physical emergence-of-time claim.

The next clean mathematical target is the fixed-\(n\) version, preferably by factorial moments using the same null-waist overlap lemma.
