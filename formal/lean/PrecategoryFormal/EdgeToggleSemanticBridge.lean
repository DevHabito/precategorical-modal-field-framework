import PrecategoryFormal.GraphSCCBridge
import PrecategoryFormal.EdgeToggleSensitivity

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Interpret an MF-R011 five-vertex bit mask as an ordinary Boolean digraph. -/
def maskGraph5 (g : GraphMask 5) : BoolDigraph :=
  fun u v => hasEdge g u.val v.val

/-- Reflexivity plus the original edge relation. -/
def referenceInitial5 (g : GraphMask 5) : BoolDigraph :=
  fun u v => decide (u = v) || maskGraph5 g u v

/-- One semantic Floyd-Warshall relation update through intermediate vertex `k`. -/
def referenceStep5 (r : BoolDigraph) (k : Vertex) : BoolDigraph :=
  fun u v => r u v || (r u k && r k v)

/--
A definitionally independent five-step reference closure. Unlike `reachRows`,
this presentation is a direct relation transformer and is convenient for proofs.
-/
def referenceClosure5 (g : GraphMask 5) : BoolDigraph :=
  referenceStep5
    (referenceStep5
      (referenceStep5
        (referenceStep5
          (referenceStep5 (referenceInitial5 g) 0) 1) 2) 3) 4

/-- Every `true` entry of a Boolean relation denotes genuine mathematical reachability. -/
def RelationSound5 (g : GraphMask 5) (r : BoolDigraph) : Prop :=
  ∀ u v, r u v = true → Reach (maskGraph5 g) u v

/-- A Boolean relation is closed under one selected intermediate vertex. -/
def RelationClosedAt5 (r : BoolDigraph) (k : Vertex) : Prop :=
  ∀ u v, r u k = true → r k v = true → r u v = true

theorem referenceInitial5_sound (g : GraphMask 5) :
    RelationSound5 g (referenceInitial5 g) := by
  intro u v h
  have h' : decide (u = v) = true ∨ maskGraph5 g u v = true := by
    simpa [referenceInitial5] using h
  rcases h' with huv | hedge
  · have huv' : u = v := by simpa using huv
    subst v
    exact Relation.ReflTransGen.refl
  · exact Relation.ReflTransGen.single hedge

/-- Floyd-Warshall's elementary update preserves reachability soundness. -/
theorem referenceStep5_sound
    (g : GraphMask 5) (r : BoolDigraph) (k : Vertex)
    (h : RelationSound5 g r) : RelationSound5 g (referenceStep5 r k) := by
  intro u v huv
  have huv' : r u v = true ∨ (r u k = true ∧ r k v = true) := by
    simpa [referenceStep5] using huv
  rcases huv' with direct | via
  · exact h u v direct
  · exact (h u k via.1).trans (h k v via.2)

/-- The direct five-step reference closure never invents a path. -/
theorem referenceClosure5_sound (g : GraphMask 5) :
    RelationSound5 g (referenceClosure5 g) := by
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  exact referenceInitial5_sound g

/-- Every Floyd-Warshall step contains the previous relation. -/
theorem referenceStep5_contains
    (r : BoolDigraph) (k u v : Vertex) (h : r u v = true) :
    referenceStep5 r k u v = true := by
  simp [referenceStep5, h]

/-- One Floyd-Warshall step is closed under the intermediate vertex it adds. -/
theorem referenceStep5_closedAt_self (r : BoolDigraph) (k : Vertex) :
    RelationClosedAt5 (referenceStep5 r k) k := by
  intro u v huk hkv
  have huk' : r u k = true := by
    have hcases : r u k = true ∨ (r u k = true ∧ r k k = true) := by
      simpa [referenceStep5] using huk
    exact hcases.elim id And.left
  have hkv' : r k v = true := by
    have hcases : r k v = true ∨ (r k k = true ∧ r k v = true) := by
      simpa [referenceStep5] using hkv
    exact hcases.elim id And.right
  simp [referenceStep5, huk', hkv']

