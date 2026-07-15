# Result Classification Matrix

**Project:** Pre-Categorical Modal Field Framework  
**Author:** Felipe Gianini Romero  
**Status:** Editorial-scientific source of truth for manuscript restructuring

## Purpose

This document classifies each major claim by mathematical status, evidence type, novelty status, permitted wording, prohibited overclaim, reproducibility status, and manuscript destination. The classification unit is a scientific claim, not an audit number.

No item is labeled a definitively new theorem unless a dedicated claim-level literature review has been completed. Strong candidates are marked as potentially original.

## Executive summary

- Total classified claims: **69**
- P0 editorial/research priority: **36**
- Claims assigned to the foundational manuscript: **53**
- Claims assigned to the combinatorics manuscript: **11**
- Items with a public-repository reproducibility gap: **3**

### Strongest candidates for claim-level novelty review

- **MF-R008 — Count of minimum-representative quotient-poset codes**: POTENTIALLY ORIGINAL ELEMENTARY COROLLARY; SEARCH REQUIRED
- **MF-R011 — Single-edge flip changes the n=5 condensation preorder with probability 75/256**: POTENTIALLY ORIGINAL FINITE STATISTIC
- **MF-R036 — No nontrivial continuous cardinal score satisfies both extension stability and full positive-affine invariance**: POTENTIALLY ORIGINAL FORMULATION; HIGH-PRIORITY NOVELTY SEARCH
- **MF-R047 — Q_lambda(aq+c)=c+a Q_{a lambda}(q)**: POTENTIALLY ORIGINAL EMPHASIS; ALGEBRA ITSELF ELEMENTARY
- **MF-R048 — Q'_lambda=(1-a) q_bar + a Q_{a lambda}**: POTENTIALLY ORIGINAL AND TECHNICALLY STRONG; NOVELTY SEARCH REQUIRED
- **MF-R049 — A single Q_lambda is not generally a dynamically closed state variable**: POTENTIALLY ORIGINAL FRAMEWORK CONSEQUENCE
- **MF-R067 — Current minimal architecture is (R,q,mu,K,pi)**: POTENTIALLY ORIGINAL SYNTHESIS
- **MF-R068 — The obstruction map is a framework-level contribution**: ORIGINAL ORGANIZATION; INDIVIDUAL ITEMS HAVE UNEQUAL NOVELTY

## Evidence taxonomy

- **CLASSICAL_THEOREM** — Known theorem used as mathematical background. It must be attributed and must not be presented as a project discovery.
- **DIRECT_COROLLARY** — A short logical consequence of a known theorem or of a declared definition.
- **EXACT_ENUMERATION** — An exhaustive finite computation. Exact for the declared finite ensemble, not automatically asymptotic.
- **CONSTRUCTIVE_COUNTEREXAMPLE** — An explicit witness disproving a universal claim under stated assumptions.
- **MONTE_CARLO** — Seeded finite numerical evidence. Its scope is the declared generator, sample sizes, and gates.
- **SOFTWARE_REGRESSION** — A test that an implementation respects an already proved identity. It is not independent evidence for the theorem.
- **FRAMEWORK_SYNTHESIS** — A project contribution that organizes known and new results into a coherent architecture.
- **PHYSICAL_HYPOTHESIS** — A proposed bridge to physics that has not been derived or empirically established.

## Editorial rules

1. Classical results must appear as prior work or background propositions.
2. A computational pass does not convert a classical identity into a new theorem.
3. Exact finite enumeration must state the ensemble, size, and equivalence relation.
4. Monte Carlo results must state seed, generator, sample sizes, and frozen gates.
5. Failed and corrective protocols remain in the repository but usually leave the main manuscript.
6. Physical identifications require an operational map, not mathematical resemblance.
7. The A-number sequence belongs in provenance and supplements, not in the main article narrative.

## Affine covariance of Q

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R047 | Q_lambda(aq+c)=c+a Q_{a lambda}(q) | PROVED ALGEBRAICALLY | POTENTIALLY ORIGINAL EMPHASIS; ALGEBRA ITSELF ELEMENTARY | EXACT_IDENTITY | The scale transformation changes the effective lambda and therefore couples score scale to the parameter. | A physical renormalization-group law. | FOUNDATIONAL | KEEP AS CORE IDENTITY | P0 |

## Analytic interval signature

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R018 | A scalar analytic interval signature failed selected null rejection | FAILED_PROTOCOL | NO NOVELTY CLAIM BEYOND DOCUMENTED FAILURE | ANALYTIC_FORMULA + MONTE_CARLO | The tested scalar signature is insufficient. | A general impossibility theorem for analytic signatures. | SUPPLEMENT_ONLY | MOVE TO FAILURE HISTORY | P3 |

## Atomicity versus terminality

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R042 | Atomicity and terminality are logically distinct | PROVED | CLEAN FRAMEWORK-SPECIFIC ILLUSTRATION OF CLASSICAL DISTINCTION | CONSTRUCTIVE_EXAMPLES | Terminal nodes and measure atoms must not be identified. | A classification of all refinement measures. | FOUNDATIONAL | KEEP AS A STRONG EXAMPLE | P1 |

