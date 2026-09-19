import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

open scoped BigOperators

/-- Number of directed non-loop edge coordinates on `n` labeled vertices. -/
def edgeCount (n : Nat) : Nat := n * (n - 1)

/-- Number of loopless labeled digraphs in the declared bit-mask ensemble. -/
def graphCount (n : Nat) : Nat := 2 ^ edgeCount n

/-- A loopless labeled digraph encoded by one bit per directed non-loop edge. -/
abbrev GraphMask (n : Nat) := Fin (graphCount n)

/--
Index of the directed edge `u → v` in row-major order with the diagonal removed.
This definition is used only when `u,v < n` and `u ≠ v`.
-/
def edgeIndex (n u v : Nat) : Nat :=
  u * (n - 1) + if v < u then v else v - 1

/-- Boolean adjacency predicate for the declared loopless bit-mask graph. -/
def hasEdge {n : Nat} (g : GraphMask n) (u v : Nat) : Bool :=
  if _h : u < n ∧ v < n ∧ u ≠ v then
    g.val.testBit (edgeIndex n u v)
  else
    false

/-- Reflexive adjacency row before transitive closure, represented as a bitset. -/
def initialReachRow {n : Nat} (g : GraphMask n) (u : Nat) : Nat :=
  (List.range n).foldl
    (fun row v => if hasEdge g u v then row ||| (1 <<< v) else row)
    (1 <<< u)

/-- Initial reflexive reachability matrix, represented by one bitset row per vertex. -/
def initialReachRows {n : Nat} (g : GraphMask n) : Array Nat :=
  (List.range n).foldl (fun rows u => rows.push (initialReachRow g u)) #[]

/-- One in-place Warshall step using vertex `k` as an allowed intermediate. -/
def warshallStep (n k : Nat) (rows : Array Nat) : Array Nat :=
  let rowK := rows[k]!
  (List.range n).foldl
    (fun acc u =>
      let rowU := acc[u]!
      if rowU.testBit k then acc.set! u (rowU ||| rowK) else acc)
    rows

/-- Executable reflexive-transitive closure of the declared graph. -/
def reachRows {n : Nat} (g : GraphMask n) : Array Nat :=
  (List.range n).foldl (fun rows k => warshallStep n k rows) (initialReachRows g)

/-- Pack the full reflexive reachability matrix into one natural-number code. -/
def reachCode {n : Nat} (g : GraphMask n) : Nat :=
  let rows := reachRows g
  (List.range n).foldl
    (fun code u => code ||| ((rows[u]!) <<< (u * n)))
    0

/-- Toggle exactly one directed non-loop edge coordinate. -/
def toggleMask {n : Nat} (g : GraphMask n) (e : Fin (edgeCount n)) : GraphMask n :=
  ⟨g.val ^^^ (1 <<< e.val), by
    apply Nat.xor_lt_two_pow g.isLt
    rw [Nat.one_shiftLeft]
    exact Nat.pow_lt_pow_of_lt (by decide) e.isLt⟩

/-- Cache all reachability codes once before the edge-toggle scan. -/
def reachCodeTable (n : Nat) : Array Nat :=
  Array.ofFn (fun g : GraphMask n => reachCode g)

/-- Indicator that one ordered graph-edge pair changes the full reachability code. -/
def edgeToggleChanges
    {n : Nat} (table : Array Nat) (g : GraphMask n) (e : Fin (edgeCount n)) : Nat :=
  if table[g.val]! = table[(toggleMask g e).val]! then 0 else 1

/-- Exact number of ordered `(graph, directed-edge)` pairs that change reachability. -/
def changedPairCount (n : Nat) : Nat :=
  let table := reachCodeTable n
  ∑ g : GraphMask n, ∑ e : Fin (edgeCount n), edgeToggleChanges table g e

/-- Independent Lean finite computation for `n = 2`. -/
theorem changedPairCount_two : changedPairCount 2 = 8 := by
  native_decide

/-- Independent Lean finite computation for `n = 3`. -/
theorem changedPairCount_three : changedPairCount 3 = 288 := by
  native_decide

/-- Independent Lean finite computation for `n = 4`. -/
theorem changedPairCount_four : changedPairCount 4 = 24576 := by
  native_decide

/--
Independent Lean finite computation for the MF-R011 numerator at `n = 5`.
The historical Python result is not imported into this definition or proof.
-/
theorem changedPairCount_five : changedPairCount 5 = 6144000 := by
  native_decide

/-- The declared ordered-pair ensemble has size `8` for `n = 2`. -/
theorem orderedPairCount_two : edgeCount 2 * graphCount 2 = 8 := by
  native_decide

/-- The declared ordered-pair ensemble has size `384` for `n = 3`. -/
theorem orderedPairCount_three : edgeCount 3 * graphCount 3 = 384 := by
  native_decide

/-- The declared ordered-pair ensemble has size `49152` for `n = 4`. -/
theorem orderedPairCount_four : edgeCount 4 * graphCount 4 = 49152 := by
  native_decide

/-- The declared ordered-pair ensemble has size `20,971,520` for `n = 5`. -/
theorem orderedPairCount_five : edgeCount 5 * graphCount 5 = 20971520 := by
  native_decide

/-- The exact `n = 2` ratio is `1`. -/
theorem edgeToggleProbability_two_crossmul :
    changedPairCount 2 = edgeCount 2 * graphCount 2 := by
  rw [changedPairCount_two, orderedPairCount_two]

/-- The exact `n = 3` ratio is `3/4`. -/
theorem edgeToggleProbability_three_crossmul :
    changedPairCount 3 * 4 = edgeCount 3 * graphCount 3 * 3 := by
  rw [changedPairCount_three, orderedPairCount_three]

/-- The exact `n = 4` ratio is `1/2`. -/
theorem edgeToggleProbability_four_crossmul :
    changedPairCount 4 * 2 = edgeCount 4 * graphCount 4 := by
  rw [changedPairCount_four, orderedPairCount_four]

/-- The `n = 5` exact ratio reduces to `75/256`. -/
theorem edgeToggleProbability_five_crossmul :
    changedPairCount 5 * 256 = edgeCount 5 * graphCount 5 * 75 := by
  rw [changedPairCount_five, orderedPairCount_five]

end PrecategoryFormal
