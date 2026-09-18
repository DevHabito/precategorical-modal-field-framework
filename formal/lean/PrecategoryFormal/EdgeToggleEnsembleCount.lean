import PrecategoryFormal.EdgeToggleFastCount
import PrecategoryFormal.EdgeTogglePairing
import PrecategoryFormal.EdgeToggleRelabel

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
-/
def fixedEdgeNoReachFastCountFive (u v : Fin 5) : Nat :=
  if h : u = v then
    0
  else
    let pos := nonloopEdgeBitIndex 5 u.val v.val
    let families := separatorBitLists 5 u v
    countNatWhere (2 ^ 19) fun compressed =>
      noReachWithBitLists (insertZeroBit pos compressed) families

/-- Sum of the fixed-absent-edge non-reachability counts over all 20 directed non-loop edges. -/
def allDirectedEdgeNoReachCountFive : Nat :=
  (List.finRange 5).foldl
    (fun total u =>
      (List.finRange 5).foldl
        (fun subtotal v =>
          if u = v then subtotal
          else subtotal + fixedEdgeNoReachFastCountFive u v)
        total)
    0

/--
Full five-vertex fixed-edge checksum.

This is deliberately stronger than multiplying the distinguished `0 → 1`
count by 20: all twenty directed non-loop edge positions are independently
evaluated by the semantically verified checker.
-/
theorem allDirectedEdgeNoReachCountFive_exact :
    allDirectedEdgeNoReachCountFive = 3072000 := by
  native_decide

/--
Each absent-base pivotal graph contributes both orientations of the toggle
inside its absent/present pair.
-/
def mfR011ChangedGraphEdgePairsFive : Nat :=
  2 * allDirectedEdgeNoReachCountFive

/-- Exact numerator of the declared MF-R011 ordered graph-edge ensemble at n=5. -/
theorem mfR011ChangedGraphEdgePairsFive_exact :
    mfR011ChangedGraphEdgePairsFive = 6144000 := by
  rw [mfR011ChangedGraphEdgePairsFive, allDirectedEdgeNoReachCountFive_exact]
  norm_num

/-- Exact size of the uniform ordered graph-edge ensemble at n=5. -/
def mfR011GraphEdgePairsFive : Nat :=
  (2 ^ directedNonloopEdgeCount 5) * directedNonloopEdgeCount 5

theorem mfR011GraphEdgePairsFive_exact :
    mfR011GraphEdgePairsFive = 20971520 := by
  norm_num [mfR011GraphEdgePairsFive, directedNonloopEdgeCount]

/--
Exact cross-multiplied probability identity.  This avoids introducing any
floating-point or rational-normalization layer into the kernel statement.
-/
theorem mf_r011_p5_exact :
    mfR011ChangedGraphEdgePairsFive * 256 =
      75 * mfR011GraphEdgePairsFive := by
  rw [mfR011ChangedGraphEdgePairsFive_exact, mfR011GraphEdgePairsFive_exact]
  norm_num

end PrecategoryFormal
