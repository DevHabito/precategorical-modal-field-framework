import PrecategoryFormal.RepresentativeCode

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- A finite directed graph on the five labeled witness vertices. -/
abbrev BoolDigraph := Vertex → Vertex → Bool

/-- The first A8.1 graph: the directed 4-cycle `0→2→3→4→0`, with `1` isolated. -/
def graphA (u v : Vertex) : Bool :=
  decide (
    (u = 0 ∧ v = 2) ∨
    (u = 2 ∧ v = 3) ∨
    (u = 3 ∧ v = 4) ∨
    (u = 4 ∧ v = 0))

/-- The second A8.1 graph: `0→2→3→0` and the 2-cycle `1↔4`. -/
def graphB (u v : Vertex) : Bool :=
  decide (
    (u = 0 ∧ v = 2) ∨
    (u = 2 ∧ v = 3) ∨
    (u = 3 ∧ v = 0) ∨
    (u = 1 ∧ v = 4) ∨
    (u = 4 ∧ v = 1))

/-- Mathematical directed reachability: reflexive-transitive closure of the edge relation. -/
def Reach (g : BoolDigraph) (u v : Vertex) : Prop :=
  Relation.ReflTransGen (fun x y => g x y = true) u v

/-- Two vertices are in the same strongly connected component. -/
def MutualReach (g : BoolDigraph) (u v : Vertex) : Prop :=
  Reach g u v ∧ Reach g v u

/--
A finite bounded-path predicate used only as a certificate producer.
`ReachWithin n g u v` means there is a path from `u` to `v` using at most `n` edges.
For five fixed vertices the recursion explicitly considers every possible final predecessor.
-/
def ReachWithin : Nat → BoolDigraph → Vertex → Vertex → Prop
  | 0, _, u, v => u = v
  | n + 1, g, u, v =>
      ReachWithin n g u v ∨
      (ReachWithin n g u 0 ∧ g 0 v = true) ∨
      (ReachWithin n g u 1 ∧ g 1 v = true) ∨
      (ReachWithin n g u 2 ∧ g 2 v = true) ∨
      (ReachWithin n g u 3 ∧ g 3 v = true) ∨
      (ReachWithin n g u 4 ∧ g 4 v = true)

/-- Every bounded certificate denotes genuine reflexive-transitive reachability. -/
theorem reachWithin_sound (g : BoolDigraph) {n : Nat} {u v : Vertex}
    (h : ReachWithin n g u v) : Reach g u v := by
  induction n generalizing u v with
  | zero =>
      change u = v at h
      subst v
      exact Relation.ReflTransGen.refl
  | succ n ih =>
      change
        ReachWithin n g u v ∨
        (ReachWithin n g u 0 ∧ g 0 v = true) ∨
        (ReachWithin n g u 1 ∧ g 1 v = true) ∨
        (ReachWithin n g u 2 ∧ g 2 v = true) ∨
        (ReachWithin n g u 3 ∧ g 3 v = true) ∨
        (ReachWithin n g u 4 ∧ g 4 v = true) at h
      rcases h with h | h0 | h1 | h2 | h3 | h4
      · exact ih h
      · exact (ih h0.1).tail h0.2
      · exact (ih h1.1).tail h1.2
      · exact (ih h2.1).tail h2.2
      · exact (ih h3.1).tail h3.2
      · exact (ih h4.1).tail h4.2

/-- Every graph-A edge stays inside one proposed SCC block. -/
theorem graphA_edge_preserves_block (u v : Vertex) :
    graphA u v = true → blockMinA u = blockMinA v := by
  fin_cases u <;> fin_cases v <;> native_decide

/-- Every graph-B edge stays inside one proposed SCC block. -/
theorem graphB_edge_preserves_block (u v : Vertex) :
    graphB u v = true → blockMinB u = blockMinB v := by
  fin_cases u <;> fin_cases v <;> native_decide

/-- Any graph-A path stays inside one proposed SCC block. -/
theorem graphA_reach_preserves_block {u v : Vertex} (h : Reach graphA u v) :
    blockMinA u = blockMinA v := by
  induction h with
  | refl => rfl
  | tail hreach hedge ih =>
      exact ih.trans (graphA_edge_preserves_block _ _ hedge)

