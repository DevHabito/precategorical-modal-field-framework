# Lean 4 formalization checkpoint — A115/A119

Date: 2026-11-06  
Source baseline: main at 89e2668c3aef3fbff5a7f399f86de7d27e467da1  
Branch: `formal/a115-a122-critical-audit-20261106`  
Build commit: `92c21604c6ef2fac85f116c491c4a9e693ce391d`

## Exact scope

Added `PrecategoryFormal/TargetDeformationAudit.lean`, imported by `PrecategoryFormal.lean`, to the existing pinned Lean 4.33.1/Mathlib 4.33.1 Lake project.

Four obligations, with no `sorry`, `admit`, or introduced axioms:

1. `target_affine_scaled_cancellation`: the target-affine coefficient cancels under a scaled adjacent difference. This is only one channel of A115's complete ten-term expression.
2. `critical_surface_substitution`: if the critical equation holds and the denominator is nonzero, solve it for `q`. This is only A119's algebraic substitution.
3. `critical_substitution_positive`: from separately supplied positivity hypotheses, obtain positivity of `q`.
4. `even_cutoff_rational_positive`: a fixed exact rational inequality used by the even-parity A119 deep-cell cutoff.

**Do not equate successful compilation of these lemmas with a Lean proof of A115, A119, or A122.** The key analytical asymptotic theorems, original finite optimization model, and the interval exhaustion over 6,400 real boxes are NOT formalized in Lean here.

## Verification provenance

The execution environment has no `lean` or `lake` binary and cannot reach GitHub directly for toolchain installation. Therefore the branch activates the existing GitHub Actions `Lean formal verification` pipeline on changes under `formal/lean/**`.

GitHub Actions run: https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42302765344

Initial checks observed: checkout SUCCESS, placeholder scan SUCCESS, pinned toolchain bootstrap SUCCESS; the project build was still IN PROGRESS at the time this checkpoint was prepared. **No Lean PASS is claimed unless that exact run reports a successful build.** Do not infer a PASS from commit acceptance or the absence of prohibited placeholders.

## Independent numerical checks re-executed this session

Both separately written Python `Fraction` scripts were run locally from `/mnt/data/verify_a119.py` and `/mnt/data/check_a122.py`. They reported:
- A119: 2,304 even and 4,096 odd rational covering boxes with positive lower endpoints; minimal lower endpoint fractions exactly match A119's published manuscript; both cutoff lower bounds positive.
- A122: interval-logarithm evaluation for `s=129/1000`, even parity, has `Omega_even(xi)<0` at `tau=131/1000` and `Omega_even(xi)>0` at `tau=132/1000`.

These are computational validations of explicitly stated formulas, **not** Lean proofs and **not** a certificate of originality.

## Remaining Lean milestones

A. Encode the finite-support probability measures and exact primal constraints.
B. Derive the determinant/cofactor reduced factor `E_M,k` and the full ten-term expansion from those definitions.
C. Reconstruct the first- and second-order coefficients without quoting the A118 script.
D. Prove all interval inclusion operations and tail bounds, and verify the A119 6,400 rational covering certificates with a checked reflection mechanism or a separately trusted proof format.
E. Formalize the ceiling contact and parity-dependent limit, including resonant endpoints; then the actual sign consequences.
F. Retain explicit publication gates for novelty and independently reviewed prior art.

No claims of the full A115–A122 theorems' kernel verification should be made before milestones A–E are complete.
