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

/--
Sum of the exact fixed-absent-edge non-reachability counts over all twenty
directed non-loop edge positions on five labeled vertices.
-/
def allDirectedEdgeNoReachCountFive : Nat :=
  fixedEdgeNoReachFastCountFive 0 1 +
  fixedEdgeNoReachFastCountFive 0 2 +
  fixedEdgeNoReachFastCountFive 0 3 +
  fixedEdgeNoReachFastCountFive 0 4 +
  fixedEdgeNoReachFastCountFive 1 0 +
  fixedEdgeNoReachFastCountFive 1 2 +
  fixedEdgeNoReachFastCountFive 1 3 +
  fixedEdgeNoReachFastCountFive 1 4 +
  fixedEdgeNoReachFastCountFive 2 0 +
  fixedEdgeNoReachFastCountFive 2 1 +
  fixedEdgeNoReachFastCountFive 2 3 +
  fixedEdgeNoReachFastCountFive 2 4 +
  fixedEdgeNoReachFastCountFive 3 0 +
  fixedEdgeNoReachFastCountFive 3 1 +
  fixedEdgeNoReachFastCountFive 3 2 +
  fixedEdgeNoReachFastCountFive 3 4 +
  fixedEdgeNoReachFastCountFive 4 0 +
  fixedEdgeNoReachFastCountFive 4 1 +
  fixedEdgeNoReachFastCountFive 4 2 +
  fixedEdgeNoReachFastCountFive 4 3

/--
Full five-vertex fixed-edge checksum.

The twenty expensive finite computations are proved in five independent source
shards.  This theorem only composes those kernel-checked results.
-/
theorem allDirectedEdgeNoReachCountFive_exact :
    allDirectedEdgeNoReachCountFive = 3072000 := by
  rcases fixedEdgeNoReachFastCountFive_source0 with ⟨h01, h02, h03, h04⟩
  rcases fixedEdgeNoReachFastCountFive_source1 with ⟨h10, h12, h13, h14⟩
  rcases fixedEdgeNoReachFastCountFive_source2 with ⟨h20, h21, h23, h24⟩
  rcases fixedEdgeNoReachFastCountFive_source3 with ⟨h30, h31, h32, h34⟩
  rcases fixedEdgeNoReachFastCountFive_source4 with ⟨h40, h41, h42, h43⟩
  rw [
    allDirectedEdgeNoReachCountFive,
    h01, h02, h03, h04,
    h10, h12, h13, h14,
    h20, h21, h23, h24,
    h30, h31, h32, h34,
    h40, h41, h42, h43
  ]
  norm_num

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
Exact cross-multiplied probability identity. This avoids introducing any
floating-point or rational-normalization layer into the kernel statement.
-/
theorem mf_r011_p5_exact :
    mfR011ChangedGraphEdgePairsFive * 256 =
      75 * mfR011GraphEdgePairsFive := by
  rw [mfR011ChangedGraphEdgePairsFive_exact, mfR011GraphEdgePairsFive_exact]
  norm_num

end PrecategoryFormal
