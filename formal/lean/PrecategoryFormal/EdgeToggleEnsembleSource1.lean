import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact fixed-absent-edge counts for the four non-loop edges sourced at vertex 1. -/
theorem fixedEdgeNoReachFastCountFive_source1 :
    fixedEdgeNoReachFastCountFive 1 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 4 = 153600 := by
  native_decide

end PrecategoryFormal
