# A115–A122: independent-paper feasibility and originality gate

**Date:** 2026-11-06  
**Base:** `main` at `89e2668c3aef3fbff5a7f399f86de7d27e467da1`  
**Status:** preliminary, critical review; NOT a novelty certificate or independent proof verification.  
**Purpose:** stop result accumulation and test whether the existing theorems justify a self-contained mathematical paper.

## 1. Precise object (not a physical model)

The earlier A110–A114 literature-positioning note expresses the underlying optimization problem as a ratio of finite-support probability-generating transforms, `G_mu(tau)/G_nu(tau)`, with matched first moments and bilateral transform-difference constraints. This reformulation must be reproduced explicitly in any independent manuscript; architecture labels alone do not define an externally reviewable problem.

The A115–A122 files specialize to `beta=1/8`, `delta=1/1875`, `s in [129/1000,133/1000]`, and deformed target `tau`. These values are **fixed hypotheses**, not experimentally fitted universal constants. Explain their provenance or consider separately whether statements extend to an open parameter region. Do not generalize without proof.

## 2. Dictionary for a prospective paper

| Internal expression | Mathematical meaning | Role |
|---|---|---|
| `M`, `h=floor(M/2)` | support truncation / midpoint index | large parameter |
| `s`, `beta`, `tau` | transform evaluation nodes in (0,1) | parameters |
| `delta`, `epsilon_tau,M` | prescribed band width and normalized tolerance | hypotheses |
| `G_mu(r)=sum_x mu_x r^x` | discrete Laplace/probability-generating transform | classical definition |
| `E_M,k` | reduced adjacent-factor expression from the exact finite optimization | derived project object; define from scratch |
| `J_tau,k=E_M,k-tau^(-1)E_M,k+1` | adjacent-factor comparison | project object |
| `c=log(tau)/(2 log(s))` | moving contact fraction | asymptotic coordinate |
| `b_M=ceil(Mc)`, `rho_M=b_M-Mc` | discrete contact and ceiling phase | arithmetic effect |
| `tau_M=s+lambda/M` | collision scaling | boundary-layer coordinate |
| `Lambda_p`, `Xi_p` | first and second collision-layer coefficients | derived quantities |
| `Phi_p(x)=P_p s^x-Q_p` | fixed-interior limiting sign front | derived quantity |
| `Omega_p(x)` | next algebraic correction | derived quantity |

The manuscript must distinguish a `J` comparison, a sign statement about `E`, a local extremum, and a **global** optimizer. These are not interchangeable.

## 3. Dependency and claim ledger

| Group | What the repository states | Publication gate |
|---|---|---|
| A115 | exact target deformation and cancellation | independently derive coefficients and factor contract |
| A116 | compact-interior eventual positivity; non-uniform collision boundary | check uniform error terms and negative boundary certificate |
| A117 | parity-specific collision cells and `M N_M -> Lambda_p` | inspect resonant half-open endpoints; check both parities |
| A118 | `N_M=Lambda_p/M+Xi_p/M^2+o(M^-2)` | independent algebraic verification |
| A119 | `Xi_p>0` on critical surfaces by rational interval exhaustion | rerun code, independently inspect interval inclusion and tail exclusion |
| A120 | rounding-phase formula and infinitely often sign reversals | separate new model-specific asymptotic from classical irrational-rotation equidistribution |
| A121 | sign staircase and two-adjacent-site **local** behavior | avoid claiming global maximizer; verify passage from limiting signs to finite signs |
| A122 | `Phi_p(x_M)+Omega_p(x_M)/M` with superalgebraic remainder; conditional near-resonant drift | verify dependence on moving phase; never infer an arithmetic resonant subsequence from a continuous critical root |

These summaries describe **repository claims**, not independent validation of every theorem.

## 4. Literature: verified close neighbors and attribution boundaries

