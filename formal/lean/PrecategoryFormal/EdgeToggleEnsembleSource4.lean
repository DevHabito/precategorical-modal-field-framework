import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact compressed fixed-absent-edge counts for the four non-loop edges sourced at vertex 4. -/
theorem fixedEdgeNoReachFastCountFive_source4 :
    fixedEdgeNoReachFastCountFive 4 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 3 = 153600 := by
  native_decide

/-- Direct full-`2^20`-mask reproduction for the four source-4 edges. -/
theorem fixedEdgeNoReachDirectCountFive_source4 :
    fixedEdgeNoReachDirectCountFive 4 0 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 4 1 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 4 2 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 4 3 = 153600 := by
  native_decide

/-- Direct full-mask subtotal for the four non-loop edges sourced at vertex 4. -/
def fixedEdgeNoReachDirectTotalFive_source4 : Nat :=
  fixedEdgeNoReachDirectCountFive 4 0 +
  fixedEdgeNoReachDirectCountFive 4 1 +
  fixedEdgeNoReachDirectCountFive 4 2 +
  fixedEdgeNoReachDirectCountFive 4 3

/-- Exact source-4 subtotal, derived only from the four direct certificates above. -/
theorem fixedEdgeNoReachDirectTotalFive_source4_exact :
    fixedEdgeNoReachDirectTotalFive_source4 = 614400 := by
  rcases fixedEdgeNoReachDirectCountFive_source4 with ⟨h40, h41, h42, h43⟩
  norm_num [fixedEdgeNoReachDirectTotalFive_source4, h40, h41, h42, h43]

end PrecategoryFormal
