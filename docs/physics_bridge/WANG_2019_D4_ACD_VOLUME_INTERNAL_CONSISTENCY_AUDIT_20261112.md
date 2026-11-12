# Internal consistency audit of Wang (2019) ACD volume: Eqs. (74)+(76) versus Eq. (79)

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal algebraic audit of published equations; external review still required  
**Scope:** four-dimensional Ricci-flat Alexandrov causal diamonds  
**Reference:** Jinzhao Wang, *Geometry of small causal diamonds*, Phys. Rev. D 100, 064020 (2019), arXiv:1904.01034v2  
**Purpose:** determine whether the previously observed exact-geometry discrepancy originates in the null-cone calculation or in the final integration

## 1. Main finding

The published null-cone boundary, Eq. (74), and the published RNC volume density, Eq. (76), can be integrated directly in \(d=4\).

Doing so gives

\[
\boxed{
\frac{V}{V_0}
=
1+
L^4
\left[
\frac{17}{630}E^2
+
\frac1{210}B^2
\right]
+
O(L^5).
}
\]

The printed \(d=4\) specialization of Eq. (79), however, is

\[
\boxed{
\left.
\frac{V}{V_0}
\right|_{\rm Eq.(79)}
=
1+
L^4
\left[
\frac{127}{4725}E^2
+
\frac1{105}B^2
\right]
+
O(L^5).
}
\]

The exact differences are

\[
\boxed{
\Delta v_E
=
\frac1{9450},
}
\]

\[
\boxed{
\Delta v_B
=
-\frac1{210}.
}
\]

This audit does not use Kasner or the symmetric plane wave as an input.

Those exact geometries now become independent checks of the direct integration of the published intermediate equations.

## 2. Published ingredients

For the upper cone in \(d=4\), set \(L=1\) temporarily.

Equation (74) gives

\[
r_+(t,n)
=
(1-t)
\left[
1+a_1+a_2
\right],
\]

where

\[
a_1
=
\frac16E_{nn},
\]

and

\[
\begin{aligned}
a_2
={}&
\frac1{24}E_{nn}^2
-
\frac{t}{45}(E^2)_{nn}
\\
&+
\frac{(1-t)^2}{90}
n^in^j
\left[
E_i{}^lE_{lj}
+
\left(
H_i{}^m{}_jH_{lmk}
-
E_{ij}E_{lk}
\right)n^ln^k
\right].
\end{aligned}
\]

The index placement \(H_i{}^m{}_j\) is read directly from the published PDF.

Equation (76) gives

\[
\sqrt{|g|}
=
1-\frac{Q(x)}{180}
+
O(C^3),
\]

with

\[
Q
=
C^\gamma{}_\mu{}^\alpha{}_\nu
C_{\gamma\rho\alpha\sigma}
x^\mu x^\nu x^\rho x^\sigma.
\]

Because the density correction is already quadratic in curvature, it may be integrated over the flat cone.

## 3. Normalization

In \(d=4\),

\[
V_0
=
\frac{2\pi}{3}L^4.
\]

After setting \(L=1\), doubling the upper half and dividing by \(V_0\) gives the common normalization factor

\[
12
\]

for the angularly averaged \(t,r\) integrals.

The powers of \(L\) are restored at the end.

## 4. Pure-electric cone contribution

Set

\[
B_{ij}=0.
\]

For a symmetric trace-free \(E_{ij}\) on \(S^2\),

\[
\left\langle
E_{nn}^2
\right\rangle
=
\frac{2}{15}E^2,
\]

and

\[
\left\langle
(E^2)_{nn}
\right\rangle
=
\frac13E^2.
\]

The flat radial integral contains

\[
r_+^3.
\]

Through quadratic curvature,

\[
(1+a_1+a_2)^3
=
1+3a_1+3a_2+3a_1^2+O(C^3).
\]

The linear term averages to zero.

Thus

\[
\frac{\delta V_{\rm cone,E}}{V_0}
=
12E^2
\int_0^1
(1-t)^3
\left[
\frac{2/15}{24}
+
\frac{2/15}{36}
-
\frac{t}{135}
+
\frac{(1-t)^2}{90}
\left(
\frac13-\frac{2}{15}
\right)
\right]dt.
\]

The integral is exact:

\[
\boxed{
\frac{\delta V_{\rm cone,E}}{V_0}
=
\frac1{36}E^2.
}
\]

## 5. Pure-electric volume-density contribution

The tensorial Eq. (76) gives, after the \(S^2\) average,

\[
\boxed{
\frac{\langle Q_E\rangle}{E^2}
=
\frac{
3r^4+5t^4
}{5}.
}
\]

Therefore

\[
\frac{\delta V_{\sqrt g,E}}{V_0}
=
-\frac1{15}
E^2
\int_0^1dt
\int_0^{1-t}dr\,
r^2
\frac{
3r^4+5t^4
}{5}.
\]

The double integral is

\[
\frac1{84},
\]

so

\[
\boxed{
\frac{\delta V_{\sqrt g,E}}{V_0}
=
-\frac1{1260}E^2.
}
\]

Adding the two pieces,

\[
\frac1{36}
-
\frac1{1260}
=
\boxed{
\frac{17}{630}
}.
\]

Hence Eqs. (74) and (76) imply

\[
\boxed{
v_E=\frac{17}{630}.
}
\]

## 6. Pure-magnetic cone contribution

Now set

\[
E_{ij}=0.
\]

In four dimensions,

\[
H_{ijk}
=
\epsilon_{jkm}B_i{}^m,
\]

and

\[
H^2=2B^2.
\]

The only quadratic cone term from Eq. (74) is

