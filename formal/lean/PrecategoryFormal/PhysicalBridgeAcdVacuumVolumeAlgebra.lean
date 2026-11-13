import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Algebraic reduction of the electric-sector ACD volume coefficient obtained
by adding the moving-boundary and RNC-determinant contributions.

This theorem certifies only the rational identity. It does not formalize
the geometric derivation of the two input terms.
-/
theorem acdVacuumElectricCoefficient
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h2 : d + 2 ≠ 0)
    (h3 : d + 3 ≠ 0)
    (h4 : d + 4 ≠ 0) :
    (7 * d + 2) / (180 * (d + 2))
      -
    (d ^ 2 + 2 * d + 8) /
      (60 * (d + 1) * (d + 2) * (d + 3) * (d + 4))
      =
    d * (7 * d ^ 2 + 44 * d + 58) /
      (180 * (d + 1) * (d + 3) * (d + 4)) := by
  field_simp [h1, h2, h3, h4]
  ring

/--
Algebraic reduction of the hook/magnetic-sector ACD volume coefficient.
-/
theorem acdVacuumHookCoefficient
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h2 : d + 2 ≠ 0)
    (h3 : d + 3 ≠ 0)
    (h4 : d + 4 ≠ 0) :
    d / (60 * (d + 1) * (d + 2))
      +
    d ^ 2 /
      (60 * (d + 1) * (d + 2) * (d + 3) * (d + 4))
      =
    d * (d + 6) /
      (60 * (d + 1) * (d + 3) * (d + 4)) := by
  field_simp [h1, h2, h3, h4]
  ring

/--
Expansion of the corrected electric numerator in the normalization used by
the published all-dimensional closed form.
-/
theorem acdVacuumElectricNumerator (d : ℝ) :
    (d + 2) * (7 * d ^ 2 + 44 * d + 58)
      =
    7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 116 := by
  ring

/--
The hook-sector numerator implied by the direct integration is one half of
the corresponding printed coefficient 6(d+2)(d+6).
-/
theorem acdVacuumHookNumerator (d : ℝ) :
    3 * (d + 2) * (d + 6)
      =
    (6 * (d + 2) * (d + 6)) / 2 := by
  ring

/--
Four-dimensional electric reduction after D^2 = 4 E^2.
-/
theorem acdVacuumD4ElectricReduction :
    (4 * (7 * 4 ^ 2 + 44 * 4 + 58) /
        (180 * (4 + 1) * (4 + 3) * (4 + 4)) : ℚ)
      +
    4 *
      (-4 /
        (120 * (4 + 1) * (4 + 3) * (4 + 4)) : ℚ)
      =
    17 / 630 := by
  norm_num

/--
Four-dimensional magnetic reduction after H^2 = 2 B^2.
-/
theorem acdVacuumD4MagneticReduction :
    2 *
      (4 * (4 + 6) /
        (60 * (4 + 1) * (4 + 3) * (4 + 4)) : ℚ)
      =
    1 / 210 := by
  norm_num

/--
The all-dimensional corrected coefficient combination selected by a
trace-free Cahen--Wallach plane wave.

For such a wave:
  E^2 = Tr(P^2)/4,
  H^2 = Tr(P^2)/2,
  D^2 = Tr(P^2).

The identity below is exactly the algebra needed to compare the general
coefficient formula with the independent Jacobi-determinant calculation.
-/
theorem acdVacuumPlaneWaveCombination
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h3 : d + 3 ≠ 0)
    (h4 : d + 4 ≠ 0) :
    (d * (7 * d ^ 2 + 44 * d + 58) /
        (180 * (d + 1) * (d + 3) * (d + 4))) / 4
      +
    (d * (d + 6) /
        (60 * (d + 1) * (d + 3) * (d + 4))) / 2
      -
    d /
      (120 * (d + 1) * (d + 3) * (d + 4))
      =
    d * (7 * d + 22) /
      (720 * (d + 1) * (d + 3)) := by
  field_simp [h1, h3, h4]
  ring

/--
The d=4 corrected parent-volume coefficients give the exact type-N
Cahen--Wallach coefficient 1/63 multiplying omega^4 L^4 when
E^2 = B^2 = omega^4/2.
-/
theorem acdVacuumD4PlaneWaveReduction :
    (((17 / 630 : ℚ) + (1 / 210 : ℚ)) / 2)
      =
    1 / 63 := by
  norm_num


/--
Raw electric moving-boundary coefficient from the three terms that arise
when the printed null-cone radius is raised to the spatial power and angular
averaged.
-/
theorem acdVacuumBoundaryElectricReduction
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h2 : d + 2 ≠ 0) :
    (1 / 36 : ℝ)
      - 1 / (45 * (d + 1))
      + d * (d - 1) / (90 * (d + 1) * (d + 2))
      =
    (7 * d + 2) / (180 * (d + 2)) := by
  field_simp [h1, h2]
  ring

/--
The corrected d=5 coefficients evaluated on the exact Weyl invariants of a
transversely boosted LRS-Kasner observer.

The invariant formulas are:
  E^2 = (v^4 + 2 v^2 + 3) / (4(1-v^2)^2),
  H^2 = 3 v^2 / (1-v^2)^2,
  D^2 = (7 v^4 + 2 v^2 + 3) / (2(1-v^2)^2).

