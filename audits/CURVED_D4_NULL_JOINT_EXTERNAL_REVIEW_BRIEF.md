# Review request: the null-joint estimate in curved 3+1 dimensions

In a regular Lorentzian diamond, sample two events independently from normalized physical volume. For a comparable pair, let \(\Delta\) be the volume fraction of events comparable to exactly one member of the pair. The target claim is
\[
F_4(t)=\Pr(X\sim Y,\ \Delta(X,Y)\le t)\sim C_{4,g}t^3.
\]
The sharp recovery theorem uses this estimate to obtain \(1-p_4(n)\sim 3C_{4,g}/n\) after controlling the remaining failure modes. Its conclusion is recovery of the sampled order up to global reversal.

## Proofs to review

1. [Regular curved recovery theorem, Sections 2 and 5](../docs/physics_bridge/ALLD_CURVED_REGULAR_ORIENTATION_RECOVERY_THEOREM_20261112.md#2-regular-diamond-hypotheses). Check which hypotheses apply to a fixed regular diamond and which follow only in the sufficiently small local construction.
2. [Null-joint edge estimate, Sections 3–7 and 11](../docs/physics_bridge/ALLD_CURVED_REGULAR_JOINT_EDGE_TAIL_THEOREM_20261112.md#3-thin-null-endpoint-volume-laws). Check the uniform expansion of the distinguishing volume and causal cap as both endpoints approach the joint. Identify a bound that justifies passing from compact sets in the scaled variables to the entire integration domain, including mixed regimes in which one scaled depth is large. Check that the complementary bulk and single-face sectors contribute \(o(t^3)\).
3. [Penrose-scaled domain convergence](../docs/physics_bridge/PENROSE_SCALED_ALEXANDROV_DOMAIN_CONVERGENCE_20261112.md) and [local compact containment](../docs/physics_bridge/LOCAL_PENROSE_COMPACT_CONTAINMENT_THEOREM_20261112.md). Check the uniformity across the compact family of generators and whether the containment argument covers each regime used in the edge estimate.
4. [Curved joint coefficient normalization](CURVED_JOINT_COEFFICIENT_NORMALIZATION_AUDIT_20261112.md). Trace the factor for the two time orders, the normalized pair measure, and the resulting factors \(C_{4,\eta}=3\pi\) and \(3C_{4,\eta}=9\pi\).

Please point to the first unsupported inference, if any, and state the smallest additional bound or geometric hypothesis needed to close it. A proof of uniform domination with explicit dependencies, or a regular example where it fails, would resolve the main review question.

## Reproduced checks

- The [symbolic normalization script](../tools/verify_curved_joint_coefficient_normalization.py) and [flat coefficient regression](../tools/verify_curved_joint_flat_regression.py) passed.
- The [flat importance sampler](../tools/minkowski_null_joint_twin_asymptotic.py) probes the flat two-point integral at finite effective sample sizes.
- The [Lean module](../formal/lean/PrecategoryFormal/PhysicalBridgeTwinCoefficientAlgebra.lean) covers the algebraic factorization and final flat normalization. Uniform geometric domination and the probabilistic limit require separate verification.
