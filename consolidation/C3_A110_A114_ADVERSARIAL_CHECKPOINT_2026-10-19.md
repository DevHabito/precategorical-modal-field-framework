# C3 / A110–A114 — adversarial assurance checkpoint

**Date:** 2026-10-19  
**Status:** independent finite regression PASSED in GitHub Actions run
[39339986503](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39339986503);
full analytic and theorem-level originality review remain OPEN.
This is NOT a clean-room proof or a general certificate for A110–A114.

## 1. Frozen problem contract

The promoted analytic-tail results use:

- integer `M >= 521`;
- real `129/1000 <= s <= 133/1000`;
- `beta = 1/8`, `gamma = 1/16`, `tau = 1/2`;
- `h = floor(M/2)`;
- source-dependent parity-normalized tolerance
  `epsilon = 1 / (1875 * 2^h)` for even `M`,
  `epsilon = 1 / (2500 * 2^h)` for odd `M`;
- `b = ceil(M * log(2)/(-2*log(s)))`.

The first audit tool computes `b` by exact rational binary search, using
`s^(2b) <= 2^(-M) < s^(2(b-1))`. No logarithmic floating-point
comparison selects a contact.

**Contact domain matters.** The source A84 adjacent-factor contract
explicitly uses `2 <= k < floor(M/2)-1`. Statements about
`E_(M,k)` on this domain must NOT silently be extended to arbitrary
algebraic values of `k`. For example, the formula degenerates at
`k=M-1`, which is outside the declared domain and cannot falsify a
strict-sign result on admissible contacts.

## 2. Different optimization problems: do not conflate them

### A113 — compressed objective only

Set `E_k = V_(k+1)-V_k` up to the orientation-positive cofactor
normalization of A84. The frozen theorem claims

- `E_k > 0` for admissible `k <= b`;
- `E_k < 0` for admissible `k >= b+3`;
- `E_(b+1) - 2*E_(b+2) > 0`.

The central inequality prohibits a negative-to-positive second change
between the two central increments. Conditional on the complete uniform
remote-sign claims, it implies exactly one compressed sign variation and
a maximizing contact among `b+1,b+2,b+3`.

The unproved stronger inequality
`E_(b+1)-E_(b+2)>0` is false. It must not be substituted for the
published nesting inequality.

### A112 — strict gamma-plus lifted basis

The A112 theorem applies to the frozen
`P={0,j,j+1,M}`, `Q={1,h,h+1}`, gamma-plus architecture **inside a
strict compressed-maximizer phase for the fixed `j`**. Within those
premises, strict KKT is equivalent to
`p_j > 0` and `p_(j+1) > 0`.
It does NOT say that a contact index `j=b+1` or `j=b+2` alone
guarantees the q2 reduced-cost gate.

A112 locality additionally excludes a strict gamma-plus lift at `j=b+3`;
that case requires a different family.

### A114 — full lifted LP active-set decision

A114-A covers strict compressed `b+3` through an endpoint-released basis;
B1 covers strict `b+1`; B2-A/B/C/D/E cover strict `b+2` including
named inner and outer equality boundaries.

These theorems are **conditional on the exact frozen band/target/source
contract**. Compressed maximality is not full KKT feasibility. Some
A114 records dated September 13 explicitly call boundaries OPEN;
the later September 14 theorem files and the current A114 README
supersede those *status labels*. The historical files are retained.

In particular, A114's own README says that the separate surfaces of
non-strict **compressed maximizer ties** must be handled by A114-C1/C2
and do not follow just from its strict-phase theorem. Do not
interpret a strict-phase classification as a classification of an
unrestricted parametric LP.

## 3. Independently executed exact falsification controls

`tools/independent_c3_adversarial_checks.py` contains an independently
written `Fraction` oracle for the A84 adjacent cofactor, an independent
seven-equation linear solve for the compressed objective, and a separate
eight-equation gamma-plus primal/dual solve for the q2 reduced cost.

The first three reported controls were independently calculated before
adding the CI script. The CI is a separate acceptance gate.

| Frozen exact control | Observed fact | Correct interpretation |
|---|---|---|
| `M=561, s=129/1000, b=95` | `E_(b+2)>0` | Compressed `b+3` phase exists |
| `M=661, s=129/1000, b=112` | `E_(b+3)<0` | Reject historical false-positive numerical alarm |
| `M=2049, s=133/1000, b=353` | `E_(b+1)<0`, `E_(b+2)<0`, `E_(b+1)-E_(b+2)<0`, yet `E_(b+1)-2E_(b+2)>0` | Stronger second-secant conjecture is false |
| `M=821,886,951; s=129/1000` | `E_(b+2)>0` despite `3(b+2)-h>=13` | Reject A114-C2's abandoned dyadic shortcut |
| `M=600, s=133/1000, j=b+2=106` | `p_j>0`, `p_(j+1)<0`, `R_Q(2)<0` | Contact localization alone is insufficient for A112's q2 gate |