## CLT status

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R054 | Central-limit convergence is asymptotic and requires independence or mixing plus tail... | CLASSICAL CONDITIONAL RESULT | CLASSICAL | CLASSICAL_THEOREM + CORRECTED NUMERICAL DIAGNOSTIC | Gaussian universality is a conditional asymptotic regime, not an automatic consequence of centering. | Exact finite-scale Gaussianity or convergence of all nonlinear observables. | FOUNDATIONAL | KEEP AS BACKGROUND FOR A37 RESULT | P1 |

## Certified obstruction

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R020 | Global interval statistics can accept orders with local non-2D obstructions | COMPUTATIONALLY CERTIFIED COUNTEREXAMPLE FAMILY | PROJECT-SPECIFIC COUNTEREXAMPLE; CONSTRUCTION MAY BE ORIGINAL | CONSTRUCTIVE_COUNTEREXAMPLE + MONTE_CARLO SEARCH | Passing the global interval statistic is not sufficient for local 2D order structure. | A complete forbidden-suborder characterization of manifold-likeness. | FOUNDATIONAL METHODS / SUPPLEMENT | KEEP AS THE MAIN LESSON OF A12-A17 | P2 |

## Clock non-uniqueness

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R013 | Internal order does not select a unique scalar clock | EXACT_FINITE_COMPUTATION | PROJECT-SPECIFIC FINITE NONUNIQUENESS RESULT | EXACT_ENUMERATION + COUNTEREXAMPLES | The condensation order alone does not choose among these natural scalarizations. | No scalar clock can ever be defined, or physical time is impossible. | COMBINATORICS + FOUNDATIONAL | KEEP AS FINITE COUNTEREVIDENCE, NOT UNIVERSAL NO-GO | P1 |

## Context-scale incompatibility

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R036 | No nontrivial continuous cardinal score satisfies both extension stability and full... | PROVED | POTENTIALLY ORIGINAL FORMULATION; HIGH-PRIORITY NOVELTY SEARCH | NO_GO_THEOREM | The three audited requirements are jointly incompatible for a nontrivial cardinal score. | No meaningful score can ever be defined, or the theorem applies outside its explicit axioms. | FOUNDATIONAL | PROMOTE TO A CENTRAL THEOREM AFTER LITERATURE REVIEW | P0 |

## Copula identifiability

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R024 | The induced order law depends on the copula, not continuous marginals | PROVED | CLASSICAL COROLLARY APPLIED TO PREGEOMETRY | DIRECT_COROLLARY OF SKLAR | Order observations cannot identify latent marginal scales within a fixed copula class. | A new copula theorem or recovery of spacetime measure from order alone. | FOUNDATIONAL | KEEP AS CLASSICAL PILLAR WITH CLEAR ATTRIBUTION | P0 |

## Covariance-aware interval signature

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R019 | A covariance-aware multivariate signature passed its targeted model checks | COMPUTATIONALLY DEMONSTRATED | PROJECT-SPECIFIC NUMERICAL RESULT | MONTE_CARLO MODEL CHECK | The signature is a useful necessary model check against those nulls. | A sufficient certificate of 2D embeddability or manifold-likeness. | SUPPLEMENT_ONLY | PRESENT ONLY TO MOTIVATE THE COUNTEREXAMPLE | P3 |

## Cumulant hierarchy

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R050 | Q_lambda depends on the cumulant hierarchy | PROVED UNDER ANALYTICITY | CLASSICAL CUMULANT EXPANSION | CLASSICAL_SERIES + NUMERICAL_APPROXIMATION | Higher cumulants explain the generic failure of mean-variance closure. | A globally convergent expansion for heavy-tailed laws. | FOUNDATIONAL | KEEP AS DERIVATION SUPPORT, NOT NEW RESULT | P1 |

## Dependence obstruction

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R057 | Shared non-Gaussian factors can block Gaussian coarse-graining | PROVED | CLASSICAL COMMON-FACTOR COUNTEREXAMPLE | ANALYTIC_COUNTEREXAMPLE | Independence or adequate mixing is a substantive requirement for Gaussian universality. | That all correlated systems fail to Gaussianize. | FOUNDATIONAL | KEEP AS ONE CLEAN COUNTEREXAMPLE | P1 |

## Duration coarse-graining

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R015 | No single multiplicative scale preserves all chain durations in the stated quotient... | PROVED | ELEMENTARY PROJECT-SPECIFIC COUNTEREXAMPLE | CONSTRUCTIVE_COUNTEREXAMPLE | Naive quotienting does not preserve all ordinal durations by a single scale factor. | A universal impossibility for every possible duration coarse-graining. | FOUNDATIONAL | KEEP AS ILLUSTRATIVE COUNTEREXAMPLE | P2 |

