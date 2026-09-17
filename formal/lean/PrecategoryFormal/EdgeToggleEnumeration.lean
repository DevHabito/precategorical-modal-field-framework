import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Number of directed non-loop edge slots on `n` labeled vertices. -/
def directedNonloopEdgeCount (n : Nat) : Nat := n * (n - 1)

/--
Row-major edge-bit index with the diagonal removed. For a fixed source `u`,
target labels below `u` keep their index and labels above `u` are shifted down
by one. The distinguished edge `0 → 1` therefore occupies bit zero.
-/
def nonloopEdgeBitIndex (n u v : Nat) : Nat :=
  u * (n - 1) + if v < u then v else v - 1

/-- Decode one loopless directed edge from a natural-number graph mask. -/
def maskHasDirectedEdge (n graph u v : Nat) : Bool :=
  if u < n ∧ v < n ∧ u ≠ v then
    graph.testBit (nonloopEdgeBitIndex n u v)
  else
    false

/--
Mask of graph-edge positions that leave a vertex cut. Bit `e` is set exactly
when the source of edge slot `e` lies in `cut` and its target lies outside.
-/
def cutOutgoingEdgeMask (n cut : Nat) : Nat :=
  (List.range n).foldl
    (fun acc u =>
      (List.range n).foldl
        (fun acc v =>
          if cut.testBit u && !(cut.testBit v) then
            if u = v then acc
            else acc ||| (1 <<< nonloopEdgeBitIndex n u v)
          else
            acc)
        acc)
    0

/-- All cuts that contain `source` and exclude `target`, encoded by their outgoing-edge masks. -/
def separatingCutEdgeMasks (n source target : Nat) : List Nat :=
  (List.range (2 ^ n)).filterMap fun cut =>
    if cut.testBit source && !(cut.testBit target) then
      some (cutOutgoingEdgeMask n cut)
    else
      none

/--
Executable cut certificate for non-reachability: some source/target-separating
cut has no graph edge leaving it.
-/
def noReachCutBool (n graph source target : Nat) : Bool :=
  let cuts := separatingCutEdgeMasks n source target
  cuts.any fun outgoing => (graph &&& outgoing) == 0

/-- Tail-recursive exact counter over natural numbers `[0,bound)`. -/
def countNatWhereAux (f : Nat → Bool) : Nat → Nat → Nat
  | 0, acc => acc
  | k + 1, acc => countNatWhereAux f k (if f k then acc + 1 else acc)

/-- Exact count of inputs in `[0,bound)` satisfying a Boolean predicate. -/
def countNatWhere (bound : Nat) (f : Nat → Bool) : Nat :=
  countNatWhereAux f bound 0

/--
Number of graph masks with the distinguished bit `0 → 1` fixed to zero and
with a cut certificate separating `0` from `1`.

A compressed `(m-1)`-bit mask is shifted left once, so the missing distinguished
edge remains exactly bit zero. The list of only `2^(n-2)` relevant separating
cuts is computed once and reused for every graph mask.
-/
def fixed01NoReachCount (n : Nat) : Nat :=
  let m := directedNonloopEdgeCount n
  if 2 ≤ n then
    let cuts := separatingCutEdgeMasks n 0 1
    countNatWhere (2 ^ (m - 1)) fun compressed =>
      let graph := compressed <<< 1
      cuts.any fun outgoing => (graph &&& outgoing) == 0
  else
    0

/-- There are exactly `2^(n-2)` relevant cuts in the small cases used by MF-R011. -/
theorem separatingCut_count_small :
    (separatingCutEdgeMasks 2 0 1).length = 1 ∧
    (separatingCutEdgeMasks 3 0 1).length = 2 ∧
    (separatingCutEdgeMasks 4 0 1).length = 4 ∧
    (separatingCutEdgeMasks 5 0 1).length = 8 := by
  native_decide

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
