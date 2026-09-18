import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact fixed-absent-edge counts for the four non-loop edges sourced at vertex 2. -/
theorem fixedEdgeNoReachFastCountFive_source2 :
    fixedEdgeNoReachFastCountFive 2 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 4 = 153600 := by
  native_decide

end PrecategoryFormal