## Dynamic contraction identity

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R048 | Q'_lambda=(1-a) q_bar + a Q_{a lambda} | PROVED | POTENTIALLY ORIGINAL AND TECHNICALLY STRONG; NOVELTY SEARCH REQUIRED | EXACT_DYNAMIC_IDENTITY | The contraction transports the whole Q(lambda) curve by rescaling lambda. | A fundamental physical evolution equation or closure of the full RZS dynamics. | FOUNDATIONAL | PROMOTE TO CENTRAL PROPOSITION AFTER LITERATURE REVIEW | P0 |

## Dynamic non-closure

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R049 | A single Q_lambda is not generally a dynamically closed state variable | PROVED | POTENTIALLY ORIGINAL FRAMEWORK CONSEQUENCE | CONSTRUCTIVE_COUNTEREXAMPLE + EXACT_IDENTITY | One point of the Q curve is insufficient for exact dynamics in general. | No finite-dimensional closure can exist under any restricted distribution family. | FOUNDATIONAL | KEEP AS CENTRAL THEOREM/COUNTEREXAMPLE | P0 |

## Effective path cost

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R030 | D_eff scales covariantly and normalized D_hat is gauge invariant | PROVED | ELEMENTARY CONSEQUENCE OF EXPONENTIAL EDGE COSTS | EXACT_IDENTITY | D_eff is a computational round-trip relational cost defined up to global scale. | Physical distance, a Lorentzian metric, calibrated length, or spacetime geometry. | FOUNDATIONAL | KEEP WITH STRONG TERMINOLOGY CONTROL | P0 |

## Effective score

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R046 | Q_lambda is statically associative | PROVED | CLASSICAL QUASI-ARITHMETIC / LOG-SUM-EXP PROPERTY | EXACT_IDENTITY | Q_lambda is an exact static sufficient score for the corresponding partition sum. | A unique coarse-graining variable for every observable or a thermodynamic state variable. | FOUNDATIONAL | KEEP, BUT ATTRIBUTE QUASI-ARITHMETIC STRUCTURE | P0 |

## Encoding enumeration

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R008 | Count of minimum-representative quotient-poset codes | PROVED | POTENTIALLY ORIGINAL ELEMENTARY COROLLARY; SEARCH REQUIRED | COMBINATORIAL_PROOF + EXACT_ENUMERATION | The old 5,234 result exactly counts the declared intermediate code. | Calling 5,234 the number of full labeled condensation structures. | COMBINATORICS | KEEP AS CORRECTIVE PROPOSITION | P0 |

## Encoding non-injectivity

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R009 | Minimum-representative code is not injective | PROVED | PROJECT-SPECIFIC CORRECTIVE RESULT | CONSTRUCTIVE_COUNTEREXAMPLE | The earlier wording was ambiguous because the implementation discarded SCC membership information. | Calling the discrepancy fabrication or treating all A8 outputs as invalid. | COMBINATORICS + ERRATUM | KEEP PROMINENTLY AS CORRECTION | P0 |

## Endogenous symmetry breaking

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R026 | Equivariant endogenous dynamics preserve observational equivalence | PROVED UNDER STATED ASSUMPTIONS | LIKELY STANDARD GROUP-EQUIVARIANCE PRINCIPLE; PROJECT APPLICATION | EQUIVARIANCE_THEOREM | Purely endogenous equivariant evolution cannot break the targeted order-preserving symmetry. | That dynamics can never break symmetry when stochastic laws, boundary conditions, or new primitives are non-equivariant. | FOUNDATIONAL | KEEP AS CONDITIONAL THEOREM WITH GROUP-THEORY ATTRIBUTION | P1 |

## Enumeration of preorders

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R007 | Count of full labeled condensation preorders | PROVED | LIKELY CLASSICAL ENUMERATION OF FINITE PREORDERS | COMBINATORIAL_PROOF + EXACT_ENUMERATION | The formula and the n=5 count are correct for full labeled reachability preorders. | Presenting the formula as novel before checking finite-preorder literature. | COMBINATORICS | KEEP, BUT ATTRIBUTE IF PRIOR FORMULA FOUND | P0 |

## Exact n=5 counts

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R010 | Three distinct equivalence levels at n=5 | EXACT_FINITE_COMPUTATION | ORIGINAL REPRODUCTION / CORRECTIVE ENUMERATION | EXACT_ENUMERATION | These exact finite counts distinguish three well-defined quotient levels. | An asymptotic result or a physical prediction. | COMBINATORICS | KEEP AS CORE DATA TABLE | P0 |

## Exponential-family selection

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R034 | Difference-based odds and IIA select an exponential score family | PROVED UNDER REGULARITY ASSUMPTIONS | CLASSICAL LUCE / CAUCHY RESULT; ATTRIBUTE | FUNCTIONAL_EQUATION | These axioms narrow the family to exponentials but do not fix lambda. | A wholly new derivation of multinomial logit or proof that nature obeys IIA. | FOUNDATIONAL | REWRITE AS CLASSICAL THEOREM WITH PROJECT-SPECIFIC CONSEQUENCE | P0 |

