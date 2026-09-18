import PrecategoryFormal.EdgeTogglePrecomputed

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Exact fixed-edge non-reachability count through the semantically proved
precomputed checker. The distinguished directed edge is `0 → 1`, which
occupies bit zero in the row-major loopless encoding; shifting a compressed
mask left by one therefore fixes that edge to absent.

The separator bit families depend only on `n,0,1` and are built once, outside
the graph-count loop.
-/
def fixed01NoReachFastCount (n : Nat) : Nat :=
  let m := directedNonloopEdgeCount n
  if h : 2 ≤ n then
    let source : MaskVertex n := ⟨0, by omega⟩
    let target : MaskVertex n := ⟨1, by omega⟩
    let families := separatorBitFamilies n source target
    countNatWhere (2 ^ (m - 1)) fun compressed =>
      noReachWithBitFamilies (compressed <<< 1) families
  else
    0

/-- Fast semantic checker reproduces the established small fixed-edge counts. -/
theorem fixed01NoReachFastCount_small :
    fixed01NoReachFastCount 2 = 2 ∧
    fixed01NoReachFastCount 3 = 24 ∧
    fixed01NoReachFastCount 4 = 1024 := by
  native_decide

/--
Central independent finite certificate for MF-R011: among the `2^19`
five-vertex loopless digraphs with `0 → 1` fixed absent, exactly 153600 have
no directed path from 0 to 1.

The computation uses only the precomputed edge-bit families whose Boolean
acceptance predicate was proved equivalent to mathematical
`Relation.ReflTransGen` non-reachability.
-/
theorem fixed01NoReachFastCount_five :
    fixed01NoReachFastCount 5 = 153600 := by
  native_decide

/-- Agreement with the original optimized C1 finite count. -/
theorem fixed01NoReachFast_agrees_optimized_five :
    fixed01NoReachFastCount 5 = fixed01NoReachCount 5 := by
  rw [fixed01NoReachFastCount_five, fixed01NoReachCount_five]

end PrecategoryFormal
