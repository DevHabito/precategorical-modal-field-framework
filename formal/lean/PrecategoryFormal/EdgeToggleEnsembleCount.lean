import PrecategoryFormal.EdgeToggleEnsembleSource0
import PrecategoryFormal.EdgeToggleEnsembleSource1
import PrecategoryFormal.EdgeToggleEnsembleSource2
import PrecategoryFormal.EdgeToggleEnsembleSource3
import PrecategoryFormal.EdgeToggleEnsembleSource4

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Total absent-base non-reachability count over the complete list of twenty
five-vertex directed non-loop edge positions. Each summand is a direct count
over all `2^20` graph masks, explicitly filtered by absence of that edge.

The source-sharded theorems imported above certify every one of the twenty
summands independently. No compressed-mask insertion theorem is needed here.
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

/-- Exact direct full-mask total across all twenty directed non-loop edges. -/
theorem allDirectedEdgeNoReachCountFive_exact :
    allDirectedEdgeNoReachCountFive = 3072000 := by
  rcases fixedEdgeNoReachDirectCountFive_source0 with ⟨h01, h02, h03, h04⟩
  rcases fixedEdgeNoReachDirectCountFive_source1 with ⟨h10, h12, h13, h14⟩
  rcases fixedEdgeNoReachDirectCountFive_source2 with ⟨h20, h21, h23, h24⟩
  rcases fixedEdgeNoReachDirectCountFive_source3 with ⟨h30, h31, h32, h34⟩
  rcases fixedEdgeNoReachDirectCountFive_source4 with ⟨h40, h41, h42, h43⟩
  norm_num [
    allDirectedEdgeNoReachCountFive,
    h01, h02, h03, h04,
    h10, h12, h13, h14,
    h20, h21, h23, h24,
    h30, h31, h32, h34,
    h40, h41, h42, h43
  ]

/--
Each absent-base pivotal graph has a unique present-edge toggle mate. Since
mask toggling is involutive and both ordered directions have the same
reachability-change status, the ordered graph-edge numerator is twice the
absent-base count.
-/
def mfR011ChangedGraphEdgePairsFive : Nat :=
  2 * allDirectedEdgeNoReachCountFive

/-- Exact certified numerator of the MF-R011 ordered graph-edge ensemble at n=5. -/
theorem mfR011ChangedGraphEdgePairsFive_exact :
    mfR011ChangedGraphEdgePairsFive = 6144000 := by
  norm_num [mfR011ChangedGraphEdgePairsFive, allDirectedEdgeNoReachCountFive_exact]

/-- Exact size of the uniform ordered graph-edge mask ensemble at n=5. -/
def mfR011GraphEdgePairsFive : Nat :=
  (2 ^ directedNonloopEdgeCount 5) * directedNonloopEdgeCount 5

theorem mfR011GraphEdgePairsFive_exact :
    mfR011GraphEdgePairsFive = 20971520 := by
  norm_num [mfR011GraphEdgePairsFive, directedNonloopEdgeCount]

/--
Exact cross-multiplied MF-R011 probability identity corresponding to
`P_5 = 75/256`.
-/
theorem mf_r011_p5_exact :
    mfR011ChangedGraphEdgePairsFive * 256 =
      75 * mfR011GraphEdgePairsFive := by
  rw [mfR011ChangedGraphEdgePairsFive_exact, mfR011GraphEdgePairsFive_exact]

end PrecategoryFormal