## External calibration witness

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R027 | A calibrated non-invariant mark can break order degeneracy | PROVED BY CONSTRUCTION | ELEMENTARY / PROJECT-SPECIFIC | CONSTRUCTIVE_WITNESS | Additional calibrated structure can break the degeneracy. | That the required calibration has been physically derived. | FOUNDATIONAL | KEEP TO CLARIFY WHAT INFORMATION IS MISSING | P1 |

## Finite additive measure

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R040 | Positive leaf weights have a unique additive extension on a finite refinement tree | PROVED | CLASSICAL FINITE ADDITIVITY RESULT; PROJECT APPLICATION | FINITE_MEASURE_THEOREM + EXACT_TESTS | Once leaf weights are supplied, additive mass is path-independent and uniquely determined. | That terminal leaves or their weights are physically selected. | FOUNDATIONAL | RECAST AS LEMMA, MOVE LARGE TEST TABLES TO REPOSITORY | P1 |

## Finite graph observability

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R001 | Degree data do not determine the audited structural profile | EXACT_FINITE_COMPUTATION | ORIGINAL_FINITE_COMPUTATION; DEFINITIONS NEED FORMALIZATION | EXACT_ENUMERATION | Degree information is insufficient for the particular structural observables audited at n=5. | A general asymptotic theorem, or a claim that degree data never identify any relevant structure. | COMBINATORICS | KEEP AS SUPPORTING ENUMERATION; DEFINE EVERY PROFILE FORMALLY | P1 |

## Finite information compression

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R002 | Exact finite rate-distortion curves inside degree fibers | EXACT_FINITE_COMPUTATION | APPLICATION OF CLASSICAL THEORY; NO GENERAL NOVELTY CLAIM | EXACT_FINITE_OPTIMIZATION | The stated finite optimization results are exact for the declared controls. | A new general rate-distortion theorem or a physical information law. | SUPPLEMENT_ONLY | MOVE OUT OF MAIN FOUNDATIONAL NARRATIVE | P3 |

## Flow aggregation

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R062 | Joint flows aggregate exactly when occupancy is supplied | PROVED | CLASSICAL CONDITIONAL-FLOW CONSTRUCTION | EXACT_IDENTITY | Carrying joint flow or occupancy restores exact dynamic aggregation. | That the physical origin, dynamics, or uniqueness of pi is known. | FOUNDATIONAL | KEEP AS CORE POSITIVE RESULT | P0 |

## Framework architecture

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R067 | Current minimal architecture is (R,q,mu,K,pi) | CONCEPTUAL ARCHITECTURE; NOT A UNIQUENESS THEOREM | POTENTIALLY ORIGINAL SYNTHESIS | FRAMEWORK_SYNTHESIS | The framework gives a disciplined provisional inventory of information needed for order, measure, transition, and coarse-grained flow. | A proven unique ontology, a final fundamental theory, or derivation of all primitives. | FOUNDATIONAL | MAKE THIS THE POSITIVE THESIS OF THE FOUNDATIONAL PAPER | P0 |

## Gaussian closure

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R051 | Gaussian affine dynamics close exactly in mean and variance | PROVED | CLASSICAL GAUSSIAN CLOSURE | CLASSICAL_CONDITIONAL_THEOREM + SIMULATION | Mean-variance closure is exact inside the Gaussian invariant family. | That centering, finite variance, or the present RZS law derives Gaussianity. | FOUNDATIONAL | KEEP AS CONDITIONAL SPECIAL CASE | P0 |

## Gaussian selection

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R053 | Gaussianity is selected only by additional strong assumption packages | CLASSICAL CONDITIONAL RESULTS | CLASSICAL; SYNTHESIS IS FRAMEWORK VALUE | CLASSICAL_THEOREM_SYNTHESIS + REGRESSION_TESTS | The framework can list sufficient Gaussian-selection principles and identify which are currently absent. | That the present RZS dynamics derives Gaussian noise. | FOUNDATIONAL | KEEP AS SYNTHESIS; REDUCE AUDIT LOG IN MAIN TEXT | P1 |

## Heavy-tail obstruction

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R056 | Finite variance does not guarantee finite Q_lambda | PROVED | CLASSICAL; IMPORTANT APPLICATION | CLASSICAL_TAIL_RESULT + FRAMEWORK CONSEQUENCE | The partition-score formalism requires stronger tail control than finite variance. | That every heavy-tailed alternative is inadmissible for every observable. | FOUNDATIONAL | KEEP AS STRONG DOMAIN-OF-DEFINITION WARNING | P0 |

## Infinite refinement

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R041 | Consistent finite-branching refinements define a projective measure without terminal... | PROVED VIA STANDARD THEOREM | CLASSICAL KOLMOGOROV/DANIELL EXTENSION APPLICATION | CLASSICAL_EXTENSION_THEOREM + EXAMPLES | Terminal ontology is not mathematically required for a projective measure. | A new extension theorem or proof that physical reality is infinitely divisible. | FOUNDATIONAL | KEEP AS CLASSICAL PILLAR, NOT NEW THEOREM | P0 |