/-- Any graph-B path stays inside one proposed SCC block. -/
theorem graphB_reach_preserves_block {u v : Vertex} (h : Reach graphB u v) :
    blockMinB u = blockMinB v := by
  induction h with
  | refl => rfl
  | tail hreach hedge ih =>
      exact ih.trans (graphB_edge_preserves_block _ _ hedge)

/--
Independent finite certificate: equal graph-A block minima always have a path
of at most four edges in the original graph.
-/
theorem graphA_same_block_reachWithin4 (u v : Vertex) :
    blockMinA u = blockMinA v → ReachWithin 4 graphA u v := by
  fin_cases u <;> fin_cases v <;> simp [ReachWithin, graphA, blockMinA]

/-- Equal graph-B block minima always have a path of at most four edges. -/
theorem graphB_same_block_reachWithin4 (u v : Vertex) :
    blockMinB u = blockMinB v → ReachWithin 4 graphB u v := by
  fin_cases u <;> fin_cases v <;> simp [ReachWithin, graphB, blockMinB]

/-- In graph A, the declared block map agrees exactly with SCC equivalence. -/
theorem graphA_mutualReach_iff_same_block (u v : Vertex) :
    MutualReach graphA u v ↔ blockMinA u = blockMinA v := by
  constructor
  · intro h
    exact graphA_reach_preserves_block h.1
  · intro h
    constructor
    · exact reachWithin_sound graphA (graphA_same_block_reachWithin4 u v h)
    · exact reachWithin_sound graphA (graphA_same_block_reachWithin4 v u h.symm)

/-- In graph B, the declared block map agrees exactly with SCC equivalence. -/
theorem graphB_mutualReach_iff_same_block (u v : Vertex) :
    MutualReach graphB u v ↔ blockMinB u = blockMinB v := by
  constructor
  · intro h
    exact graphB_reach_preserves_block h.1
  · intro h
    constructor
    · exact reachWithin_sound graphB (graphB_same_block_reachWithin4 u v h)
    · exact reachWithin_sound graphB (graphB_same_block_reachWithin4 v u h.symm)

/-- The graph-A block representative is mutually reachable with its vertex. -/
theorem graphA_rep_in_scc (v : Vertex) : MutualReach graphA (blockMinA v) v := by
  apply (graphA_mutualReach_iff_same_block _ _).2
  exact (blockMinA_valid v).1

/-- The graph-B block representative is mutually reachable with its vertex. -/
theorem graphB_rep_in_scc (v : Vertex) : MutualReach graphB (blockMinB v) v := by
  apply (graphB_mutualReach_iff_same_block _ _).2
  exact (blockMinB_valid v).1

/-- The graph-A representative is the minimum labeled vertex in its SCC. -/
theorem graphA_rep_is_minimum (v u : Vertex) (h : MutualReach graphA u v) :
    (blockMinA v).val ≤ u.val := by
  have hblocks : blockMinA u = blockMinA v :=
    (graphA_mutualReach_iff_same_block u v).1 h
  have hmin := (blockMinA_valid u).2
  simpa [hblocks] using hmin

/-- The graph-B representative is the minimum labeled vertex in its SCC. -/
theorem graphB_rep_is_minimum (v u : Vertex) (h : MutualReach graphB u v) :
    (blockMinB v).val ≤ u.val := by
  have hblocks : blockMinB u = blockMinB v :=
    (graphB_mutualReach_iff_same_block u v).1 h
  have hmin := (blockMinB_valid u).2
  simpa [hblocks] using hmin

/-- Distinct SCCs in graph A have no directed reachability between them. -/
theorem graphA_no_cross_reach {u v : Vertex}
    (hblocks : blockMinA u ≠ blockMinA v) : ¬ Reach graphA u v := by
  intro hreach
  exact hblocks (graphA_reach_preserves_block hreach)

/-- Distinct SCCs in graph B have no directed reachability between them. -/
theorem graphB_no_cross_reach {u v : Vertex}
    (hblocks : blockMinB u ≠ blockMinB v) : ¬ Reach graphB u v := by
  intro hreach
  exact hblocks (graphB_reach_preserves_block hreach)

