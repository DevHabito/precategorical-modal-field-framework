import PrecategoryFormal.GraphSCCBridge

namespace PrecategoryFormal.PhysicalBridge

/--
The explicit directed cycle already formalized in graphA cannot carry a scalar
rank that increases strictly along every directed edge.

This is the finite algebraic core of the pregeometric acyclicity gate. It does
not claim that every physical notion of time must be a scalar rank.
-/
theorem graphA_cycle_forbids_strict_edge_time_rank
    (tau : Vertex → ℚ) :
    ¬ (∀ u v : Vertex, graphA u v = true → tau u < tau v) := by
  intro h
  have h02 : tau (0 : Vertex) < tau (2 : Vertex) := by
    exact h 0 2 (by native_decide)
  have h23 : tau (2 : Vertex) < tau (3 : Vertex) := by
    exact h 2 3 (by native_decide)
  have h34 : tau (3 : Vertex) < tau (4 : Vertex) := by
    exact h 3 4 (by native_decide)
  have h40 : tau (4 : Vertex) < tau (0 : Vertex) := by
    exact h 4 0 (by native_decide)
  linarith

/--
The four vertices of graphA's directed cycle belong to one SCC. Thus any
SCC-level quotient necessarily identifies distinct vertices from the cycle.
-/
theorem graphA_cycle_is_collapsed_by_scc :
    MutualReach graphA (0 : Vertex) (2 : Vertex) ∧
    MutualReach graphA (2 : Vertex) (3 : Vertex) ∧
    MutualReach graphA (3 : Vertex) (4 : Vertex) := by
  constructor
  · exact (graphA_mutualReach_iff_same_block 0 2).2 (by native_decide)
  constructor
  · exact (graphA_mutualReach_iff_same_block 2 3).2 (by native_decide)
  · exact (graphA_mutualReach_iff_same_block 3 4).2 (by native_decide)

end PrecategoryFormal.PhysicalBridge
