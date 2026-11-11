import PrecategoryFormal.A118LogTaylorRemainder

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

namespace PrecategoryFormal.A118CollisionExponentBridge

/--
Exact algebraic link between the collision log exponent and the third-
order logarithm remainder, without a Taylor or asymptotic assumption.
This identity is valid whenever x is nonzero.
-/
theorem exact_collision_exponent_decomposition
    (x α b : ℝ) (hx : x ≠ 0) :
    (-1/(2*x)+b)*Real.log (1+2*α*x)+α-
        (α^2+2*b*α)*x-
        (-(4/3)*α^3-2*b*α^2)*x^2 =
      (-1/(2*x)+b)*
        (Real.log (1+2*α*x)-
          (2*α*x-(2*α*x)^2/2+(2*α*x)^3/3))+
      (8/3)*b*α^3*x^3 := by
  field_simp [hx]
  ring

/--
The formally checked real log remainder applies throughout the
exact frozen A118 collision box, not just at finitely many probes.
The coefficient b is absent because this is the logarithm step.
-/
theorem collision_log_remainder_enclosure
    (x α : ℝ)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1/1000)
    (hα0 : 0 ≤ α) (hα1 : α ≤ 45) :
    |Real.log (1+2*α*x)-
      (2*α*x-(2*α*x)^2/2+(2*α*x)^3/3)| ≤
      (2*α*x)^4/(1-2*α*x) := by
  have hnonneg : 0 ≤ 2*α*x := by positivity
  have h1 : α*x ≤ 45*x :=
    mul_le_mul_of_nonneg_right hα1 hx0
  have h2 : 45*x ≤ (45:ℝ)/1000 := by
    nlinarith
  have hupper : 2*α*x ≤ (9:ℝ)/100 := by
    nlinarith
  exact PrecategoryFormal.A118LogTaylorRemainder.log_one_add_cubic_remainder
    (2*α*x) hnonneg hupper

end PrecategoryFormal.A118CollisionExponentBridge
