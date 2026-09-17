import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Number of directed non-loop edge slots on `n` labeled vertices. -/
def directedNonloopEdgeCount (n : Nat) : Nat := n * (n - 1)

/--
Row-major edge-bit index with the diagonal removed.  For a fixed source `u`,
target labels below `u` keep their index and labels above `u` are shifted down
by one.  The distinguished edge `0 → 1` therefore occupies bit zero.
-/
def nonloopEdgeBitIndex (n u v : Nat) : Nat :=
  u * (n - 1) + if v < u then v else v - 1

/-- Decode one loopless directed edge from a natural-number graph mask. -/
def maskHasDirectedEdge (n graph u v : Nat) : Bool :=
  if u < n ∧ v < n ∧ u ≠ v then
    graph.testBit (nonloopEdgeBitIndex n u v)
  else
    false

/-- Bit mask of all direct out-neighbours of `u`. -/
def outgoingVertexMask (n graph u : Nat) : Nat :=
  (List.range n).foldl
    (fun acc v =>
      if maskHasDirectedEdge n graph u v then acc ||| (1 <<< v) else acc)
    0

/-- One monotone reachability expansion step. -/
def expandReachMask (n graph reached : Nat) : Nat :=
  (List.range n).foldl
    (fun acc u =>
      if reached.testBit u then acc ||| outgoingVertexMask n graph u else acc)
    reached

/-- Iterate the reachability expansion a prescribed number of times. -/
def closeReachMask : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, reached => reached
  | fuel + 1, n, graph, reached =>
      closeReachMask fuel n graph (expandReachMask n graph reached)

/-- Executable bounded reachability used by the independent finite enumeration. -/
def maskReachableBool (n graph source target : Nat) : Bool :=
  (closeReachMask n n graph (1 <<< source)).testBit target

/-- Tail-recursive exact counter over natural numbers `[0,bound)`. -/
def countNatWhereAux (f : Nat → Bool) : Nat → Nat → Nat
  | 0, acc => acc
  | k + 1, acc => countNatWhereAux f k (if f k then acc + 1 else acc)

/-- Exact count of inputs in `[0,bound)` satisfying a Boolean predicate. -/
def countNatWhere (bound : Nat) (f : Nat → Bool) : Nat :=
  countNatWhereAux f bound 0

/--
Number of graph masks with the distinguished bit `0 → 1` fixed to zero and
with no bounded reachability from `0` to `1`.

A compressed `(m-1)`-bit mask is shifted left once, so the missing distinguished
edge remains exactly bit zero.
-/
def fixed01NoReachCount (n : Nat) : Nat :=
  let m := directedNonloopEdgeCount n
  if 2 ≤ n then
    countNatWhere (2 ^ (m - 1)) fun compressed =>
      !(maskReachableBool n (compressed <<< 1) 0 1)
  else
    0

/-- Independent finite checkpoints underlying MF-R011. -/
theorem fixed01NoReachCount_small :
    fixed01NoReachCount 2 = 2 ∧
    fixed01NoReachCount 3 = 24 ∧
    fixed01NoReachCount 4 = 1024 := by
  native_decide

/-- The five-vertex distinguished-edge count. -/
theorem fixed01NoReachCount_five : fixed01NoReachCount 5 = 153600 := by
  native_decide

/-- Arithmetic checkpoint corresponding to the historical ordered-pair counts. -/
theorem mf_r011_paired_count_arithmetic :
    2 * 2 * 2 = 8 ∧
    2 * 6 * 24 = 288 ∧
    2 * 12 * 1024 = 24576 ∧
    2 * 20 * 153600 = 6144000 := by
  norm_num

/-- Exact reduction of the five-vertex fixed-edge fraction to `75/256`. -/
theorem mf_r011_fraction_five_arithmetic :
    153600 * 256 = 75 * (2 ^ 19) := by
  norm_num

end PrecategoryFormal