/-- A candidate block-minimum map exactly describes SCCs and their minimum labels. -/
def ExactSCCMinimumMap (g : BoolDigraph) (blockMin : Vertex → Vertex) : Prop :=
  (∀ u v, MutualReach g u v ↔ blockMin u = blockMin v) ∧
  (∀ v, MutualReach g (blockMin v) v) ∧
  (∀ v u, MutualReach g u v → (blockMin v).val ≤ u.val)

/-- The quotient is an antichain when distinct SCC representatives never reach one another. -/
def QuotientAntichain (g : BoolDigraph) (blockMin : Vertex → Vertex) : Prop :=
  ∀ u v, blockMin u = u → blockMin v = v → u ≠ v → ¬ Reach g u v

/--
The graph semantically realizes a condensation structure whose strict quotient-order
matrix is empty, hence whose lower 25 historical code bits are zero.
-/
def GraphRealizesAntichainCondensation
    (g : BoolDigraph) (q : CondensationStructure) : Prop :=
  ExactSCCMinimumMap g q.blockMin ∧
  QuotientAntichain g q.blockMin ∧
  q.quotientOrderCode = 0

theorem graphA_exactSCCMinimumMap : ExactSCCMinimumMap graphA blockMinA := by
  refine ⟨graphA_mutualReach_iff_same_block, graphA_rep_in_scc, ?_⟩
  intro v u h
  exact graphA_rep_is_minimum v u h

theorem graphB_exactSCCMinimumMap : ExactSCCMinimumMap graphB blockMinB := by
  refine ⟨graphB_mutualReach_iff_same_block, graphB_rep_in_scc, ?_⟩
  intro v u h
  exact graphB_rep_is_minimum v u h

theorem graphA_quotient_antichain : QuotientAntichain graphA blockMinA := by
  intro u v hu hv huv hreach
  apply huv
  calc
    u = blockMinA u := hu.symm
    _ = blockMinA v := graphA_reach_preserves_block hreach
    _ = v := hv

theorem graphB_quotient_antichain : QuotientAntichain graphB blockMinB := by
  intro u v hu hv huv hreach
  apply huv
  calc
    u = blockMinB u := hu.symm
    _ = blockMinB v := graphB_reach_preserves_block hreach
    _ = v := hv

theorem graphA_realizes_witnessA :
    GraphRealizesAntichainCondensation graphA witnessA := by
  refine ⟨?_, ?_, rfl⟩
  · simpa [witnessA] using graphA_exactSCCMinimumMap
  · simpa [witnessA] using graphA_quotient_antichain

theorem graphB_realizes_witnessB :
    GraphRealizesAntichainCondensation graphB witnessB := by
  refine ⟨?_, ?_, rfl⟩
  · simpa [witnessB] using graphB_exactSCCMinimumMap
  · simpa [witnessB] using graphB_quotient_antichain

/--
Graph-level MF-R009 bridge: the two explicit A8.1 directed graphs induce the
minimum-block maps used by the representative-code collision.
-/
theorem mf_r009_graph_to_scc_bridge :
    (∀ u v, MutualReach graphA u v ↔ blockMinA u = blockMinA v) ∧
    (∀ u v, MutualReach graphB u v ↔ blockMinB u = blockMinB v) := by
  exact ⟨graphA_mutualReach_iff_same_block, graphB_mutualReach_iff_same_block⟩

/--
End-to-end explicit witness theorem for MF-R009.

The original directed graphs realize two distinct condensation structures;
each strict quotient is an antichain, and both structures receive exactly the
same historical representative code `100663296`.
-/
theorem mf_r009_graph_level_code_collision :
    GraphRealizesAntichainCondensation graphA witnessA ∧
    GraphRealizesAntichainCondensation graphB witnessB ∧
    witnessA ≠ witnessB ∧
    historicalRepresentativeCode witnessA = 100663296 ∧
    historicalRepresentativeCode witnessB = 100663296 := by
  exact ⟨
    graphA_realizes_witnessA,
    graphB_realizes_witnessB,
    witnesses_distinct,
    witnessA_code,
    witnessB_code
  ⟩

end PrecategoryFormal
