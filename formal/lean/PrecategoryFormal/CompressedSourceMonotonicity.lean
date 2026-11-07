import PrecategoryFormal.CompressedSourcePowerBound

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedSourceSign

/--
The original central shape L_h for h=n+2. Writing h as n+2
keeps the formal derivative bound valid for every natural n
without subtracting from a Nat index.
-/
def sourceShape (n : ℕ) (r : ℝ) : ℝ :=
  r - ((n : ℝ)+2) * r^(n+2) + ((n : ℝ)+1) * r^(n+3)

/--
The exact polynomial derivative, for every r and every n.
This identifies the positive expression already proved in
CompressedSourcePowerBound with an actual real derivative.
-/
theorem sourceShape_hasDerivAt (n : ℕ) (r : ℝ) :
    HasDerivAt (sourceShape n)
      (1 - ((n : ℝ)+2)^2*r^(n+1) +
        (((n : ℝ)+2)^2-1)*r^(n+2)) r := by
  have hp2 :
      HasDerivAt (fun x : ℝ => x^(n+2))
        (((n : ℝ)+2)*r^(n+1)) r := by
    simpa [show n+2-1=n+1 by omega, Nat.cast_add] using
      (hasDerivAt_pow (n+2) r)
  have hp3 :
      HasDerivAt (fun x : ℝ => x^(n+3))
        (((n : ℝ)+3)*r^(n+2)) r := by
    simpa [show n+3-1=n+2 by omega, Nat.cast_add] using
      (hasDerivAt_pow (n+3) r)
  have hsum :=
    ((hasDerivAt_id r).sub (hp2.const_mul ((n : ℝ)+2))).add
      (hp3.const_mul ((n : ℝ)+1))
  unfold sourceShape
  convert hsum using 1
  · funext x
    simp only [Pi.sub_apply, Pi.add_apply, id_eq]
  · ring

/--
Uniform strict increase of L_(n+2) on the original small-node
interval. The proof uses a positive derivative and the Mathlib
mean-value theorem, rather than finitely many sample values.
-/
theorem sourceShape_strictMonoOn (n : ℕ) :
    StrictMonoOn (sourceShape n) (Set.Ioo (0 : ℝ) (1/4)) := by
  apply strictMonoOn_of_hasDerivWithinAt_pos (convex_Ioo (0 : ℝ) (1/4))
  · have hc : Continuous (sourceShape n) := by
      unfold sourceShape
      fun_prop
    exact hc.continuousOn
  · intro x hx
    exact (sourceShape_hasDerivAt n x).hasDerivWithinAt
  · intro x hx
    have hx' : x ∈ Set.Ioo (0 : ℝ) (1/4) := by
      simpa only [interior_Ioo] using hx
    exact source_shape_derivative_expression_positive n x hx'.1 hx'.2

end PrecategoryFormal.CompressedSourceSign
