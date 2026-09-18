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
-/
def fixedEdgeNoReachFastCountFive (u v : Fin 5) : Nat :=
  if _h : u = v then
    0
  else
    let pos := nonloopEdgeBitIndex 5 u.val v.val
    let families := separatorBitLists 5 u v
    countNatWhere (2 ^ 19) fun compressed =>
      noReachWithBitLists (insertZeroBit pos compressed) families

end PrecategoryFormal