## Interval statistics

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R016 | Broad interval-feature classifier did not satisfy all confirmatory gates | FAILED_PROTOCOL | NO THEOREM OR NOVELTY CLAIM | MONTE_CARLO + MACHINE_LEARNING_PROTOCOL | The broad protocol was insufficient under its frozen gates. | Evidence for or against manifold emergence in nature. | SUPPLEMENT_ONLY | REMOVE FROM MAIN TEXT; RETAIN AS PROVENANCE | P3 |

## Kernel underdetermination

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R033 | Scale-free standardized q scores admit infinitely many local kernels | PROVED BY EXPLICIT INFINITE FAMILY | LIKELY ELEMENTARY UNDERDETERMINATION; PROJECT APPLICATION | CONSTRUCTIVE_FAMILY | The audited symmetry and locality principles leave the kernel law underdetermined. | That no additional axiom can select a law. | FOUNDATIONAL | KEEP AS SETUP FOR LUCE/IIA RESULT | P1 |

## Kernel-sufficient score

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R059 | Q_lambda exactly preserves the exponential kernel under grouping | PROVED | ELEMENTARY BUT CENTRAL PROJECT-SPECIFIC CONSEQUENCE | EXACT_SUFFICIENT-STATISTIC IDENTITY | Q_lambda is the exact static message for this declared observable. | The unique coarse variable for every law or a physical thermodynamic potential. | FOUNDATIONAL | KEEP AS CORE POSITIVE RESULT | P0 |

## Legacy RZS geometry

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R064 | Effective round-trip shortest-path geometry is computational, not yet physical | CONSTRUCTION VERIFIED | PROJECT-SPECIFIC CONSTRUCTION | DEFINITION + EXACT_TESTS | The construction defines an effective computational geometry up to global scale. | Physical distance, spacetime interval, calibrated length, or uniqueness. | FUTURE_GEOMETRY / FOUNDATIONAL | ARCHIVE CODE BEFORE USING IN A NEW MANUSCRIPT | P0 |

## Local-global diagnostics

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R021 | Local and global checks still admitted clustered exact 2D counterexamples | FAILED_PROTOCOL | NO GENERAL NOVELTY CLAIM | MONTE_CARLO PROTOCOL | Adding local checks did not solve the selected global-signature ambiguity. | That local diagnostics can never complement global statistics. | SUPPLEMENT_ONLY | REMOVE FROM MAIN TEXT; RETAIN AS DEVELOPMENT HISTORY | P3 |

## Median non-closure

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R060 | Mass plus weighted median is not a closed hierarchical message | PROVED | ELEMENTARY PROJECT-SPECIFIC COUNTEREXAMPLE | EXACT_COUNTEREXAMPLE | Median is robust but that scalar summary is not hierarchically closed. | No hierarchical quantile sketch or richer summary can exist. | FOUNDATIONAL / SUPPLEMENT | KEEP AS SHORT COUNTEREXAMPLE | P2 |

## Multiplicity semantics

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R039 | Relation plus q cannot distinguish descriptive clones from ontically distinct copies | PROVED UNDER REPRESENTATIONAL ASSUMPTIONS | POTENTIALLY ORIGINAL FRAMEWORK FORMULATION; BASIC LOGIC IS GENERAL | SEMANTIC_IDENTIFIABILITY_NO_GO | An additional refinement/multiplicity semantics is required to distinguish the two interpretations. | Proof that copies can never be physically distinguished by any enriched future theory. | FOUNDATIONAL | KEEP AS CORE MOTIVATION FOR mu | P0 |

## Multiscale diagnostics

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R022 | Multiscale self-similarity detects some heterogeneous regimes but not compact clustering | FAILED / PARTIAL NUMERICAL RESULT | PROJECT-SPECIFIC NUMERICAL FINDING | MONTE_CARLO PROTOCOL | The tested multiscale statistic is sensitive to some regime heterogeneity but not to all compact mixtures. | A universal multiscale no-go. | SUPPLEMENT_ONLY | KEEP AS NEGATIVE METHOD RESULT, NOT CORE THEORY | P3 |

## No-go catalogue

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R068 | The obstruction map is a framework-level contribution | SUPPORTED BY MIXED CLASSICAL AND PROJECT-SPECIFIC RESULTS | ORIGINAL ORGANIZATION; INDIVIDUAL ITEMS HAVE UNEQUAL NOVELTY | FRAMEWORK_SYNTHESIS | The catalogue clarifies which additional structures are logically needed in the current programme. | Presenting every no-go as equally deep or technically novel. | FOUNDATIONAL | KEEP, BUT TYPOGRAPHICALLY SEPARATE DEFINITIONS, CLASSICAL COROLLARIES, AND NONTRIVIAL... | P0 |

## Non-Gaussian innovations

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R052 | Centering does not Gaussianize innovations or eliminate higher cumulants | PROVED / COMPUTATIONALLY DEMONSTRATED | CLASSICAL TIME-SERIES FACT | CUMULANT_IDENTITY + MONTE_CARLO | Centered noise is not equivalent to Gaussian noise. | A universal statement about every interacting RZS graph process. | FOUNDATIONAL | KEEP AS CORRECTION TO A COMMON ASSUMPTION | P1 |

