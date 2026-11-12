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

end PrecategoryFormal.PhysicalBridge
