> **RESOLUTION — 2026-11-12:** the parent-volume normalization question is now closed at the computational-algebra level. A new formal-jet calculation avoids the unstable global symbolic expansion in \(w=\mu^2\), solves the null cones independently at exact rational directions, reconstructs the directional \(L^2\) and \(L^4\) polynomials, and validates them on four held-out rational directions. It gives
> \[
> \langle c_2\rangle=0,\qquad
> \langle c_4\rangle=\frac{34}{8505}.
> \]
> Because the normalized angular/time directional integral has flat value \(1/2\), the physical volume ratio is twice this quantity:
> \[
> \boxed{
> \frac{V_{\rm Kasner}}{V_{\rm flat}}
> =
> 1+\frac{68}{8505}L^4+O(L^6).
> }
> \]
> Thus
> \[
> \boxed{v_E=\frac{17}{630}}
> \]
> for \(E^2=8/27\). The earlier temporary \(136/8505\) diagnosis is false. The original monolithic symbolic-\(w\) checker remains diagnostic; the repaired parent-volume checker is \`tools/derive_d4_kasner_parent_volume_directional_jets.py\`.

# Audit: Kasner parent-volume normalization and independent numerical cross-check

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** normalization issue resolved by an exact directional formal-jet reconstruction + independent numerical physical-volume regression  
**Purpose:** record and resolve a false normalization alarm without hiding the intermediate mistake

## 1. Why this audit exists

The first symbolic Kasner checker formed a directional time/angle integral and labeled one of its intermediate quantities as a normalized parent-volume ratio.

Inspecting its flat term suggested a missing factor \(2\), because the normalized angular average of the flat directional time integral is

\[
\int_{-1}^{0}(1+Y)^3dY
+
\int_{0}^{1}(1-Y)^3dY
=
\frac12.
\]

A temporary patch therefore multiplied that intermediate quantity by \(2\) and tentatively doubled the reported \(L^4\) coefficient.

That conclusion was not accepted without an independent physical-volume calculation.

## 2. Independent calculation

A second implementation starts directly from

\[
V
=
\int_{1-L}^{1+L}
dt\,
t
\int d\Omega
\int_0^{\rho_{\max}(t,\Omega)}
\rho^2d\rho,
\]

for the LRS Kasner metric

\[
ds^2
=
-dt^2
+
t^{-2/3}dx^2
+
t^{4/3}(dy^2+dz^2).
\]

Here

\[
\sqrt{\det g_{\rm spatial}}=t.
\]

For every angular direction separately, the code:

1. solves the conserved-momentum null-geodesic direction equation;
2. computes the future cone from the past tip;
3. computes the past cone from the future tip;
4. solves for their direction-dependent crossing time;
5. integrates the correct cone on each side of that crossing;
6. performs the full \(\mu\in[-1,1]\) integral, not a normalized angular average.

The final quantity is normalized directly by

\[
V_{\rm flat}
=
\frac{2\pi}{3}L^4.
\]

Therefore its flat limit is \(1\) by construction.

The repository implementation is

tools/check_d4_kasner_parent_volume_numerically.py.

## 3. Executed regression

An equivalent implementation was executed during the audit.

The measured scaled coefficients

\[
c(L)
=
\frac{V/V_{\rm flat}-1}{L^4}
\]

were:

| \(L\) | \(c(L)\) |
|---:|---:|
| 0.18 | 0.00823097532273 |
| 0.15 | 0.00815760604614 |
| 0.12 | 0.00809847516015 |
| 0.10 | 0.00806668731368 |
| 0.08 | 0.00804085094949 |

An even fit

\[
c(L)
=
c_0+c_2L^2+c_4L^4
\]

gives approximately

\[
c_0
=
0.0079953198.
\]

The rational value previously obtained for the physical Kasner volume is

\[
\boxed{
\frac{68}{8505}
=
0.00799529688418\ldots
}
\]

and the present extrapolation differs by about

\[
2.3\times10^{-8}.
\]

Thus the direct physical integration supports

\[
\boxed{
\frac{V_{\rm Kasner}}{V_{\rm flat}}
=
1+
\frac{68}{8505}L^4
+
O(L^6)
}
\]

rather than the temporarily proposed doubled coefficient.

## 4. Electric invariant conversion

At the centered Kasner midpoint,

\[
E^2=\frac8{27},
\qquad
B=0.
\]

Therefore

\[
\frac{
68/8505
}{
8/27
}
=
\boxed{
\frac{17}{630}.
}
\]

Numerically, the direct Kasner volume is therefore consistent with the purely electric coefficient

\[
v_E=\frac{17}{630}
\]

obtained independently by integrating the printed RNC intermediate equations in Wang (2019).

## 5. What went wrong in the symbolic checker

The current evidence shows that the naive diagnosis

\[
\text{“flat intermediate integral is }1/2
\Rightarrow
\text{physical }L^4\text{ coefficient doubles”}
\]

was incomplete.

The symbolic assembly contains another normalization/bookkeeping issue in its perturbative coefficient, so changing only the global factor creates a false doubled result.

The symbolic script has therefore been converted into diagnostic mode.

It must satisfy two conditions before being restored as an exact checker:

1. its flat normalized parent volume must equal \(1\);
2. its \(L^4\) coefficient must agree with the independently normalized physical-volume calculation.

No exact PASS is currently claimed for that script.

## 6. Scientific consequence

The false factor-two alarm does **not** currently overturn the Kasner physical-volume evidence.

The correct status is:

\[
\boxed{
\text{Kasner numerical volume supports }v_E=17/630,
}
\]

while

\[
\boxed{
\text{the exact symbolic Kasner implementation remains under audit.}
}
\]

Accordingly, Kasner should not yet be advertised as a second exact analytic proof, but it remains a strong independent numerical geometry check.

## 7. Relation to the literature audit

Wang's paper explicitly uses fourth-order RNC/geodesic expansions containing second covariant derivatives of curvature before simplifying the vacuum ACD geometry. The printed ACD null-boundary expression used for the final volume is described as abridged.

This makes it especially important not to infer a physical correction from one internal normalization issue in a separate Kasner implementation.

The current direct Kasner regression, the exact symmetric-plane-wave volume, and the re-integration of the published intermediate equations are mutually consistent at the level tested.

## 8. Next target

The next task is purely technical but important:

\[
\boxed{
\text{repair the symbolic Kasner parent-volume series so that its }
L^0
\text{ and }
L^4
\text{ normalizations agree simultaneously.}
}
\]

Only after that repair should the full Kasner recovery assembly be promoted again from numerical cross-check to exact analytic calibration.


## 9. Independent intrinsic-edge numerical check

A second direct calculation now audits the local invariant edge factor independently of the symbolic series code.

For each direction \(\mu\), the checker:

1. solves the exact Kasner null first integrals for both tips;
2. finds the direction-dependent edge crossing;
3. computes both affine lengths;
4. evaluates the Synge endpoint-gradient cross-normalization
   \[
   \chi
   =
   \left|
   g^{-1}
   \left(
   d(2\sigma_-),
   d(2\sigma_+)
   \right)
   \right|;
   \]
5. differentiates the exact numerical edge embedding to obtain \(dA\);
6. integrates
   \[
   \left\langle
   \frac{dA}{dA_0}
   \left(
   \frac{\chi}{\chi_0}
   \right)^{-3}
   \right\rangle.
   \]

The measured coefficients

\[
\frac{
\langle(dA/dA_0)(\chi/\chi_0)^{-3}\rangle-1
}{
E^2L^4
}
\]

were:

| \(L\) | measured |
|---:|---:|
| 0.18 | 0.0560677397 |
| 0.15 | 0.0556780374 |
| 0.12 | 0.0553637284 |
| 0.10 | 0.0551947063 |
| 0.08 | 0.0550572250 |

An even fit in \(L^2\) gives approximately

\[
0.05481491.
\]

The exact symbolic target from the local edge calculation is

\[
\boxed{
\frac{37}{675}
=
0.0548148148\ldots
}
\]

with a difference of about

\[
9\times10^{-8}.
\]

Thus both of the following Kasner ingredients now have independent physical numerical checks:

\[
\boxed{
v_E^{\rm parent}
=
\frac{17}{630},
}
\]

and

\[
\boxed{
v_E^{\rm edge-cross}
=
\frac{37}{675}.
}
\]

Combining them with the separately derived universal thin-null contribution

\[
-\frac1{105}E^2L^4
\]

gives

\[
\frac{17}{630}
+
\frac{37}{675}
-
\frac1{105}
=
\boxed{
\frac{683}{9450}.
}
\]

Therefore the Kasner geometry again supports the Schwarzschild recovery coefficient at the level of two independent numerical geometric integrations plus the analytic thin-null theorem.

The remaining open issue is no longer the physical Kasner result; it is the repair and successful execution of the exact symbolic Kasner series checker.

The numerical edge checker is

tools/check_d4_kasner_edge_cross_numerically.py.


## 10. Exact directional formal-jet reconstruction

The repaired calculation treats the angular parameter

\[
w=\mu^2
\]

as an exact rational value while performing the \(L\)-series algebra.

This avoids carrying a free symbolic \(w\) through every square root and nonlinear series operation.

For each fixed rational direction, the calculation:

1. expands the past and future null first integrals as formal jets in \(L\);
2. solves the conserved-momentum direction parameter coefficient by coefficient;
3. solves the direction-dependent cone crossing through \(L^4\);
4. integrates the physical directional volume through \(L^4\).

Five exact rational directions reconstruct

\[
\boxed{
c_2(w)
=
\frac{
7(45w^2-57w+10)
}{
540
},
}
\]

and

\[
\boxed{
c_4(w)
=
\frac{
56133w^4
-152334w^3
+138393w^2
-46632w
+3608
}{
54432
}.
}
\]

Four additional directions were not used in the interpolation:

\[
w=\frac9{16},
\qquad
\frac34,
\qquad
\frac23,
\qquad
\frac56.
\]

Every held-out \(c_2\) and \(c_4\) value agrees with the reconstructed polynomials with exact rational difference

\[
0.
\]

Using

\[
\left\langle w^k\right\rangle_{S^2}
=
\frac1{2k+1},
\]

one obtains

\[
\boxed{
\left\langle c_2\right\rangle=0,
}
\]

and

\[
\boxed{
\left\langle c_4\right\rangle
=
\frac{34}{8505}.
}
\]

The raw directional integral has flat value \(1/2\), so

\[
\boxed{
\frac{V_{\rm Kasner}}{V_{\rm flat}}
=
2
\left[
\frac12+
\frac{34}{8505}L^4+O(L^6)
\right]
=
1+\frac{68}{8505}L^4+O(L^6).
}
\]

This agrees exactly with the rational target inferred from the independently normalized physical-volume regression.

The checker is

\`tools/derive_d4_kasner_parent_volume_directional_jets.py\`.

The derivation uses exact rational arithmetic at every sampled direction. The angular polynomial is reconstructed from exact values and tested on four exact held-out directions; it is therefore classified here as an **exact computational reconstruction**, distinct from a handwritten symbolic proof in a free angular variable.


## 11. CI closure of the repaired normalization audit

The updated workflow

.github/workflows/research-kasner-normalization-audit.yml

ran both exact implementations on GitHub Actions:

1. tools/derive_d4_kasner_parent_volume_exact.py
2. tools/derive_d4_kasner_parent_volume_directional_jets.py

Workflow run:

\[
\boxed{\text{43335082471}}
\]

completed with conclusion

\[
\boxed{\text{success}}.
\]

The job step

\[
\text{Run stable exact Kasner parent-volume checker}
\]

passed, and the independent step

\[
\text{Cross-check exact directional Kasner jets}
\]

also passed.

The tested commit was

7e050ec98c4d14fc8143f6516609f87a1d30e402.

Therefore the repaired parent-volume normalization is now covered by two distinct exact computational implementations in CI.