## Observable-relative coarse-graining

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R063 | There is no observable-independent unique scalar coarse-graining of q | SUPPORTED BY EXACT IDENTITIES AND COUNTEREXAMPLES | ORIGINAL SYNTHESIS; COMPONENTS MOSTLY CLASSICAL | FRAMEWORK_SYNTHESIS | A coarse-graining rule must be specified relative to the observable or dynamics it is meant to preserve. | A universal proof that no richer common state representation exists. | FOUNDATIONAL | KEEP AS CENTRAL ORGANIZING PRINCIPLE | P0 |

## Operational q kernel

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R031 | Exponential transition log-odds encode q contrasts | PROVED FOR DECLARED KERNEL | CLASSICAL MULTINOMIAL-LOGIT IDENTITY APPLIED TO q | EXACT_IDENTITY + SYNTHETIC RECOVERY | The exponential kernel makes q contrasts operational in transition odds. | That the kernel or beta follows from the RZS primitives. | FOUNDATIONAL | KEEP AS CANDIDATE MODEL WITH CLASSICAL ATTRIBUTION | P0 |

## Order encoding

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R006 | Full reachability preorder encodes SCC partition and quotient order | PROVED | LIKELY CLASSICAL / ELEMENTARY COROLLARY | DIRECT_COROLLARY | The full labeled reachability preorder is an injective representation of the complete labeled condensation structure. | That the representation is a newly discovered graph invariant. | COMBINATORICS | KEEP AS DEFINITIONAL LEMMA | P0 |

## Order from directed relations

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R005 | Condensation of a digraph defines a partial order | PROVED / STANDARD | CLASSICAL; ATTRIBUTE, DO NOT CLAIM NOVELTY | CLASSICAL_THEOREM | A directed relation canonically induces an internal quotient order through SCC condensation. | Discovery of the SCC condensation theorem, physical time, or a unique temporal arrow. | COMBINATORICS + FOUNDATIONAL | STATE AS BACKGROUND PROPOSITION | P0 |

## Order-measure identifiability

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R023 | Strict coordinatewise monotone transforms preserve product order | PROVED / DEFINITIONAL | CLASSICAL; ATTRIBUTE, DO NOT CLAIM NUMERICAL VALIDATION AS EVIDENCE | CLASSICAL_IDENTITY + SOFTWARE_REGRESSION | Order-only data are invariant under monotone recalibration of latent marginals. | A new theorem established by 270 simulations. | FOUNDATIONAL | REPLACE AUDIT EMPHASIS WITH A SHORT PROOF | P0 |

## Order-only no-go

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R025 | No deterministic order-only estimator can distinguish monotone-equivalent latent models | PROVED | DIRECT INFORMATION-THEORETIC COROLLARY; FRAMEWORK APPLICATION | IDENTIFIABILITY_THEOREM | Additional non-order information is necessary to identify latent marginal quantities. | That every physically relevant measure is forever unrecoverable from any enriched relational model. | FOUNDATIONAL | KEEP AS CENTRAL, BUT LABEL AS IDENTIFIABILITY COROLLARY | P0 |

## Ordinal durations

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R014 | Longest-chain duration is highly but not universally additive | EXACT_FINITE_COMPUTATION | ORIGINAL FINITE STATISTICS; DEFINITIONS CLASSICAL | EXACT_ENUMERATION | Longest-chain depth is the strongest audited ordinal duration candidate at this finite size. | Proper time, a physical metric, exact additivity in general, or continuum scaling. | COMBINATORICS + FOUNDATIONAL | KEEP SELECTED NUMBERS IN COMBINATORICS PAPER | P1 |

## Partial noise universality

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R055 | Matched mean and variance universalize low-order linear observables but not... | CONDITIONAL MODEL RESULT | PROJECT-SPECIFIC SYNTHESIS OF CLASSICAL LINEAR-PROCESS FACTS | ANALYTIC_CUMULANTS + MONTE_CARLO | Noise details can be dispensable for some observables and essential for others. | Universality of the full RZS graph dynamics. | FOUNDATIONAL | KEEP AS QUALIFIED OBSERVABLE-DEPENDENCE RESULT | P1 |

## Partition-sum weights

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R044 | W_lambda(B)=sum mu_l exp(-lambda q_l) is exactly projective and gauge covariant | PROVED | CLASSICAL LOG-SUM-EXP / PARTITION-FUNCTION ALGEBRA APPLIED TO FRAMEWORK | EXACT_IDENTITY + ENUMERATIVE TEST | This weight is an exact static projective message for the chosen exponential law. | Thermodynamic energy, physical temperature, or a derived fundamental law. | FOUNDATIONAL | KEEP AS BRIDGE TO Q_lambda | P0 |

## Perturbation sensitivity

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R011 | Single-edge flip changes the n=5 condensation preorder with probability 75/256 | EXACT_FINITE_COMPUTATION | POTENTIALLY ORIGINAL FINITE STATISTIC | EXACT_ENUMERATION | The fraction is exactly 75/256 for the declared finite ensemble. | A general formula, limiting probability, or universal robustness constant. | COMBINATORICS | KEEP AS OPEN-PROBLEM MOTIVATION | P0 |

