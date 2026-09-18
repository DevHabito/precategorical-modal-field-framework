import PrecategoryFormal.EdgeToggleFastCount

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Insert an absent bit at position `pos` into a compressed natural-number mask.
Bits below `pos` are unchanged; compressed bits at and above `pos` are
shifted upward by one position.
-/
def insertZeroBit (pos compressed : Nat) : Nat :=
  let base := 2 ^ pos
  (compressed % base) + (2 * base) * (compressed / base)

/--
Exact semantic non-reachability count for one directed edge position on five
labeled vertices, with that distinguished edge fixed absent.

The `2^19` compressed masks parametrize the remaining nineteen edge bits.
The graph predicate is the precomputed checker already proved equivalent to
mathematical `Relation.ReflTransGen` non-reachability.

This compressed counter is retained as an optimization/cross-check. The
end-to-end ensemble certificate below also has a direct `2^20`-mask version
that does not depend on the correctness of `insertZeroBit`.
-/
def fixedEdgeNoReachFastCountFive (u v : Fin 5) : Nat :=
  if _h : u = v then
    0
  else
    let pos := nonloopEdgeBitIndex 5 u.val v.val
    let families := separatorBitLists 5 u v
    countNatWhere (2 ^ 19) fun compressed =>
      noReachWithBitLists (insertZeroBit pos compressed) families

/--
Direct full-mask predicate: the distinguished edge is absent and the target is
not mathematically reachable from the source, using the precomputed checker
already proved equivalent to `Relation.ReflTransGen` non-reachability.
-/
def fixedEdgeAbsentNoReachBoolFive
    (graph : Nat) (u v : Fin 5) : Bool :=
  !(maskHasDirectedEdge 5 graph u.val v.val) &&
    noReachWithBitLists graph (separatorBitLists 5 u v)

/-- Semantic meaning of the direct full-mask predicate. -/
theorem fixedEdgeAbsentNoReachBoolFive_eq_true_iff
    (graph : Nat) (u v : Fin 5) :
    fixedEdgeAbsentNoReachBoolFive graph u v = true ↔
      (¬ maskRelation 5 graph u v) ∧
      (¬ RelationReach (maskRelation 5 graph) u v) := by
  simp [
    fixedEdgeAbsentNoReachBoolFive,
    maskRelation,
    noReachWithBitLists_eq_true_iff
  ]

/--
Direct exact count over the entire five-vertex mask ensemble `[0,2^20)`.
Unlike `fixedEdgeNoReachFastCountFive`, this definition does not insert a zero
bit into a compressed mask; it explicitly filters all graph masks by absence
of the distinguished edge.
-/
def fixedEdgeNoReachDirectCountFive (u v : Fin 5) : Nat :=
  if _h : u = v then
    0
  else
    let families := separatorBitLists 5 u v
    countNatWhere (2 ^ directedNonloopEdgeCount 5) fun graph =>
      !(maskHasDirectedEdge 5 graph u.val v.val) &&
        noReachWithBitLists graph families

end PrecategoryFormal
