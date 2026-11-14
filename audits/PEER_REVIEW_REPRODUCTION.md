# Peer review guide

This guide covers the A115–A122 optimization chain and the separate causal
reconstruction results in flat and regular curved diamonds. Each reviewer
can start with one of the questions below. Record the full commit SHA of
the checkout used for review. If opening this guide on GitHub, use the commit
permalink supplied with the review materials.

| Review topic | Claim and check |
| --- | --- |
| A115–A119 | A115 gives an exact counterexample to a universal deformed-target threshold. A119 excludes vanishing of the second coefficient on the declared critical surface. Check whether the substitution, finite cutoff and rational interval boxes cover the entire admissible domain. [Theorem chain and evidence](../consolidation/CORE_RESULTS_MAP.md#c4--target-deformed-central-nesting-and-boundary-layer) |
| A120–A122 | A122 gives an asymptotic expansion at fixed interior parameters and a zero of the intrinsic resonant coefficient for even parity. Check the remainder estimates and the endpoint sign certificate. The arithmetic realization of the resonant subsequence is open. [Theorem chain and evidence](../consolidation/CORE_RESULTS_MAP.md#c5--fixed-interior-rounding-phase-staircase-and-resonance) |
| Flat 2+1 and 3+1 | The leading errors for recovery up to global reversal are \(32\pi/(3n)\) and \(9\pi/n\). Check the geometric source of each constant and the bounds on failures without adjacent twins. [2+1](../docs/physics_bridge/MINKOWSKI_D3_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md) · [3+1](../docs/physics_bridge/MINKOWSKI_ALLD_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md#3-the-31-law) |
| Flat 3+1 connectivity | Combine the fixed-cardinality isolate limit with the vanishing probability of multiple components containing edges to obtain \(\Pr(G_n\text{ connected})\to e^{-3\pi}\). Check the common sampling regime in both premises. [Connectivity corollary](../docs/physics_bridge/MINKOWSKI_4D_FIXED_N_ISOLATED_POISSON_THEOREM_20261111.md#12-consequence-for-connectedness) |
| Curved 3+1 | Check uniform domination and the complementary sectors in the small-disagreement estimate near the null joint. [Focused review brief](CURVED_D4_NULL_JOINT_EXTERNAL_REVIEW_BRIEF.md) |

The A115–A122 sources are still chronological theorem notes. The result map
is an index for review, and the standalone manuscript remains to be assembled.

## Reproduce the computations

Run from the repository root. The reference Python environment was Python
3.12.14 with NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0 and mpmath 1.3.0.
Use a virtual environment for these dependencies. The A-series scripts write
JSON next to their own source, so the commands below run them in a temporary copy.

```bash
set -euo pipefail
git rev-parse HEAD
python --version
python -m pip install numpy==2.3.5 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
review_out=$(mktemp -d)
updates=MFRP_Informational_Requirements_A39-A109/research_updates
for n in {115..122}; do
    cp -R "$updates/A$n" "$review_out/"
    python "$review_out/A$n/"*.py > "$review_out/A$n.log"
    python -m json.tool --sort-keys "$updates/A$n/"*.json > "$review_out/expected.json"
    python -m json.tool --sort-keys "$review_out/A$n/"*.json > "$review_out/actual.json"
    cmp "$review_out/expected.json" "$review_out/actual.json"
done
python tools/verify_d3_bulk_recovery_constant.py
python docs/physics_bridge/minkowski_higher_dimensional_upo_pilot.py --output "$review_out/pilot.json" > "$review_out/pilot.log"
python docs/physics_bridge/minkowski_4d_isolated_poisson_moments.py > "$review_out/isolates-d4.json"
python tools/verify_curved_joint_coefficient_normalization.py
python tools/verify_curved_joint_flat_regression.py
printf 'Outputs: %s\n' "$review_out"
```

The pilot emits its full main grid as `runs`. In the published snapshot, match
`(dimension, n)` to `(d, n)` and compare `mean_isolated_vertices` to
`mean_isolated`. The fixed-cardinality isolate simulation reports finite
moments. The rare zero-isolate probability is obtained from the limiting
theorem.

## Recorded replay

All eight A-series JSON outputs matched after normalizing layout. The seeded
pilot reproduced all 21 published main-grid rows, including the corrected
isolation means, and the exact classifier counts. All five published
fixed-cardinality isolate blocks also reproduced. The 2+1 quadrature passed
at both integration tolerances, and the curved normalization and flat
regression checks passed.

## Lean 4 proof scope

The project pins Lean and mathlib in [formal/lean](../formal/lean/).
Both modules below built with Lean 4.33.1 and passed separate
`leanchecker` replays.

```bash
cd formal/lean
lake exe cache get
lake build PrecategoryFormal.PhysicalBridgeRecoveryChecks PrecategoryFormal.ReducedOptimizationChecks
lake env leanchecker PrecategoryFormal.PhysicalBridgeRecoveryChecks
lake env leanchecker PrecategoryFormal.ReducedOptimizationChecks
```

- [Recovery checks](../formal/lean/PrecategoryFormal/PhysicalBridgeRecoveryChecks.lean)
  cover the reduced 2+1 integral, the half-line exponential and Gaussian factors, and 3+1
  normalization, and the graph and squeeze steps of the connectivity corollary.
  The original change of variables, sprinkling limits and uniform geometric
  estimates remain in the paper proofs.
- [Optimization checks](../formal/lean/PrecategoryFormal/ReducedOptimizationChecks.lean)
  cover the A119 critical substitution, rational cutoff arithmetic, and A122
  drift monotonicity. The A119 interval certificate and its coverage, the A122
  asymptotic remainder, and the full A115–A122 theorem chain remain outside
  these Lean modules.
