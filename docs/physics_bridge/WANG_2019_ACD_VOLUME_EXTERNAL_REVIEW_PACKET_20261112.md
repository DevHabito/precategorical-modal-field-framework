> **Boosted non-type-N update — 2026-11-13:** a direct five-dimensional LRS-Kasner physical-volume calculation has now tested the corrected law in observer frames with \(H^2\neq0\), independently of Wang Eq. (74). The null-cone intersection is reduced exactly, slice by slice, to the lens volume of two three-balls, avoiding the angular switching error that invalidated the first numerical attempt. GitHub Actions run **43411592007** completed successfully. For \(v=0.3,0.5,0.7\), the \(L\to0\) extrapolation errors relative to the re-integrated law are approximately \(6.7\times10^{-6}\), \(1.16\times10^{-5}\), and \(1.37\times10^{-5}\), while the errors relative to the printed Eq. (79) are approximately \(6.14\times10^{-4}\), \(2.70\times10^{-3}\), and \(1.17\times10^{-2}\), respectively. An attempted inversion of these scalar data for the full \((A_5,B_5,C_5)\) vector was found to be numerically ill-conditioned and is explicitly **not** used as primary evidence. See \`D5_BOOSTED_KASNER_DIRECT_ACD_VOLUME_CHECK_20261113.md\`.

> **Higher-dimensional exact update — 2026-11-12:** the LRS-Kasner evidence in \(d=5,6\) has been upgraded from numerical regression to exact rational directional-jet verification. The new exact results are
> \[
> V^{(5)}/V_{\rm flat}^{(5)}
> =
> 1+\frac{25}{1152}L^4+O(L^6),
> \]
> and
> \[
> V^{(6)}/V_{\rm flat}^{(6)}
> =
> 1+\frac{2288}{65625}L^4+O(L^6),
> \]
> in exact agreement with the re-integrated all-\(d\) coefficients. Each polynomial reconstruction uses held-out rational directions with exact zero residual. GitHub Actions run \(43339417105\) completed successfully with both new checkers. See \`EXACT_D5_D6_LRS_KASNER_ACD_VOLUME_CHECKS_20261112.md\`.
>
> A third invariant-direction target has also been prepared: a transverse boost of the \(d=5\) LRS-Kasner observer produces
> \[
> H^2(v)=\frac{3v^2}{(1-v^2)^2}\ne0,
> \]
> with predicted corrected coefficient
> \[
> c_5(v)=\frac{8v^4+24v^2+25}{1152(1-v^2)^2}.
> \]
> Direct boosted-volume integration is not yet accepted: a first generic angular quadrature failed the flat Lorentz-invariance control at order \(10^{-4}\), comparable to the desired \(L^4\) signal. No coefficient was inferred from that failed route.

# External review packet: vacuum Alexandrov-volume coefficient audit

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Repository:** precategorical-modal-field-framework  
**Status:** internal exact/computational audit prepared for adversarial external review  
**Primary literature target:** Jinzhao Wang, *Geometry of small causal diamonds*, Phys. Rev. D 100, 064020 (2019), arXiv:1904.01034  
**DOI:** 10.1103/PhysRevD.100.064020

## 1. Review question

The narrow question is:

> Does direct integration of the publicly printed intermediate vacuum ACD formulas in Wang (2019), Eqs. (74)--(78), reproduce the coefficients printed in Eq. (79)?

The repository answer is:

\[
\boxed{\text{No, under the conventions printed in the paper.}}
\]

The direct re-integration instead gives

\[
\boxed{
V^{(d)}
=
\frac{2\Omega_{d-2}L^d}{d(d-1)}
+
\Omega_{d-2}L^{d+4}
\frac{
(7d^3+58d^2+146d+116)E^2
+
3(d+2)(d+6)H^2
-
\frac32(d+2)D^2
}{
90(d-1)(d+1)(d+2)(d+3)(d+4)
}
+
O(L^{d+5}).
}
\]

The printed Eq. (79) has

\[
(7d^3+58d^2+146d+108)E^2
+
6(d+2)(d+6)H^2
-
\frac32(d+2)D^2.
\]

Thus the candidate corrections implied by the printed intermediate equations are

\[
\boxed{108\to116}
\]

and

\[
\boxed{
6(d+2)(d+6)
\to
3(d+2)(d+6),
}
\]

with the \(D^2\) coefficient unchanged.

This packet does **not** assert a published erratum. It asks for independent verification of an exact internal inconsistency.

## 2. Relative coefficient form

Write

\[
\frac{V(D_L)}{V_{\rm flat}(L)}
=
1+
L^4
\left[
A_dE^2+B_dH^2+C_dD^2
\right]
+
o(L^4).
\]

The direct integration gives

\[
\boxed{
A_d=
\frac{
d(7d^2+44d+58)
}{
180(d+1)(d+3)(d+4)
},
}
\]

\[
\boxed{
B_d=
\frac{
d(d+6)
}{
60(d+1)(d+3)(d+4)
},
}
\]

\[
\boxed{
C_d=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
}
\]

## 3. Short d=4 hand check

In \(3+1\),

\[
D^2=4E^2,
\qquad
H^2=2B^2.
\]

Using the printed null-cone boundary and RNC determinant terms:

### Electric sector

Moving boundary:

\[
\boxed{
v_E^{\rm boundary}
=
\frac1{36}.
}
\]

RNC determinant:

\[
\boxed{
v_E^{\det g}
=
-\frac1{1260}.
}
\]

Therefore

\[
\boxed{
v_E
=
\frac1{36}-\frac1{1260}
=
\frac{17}{630}.
}
\]

### Magnetic sector

Moving boundary:

\[
\boxed{
v_B^{\rm boundary}
=
\frac1{225}.
}
\]

RNC determinant:

\[
\boxed{
v_B^{\det g}
=
\frac1{3150}.
}
\]

Therefore

\[
\boxed{
v_B
=
\frac1{225}+\frac1{3150}
=
\frac1{210}.
}
\]

Hence the direct \(d=4\) result is

\[
\boxed{
\frac{V(D_L)}{V_{\rm Mink}(L)}
=
1+
L^4
\left[
\frac{17}{630}E^2+
\frac1{210}B^2
\right]
+
o(L^4).
}
\]

The printed Eq. (79) instead reduces to

\[
\frac{127}{4725}E^2+
\frac1{105}B^2.
\]

The exact differences are

\[
\boxed{
\Delta v_E=\frac1{9450},
\qquad
\Delta v_B=-\frac1{210}.
}
\]

Human-readable derivation:

docs/physics_bridge/D4_ACD_VOLUME_HAND_DERIVATION_FROM_WANG_INTERMEDIATE_EQS_20261112.md

## 4. Exact symbolic re-integration

Principal symbolic auditors:

- tools/audit_wang2019_d4_acd_volume_eq79.py
- tools/audit_wang2019_alld_acd_volume_eq79.py
- tools/verify_alld_weyl_angular_contractions.py

The GitHub Actions workflow

.github/workflows/research-acd-volume-audits.yml

executed successfully on commit

c294a5c09ce1eb73b1f158d8ac6ce1b6d45b7d2a

in workflow run

43329307058.

The successful job executed:

1. the d=4 Wang audit;
2. the all-d Wang audit;
3. the all-d Cahen--Wallach check;
4. random algebraic-Weyl contraction stress tests.

The current blobs of those audit files were checked against the blobs from the successful run and are identical.

## 5. CAS-independent rational regression

A separate implementation avoids SymPy:

tools/regress_wang_acd_volume_fraction_only.py

It uses only Python fractions.Fraction, factorials, elementary beta integrals, and the angular contractions printed in the source paper.

It checks integer dimensions

\[
4\le d\le20
\]

against the symbolic formula.

## 6. Exact all-dimensional Cahen--Wallach check

For the symmetric Ricci-flat plane wave

\[
ds^2
=
-2du\,dv
+
\delta_{AB}dx^Adx^B
+
P_{AB}x^Ax^Bdu^2,
\]

with

\[
\operatorname{Tr}P=0,
\]

define

\[
T_2=\operatorname{Tr}(P^2).
\]

The exact Jacobi-determinant calculation gives

\[
\frac{V_{\rm PW}}{V_{\rm flat}}
=
1+
\lambda_dU^4T_2+\cdots,
\]

where

\[
\boxed{
\lambda_d
=
\frac{
d(7d+22)
}{
2880(d+1)(d+3)
}.
}
\]

For a centered interval,

\[
U=\sqrt2L.
\]

The central observer measures

\[
E^2=\frac14T_2,
\qquad
H^2=\frac12T_2,
\qquad
D^2=T_2.
\]

The re-integrated coefficients satisfy the exact identity

\[
\boxed{
\frac{A_d}{4}
+
\frac{B_d}{2}
+
C_d
=
\frac{
d(7d+22)
}{
720(d+1)(d+3)
}
=
4\lambda_d.
}
\]

The printed Eq. (79) does not satisfy this identity.

Checker:

tools/verify_alld_cahen_wallach_acd_volume.py

## 7. Independent LRS-Kasner electric check

For the \(3+1\) LRS Kasner vacuum

\[
ds^2
=
-dt^2
+
t^{-2/3}dx^2
+
t^{4/3}(dy^2+dz^2),
\]

with tips at

\[
t=1\pm L,
\]

the midpoint has

\[
B=0,
\qquad
E^2=\frac8{27}.
\]

A stable exact truncated-series calculation gives

\[
\boxed{
\frac{V_{\rm Kasner}}{V_{\rm flat}}
=
1+
\frac{68}{8505}L^4
+
O(L^6).
}
\]

Therefore

\[
\boxed{
v_E
=
\frac{68/8505}{8/27}
=
\frac{17}{630}.
}
\]

Authoritative stable checker:

tools/derive_d4_kasner_parent_volume_exact.py

Its GitHub Actions audit completed successfully in workflow run

43329109917

on commit

da84e90e98dda8f9cff66bc32f418c671382f66d.

The current checker blob is identical to the tested blob.

A second independent directional-jet implementation is:

tools/derive_d4_kasner_parent_volume_directional_jets.py

It reconstructs the exact directional coefficients

\[
c_2(w)
=
\frac{
7(45w^2-57w+10)
}{
540
},
\]

\[
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
},
\]

from exact rational directions and verifies additional held-out rational directions.

The spherical average gives

\[
\langle c_2\rangle=0,
\qquad
\langle c_4\rangle=\frac{34}{8505},
\]

so the physical ratio is again

\[
1+\frac{68}{8505}L^4+\cdots.
\]

## 8. Higher-dimensional LRS-Kasner regression

The independent numerical tool

tools/check_alld_lrs_kasner_acd_volume_numerically.py

tests a non-type-N invariant direction in higher dimensions.

For \(n=d-1\),

\[
p_\parallel=-\frac{n-2}{n},
\qquad
p_\perp=\frac2n,
\]

and

\[
E^2=
\frac{
4(n-2)^2(n-1)
}{
n^3
},
\]

\[
D^2=
\frac{
16(n-1)(n-2)
}{
n^3
}.
\]

The direct physical-volume integration agrees with

\[
A_dE^2+C_dD^2
\]

in the tested dimensions \(d=4,5,6\).

These are numerical regressions, not exact proofs.

## 9. Lean-certified algebraic layer

The file

formal/lean/PrecategoryFormal/PhysicalBridgeAcdVacuumVolumeAlgebra.lean

formalizes the rational-algebra layer only.

It proves:

- the electric boundary-plus-determinant reduction;
- the hook/magnetic reduction;
- the corrected electric numerator \(+116\);
- the factor-\(1/2\) relation for the printed hook numerator;
- the \(d=4\) reductions \(17/630\) and \(1/210\);
- the all-d Cahen--Wallach coefficient combination;
- the \(d=4\) plane-wave reduction.

It does **not** formalize the differential geometry or the tensorial derivation of the input contractions.

GitHub Actions run

43328112419

completed successfully. In particular, kernel replay for

PrecategoryFormal.PhysicalBridgeAcdVacuumVolumeAlgebra

completed successfully with no proof placeholders.

The current Lean source blob is identical to the tested blob.

## 10. Evidence hierarchy

### Exact and directly reproducible

1. hand d=4 angular integration;
2. SymPy d=4 re-integration;
3. symbolic all-d re-integration;
4. random algebraic-Weyl contraction regressions;
5. exact all-d Cahen--Wallach Jacobi calculation;
6. exact d=4 Kasner parent-volume truncated series;
7. Lean kernel replay of the rational-algebra layer.

### Independent numerical evidence

1. direct physical d=4 Kasner volume;
2. higher-dimensional LRS-Kasner d=5,6 regressions.

### Not yet available

1. public access to Wang's supplemental Section C derivation;
2. independent review by another researcher;
3. confirmation from the original author;
4. a published erratum;
5. complete formalization of the tensor/RNC geometry in Lean.

## 11. Claim boundary

The strongest claim justified internally is:

> Direct re-integration of Wang's publicly printed intermediate equations yields a different vacuum ACD coefficient formula from the printed Eq. (79). The re-integrated formula is independently consistent with exact Cahen--Wallach geometry, exact d=4 Kasner parent-volume algebra, higher-dimensional Kasner numerical checks, and Lean-certified rational reductions.

The following stronger claims are **not** made:

- that Wang's paper has been formally corrected;
- that the exact line-level source of the printed discrepancy is known;
- that the supplemental derivation necessarily contains the same issue;
- that this discrepancy has priority over any unpublished observation;
- that the result has passed external peer review.

## 12. Questions for an external reviewer

1. Is the transcription of Wang Eq. (74) used here exact, especially the \(H_i{}^m{}_jH_{lmk}\) contraction?
2. Are the \(S^{d-2}\) angular contractions applied with the same conventions as the paper?
3. Does independent integration of Eqs. (74), (76), and (78) give the numerator constant \(116\) or \(108\)?
4. Does the \(H^2\) numerator reduce to \(3(d+2)(d+6)\) or \(6(d+2)(d+6)\)?
5. Can the supplemental Section C derivation identify a convention or omitted term that reconciles the printed Eq. (79) with the exact plane-wave and Kasner checks?

A negative answer to any point should be accompanied by the smallest explicit algebraic counterstep possible.

## 13. Minimal reproduction map

1. Read:
   docs/physics_bridge/D4_ACD_VOLUME_HAND_DERIVATION_FROM_WANG_INTERMEDIATE_EQS_20261112.md
2. Run:
   python tools/audit_wang2019_d4_acd_volume_eq79.py
3. Run:
   python tools/audit_wang2019_alld_acd_volume_eq79.py
4. Run:
   python tools/verify_alld_cahen_wallach_acd_volume.py
5. Run:
   python tools/derive_d4_kasner_parent_volume_exact.py
6. Build/replay:
   PrecategoryFormal.PhysicalBridgeAcdVacuumVolumeAlgebra

Full audit notes:

- docs/physics_bridge/WANG_2019_D4_ACD_VOLUME_INTERNAL_CONSISTENCY_AUDIT_20261112.md
- docs/physics_bridge/ALLD_VACUUM_ACD_VOLUME_EQ79_INTERNAL_AUDIT_20261112.md
- docs/physics_bridge/WANG_2019_ACD_VOLUME_ALLD_PLANE_WAVE_VALIDATION_20261112.md
- docs/physics_bridge/D4_KASNER_PARENT_VOLUME_NORMALIZATION_AUDIT_20261112.md

## 14. Literature-access note

The public APS article page identifies supplemental material, but the supplemental item was subscription-restricted during the 2026-11-12 audit.

A targeted public search did not locate an accessible copy of Section C, a published erratum for Eq. (79), or an independent later reproduction of the exact Weyl-quadratic ACD volume coefficients.

That search result is only an access/literature-status statement. It is not a novelty proof.


## 15. Updated Kasner CI status

After this packet was first assembled, the second exact Kasner implementation was added to the dedicated GitHub Actions workflow.

Run

\[
\boxed{\text{43335082471}}
\]

completed successfully on commit

7e050ec98c4d14fc8143f6516609f87a1d30e402.

Both steps passed:

- stable exact symbolic-\(w\) truncated-series checker;
- independent exact rational-direction/held-out-jet checker.

This strengthens only the internal reproducibility of the Kasner parent-volume result. It does not replace external review.
