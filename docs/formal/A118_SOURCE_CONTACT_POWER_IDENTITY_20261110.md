# A118 first-jet source-contact identity without an extra relation hypothesis

**Date:** 10 November 2026. **Branch:** `research/a115-a119-uniform-remainder-20261110`.
**Evidence status:** new Lean lemmas submitted, kernel CI pending.

The corrected algebraic identity in `A118SourceFirstJet` has one source representation condition: `s*z=(s^(r-2))⁻¹`. This note establishes that the condition is a consequence of the original contact factor, not an additional optimization assumption.

For any nonzero real s and natural n,

[
s(s^{n+1})^{-1}=(s^n)^{-1}.
]

With the actual contact deficit r=n+2 and z=(s^(n+1))⁻¹, the source condition holds automatically. The [Lean module](../../formal/lean/PrecategoryFormal/A118SourceContactPower.lean) submits this identity and `source_slope_equals_xi_at_contact`, which reduces the algebraic A115 source-jet slope to the published A118 `xiPublished` for either parity.

**What it does not claim:** the already-corrected source-slope formula is still an *algebraic first-order-jet computation*; a general real-derivative theorem for the original rational bracket and its exponential collision powers remains unproved in Lean. The uniform cubic remainder proof, full F2/F3 optimization and historical originality likewise remain open.

The original intermediate `source_xi_minus_published` formula submitted earlier omitted a factor `etaH`, caused a Lean failure, and was corrected. This contact-power module neither restores that false formula nor bypasses the correction.


## First compilation gate and correction

[GitHub Actions 42925831382](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42925831382) failed at the final application because Lean reached its default deterministic heartbeat limit during definitional equality. The log contained no failed algebraic equality, but this is still a **failed proof attempt**. The next revision names the instantiated theorem explicitly, raises the local module heartbeat budget, and leaves the exact theorem statement and source-contact assumptions unchanged. Kernel approval remains pending.