## Projective branch fractions

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R043 | Exact regrouping consistency gives conditional ratios of additive weights | PROVED | CLASSICAL CONDITIONAL-PROBABILITY STRUCTURE | MEASURE-THEORETIC IDENTITY | Projective regrouping selects the ratio architecture once W is given. | That projectivity selects the terminal weights or their physical origin. | FOUNDATIONAL | STATE AS CONDITIONAL-MEASURE LEMMA | P0 |

## Projective graph laws

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R003 | Finite projective-family polytope is a simplex | PROVED_FOR_DECLARED_FINITE_SYSTEM | LIKELY DIRECT COROLLARY OF PROJECTIVE KERNEL CONSTRUCTION | PROOF + EXACT_ENUMERATION | Finite projectivity alone leaves the top-level distribution unconstrained and therefore does not select a unique law. | That projectivity never constrains infinite families, or that the result is a new extension theorem. | FOUNDATIONAL | RECAST AS A SHORT PROPOSITION WITH PRIOR-WORK ATTRIBUTION | P2 |

## Quasi-arithmetic coarse-graining

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R058 | Translation-covariant decomposable quasi-arithmetic means reduce to arithmetic or... | CLASSICAL UNDER REGULARITY ASSUMPTIONS | CLASSICAL KOLMOGOROV-NAGUMO/ACZEL RESULT | CLASSICAL_CHARACTERIZATION + NUMERICAL_CHECKS | The audited regular mean class contains two translation-covariant families relevant to the framework. | A new classification theorem or uniqueness of a physical coarse-graining. | FOUNDATIONAL | REWRITE AS CLASSICAL THEOREM WITH CONSEQUENCES | P0 |

## Refinement boundary

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R038 | Weighted standardization is singular at zero variance and not uniformly stable near... | PROVED / DEMONSTRATED | PROJECT-SPECIFIC BOUNDARY OBSTRUCTION | CONSTRUCTIVE_COUNTEREXAMPLE + LIMIT_ANALYSIS | The proposed standardized message needs an explicit nondegeneracy domain or a different boundary treatment. | That all weighted coarse-graining is unstable. | FOUNDATIONAL | KEEP AS TECHNICAL LIMIT OR APPENDIX RESULT | P2 |

## Refinement with base measure

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R037 | Additive base measure restores exact clone/refinement invariance for weighted messages | PROVED AWAY FROM SINGULAR BOUNDARY | LIKELY STANDARD WEIGHTED-MEASURE COROLLARY | EXACT_IDENTITY + COMPUTATIONAL_TEST | Base-measure weighting removes naive clone-count dependence. | That the origin or physical semantics of mu are derived. | FOUNDATIONAL | KEEP POSITIVE IDENTITY; REPORT OVERALL FAILURE HONESTLY | P1 |

## Regge eligibility

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R065 | Local simplicial consistency did not establish robust Regge curvature | NEGATIVE / BLOCKED RESULT | PROJECT-SPECIFIC NEGATIVE RESULT | COMPUTATIONAL_PROTOCOL | Robust Regge curvature and promotion to GR remain blocked. | Emergent gravity, Einstein equations, physical curvature, or successful renormalization. | FUTURE_GEOMETRY / REPOSITORY_ONLY | DO NOT INCLUDE AS POSITIVE THEORY CLAIM | P0 |

## Relational clocks

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R012 | Candidate clocks are monotone on comparable pairs | FINITE-CASE VERIFIED; GENERAL PARTS MOSTLY STANDARD | MOSTLY CLASSICAL POSITIVITY/MONOTONICITY | PROOF/ALGORITHMIC CHECK + EXACT_ENUMERATION | These functions provide legitimate ordinal coordinates on comparable pairs. | A unique clock, calibrated time, physical duration, or preferred temporal orientation. | COMBINATORICS + FOUNDATIONAL | COMPRESS TO DEFINITIONS AND ONE NONUNIQUENESS RESULT | P1 |

## Relative quantitative field

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R028 | An independent q field can evade the order-only identifiability limit | PROVED CONDITIONALLY | FRAMEWORK-SPECIFIC CONSEQUENCE | CONDITIONAL_PROPOSITION | q can supply relative quantitative information absent from order. | That the physical origin or empirical meaning of q has been derived. | FOUNDATIONAL | KEEP AS CORE DEFINITIONAL STEP | P0 |

## Scale degeneracy

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R032 | Raw q scale and exponential strength are jointly degenerate | PROVED | STANDARD PARAMETERIZATION DEGENERACY | EXACT_IDENTIFIABILITY_ARGUMENT | Only the product of raw-score scale and coupling strength is identifiable without calibration. | That lambda is always pure gauge after any normalization. | FOUNDATIONAL | KEEP AS SHORT IDENTIFIABILITY LEMMA | P1 |