\[
\frac{(1-t)^2}{90}
n^in^jn^ln^k
H_i{}^m{}_jH_{lmk}.
\]

The exact spherical average is

\[
\boxed{
\left\langle
n^in^jn^ln^k
H_i{}^m{}_jH_{lmk}
\right\rangle
=
\frac15B^2
=
\frac1{10}H^2.
}
\]

Therefore

\[
\frac{\delta V_{\rm cone,B}}{V_0}
=
12B^2
\int_0^1
(1-t)^3
\frac{(1-t)^2}{450}
dt.
\]

Since

\[
\int_0^1(1-t)^5dt=\frac16,
\]

we obtain

\[
\boxed{
\frac{\delta V_{\rm cone,B}}{V_0}
=
\frac1{225}B^2.
}
\]

## 7. Pure-magnetic volume-density contribution

For the tensorial Eq. (76),

\[
\boxed{
\frac{\langle Q_B\rangle}{B^2}
=
\frac25
r^2
\left(
5t^2-r^2
\right).
}
\]

Thus

\[
\frac{\delta V_{\sqrt g,B}}{V_0}
=
-\frac1{15}
B^2
\int_0^1dt
\int_0^{1-t}dr\,
r^2
\frac25
r^2
(5t^2-r^2).
\]

The double integral is

\[
-\frac1{210}.
\]

Hence

\[
\boxed{
\frac{\delta V_{\sqrt g,B}}{V_0}
=
\frac1{3150}B^2.
}
\]

Adding the cone and density pieces,

\[
\frac1{225}
+
\frac1{3150}
=
\boxed{
\frac1{210}.
}
\]

Therefore Eqs. (74) and (76) imply

\[
\boxed{
v_B=\frac1{210}.
}
\]

## 8. Direct comparison with Eq. (79)

Equation (79) states

\[
V^{(d)}
=
\frac{
2\Omega_{d-2}L^d
}{
d(d-1)
}
+
\Omega_{d-2}L^{d+4}
\frac{
(7d^3+58d^2+146d+108)E^2
+
6(d+2)(d+6)H^2
-
\frac32(d+2)D^2
}{
90(d-1)(d+1)(d+2)(d+3)(d+4)
}
+\cdots.
\]

For \(d=4\),

\[
H^2=2B^2,
\qquad
D^2=4E^2.
\]

Dividing by

\[
V_0=\frac{2\pi}{3}L^4
\]

gives

\[
v_E^{(79)}
=
\frac{127}{4725},
\]

\[
v_B^{(79)}
=
\frac1{105}.
\]

These do not equal the direct integrals of Eqs. (74) and (76).

The differences are

\[
\boxed{
\frac{17}{630}
-
\frac{127}{4725}
=
\frac1{9450},
}
\]

and

\[
\boxed{
\frac1{210}
-
\frac1{105}
=
-\frac1{210}.
}
\]

## 9. Independent exact-spacetime checks

The direct intermediate-equation result is independently reproduced by two geometries already calculated in the repository.

### LRS Kasner

The exact null-cone integration gives

\[
\frac{\delta V}{V_0}
=
\frac{17}{630}E^2L^4
\]

with

\[
B=0.
\]

### Symmetric Cahen--Wallach plane wave

The exact causal-ellipse calculation gives

\[
\frac{\delta V}{V_0}
=
\frac1{63}\omega^4L^4.
\]

Since

\[
E^2=B^2=\frac{\omega^4}{2},
\]

the pair

\[
\frac{17}{630},
\qquad
\frac1{210}
\]

gives

\[
\frac12
\left(
\frac{17}{630}
+
\frac1{210}
\right)
=
\frac1{63},
\]

exactly as required.

Thus three independent routes now agree:

1. direct integration of Wang Eqs. (74)+(76);
2. exact LRS Kasner;
3. exact symmetric plane wave.

## 10. What this changes

The earlier working hypothesis was that the discrepancy might lie in the \(C^2\) null-cone boundary.

The present audit does not support that hypothesis.

The published intermediate boundary and volume-density equations already produce the exact-geometry coefficient pair.

The discrepancy is therefore localized more sharply to the algebraic passage

\[
\boxed{
\text{Eqs. (74),(76),(78)}
\longrightarrow
\text{Eq. (79)}.
}
\]

This is a much narrower claim than saying that the RNC construction itself is wrong.

## 11. What is not yet claimed

The repository still does not claim:

- that the paper has a formally established erratum;
- that the source of the arithmetic difference has been identified line by line in the unpublished/supplemental algebra;
- that the arbitrary-dimensional version of Eq. (79) has been corrected;
- that no convention in the inaccessible supplemental derivation could affect the comparison.

However, within the equations printed in the public paper, the \(d=4\) inconsistency is exact and reproducible.

## 12. Reproducibility

The principal checker is

tools/audit_wang_d4_eq74_eq76_to_eq79_full.py

and uses exact SymPy rational arithmetic.

A separate pure-electric checker is retained at

tools/audit_wang_d4_pure_electric_eq74_to_eq79.py

because the electric sector alone already establishes an inconsistency without requiring interpretation of the \(H_i{}^m{}_j\) index placement.

## 13. Next target

The next task is no longer to reconstruct the \(C^2\) cone boundary from scratch.

The higher-value target is to reconstruct the symbolic integration from Eq. (78) in arbitrary dimension and determine which coefficient in the printed numerator of Eq. (79) changes.

In \(d=4\), the evidence requires

\[
\boxed{
v_E=\frac{17}{630},
\qquad
v_B=\frac1{210}.
}
\]

The arbitrary-dimensional audit should be performed without fitting these values.
