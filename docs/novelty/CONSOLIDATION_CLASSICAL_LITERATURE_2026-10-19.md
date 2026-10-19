# Classical literature checkpoint — 2026-10-19

**Status:** bibliographic and scope check only. This is **not** an exhaustive novelty
review, a theorem-by-theorem proof comparison, or a priority certificate.

## Why this note exists

The mathematical core combines elementary labeled-digraph facts, finite
probability, moment-constrained optimization, exponential functions, and
arithmetic phase effects. Those fields have established literature.
A project-specific formulation is not automatically a novel theorem. Conversely,
a classical technique does not automatically subsume a more restricted later
theorem. Both conclusions require an explicit statement-level comparison.

## Verified bibliographic anchors

| Source | Established prior subject | Relevant project claims | What has **not** been established |
|---|---|---|---|
| Uno and Ibaraki (1998) | Random directed-graph fixed-pair reachability and exact probability computation | MF-R011 / C1.3 | Whether the exact fraction `75/256` or project normalization was previously written down |
| Qin et al. (2017) | Edge influence through reachability changes under edge deletion | MF-R011 / C1.3 | Identity between their practical influence statistic and the project's uniform edge-toggle probability |
| Karlin and Studden (1966) | Tchebycheff systems and related moment/variation methods | C3/C4 analytic proof toolkit | That their results imply the specific frozen-KKT or target-deformation theorems without additional work |
| Winkler (1988) | Extreme points of sets of measures with generalized moment constraints | C3 moment-constrained optimization | Exact equivalence to the project's source/target KKT phase classification |
| Prékopa (1990) | Discrete moment problems and linear-programming sharp bounds | C3 moment/LP architecture | The project's particular active basis, threshold, determinant, or parameter-window results |

### Primary bibliography and verification links

1. Uno, Y. and Ibaraki, T. (1998). "Reachability Problems of Random Digraphs."
   *IEICE Transactions on Fundamentals*, E81-A(12), 2694–2702.
   Publisher index: https://globals.ieice.org/en_transactions/fundamentals/E81-A_12

2. Qin, Y., Sheng, Q. Z., Parkinson, S., and Falkner, N. J. G. (2017).
   "Edge Influence Computation in Dynamic Graphs." *DASFAA*, LNCS 10178,
   649–660. DOI: https://doi.org/10.1007/978-3-319-55699-4_41

3. Karlin, S. and Studden, W. J. (1966). *Tchebycheff Systems: With
   Applications in Analysis and Statistics*. Interscience/Wiley, New York.
   Catalog: https://search.worldcat.org/title/1034156

4. Winkler, G. (1988). "Extreme Points of Moment Sets." *Mathematics of
   Operations Research*, 13(4), 581–587.
   DOI: https://doi.org/10.1287/moor.13.4.581

5. Prékopa, A. (1990). "The Discrete Moment Problem and Linear Programming."
   *Discrete Applied Mathematics*, 27(3), 235–254.
   DOI: https://doi.org/10.1016/0166-218X(90)90068-N

The listed records establish existence, author/title metadata, scope, and
publication precedence for general subject matter. Except where the cited
abstract expressly states a problem, this note does not assert that a
particular lemma appears on a particular page. Verifying exact theorem
numbers and hypotheses still requires inspecting the full text.

## Mandatory attribution boundaries

### C1.3

The formula

`P_n = 2 * Pr(s does not reach t)`

reduces the declared sensitivity event to classical fixed-pair reachability
under the uniform independent-edge ensemble. It does not establish original
discovery of fixed-pair reachability, graph edge influence, or a general
random-digraph reachability method. The priority of the specific finite value
remains **not certified**.

### C3/C4

Moment-set extremal structure, linear-programming duality, and Tchebycheff
systems already have substantial prior literature. A113, A114, and A115–A119
must be compared at the exact level of hypotheses, contact geometry, source
window, target deformation, and conclusions. Reusing classical machinery is
not in itself a novelty failure; relabeling classical conclusions would be.

### C5

A120–A122 derive project-specific phase and resonant expansions. This small
literature checkpoint does **not** establish that their exact statements are
absent from prior asymptotic, discrete optimization, or Diophantine literature.
An independent statement-level prior-art search remains open.

## Comparison procedure before making a novelty claim

For each claim, record:

1. exact project theorem statement and hypotheses;
2. the closest older theorem in its original notation and full-text location;
3. a translation between the assumptions, including all parameter and
   support restrictions;
4. whether the earlier theorem proves, contradicts, or merely motivates the
   project claim;
5. any genuinely additional hypothesis or conclusion;
6. an external specialist's review or unresolved uncertainty.

The only safe general classification from this checkpoint is
`NOVELTY_NOT_CERTIFIED`. A literature search that finds no matching statement
cannot by itself establish priority.
