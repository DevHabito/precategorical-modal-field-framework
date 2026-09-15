import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Five labeled vertices, matching the finite A8.1 witness. -/
abbrev Vertex := Fin 5

/--
A minimal abstract condensation structure for the first formalization pilot.

`blockMin v` is the minimum-labeled representative of the block containing `v`.
`quotientOrderCode` is an opaque finite code for the strict quotient order.

This pilot intentionally formalizes the encoding-level non-injectivity first.
It does not yet derive the blocks from graph reachability; that is a separate
follow-up obligation.
-/
structure CondensationStructure where
  blockMin : Vertex → Vertex
  quotientOrderCode : Nat

/-- Minimum-representative maps are idempotent and never increase a label. -/
def ValidMinMap (f : Vertex → Vertex) : Prop :=
  ∀ v, f (f v) = f v ∧ (f v).val ≤ v.val

/-- The first A8.1 witness has blocks `{0,2,3,4}` and `{1}`. -/
def blockMinA (v : Vertex) : Vertex :=
  if v = 1 then 1 else 0

/-- The second A8.1 witness has blocks `{0,2,3}` and `{1,4}`. -/
def blockMinB (v : Vertex) : Vertex :=
  if v = 1 ∨ v = 4 then 1 else 0

theorem blockMinA_valid : ValidMinMap blockMinA := by
  intro v
  fin_cases v <;> native_decide

theorem blockMinB_valid : ValidMinMap blockMinB := by
  intro v
  fin_cases v <;> native_decide

/-- The two quotient orders are both the two-element antichain, hence code `0`. -/
def witnessA : CondensationStructure where
  blockMin := blockMinA
  quotientOrderCode := 0

def witnessB : CondensationStructure where
  blockMin := blockMinB
  quotientOrderCode := 0

/-- Whether a vertex is the minimum representative of its block. -/
def isRepresentative (q : CondensationStructure) (v : Vertex) : Bool :=
  decide (q.blockMin v = v)

/-- Add one historical representative bit when the Boolean predicate is true. -/
def weightedBit (b : Bool) (weight : Nat) : Nat :=
  if b then weight else 0

/--
The scalar minimum-representative code used by the historical A8 encoding:
the quotient-order code occupies the lower 25 bits and representative flags
occupy bits 25 through 29.

For the antichain witnesses the lower 25 bits are all zero.
-/
def historicalRepresentativeCode (q : CondensationStructure) : Nat :=
  q.quotientOrderCode
    + weightedBit (isRepresentative q 0) (2 ^ 25)
    + weightedBit (isRepresentative q 1) (2 ^ 26)
    + weightedBit (isRepresentative q 2) (2 ^ 27)
    + weightedBit (isRepresentative q 3) (2 ^ 28)
    + weightedBit (isRepresentative q 4) (2 ^ 29)

/-- Both witnesses reproduce the exact historical representative code 100663296. -/
theorem witnessA_code : historicalRepresentativeCode witnessA = 100663296 := by
  native_decide

theorem witnessB_code : historicalRepresentativeCode witnessB = 100663296 := by
  native_decide

theorem witnesses_same_representative_code :
    historicalRepresentativeCode witnessA = historicalRepresentativeCode witnessB := by
  rw [witnessA_code, witnessB_code]

/-- The full block assignments differ at vertex 4. -/
theorem witnesses_distinct : witnessA ≠ witnessB := by
  intro h
  have h4 := congrArg (fun q : CondensationStructure => q.blockMin (4 : Vertex)) h
  norm_num [witnessA, witnessB, blockMinA, blockMinB] at h4
  omega

/--
MF-R009 pilot theorem: the historical minimum-representative encoding is not
injective even on these two valid minimum-block maps with the same quotient
antichain.
-/
theorem historicalRepresentativeCode_not_injective :
    ¬ Function.Injective historicalRepresentativeCode := by
  intro hInjective
  exact witnesses_distinct (hInjective witnesses_same_representative_code)

end PrecategoryFormal
