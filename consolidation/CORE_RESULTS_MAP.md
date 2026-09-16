# Consolidation 1.0 — reduced mathematical core

This file is an editorial compression of the repository. It does not replace source proofs or audit artifacts. The goal is to identify a small number of claims that can be rewritten, formalized, and reviewed independently.

## C1 — Finite combinatorics and encoding correction

### C1.1 Minimum-representative quotient-poset code count

Source claim: **MF-R008 / A8.1**.

For the project-defined code that stores SCC minima and the quotient order but not full SCC membership, the count is

\[
N_{\mathrm{rep}}(n)
=\sum_{k=1}^{n}\binom{n-1}{k-1}p(k),
\]

where `p(k)` denotes the number of labeled partial orders on `k` elements under the declared convention.

Status: **proved and end-to-end formalized in Lean for the declared code/count statement**. The formalization derives the binomial representative-set factor, independently obtains `p(1),…,p(5)=1,3,19,219,4231` by exact `native_decide` enumeration, proves the executable encoding has exactly the semantics of labeled partial orders, derives the fiber count from an explicit code type, and proves that the canonical-coordinate presentation is equivalent to the literal `(S,P)` presentation with `P` living on the actual representative set. It further proves that every literal `(S,P)` code is realizable by an explicit loopless digraph whose SCCs are the representative fibers, whose representatives are minimum labels of those SCCs, and whose quotient reachability order is exactly `P`. Thus the literal five-vertex code type has cardinality `5234` and the abstract code-space count is not inflated by unrealizable pairs. The complete library build and module-sharded bundled `leanchecker` replay pass.

Important nonclaims: this does not retain or count full SCC memberships as part of the code, does not make the representative code injective, and does not establish novelty or priority.

Novelty status: **not certified**.

### C1.2 Non-injectivity of the minimum-representative code

Source claim: **MF-R009 / A8.1**.

The representative code discards SCC membership information and is not injective on full labeled condensation structures.

Status: **proved by constructive counterexample**.

### C1.3 Edge-toggle sensitivity at n=5

Source claim: **MF-R011 / A8.1**.

For the explicitly declared uniform graph-edge ensemble, exhaustive finite enumeration gives

\[
P_2=1,\qquad P_3=\frac34,\qquad P_4=\frac12,\qquad P_5=\frac{75}{256},
\]

where `P_n` is the probability that the declared single-edge toggle changes the induced reachability preorder.

Status: **exact finite computation**; not an asymptotic theorem.

Novelty status: **apparently unreported in the searched literature; not certified**.

---

## C2 — Exact dynamic non-closure

Source claim: **MF-R049**.

On the unrestricted finite-distribution class used in the source result, mean plus one fixed-lambda entropic/log-sum-exp score does not determine the next score under the declared update. An explicit four-point witness establishes non-closure.

Status: **proved by exact identity + constructive counterexample**.

Novelty status: **not certified**.

Formalization priority: **high**, because this can be made self-contained and does not require the broader Modal Field interpretation.

---

## C3 — Frozen exponential-moment optimization

Sources: **A112, A113**, with **A114** kept as a separate lifted layer pending governance normalization.

### C3.1 Frozen tail structural theorem

A112 gives the strict compressed support/interval structure for the frozen gamma-plus branch under its declared hypotheses.

Status: **analytic theorem**.

### C3.2 Frozen compressed one-variation theorem

A113 proves, under the frozen reduced contract with `beta=1/8`, `tau=1/2`, source window `s in [0.129,0.133]`, and `M>=521`, the central/remote sign package that localizes the compressed maximum to the central three-site window and excludes non-adjacent ties.

Status: **analytic theorem**.

### C3.3 Lifted active-set classification

A114 selects lifted KKT architectures after compressed localization.

Status for consolidation: **retain, but do not merge into C3.1/C3.2 until all theorem headers, red-team status, and longitudinal governance files agree**.

---

## C4 — Target-deformed central nesting and boundary layer

Sources: **A115–A119**.

These packages should be rewritten as one self-contained theorem chain rather than five chronological research updates.

Core content:

- exact target-node deformation formulas and exact reproduction of the frozen target at `tau=1/2`;
- refutation of a universal `M>=521` target-deformed threshold;
- eventual positivity of the central nesting factor on compact subsets of the strict interior;
- a nontrivial collision layer for `tau-s=O(1/M)`;
- parity-resolved phase classification of that collision layer;
- second-order coefficient on critical surfaces;
- proof that the critical second-order coefficient is positive on the frozen source window, excluding `Lambda=Xi=0` within that contract.

Status: **analytic theorems + exact counterexamples + computer-assisted interval certificate where explicitly declared**.

Novelty status: **not certified**.

---

## C5 — Fixed-interior rounding-phase staircase and resonance

Sources: **A120–A122**.

These packages should be rewritten as one self-contained theorem package.

For fixed strict-interior `(s,tau)`, fixed parity, and fixed offset, the remote-factor asymptotics retain the ceiling phase

\[
\rho_M=\lceil Mc\rceil-Mc,
\qquad
c=\frac{\log\tau}{2\log s}.
\]

The leading family collapses to one coordinate

\[
\Psi_{p,j}(\rho)=P_p s^{j+\rho}-Q_p,
\]

which yields a single limiting sign front and a two-site local-peak rule. A122 refines the resonant layer to

\[
\mathcal N_{M,j}
=\Phi_p(x_M)+\frac{\Omega_p(x_M)}{M}+R_{M,j},
\]

with a remainder smaller than every polynomial order for each fixed interior pair. Near resonance, arithmetic phase drift and the intrinsic `1/M` coefficient compete.

Status: **analytic theorem chain + exact finite hardening + rigorous interval-sign certificate for existence of an intrinsic double-critical target**.

Important nonclaim: **no global target-deformed compressed-maximizer theorem**.

Novelty status: **not certified**.

---

# What is deliberately not part of the mathematical core

The following are not promoted by Consolidation 1.0 into mathematical conclusions about nature:

- Modal Field ontology;
- RZS as a physical theory;
- physical spacetime, gravity, matter, quantum interpretation, or calibrated time/distance;
- the claim that the mathematical architecture is necessary for reality;
- any priority claim not backed by a dedicated literature review.

Those materials remain historically valuable and may motivate future work, but they are logically downstream from the mathematics.
