import PrecategoryFormal.EdgeToggleBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Independent reference count for the distinguished absent edge `0 → 1`.

For `n ≥ 2`, a compressed `(m-1)`-bit mask is shifted left so bit zero,
which is the `0 → 1` slot, is absent. Each resulting graph is tested with the
finite-set separator checker whose semantics were proved in
`EdgeToggleBridge.lean`.

This deliberately does not call `noReachCutBool` or `fixed01NoReachCount`.
-/
def fixed01NoReachReferenceCount (n : Nat) : Nat :=
  let m := directedNonloopEdgeCount n
  if h : 2 ≤ n then
    let source : MaskVertex n := ⟨0, by omega⟩
    let target : MaskVertex n := ⟨1, by omega⟩
    countNatWhere (2 ^ (m - 1)) fun compressed =>
      noReachFinsetBool n (compressed <<< 1) source target
  else
    0

/--
Independent semantic-reference reproduction of the small MF-R011 fixed-edge
counts. These values are computed through explicit finite subsets and
forward-closure violations, not through the optimized integer cut masks.
-/
theorem fixed01NoReachReferenceCount_small :
    fixed01NoReachReferenceCount 2 = 2 ∧
    fixed01NoReachReferenceCount 3 = 24 ∧
    fixed01NoReachReferenceCount 4 = 1024 := by
  native_decide

/-- The two independent Lean implementations agree through four vertices. -/
theorem fixed01NoReach_reference_agrees_optimized_small :
    fixed01NoReachReferenceCount 2 = fixed01NoReachCount 2 ∧
    fixed01NoReachReferenceCount 3 = fixed01NoReachCount 3 ∧
    fixed01NoReachReferenceCount 4 = fixed01NoReachCount 4 := by
  rcases fixed01NoReachReferenceCount_small with ⟨hr2, hr3, hr4⟩
  rcases fixed01NoReachCount_small with ⟨ho2, ho3, ho4⟩
  exact ⟨hr2.trans ho2.symm, hr3.trans ho3.symm, hr4.trans ho4.symm⟩

end PrecategoryFormal