This theorem certifies only the rational reduction.
-/
theorem acdVacuumD5BoostedKasnerCorrected
    (v : ℝ)
    (h : 1 - v ^ 2 ≠ 0) :
    (151 / 5184 : ℝ)
        * ((v ^ 4 + 2 * v ^ 2 + 3) /
            (4 * (1 - v ^ 2) ^ 2))
      +
    (11 / 5184 : ℝ)
        * ((3 * v ^ 2) /
            ((1 - v ^ 2) ^ 2))
      -
    (1 / 10368 : ℝ)
        * ((7 * v ^ 4 + 2 * v ^ 2 + 3) /
            (2 * (1 - v ^ 2) ^ 2))
      =
    (8 * v ^ 4 + 24 * v ^ 2 + 25) /
      (1152 * (1 - v ^ 2) ^ 2) := by
  field_simp [h]
  ring

/--
The d=5 specialization of the printed Eq. (79), evaluated on the same
boosted-Kasner Weyl invariants.
-/
theorem acdVacuumD5BoostedKasnerPrinted
    (v : ℝ)
    (h : 1 - v ^ 2 ≠ 0) :
    (3163 / 108864 : ℝ)
        * ((v ^ 4 + 2 * v ^ 2 + 3) /
            (4 * (1 - v ^ 2) ^ 2))
      +
    (11 / 2592 : ℝ)
        * ((3 * v ^ 2) /
            ((1 - v ^ 2) ^ 2))
      -
    (1 / 10368 : ℝ)
        * ((7 * v ^ 4 + 2 * v ^ 2 + 3) /
            (2 * (1 - v ^ 2) ^ 2))
      =
    (1508 * v ^ 4 + 5914 * v ^ 2 + 4713) /
      (217728 * (1 - v ^ 2) ^ 2) := by
  field_simp [h]
  ring

/--
Exact algebraic difference between the printed and corrected d=5 boosted
Kasner predictions.
-/
theorem acdVacuumD5BoostedPrintedMinusCorrected
    (v : ℝ)
    (h : 1 - v ^ 2 ≠ 0) :
    (1508 * v ^ 4 + 5914 * v ^ 2 + 4713) /
        (217728 * (1 - v ^ 2) ^ 2)
      -
    (8 * v ^ 4 + 24 * v ^ 2 + 25) /
        (1152 * (1 - v ^ 2) ^ 2)
      =
    (-2 * v ^ 4 + 689 * v ^ 2 - 6) /
      (108864 * (1 - v ^ 2) ^ 2) := by
  field_simp [h]
  ring


/--
The five electric-sector numerator contributions obtained by integrating the
printed intermediate equations sum to the corrected common numerator.

This theorem formalizes the exact polynomial identity before the final
normalization used in Eq. (79).
-/
theorem acdVacuumElectricFiveTermCommonNumerator
    (d : ℝ) :
    5 * (d + 1) * (d + 2) * (d + 3) * (d + 4)
      - 4 * (d + 2) * (d + 3) * (d + 4)
      + 2 * d * (d - 1) * (d + 3) * (d + 4)
      - 24
      - 3 * d * (d + 2)
      =
    d * (d + 2) * (7 * d ^ 2 + 44 * d + 58) := by
  ring

/--
At the common-numerator stage, replacing the corrected final electric
polynomial +116 by the printed +108 requires exactly a shift -8 d.
-/
theorem acdVacuumElectricPrintedCommonShift
    (d : ℝ) :
    d * (
        (7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 108)
          -
        (7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 116)
      )
      =
    -8 * d := by
  ring


/--
Factorization fingerprint of the corrected electric numerator.
-/
theorem acdVacuumElectricCorrectedFactorization
    (d : ℝ) :
    (d + 2) * (7 * d ^ 2 + 44 * d + 58)
      =
    7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 116 := by
  ring

/--
The printed electric numerator is exactly the corrected factorized numerator
minus eight.
-/
theorem acdVacuumElectricPrintedFactorizationRemainder
    (d : ℝ) :
    7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 108
      =
    (d + 2) * (7 * d ^ 2 + 44 * d + 58) - 8 := by
  ring


/--
General electric coefficient difference between the corrected all-d law and
the printed Eq. (79).
-/
theorem acdVacuumElectricCorrectedMinusPrinted
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h2 : d + 2 ≠ 0)
    (h3 : d + 3 ≠ 0)
    (h4 : d + 4 ≠ 0) :
    d * (7 * d ^ 2 + 44 * d + 58) /
        (180 * (d + 1) * (d + 3) * (d + 4))
      -
    d * (7 * d ^ 3 + 58 * d ^ 2 + 146 * d + 108) /
        (180 * (d + 1) * (d + 2) * (d + 3) * (d + 4))
      =
    2 * d /
      (45 * (d + 1) * (d + 2) * (d + 3) * (d + 4)) := by
  field_simp [h1, h2, h3, h4]
  ring

/--
The printed hook coefficient is exactly twice the corrected coefficient.
-/
theorem acdVacuumHookPrintedIsTwiceCorrected
    (d : ℝ)
    (h1 : d + 1 ≠ 0)
    (h3 : d + 3 ≠ 0)
    (h4 : d + 4 ≠ 0) :
    d * (d + 6) /
        (30 * (d + 1) * (d + 3) * (d + 4))
      =
    2 *
      (
        d * (d + 6) /
          (60 * (d + 1) * (d + 3) * (d + 4))
      ) := by
  ring

end PrecategoryFormal.PhysicalBridge