## Scientific boundary

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R069 | No physical spacetime, calibrated metric, gravity, or experimental mapping has been... | ESTABLISHED SCOPE BOUNDARY | NO NOVELTY CLAIM | SCIENTIFIC_STATUS / NONCLAIM | The work is a formal pre-categorical research programme with explicit open physical bridges. | Confirmed fundamental physics, emergent GR, matter, energy, or experimental support. | FOUNDATIONAL | KEEP AS A SHORT BOUNDARY SECTION, NOT A DEFENSIVE REFRAIN | P0 |

## Source occupancy obstruction

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R061 | A micro kernel and partition do not determine a unique macro transition without source... | PROVED | CLASSICAL KEMENY-SNELL/LUMPABILITY CONSEQUENCE | CLASSICAL_MARKOV_AGGREGATION FACT + NUMERICAL WITNESS | Occupancy or a lumpability condition is necessary for a unique macro Markov kernel. | A new discovery of lumpability or proof that pi is a fundamental physical field. | FOUNDATIONAL | KEEP AS CLASSICAL PILLAR FOR pi | P0 |

## Status of lambda

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R035 | After local standardization, lambda is an identifiable dimensionless model parameter... | CONDITIONAL / COMPUTATIONALLY SUPPORTED | PROJECT-SPECIFIC MODEL-STATUS RESULT | IDENTIFIABILITY_PROPOSITION + MONTE_CARLO | lambda is not removable after standardization and must be estimated or derived separately. | A fundamental constant or a value predicted by the current theory. | FOUNDATIONAL | KEEP AS STATUS RESULT; MOVE RMSE DETAILS TO SUPPLEMENT | P1 |

## Symmetry and law selection

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R004 | Exchangeability and projectivity do not select a unique graph law | PROVED_BY_EXPLICIT_FAMILY | CLASSICAL COUNTEREXAMPLE / DIRECT APPLICATION | CONSTRUCTIVE_COUNTERFAMILY | The listed symmetries and finite projectivity are insufficient for unique law selection. | A claim that no additional principled axiom could select a law. | FOUNDATIONAL | KEEP AS A SHORT CLASSICAL COUNTEREXAMPLE | P2 |

## Targeted synthetic discrimination

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R017 | Selected interval features discriminate 2D sprinklings from selected nulls | COMPUTATIONALLY DEMONSTRATED | PROJECT-SPECIFIC NUMERICAL RESULT | MONTE_CARLO + CLASSIFIER | The feature family has targeted discriminatory power for these models. | A necessary or sufficient test for manifold-likeness. | SUPPLEMENT_ONLY | SUMMARIZE BRIEFLY OR OMIT FROM FOUNDATIONAL PAPER | P3 |

## Weight underdetermination

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R045 | Projectivity does not determine terminal weights or their ontology | PROVED BY COUNTERFAMILY | GENERAL MEASURE-THEORETIC FACT / FRAMEWORK CONSEQUENCE | CONSTRUCTIVE_UNDERDETERMINATION | Consistency constrains how weights combine, not which weights nature uses. | That no physical or statistical principle could determine weights. | FOUNDATIONAL | KEEP AS CENTRAL LIMIT | P1 |

## q gauge

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R029 | Global q offset is unobservable under contrast-only constructions | PROVED | DEFINITIONAL; NO NOVELTY CLAIM | DIRECT_COROLLARY FROM DEFINITIONS | The current construction determines q only up to a global offset. | A deep independent no-go, or proof that nature has this gauge. | FOUNDATIONAL | STATE AS CONTRACT, NOT DISCOVERY | P0 |

## q-topology coherence

| ID | Claim | Mathematical status | Novelty status | Evidence | Allowed claim | Forbidden overclaim | Target | Action | Priority |
|---|---|---|---|---|---|---|---|---|---|
| MF-R066 | Prospective q-topology coherence signature passed its declared v12.9 gates | COMPUTATIONALLY DEMONSTRATED FOR DECLARED PROTOCOL | PROJECT-SPECIFIC NUMERICAL RESULT | PROSPECTIVE COMPUTATIONAL_TEST | The specific q-topology coherence signature generalized prospectively within the tested ensemble. | Physical topology, spacetime emergence, curvature, or experimental validation. | FUTURE_GEOMETRY / SUPPLEMENT | ARCHIVE AND CLASSIFY BEFORE CITATION | P1 |

## Immediate workflow

1. Run dedicated novelty searches for P0 candidate results.
2. Create a reproducibility contract for every canonical audit.
3. Split the combinatorics and foundational manuscripts using the `target_manuscript` field.
4. Move audit chronology, large gate tables, and regression checks to the repository or supplement.
5. Seek a general formula or asymptotic theory for the edge-flip probability `P_n`.
6. Rewrite each abstract only after the claim set for that manuscript is frozen.

## Machine-readable files

- `RESULT_CLASSIFICATION.csv` — complete flat matrix.
- `RESULT_CLASSIFICATION.json` — structured copy.
- `RESULT_CLASSIFICATION_SUMMARY.json` — aggregate counts and priority list.
- `RESULT_CLASSIFICATION.xlsx` — formatted review workbook.
