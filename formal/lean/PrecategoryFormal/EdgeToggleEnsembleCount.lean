import PrecategoryFormal.EdgeToggleEnsembleSource0
import PrecategoryFormal.EdgeToggleEnsembleSource1
import PrecategoryFormal.EdgeToggleEnsembleSource2
import PrecategoryFormal.EdgeToggleEnsembleSource3
import PrecategoryFormal.EdgeToggleEnsembleSource4
import PrecategoryFormal.EdgeTogglePairing
import PrecategoryFormal.EdgeToggleRelabel

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- The twenty directed non-loop edge positions on five labeled vertices. -/
abbrev DirectedNonloopEdgeFive :=
  {e : Fin 5 × Fin 5 // e.1 ≠ e.2}

/-- There are exactly twenty directed non-loop edge positions on five vertices. -/
theorem directedNonloopEdgeFive_card :
    Fintype.card DirectedNonloopEdgeFive = 20 := by
  native_decide

/--
The compressed `2^19` implementation reproduces the same count at every
non-loop edge position. This is retained as an independent optimization
cross-check; the final ensemble numerator below is based on the direct
`2^20`-mask implementation instead.
-/
theorem fixedEdgeNoReachFastCountFive_all_nonloop
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeNoReachFastCountFive u v = 153600 := by
  rcases fixedEdgeNoReachFastCountFive_source0 with ⟨h01, h02, h03, h04⟩
  rcases fixedEdgeNoReachFastCountFive_source1 with ⟨h10, h12, h13, h14⟩
  rcases fixedEdgeNoReachFastCountFive_source2 with ⟨h20, h21, h23, h24⟩
  rcases fixedEdgeNoReachFastCountFive_source3 with ⟨h30, h31, h32, h34⟩
  rcases fixedEdgeNoReachFastCountFive_source4 with ⟨h40, h41, h42, h43⟩
  fin_cases u <;> fin_cases v
  · exact (huv rfl).elim
  · exact h01
  · exact h02
  · exact h03
  · exact h04
  · exact h10
  · exact (huv rfl).elim
  · exact h12
  · exact h13
  · exact h14
  · exact h20
  · exact h21
  · exact (huv rfl).elim
  · exact h23
  · exact h24
  · exact h30
  · exact h31
  · exact h32
  · exact (huv rfl).elim
  · exact h34
  · exact h40
  · exact h41
  · exact h42
  · exact h43
  · exact (huv rfl).elim

/--
Direct full-mask certificate: every non-loop edge position has exactly 153600
five-vertex masks in which that edge is absent and its target is unreachable
from its source. No compressed-mask insertion is used in these certificates.
-/
theorem fixedEdgeNoReachDirectCountFive_all_nonloop
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeNoReachDirectCountFive u v = 153600 := by
  rcases fixedEdgeNoReachDirectCountFive_source0 with ⟨h01, h02, h03, h04⟩
  rcases fixedEdgeNoReachDirectCountFive_source1 with ⟨h10, h12, h13, h14⟩
  rcases fixedEdgeNoReachDirectCountFive_source2 with ⟨h20, h21, h23, h24⟩
  rcases fixedEdgeNoReachDirectCountFive_source3 with ⟨h30, h31, h32, h34⟩
  rcases fixedEdgeNoReachDirectCountFive_source4 with ⟨h40, h41, h42, h43⟩
  fin_cases u <;> fin_cases v
  · exact (huv rfl).elim
  · exact h01
  · exact h02
  · exact h03
  · exact h04
  · exact h10
  · exact (huv rfl).elim
  · exact h12
  · exact h13
  · exact h14
  · exact h20
  · exact h21
  · exact (huv rfl).elim
  · exact h23
  · exact h24
  · exact h30
  · exact h31
  · exact h32
  · exact (huv rfl).elim
  · exact h34
  · exact h40
  · exact h41
  · exact h42
  · exact h43
  · exact (huv rfl).elim

/--
Total absent-base non-reachability count over the complete list of twenty
five-vertex directed non-loop edge positions. Each summand is a direct count
over all `2^20` graph masks, explicitly filtered by absence of that edge.
-/
def allDirectedEdgeNoReachCountFive : Nat :=
  fixedEdgeNoReachDirectCountFive 0 1 +
  fixedEdgeNoReachDirectCountFive 0 2 +
  fixedEdgeNoReachDirectCountFive 0 3 +
  fixedEdgeNoReachDirectCountFive 0 4 +
  fixedEdgeNoReachDirectCountFive 1 0 +
  fixedEdgeNoReachDirectCountFive 1 2 +
  fixedEdgeNoReachDirectCountFive 1 3 +
  fixedEdgeNoReachDirectCountFive 1 4 +
  fixedEdgeNoReachDirectCountFive 2 0 +
  fixedEdgeNoReachDirectCountFive 2 1 +
  fixedEdgeNoReachDirectCountFive 2 3 +
  fixedEdgeNoReachDirectCountFive 2 4 +
  fixedEdgeNoReachDirectCountFive 3 0 +
  fixedEdgeNoReachDirectCountFive 3 1 +
  fixedEdgeNoReachDirectCountFive 3 2 +
  fixedEdgeNoReachDirectCountFive 3 4 +
  fixedEdgeNoReachDirectCountFive 4 0 +
  fixedEdgeNoReachDirectCountFive 4 1 +
  fixedEdgeNoReachDirectCountFive 4 2 +
  fixedEdgeNoReachDirectCountFive 4 3

/-- Exact direct full-mask total across the twenty edge positions. -/
theorem allDirectedEdgeNoReachCountFive_exact :
    allDirectedEdgeNoReachCountFive = 3072000 := by
  rcases fixedEdgeNoReachDirectCountFive_source0 with ⟨h01, h02, h03, h04⟩
  rcases fixedEdgeNoReachDirectCountFive_source1 with ⟨h10, h12, h13, h14⟩
  rcases fixedEdgeNoReachDirectCountFive_source2 with ⟨h20, h21, h23, h24⟩
  rcases fixedEdgeNoReachDirectCountFive_source3 with ⟨h30, h31, h32, h34⟩
  rcases fixedEdgeNoReachDirectCountFive_source4 with ⟨h40, h41, h42, h43⟩
  rw [
    allDirectedEdgeNoReachCountFive,
    h01, h02, h03, h04,
    h10, h12, h13, h14,
    h20, h21, h23, h24,
    h30, h31, h32, h34,
    h40, h41, h42, h43
  ]

/--
Each absent-base pivotal graph contributes both orientations of the toggle
inside its absent/present pair. The semantic factor-two statement is supplied
by `pairedEdge_toggle_changes_iff`.
-/
def mfR011ChangedGraphEdgePairsFive : Nat :=
  2 * allDirectedEdgeNoReachCountFive

/-- Exact certified numerator of the MF-R011 ordered graph-edge ensemble at n=5. -/
theorem mfR011ChangedGraphEdgePairsFive_exact :
    mfR011ChangedGraphEdgePairsFive = 6144000 := by
  rw [mfR011ChangedGraphEdgePairsFive, allDirectedEdgeNoReachCountFive_exact]

/-- Exact size of the uniform ordered graph-edge mask ensemble at n=5. -/
def mfR011GraphEdgePairsFive : Nat :=
  (2 ^ directedNonloopEdgeCount 5) * directedNonloopEdgeCount 5

theorem mfR011GraphEdgePairsFive_exact :
    mfR011GraphEdgePairsFive = 20971520 := by
  norm_num [mfR011GraphEdgePairsFive, directedNonloopEdgeCount]

/--
Exact cross-multiplied MF-R011 probability identity.

Together with the semantic edge-addition theorem, the direct full-mask
fixed-edge certificates, and the toggle-pairing theorem, this is the arithmetic
endpoint corresponding to `P_5 = 75/256`.
-/
theorem mf_r011_p5_exact :
    mfR011ChangedGraphEdgePairsFive * 256 =
      75 * mfR011GraphEdgePairsFive := by
  rw [mfR011ChangedGraphEdgePairsFive_exact, mfR011GraphEdgePairsFive_exact]

end PrecategoryFormal
