# Failed Lean proof attempt: source-shape strict monotonicity

**Date:** 7 November 2026  
**Disposition:** `NOT_LEAN_VERIFIED` — experimental file withdrawn from the formal build after three failed attempts.  
**Mathematical claim:** uniform strict increase of `L_h(r)` for `h>=2` on `(0,1/4)`. A separate self-contained analytic proof exists in [A115 source-sign note](../A115_UNIFORM_SOURCE_NUMERATOR_SIGN_20261107.md); this file records an incomplete attempt to formalize it, **not a refutation**.

## What worked before this attempt

The `CompressedSourcePowerBound.lean` module, on [GitHub Actions run 42359321885](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359321885), passed 25/25 build and kernel jobs. It proves the all-natural-index inequality `(n+2)^2*r^(n+1)<=4r`, positivity of the explicit formal derivative polynomial, and the exact parity baseline factorizations. The `CompressedSourceNumerator.lean` module passed 24/24 in [run 42358976869](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358976869).

## Three distinct failed compile attempts

1. [Run 42359621482](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359621482): `ring_nf made no progress` and unsolved goals. The proof used `convert` and sent a function-equality obligation to a scalar ring tactic.
2. [Run 42359869530](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359869530): the attempted `funext` correction reached the wrong obligation because `convert` was also comparing two elaborated `AddCommGroup Real` instances.
3. [Run 42360042902](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360042902): removing `convert` and rewriting the scalar coefficients explicitly still did not discharge a type-class instance discrepancy. The compiler contrasted `Real.instAddCommGroup` with `Real.normedAddCommGroup.toAddCommGroup` in the `HasDerivAt` expression.

None of these logs provides a counterexample to `L_h'(r)>0`. The source-level approach itself needs to be redesigned: for example, derive the derivative through a single canonical polynomial representation, or construct an elementary order proof without going through the nondefinitional function instance mismatch. A future attempt must pass both a Lean project build and the individual Leanchecker replay before being promoted.

To avoid misleading anyone, the original experimental `.lean` file was removed from the build matrix and entrypoint; its **full last attempted source** is preserved below as text.

## Last attempted Lean source — not a valid proof artifact

```lean
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
  have hcoeff :
      1 - ((n : ℝ)+2)^2*r^(n+1) +
          (((n : ℝ)+2)^2-1)*r^(n+2) =
        1 - ((n : ℝ)+2)*(((n : ℝ)+2)*r^(n+1)) +
          ((n : ℝ)+1)*(((n : ℝ)+3)*r^(n+2)) := by
    ring
  rw [hcoeff]
  simpa only [sourceShape, Pi.sub_apply, Pi.add_apply, id_eq] using hsum

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
```

**Publication rule:** do not quote the above module as a certified theorem. The all-index power bound and conditional Z-sign lemma *are* verified elsewhere, and the full handwritten source sign proof remains mathematically separate from this failed mechanization.