/-- Adding a new intermediate preserves closure under every old intermediate. -/
theorem referenceStep5_preserves_closedAt
    (r : BoolDigraph) (j k : Vertex) (hclosed : RelationClosedAt5 r j) :
    RelationClosedAt5 (referenceStep5 r k) j := by
  intro u v huj hjv
  have hujCases : r u j = true ∨ (r u k = true ∧ r k j = true) := by
    simpa [referenceStep5] using huj
  have hjvCases : r j v = true ∨ (r j k = true ∧ r k v = true) := by
    simpa [referenceStep5] using hjv
  rcases hujCases with huj0 | ⟨huk, hkj⟩
  · rcases hjvCases with hjv0 | ⟨hjk, hkv⟩
    · exact referenceStep5_contains r k u v (hclosed u v huj0 hjv0)
    · have huk' : r u k = true := hclosed u k huj0 hjk
      simp [referenceStep5, huk', hkv]
  · rcases hjvCases with hjv0 | ⟨_hjk, hkv⟩
    · have hkv' : r k v = true := hclosed k v hkj hjv0
      simp [referenceStep5, huk, hkv']
    · simp [referenceStep5, huk, hkv]

/-- The initial relation is reflexive. -/
theorem referenceInitial5_reflexive (g : GraphMask 5) :
    ∀ u : Vertex, referenceInitial5 g u u = true := by
  intro u
  simp [referenceInitial5]

/-- Floyd-Warshall preserves reflexivity. -/
theorem referenceStep5_preserves_reflexive
    (r : BoolDigraph) (k : Vertex) (href : ∀ u : Vertex, r u u = true) :
    ∀ u : Vertex, referenceStep5 r k u u = true := by
  intro u
  exact referenceStep5_contains r k u u (href u)

/-- The final reference closure is reflexive. -/
theorem referenceClosure5_reflexive (g : GraphMask 5) :
    ∀ u : Vertex, referenceClosure5 g u u = true := by
  unfold referenceClosure5
  apply referenceStep5_preserves_reflexive
  apply referenceStep5_preserves_reflexive
  apply referenceStep5_preserves_reflexive
  apply referenceStep5_preserves_reflexive
  apply referenceStep5_preserves_reflexive
  exact referenceInitial5_reflexive g

/-- The initial relation contains every original directed edge. -/
theorem referenceInitial5_contains_edges (g : GraphMask 5) :
    ∀ u v : Vertex,
      maskGraph5 g u v = true → referenceInitial5 g u v = true := by
  intro u v h
  simp [referenceInitial5, h]

/-- Floyd-Warshall preserves containment of the original edge relation. -/
theorem referenceStep5_preserves_edges
    (g : GraphMask 5) (r : BoolDigraph) (k : Vertex)
    (hedges : ∀ u v : Vertex, maskGraph5 g u v = true → r u v = true) :
    ∀ u v : Vertex,
      maskGraph5 g u v = true → referenceStep5 r k u v = true := by
  intro u v h
  exact referenceStep5_contains r k u v (hedges u v h)

/-- The final reference closure contains every original directed edge. -/
theorem referenceClosure5_contains_edges (g : GraphMask 5) :
    ∀ u v : Vertex,
      maskGraph5 g u v = true → referenceClosure5 g u v = true := by
  unfold referenceClosure5
  apply referenceStep5_preserves_edges g
  apply referenceStep5_preserves_edges g
  apply referenceStep5_preserves_edges g
  apply referenceStep5_preserves_edges g
  apply referenceStep5_preserves_edges g
  exact referenceInitial5_contains_edges g

/-- The final closure remains closed under vertex `0`. -/
theorem referenceClosure5_closedAt_zero (g : GraphMask 5) :
    RelationClosedAt5 (referenceClosure5 g) 0 := by
  unfold referenceClosure5
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  exact referenceStep5_closedAt_self (referenceInitial5 g) 0

/-- The final closure remains closed under vertex `1`. -/
theorem referenceClosure5_closedAt_one (g : GraphMask 5) :
    RelationClosedAt5 (referenceClosure5 g) 1 := by
  unfold referenceClosure5
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  exact referenceStep5_closedAt_self
    (referenceStep5 (referenceInitial5 g) 0) 1

/-- The final closure remains closed under vertex `2`. -/
theorem referenceClosure5_closedAt_two (g : GraphMask 5) :
    RelationClosedAt5 (referenceClosure5 g) 2 := by
  unfold referenceClosure5
  apply referenceStep5_preserves_closedAt
  apply referenceStep5_preserves_closedAt
  exact referenceStep5_closedAt_self
    (referenceStep5 (referenceStep5 (referenceInitial5 g) 0) 1) 2

/-- The final closure remains closed under vertex `3`. -/
theorem referenceClosure5_closedAt_three (g : GraphMask 5) :
    RelationClosedAt5 (referenceClosure5 g) 3 := by
  unfold referenceClosure5
  apply referenceStep5_preserves_closedAt
  exact referenceStep5_closedAt_self
    (referenceStep5
      (referenceStep5 (referenceStep5 (referenceInitial5 g) 0) 1) 2) 3

/-- The final closure is closed under vertex `4`. -/
theorem referenceClosure5_closedAt_four (g : GraphMask 5) :
    RelationClosedAt5 (referenceClosure5 g) 4 := by
  unfold referenceClosure5
  exact referenceStep5_closedAt_self
    (referenceStep5
      (referenceStep5
        (referenceStep5 (referenceStep5 (referenceInitial5 g) 0) 1) 2) 3) 4

/-- Closure under each of the five possible middle vertices gives transitivity. -/
theorem referenceClosure5_transitive (g : GraphMask 5) :
    ∀ u v w : Vertex,
      referenceClosure5 g u v = true →
      referenceClosure5 g v w = true →
      referenceClosure5 g u w = true := by
  intro u v w huv hvw
  fin_cases v
  · exact referenceClosure5_closedAt_zero g u w huv hvw
  · exact referenceClosure5_closedAt_one g u w huv hvw
  · exact referenceClosure5_closedAt_two g u w huv hvw
  · exact referenceClosure5_closedAt_three g u w huv hvw
  · exact referenceClosure5_closedAt_four g u w huv hvw

/--
The five-step reference closure is reflexive, contains every original edge,
and is transitive. This theorem is symbolic; it does not enumerate the `2^20`
graph masks.
-/
def ReferenceClosureLaws5 (g : GraphMask 5) : Prop :=
  let r := referenceClosure5 g
  (∀ u, r u u = true) ∧
  (∀ u v, maskGraph5 g u v = true → r u v = true) ∧
  (∀ u v w, r u v = true → r v w = true → r u w = true)

theorem referenceClosureLaws5_all :
    ∀ g : GraphMask 5, ReferenceClosureLaws5 g := by
  intro g
  exact ⟨referenceClosure5_reflexive g,
    referenceClosure5_contains_edges g,
    referenceClosure5_transitive g⟩

/-- Every mathematical path is present in the five-step reference closure. -/
theorem referenceClosure5_complete
    (g : GraphMask 5) {u v : Vertex} (h : Reach (maskGraph5 g) u v) :
    referenceClosure5 g u v = true := by
  have laws := referenceClosureLaws5_all g
  induction h with
  | refl =>
      exact laws.1 _
  | tail hreach hedge ih =>
      exact laws.2.2 _ _ _ ih (laws.2.1 _ _ hedge)

/-- The independent reference closure is exactly `Relation.ReflTransGen`. -/
theorem referenceClosure5_eq_true_iff_reach
    (g : GraphMask 5) (u v : Vertex) :
    referenceClosure5 g u v = true ↔ Reach (maskGraph5 g) u v := by
  constructor
  · exact referenceClosure5_sound g u v
  · exact referenceClosure5_complete g

/--
Audit the compact `reachCode` used in the MF-R011 enumerator against the
independent semantic reference relation, cell by cell, and certify its 25-bit bound.
This is the one remaining exhaustive all-graph semantic audit.
-/
def ReachCodeSemanticAudit5 (g : GraphMask 5) : Prop :=
  let code := reachCode g
  let r := referenceClosure5 g
  code < 2 ^ 25 ∧
    ∀ u v : Vertex, code.testBit (u.val * 5 + v.val) = r u v

private instance reachCodeSemanticAudit5Decidable (g : GraphMask 5) :
    Decidable (ReachCodeSemanticAudit5 g) := by
  unfold ReachCodeSemanticAudit5
  letI : DecidablePred (fun u : Vertex =>
      ∀ v : Vertex,
        (reachCode g).testBit (u.val * 5 + v.val) = referenceClosure5 g u v) :=
    fun _ => inferInstance
  infer_instance

/-- Exact all-graph bridge between the compact implementation and reference closure. -/
theorem reachCodeSemanticAudit5_all :
    ∀ g : GraphMask 5, ReachCodeSemanticAudit5 g := by
  native_decide

/-- Every low reachability-code bit has the intended mathematical meaning. -/
theorem reachCode_testBit_iff_reach
    (g : GraphMask 5) (u v : Vertex) :
    (reachCode g).testBit (u.val * 5 + v.val) = true ↔
      Reach (maskGraph5 g) u v := by
  have hcell := (reachCodeSemanticAudit5_all g).2 u v
  rw [hcell]
  exact referenceClosure5_eq_true_iff_reach g u v

/-- Two compact codes are equal only if the full mathematical reachability relations agree. -/
theorem reachCode_eq_implies_sameReachability5
    {g h : GraphMask 5} (hc : reachCode g = reachCode h) :
    ∀ u v : Vertex,
      Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v := by
  intro u v
  constructor
  · intro hreach
    apply (reachCode_testBit_iff_reach h u v).1
    rw [← hc]
    exact (reachCode_testBit_iff_reach g u v).2 hreach
  · intro hreach
    apply (reachCode_testBit_iff_reach g u v).1
    rw [hc]
    exact (reachCode_testBit_iff_reach h u v).2 hreach

/-- If the full mathematical reachability relations agree, their compact codes agree. -/
theorem sameReachability5_implies_reachCode_eq
    {g h : GraphMask 5}
    (hsame : ∀ u v : Vertex,
      Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v) :
    reachCode g = reachCode h := by
  apply Nat.eq_of_testBit_eq
  intro i
  by_cases hi : i < 25
  · let u : Vertex := ⟨i / 5, by omega⟩
    let v : Vertex := ⟨i % 5, by omega⟩
    have hidx : u.val * 5 + v.val = i := by
      calc
        u.val * 5 + v.val = 5 * (i / 5) + i % 5 := by
          simp [u, v, Nat.mul_comm]
        _ = i := Nat.div_add_mod i 5
    rw [← hidx, Bool.eq_iff_iff,
      reachCode_testBit_iff_reach,
      reachCode_testBit_iff_reach]
    exact hsame u v
  · have h25i : 25 ≤ i := Nat.le_of_not_gt hi
    have hg25 := (reachCodeSemanticAudit5_all g).1
    have hh25 := (reachCodeSemanticAudit5_all h).1
    have hp : 2 ^ 25 ≤ 2 ^ i := Nat.pow_le_pow_right (by decide) h25i
    have hg : reachCode g < 2 ^ i := Nat.lt_of_lt_of_le hg25 hp
    have hh : reachCode h < 2 ^ i := Nat.lt_of_lt_of_le hh25 hp
    rw [Nat.testBit_lt_two_pow hg, Nat.testBit_lt_two_pow hh]

/-- Exact semantic characterization of compact-code equality at `n = 5`. -/
theorem reachCode_eq_iff_sameReachability5 (g h : GraphMask 5) :
    reachCode g = reachCode h ↔
      ∀ u v : Vertex,
        Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v := by
  constructor
  · exact reachCode_eq_implies_sameReachability5
  · exact sameReachability5_implies_reachCode_eq

end PrecategoryFormal