1. A. Charnes and W. W. Cooper, “Programming with Linear Fractional Functionals,” *Naval Research Logistics Quarterly* **9** (1962), 181–186. DOI: https://doi.org/10.1002/nav.3800090303 . Classical fractional-programming transformation; already discussed in the repository's A110–A114 positioning note.
2. T. Gal and J. Nedoma, “Multiparametric Linear Programming,” *Management Science* **18** (1972), 406–422. DOI: https://doi.org/10.1287/mnsc.18.7.406 . Classical parametric basis-change context; already discussed in the repository.
3. A. Prékopa, “The discrete moment problem and linear programming,” *Discrete Applied Mathematics* **27** (1990), 235–254. DOI: https://doi.org/10.1016/0166-218X(90)90068-N . Classical finite-moment LP context; already discussed in the repository.
4. M. N. Huxley, “Exponential Sums and Rounding Error,” *Journal of the London Mathematical Society* **43** (1991), 367–384. DOI: https://doi.org/10.1112/JLMS/S2-43.2.367 . Verified bibliographic/abstract-level neighbor involving rounding and resonances, **not** an identified exact match to A120–A122.
5. M. F. de Almeida and J. T. V. P. Cruz, “Teorema da distribuição uniforme de sequências,” *ReviSeM* **8** (2023), 37–47. https://ri.ufs.br/handle/riufs/22663 . Exposition of Weyl's classical equidistribution theorem; irrational rotation density/equidistribution is **not** a new contribution.
6. NIST Digital Library of Mathematical Functions, section 2.8(vi), coalescing transition points, https://dlmf.nist.gov/2.8.vi . General neighboring uniform-asymptotic literature, **not** evidence that this particular LP asymptotic is already known.

**Search status:** selective comparison only. Full-text theorem-by-theorem novelty search, citation chasing, and a specialist review remain OPEN. Absence of an exact match in these references is not proof of originality.

## 5. Independent computational smoke test (run 2026-11-06)

A separate Python `fractions.Fraction` calculation reconstructed the A122 audit's published definitions `B`, `dB`, `dt`, `E`, exact power-comparison contact `b_M`, normalized factor `N`, and polynomial core `C`. This is an **independent short transcription of the formulas**, not a rerun of the repository's full audit and not a proof.

Inputs: `s=131/1000`, `tau=1/5`; the three even `M` controls were:

| M | exact contact b | sign(N) | sign(C) | approximate abs(N-C) |
|---|---:|---:|---:|---:|
| 120 | 48 | negative | negative | 0.001458519633276369 |
| 240 | 96 | negative | negative | 0.00005672742062767629 |
| 480 | 191 | negative | negative | 0.0000006865067202281025 |

Each sign and subtraction was evaluated with exact rational arithmetic; decimals above are display conversions only. These observations are compatible with the stated limiting-core behavior, but **do not independently establish** the claimed all-orders remainder or certify the A122 theorem. Notice that none of these three finite checks satisfies the much stronger `|R|<M^-3` bound: do not read the asymptotic claim as a finite uniform error bound.

## 6. Proposed independent paper

**Working title:** *Collision Layers and Arithmetic Rounding Phases in a Constrained Exponential-Moment Optimization Problem*.

Proposed argument order:
1. Explicit finite measure problem and assumptions; no internal A-number dependencies.
2. Exact reduced-factor identity, proved with an independent derivation.
3. Uniform interior asymptotic theorem, with precise compact-set quantifiers.
4. Collision-layer theorem and parity-resolved contact cells.
5. Critical-sign theorem, only after independent replay of A119's covering certificate.
6. Fixed-interior rounding-phase limit, sign front, and near-resonant drift.
7. Limitations, explicit counterexamples, classical attributions, reproducibility.

Prefer a smaller self-contained theorem package over a narrative claiming eight separate discoveries. Do **not** submit until technical and originality gates are satisfied.

## 7. Open blockers, falsification tests and epistemic controls

- **BLOCKED:** no independent full re-execution of A115–A122 audit scripts or Lean 4 verification in this review.
- **BLOCKED:** no external specialist priority/novelty confirmation.
- **BLOCKED:** a continuous double-critical point is not proof of any discrete resonant subsequence.
- **OPEN:** quantify dependence on the deliberately narrow `s` interval and fixed `beta,delta`.
- **OPEN:** reproducible bounded-error certificate for all rational boxes in A119, including correct interval dependency and finite-to-infinite tail transition.
- **OPEN:** check the exact parent optimization and dual-admissibility assumptions before presenting `E` signs as optimizer statements.
- **OPEN:** independent symbolic differentiation and the parity-odd critical surface.
- **OPEN:** compare stronger primary literature on exponential Chebyshev systems, finite Markov moment problems, parametric optimization, and lattice oscillation.

**Editorial verdict:** potentially viable as a model-specific mathematical article, but contribution not established as novel and its full proof chain not independently verified. A119/A122 arithmetic certificates deserve priority over additional conjectures. MF-R049 and RP-U004 should remain separate manuscripts; they are not evidence for A115–A122.