The oracle also scans the **full admissible contact interval**
`2<=k<h-1` for a finite set of predeclared odd/even supports and
endpoints, checking the remote signs, single sign variation and central
nesting. The normalized factor's sign is independently cross-checked
against the exact compressed LP objective difference at four consecutive
central contacts on each published-control instance.

These checks are finite, not a proof for every `M>=521` or every real
source in the interval.

### Failed test gate preserved

The first CI run of the new checker failed because its test harness
incorrectly assumed `E_(b+2)>0` at `M=661`. The published control
at that size only requires `E_(b+3)<0`, and exact computation gives
`E_(b+2)<0` there. A follow-up commit replaced the unjustified
all-cases sign assertion with case-specific exact expected signs.
No historical result was altered to recover a PASS.

The corrected independent-audit job **passed** in GitHub Actions
run `39339986503`. The exact log reports six archived negative-control
replications, the source-contact counterexample at M=600, and complete
one-variation over **2140 admissible adjacent factors** across five
frozen finite support/source cases. These remain finite checks.

### Additional pointwise lifted KKT reconstruction

The checker also reconstructs A114-B2-W1 directly at
`M=521, s=129/1000` using:
`P={90,91,521}`, `Q={0,1,260,261}`,
and the active signs `alpha+`, `beta-`, `gamma-`.
It solves the eight exact LP equations and the transposed dual system
independently of historical theorem scripts, then checks all nonbasic
P/Q atom reduced costs, active multipliers, opposite inactive slacks,
primal positivity, and primal-dual equality.

The same control's compressed maximizer is `j=b+2=91`, while the
naive gamma-plus lift has `p_(j+1)<0`. This demonstrates *at one point*
why a compressed optimum cannot be equated with a lifted feasible
basis. It does not prove A114's universal tail active-set map.
This added regression is a **separate CI gate** and must not be
described as passed until its run finishes successfully.

## 4. Independent Lean boundary (conditional logic only)

`PrecategoryFormal/CompressedCentralNesting.lean` isolates the
elementary implication

`E_(b+1)-2*E_(b+2)>0`

`=>` the pair `(E_(b+1),E_(b+2))` cannot move from nonpositive
to nonnegative. It also provides an exact rational counterexample to
the stronger, invalid inference that the second secant must be positive.

**These Lean lemmas do not prove the analytic input inequality**
`E_(b+1)-2*E_(b+2)>0` throughout the frozen tail. A successful
Lean build cannot be promoted to "A113 universally formalized."

## 5. Upstream theorem-level proof obligations still open

1. Reconstruct A112's Cramer signs and determinant-resultant
   orientations from the original LP equations, without importing
   historical cached numerators as axioms.
2. Verify A112's generalized-Vandermonde and extended-Chebyshev
   hypotheses and use of Descartes with all multiplicities and coefficient
   sign orders stated explicitly.
3. Reconstruct the exact A113 ten-term factor from the raw compressed LP;
   then independently certify the uniform tail remainders and each
   logarithmic/dyadic envelope on the entire real source window.
4. Check A114's KKT dual multipliers, all nonbasic reduced costs,
   inactive slacks and optimal-face dimensions at strict branches and
   equality boundaries. Ill-conditioned matrices forbid float64 sign gates.
5. Independently validate the strict/non-strict quantifier partition
   and determine whether the current A114-C1/C2 tie results cover every
   tie permitted by the compressed objective.
6. Compare each theorem statement, not just themes, to classical work
   on moment-set extreme points, discrete moment LPs, and Tchebycheff
   systems. Novelty is not certified.

## 6. Prior literature: verified broad scope, unresolved direct comparison

- Karlin and Studden (1966), *Tchebycheff Systems: With Applications in
  Analysis and Statistics*, Interscience: pre-existing theory of
  Tchebycheff systems, moment spaces and principal representations.
  https://books.google.com/books/about/Tchebycheff_Systems.html?id=pAmVzwEACAAJ
- Winkler (1988), "Extreme Points of Moment Sets",
  *Mathematics of Operations Research* 13(4), 581–587:
  characterization of extreme points under finitely many generalized
  moment constraints, and optimization of affine functionals.
  https://doi.org/10.1287/moor.13.4.581
- Prékopa (1990), "The Discrete Moment Problem and Linear Programming",
  *Discrete Applied Mathematics* 27(3), 235–254: finite-support
  discrete moment bounds formulated as LPs, including dual-basis
  structural results in specified moment families.
  https://doi.org/10.1016/0166-218X(90)90068-N

These primary bibliographic records establish **precedence of the
general techniques**, not whether they prove or refute the exact
A112–A114 frozen sign conditions and phase classification. A complete
theorem-by-theorem full-text comparison has not yet been performed.

## Release status

**Not certified for promotion.** This document records an explicit
contract, falsification controls, a conditional Lean extraction and
an unclosed analytic/literature audit. It does not announce a new
mathematical discovery or a physical law.
