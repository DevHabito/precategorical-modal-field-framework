import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Algebraic factorization of the d = 3 bulk coefficient denominator after the
change of variables

  x = s(1+z)/2,  y = s(1-z)/2.

This is only the polynomial identity used by the continuum derivation.  It
does not formalize the asymptotic domination step.
-/
theorem twinD3BulkDenominatorFactorization (s z : ℝ) :
    let x := s * (1 + z) / 2
    let y := s * (1 - z) / 2
    x ^ 4 + y ^ 4 + x * y * (4 - x ^ 2 - y ^ 2)
      =
    s ^ 2 / 4 *
      (s ^ 2 * z ^ 4 + 3 * s ^ 2 * z ^ 2 - 4 * z ^ 2 + 4) := by
  dsimp
  ring

/--
The endpoint simplification used when the d = 3 s-integral is evaluated at
s = 2.
-/
theorem twinD3EndpointSquare (z : ℝ) :
    z ^ 4 + 3 * z ^ 2 + (1 - z ^ 2)
      =
    (1 + z ^ 2) ^ 2 := by
  ring

/--
Leading timelike-separation factorization in the d = 4 null-waist scaling.

With
  Δt = (C-D) - (A-B)
and radial change
  Δr = (A+B) - (C+D),
the radial part of Δt²-Δr² factors as shown below.
-/
theorem twinD4WaistTimelikeFactorization
    (A B C D : ℝ) :
    ((C - D) - (A - B)) ^ 2
      - ((A + B) - (C + D)) ^ 2
      =
    4 * (C - A) * (B - D) := by
  ring

/--
Factorization of the limiting d = 4 distinguishing-volume exponent.
-/
theorem twinD4DistinguishingFactorization
    (A B C D : ℝ) :
    (C ^ 2 - A ^ 2) + (B ^ 2 - D ^ 2)
      =
    (C - A) * (C + A)
      + (B - D) * (B + D) := by
  ring

/--
The elementary constant reduction used after the two identical d = 4
one-dimensional integrals each evaluate to sqrt(pi)/4.

This theorem checks only the algebraic/square-root normalization:
  144 * (sqrt(pi)/4)^2 = 9*pi.
-/
theorem twinD4PiCoefficient :
    144 * (Real.sqrt Real.pi / 4) ^ 2
      =
    9 * Real.pi := by
  have hpi : 0 ≤ Real.pi := le_of_lt Real.pi_pos
  calc
    144 * (Real.sqrt Real.pi / 4) ^ 2
        = 9 * (Real.sqrt Real.pi) ^ 2 := by ring
    _ = 9 * Real.pi := by
      rw [Real.sq_sqrt hpi]

end PrecategoryFormal.PhysicalBridge
