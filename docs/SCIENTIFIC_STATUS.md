# Scientific status

## Established within the audited mathematical models

- Directed reachability and SCC condensation provide an internal preorder and quotient partial order.
- Order data alone do not identify continuous marginals under monotone reparameterizations.
- Relative quantitative information in `q` can be operationalized conditionally, while a global offset remains gauge.
- Exact descriptive-refinement consistency requires additive weights or equivalent projective semantics.
- Projective branch probabilities have the ratio form `W(child)/W(parent)` once positive additive subtree weights are supplied.
- The exponential effective score is an exact static sufficient statistic for the audited exponential kernel.
- A single effective score generally does not close the microscopic dynamics.
- Gaussian closure is exact only under a Gaussian state/innovation package.
- Dynamic graph coarse-graining requires source occupancy or joint flow, not only a kernel and a partition.

## Current physical-bridge literature audit

The vacuum Alexandrov-volume calculation used in the curved-spacetime bridge has undergone a separate consistency audit.

Direct re-integration of the publicly printed intermediate formulas in Wang (2019), *Geometry of small causal diamonds*, gives

\[
\frac{\delta V}{V_0}
=
L^4
\left[
A_dE^2+B_dH^2+C_dD^2
\right]
+o(L^4),
\]

with

\[
A_d=
\frac{d(7d^2+44d+58)}
{180(d+1)(d+3)(d+4)},
\]

\[
B_d=
\frac{d(d+6)}
{60(d+1)(d+3)(d+4)},
\]

and

\[
C_d=
-\frac{d}
{120(d+1)(d+3)(d+4)}.
\]

In the normalization of the paper's final Eq. (79), this corresponds to

\[
(7d^3+58d^2+146d+116)E^2
+
3(d+2)(d+6)H^2
-
\frac32(d+2)D^2,
\]

rather than the printed \(108\) constant term and factor \(6\) in the hook sector.

In \(3+1\),

\[
\frac{V}{V_0}
=
1+
L^4
\left[
\frac{17}{630}E^2+
\frac1{210}B^2
\right]
+o(L^4).
\]

Internal support now includes:

- exact direct re-integration of the printed intermediate equations;
- a successful dedicated GitHub Actions audit;
- exact all-dimensional Cahen--Wallach agreement;
- an exact \(3+1\) LRS-Kasner parent-volume series;
- higher-dimensional numerical LRS-Kasner checks;
- Lean/kernel verification of the rational-algebra layer.

This remains an **externally unverified literature-consistency result**. It is not yet a published erratum, does not establish priority, and does not change the repository's broader caution about physical interpretation.

External-review entry point:

docs/physics_bridge/WANG_2019_ACD_VOLUME_EXTERNAL_REVIEW_PACKET_20261112.md

## Not established

This repository does not derive or confirm physical spacetime, calibrated duration, physical distance, curvature, gravity, matter, quantum amplitudes, a physical value of lambda, the physical origin of q or mu, or an experimentally identified occupancy measure.

## Current minimal architecture under investigation

The working architecture is commonly summarized as `(R, q, mu, K, pi)`: relation/order, relative quantitative marks, additive measure or multiplicity, transition law, and dynamic occupancy. This is a research architecture, not a confirmed physical ontology.


## Time-origin boundary

The current physical-bridge audit does not support a claim that the provisional architecture derives physical time from a timeless substrate.

- A directed or precedence-like interpretation of \(R\) already supplies orientation.
- A dynamical interpretation of \(K\) already supplies transition/succession semantics.
- \(q\) can add calibrated asymmetry without becoming temporal rank.
- \(\mu\) supplies multiplicity/refinement semantics, not temporal order.
- \(\pi\) supplies occupancy/state information, not temporal order.

The repository now treats temporal order, reversible relational evolution, arrow/irreversibility, and metric duration as separate problems.

This boundary does not weaken the existing mathematical results. It prevents those results from being overinterpreted as a completed pregeometric theory of time.
