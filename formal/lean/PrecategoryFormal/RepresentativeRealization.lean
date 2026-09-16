import PrecategoryFormal.LiteralRepresentativeCode

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Every admitted representative set contains the globally least label `0`. -/
theorem representativeChoice_zero_mem {m k : Nat} (S : RepresentativeChoice m k) :
    (0 : CountGround m) ∈ S.1 := by
  have h := S.2
  change
    S.1 ∈ ((Finset.univ : Finset (CountGround m)).powersetCard k).filter
      (({0} : Finset (CountGround m)) ⊆ ·) at h
  exact (Finset.mem_filter.mp h).2 (by simp)

/--
A concrete block representative for every ground vertex.  Representatives are
fixed; every nonrepresentative vertex is placed in the block represented by `0`.
-/
def choiceRepresentative {m k : Nat} (S : RepresentativeChoice m k)
    (x : CountGround m) : S.1 :=
  if hx : x ∈ S.1 then ⟨x, hx⟩
  else ⟨0, representativeChoice_zero_mem S⟩

@[simp]
theorem choiceRepresentative_of_representative {m k : Nat}
    (S : RepresentativeChoice m k) (s : S.1) :
    choiceRepresentative S s.1 = s := by
  apply Subtype.ext
  simp [choiceRepresentative, s.2]

/--
Loopless realizing graph for a literal code `(S,P)`.  Distinct ground vertices
are connected directly whenever their representative blocks are ordered by `P`.
-/
def representativeRealizationGraph {m k : Nat} (S : RepresentativeChoice m k)
    (P : BoolPartialOrder S.1) (x y : CountGround m) : Bool :=
  if x = y then false else P.1 (choiceRepresentative S x) (choiceRepresentative S y)

/-- Mathematical reachability in the realizing graph. -/
def RepresentativeRealizationReach {m k : Nat} (S : RepresentativeChoice m k)
    (P : BoolPartialOrder S.1) (x y : CountGround m) : Prop :=
  Relation.ReflTransGen
    (fun u v => representativeRealizationGraph S P u v = true) x y

@[simp]
theorem representativeRealizationGraph_loopless {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1) (x : CountGround m) :
    representativeRealizationGraph S P x x = false := by
  simp [representativeRealizationGraph]

/-- Every realizing-graph edge respects the lifted quotient order. -/
theorem representativeRealizationGraph_edge_order {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1)
    {x y : CountGround m}
    (h : representativeRealizationGraph S P x y = true) :
    P.1 (choiceRepresentative S x) (choiceRepresentative S y) = true := by
  by_cases hxy : x = y
  · subst y
    simp [representativeRealizationGraph] at h
  · rw [representativeRealizationGraph, if_neg hxy] at h
    exact h

/--
Reachability in the explicit realizing graph is exactly the partial order lifted
from representatives to their SCC blocks.
-/
theorem representativeRealizationReach_iff_order {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1)
    (x y : CountGround m) :
    RepresentativeRealizationReach S P x y ↔
      P.1 (choiceRepresentative S x) (choiceRepresentative S y) = true := by
  constructor
  · intro h
    induction h with
    | refl =>
        exact P.2.1 _
    | tail hreach hedge ih =>
        exact P.2.2.2 _ _ _ ih (representativeRealizationGraph_edge_order S P hedge)
  · intro h
    by_cases hxy : x = y
    · subst y
      exact Relation.ReflTransGen.refl
    · apply Relation.ReflTransGen.single
      rw [representativeRealizationGraph, if_neg hxy]
      exact h

/-- The strongly connected components are exactly the fibers of the representative map. -/
theorem representativeRealization_mutual_iff_same_representative {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1)
    (x y : CountGround m) :
    (RepresentativeRealizationReach S P x y ∧ RepresentativeRealizationReach S P y x) ↔
      choiceRepresentative S x = choiceRepresentative S y := by
  constructor
  · rintro ⟨hxy, hyx⟩
    exact P.2.2.1 _ _
      ((representativeRealizationReach_iff_order S P x y).1 hxy)
      ((representativeRealizationReach_iff_order S P y x).1 hyx)
  · intro hrep
    constructor
    · apply (representativeRealizationReach_iff_order S P x y).2
      rw [hrep]
      exact P.2.1 _
    · apply (representativeRealizationReach_iff_order S P y x).2
      rw [hrep]
      exact P.2.1 _

/-- Each chosen representative is the minimum label in its realized SCC fiber. -/
theorem choiceRepresentative_minimal {m k : Nat}
    (S : RepresentativeChoice m k) (s : S.1) (x : CountGround m)
    (hrep : choiceRepresentative S x = s) :
    s.1.val ≤ x.val := by
  have hval := congrArg (fun z : S.1 => z.1.val) hrep
  by_cases hx : x ∈ S.1
  · simp [choiceRepresentative, hx] at hval
    omega
  · simp [choiceRepresentative, hx] at hval
    omega

/-- The quotient reachability order on the actual representatives is exactly `P`. -/
theorem representativeRealization_quotient_order {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1)
    (s t : S.1) :
    RepresentativeRealizationReach S P s.1 t.1 ↔ P.1 s t = true := by
  rw [representativeRealizationReach_iff_order]
  simp

/--
Certificate that a literal representative code is realized by an actual
loopless directed graph, with the intended SCC minima and quotient order.
-/
structure RepresentativeCodeRealization {m k : Nat}
    (S : RepresentativeChoice m k) (P : BoolPartialOrder S.1) where
  graph : CountGround m → CountGround m → Bool
  loopless : ∀ x, graph x x = false
  reach_iff_order : ∀ x y,
    Relation.ReflTransGen (fun u v => graph u v = true) x y ↔
      P.1 (choiceRepresentative S x) (choiceRepresentative S y) = true
  mutual_iff_same_representative : ∀ x y,
    (Relation.ReflTransGen (fun u v => graph u v = true) x y ∧
      Relation.ReflTransGen (fun u v => graph u v = true) y x) ↔
      choiceRepresentative S x = choiceRepresentative S y
  representative_fixed : ∀ s : S.1, choiceRepresentative S s.1 = s
  representative_minimal : ∀ (s : S.1) (x : CountGround m),
    choiceRepresentative S x = s → s.1.val ≤ x.val
  quotient_order : ∀ s t : S.1,
    Relation.ReflTransGen (fun u v => graph u v = true) s.1 t.1 ↔ P.1 s t = true

/-- Every literal `(S,P)` code in MF-R008 is realized by an explicit digraph. -/
def literalRepresentativeCodeRealization {m : Nat} (c : LiteralRepresentativeCode m) :
    RepresentativeCodeRealization c.2.1 c.2.2 where
  graph := representativeRealizationGraph c.2.1 c.2.2
  loopless := representativeRealizationGraph_loopless c.2.1 c.2.2
  reach_iff_order := representativeRealizationReach_iff_order c.2.1 c.2.2
  mutual_iff_same_representative :=
    representativeRealization_mutual_iff_same_representative c.2.1 c.2.2
  representative_fixed := choiceRepresentative_of_representative c.2.1
  representative_minimal := choiceRepresentative_minimal c.2.1
  quotient_order := representativeRealization_quotient_order c.2.1 c.2.2

end PrecategoryFormal
