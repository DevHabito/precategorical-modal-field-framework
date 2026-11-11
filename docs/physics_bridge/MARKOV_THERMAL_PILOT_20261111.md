# Markov Thermal Pilot — first controlled physical bridge

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite diagnostic + literature-grounded interpretation  
**Physical status:** no empirical validation and no claim of new stochastic thermodynamics

## 1. Question

The repository currently uses the provisional informational architecture

$$
\mathcal M=(R,q,\mu,K,\pi).
$$

Here \(R\) is relational structure, \(q\) is a quantitative mark, \(\mu\) is additive mass or multiplicity, \(K\) is a transition law, and \(\pi\) is source occupancy.

Physics does not owe the framework five independent primitives. The first bridge therefore asks:

> In an established finite Markov jump model, which of \(R,q,\mu,K,\pi\) are independent, which are derivable, and which are only alternative representations of the same physical information?

The purpose of the pilot is to make the framework lose unnecessary structure if physics permits it.

## 2. Why a Markov jump process is the first test

Stochastic thermodynamics already provides operational meanings for states, allowed transitions, transition rates, occupation probabilities, equilibrium, nonequilibrium steady states, currents, and coarse-graining.

That makes it a safer first bridge than spacetime. The variables can be compared with established physical objects before any pregeometric interpretation is attempted.

## 3. Exact reversible model

Consider three states \(0,1,2\). Work in units with

$$
\beta=\log 2
$$

and use the candidate state potential

$$
q=(0,1,2).
$$

The positive off-diagonal rates are

$$
W=
\begin{pmatrix}
0&4&1\\
8&0&3\\
4&6&0
\end{pmatrix}.
$$

The exact stationary distribution is

$$
\pi^{\rm eq}
=
\left(
\frac47,\frac27,\frac17
\right).
$$

For every unordered pair \(i,j\),

$$
\pi_i^{\rm eq}W_{ij}
=
\pi_j^{\rm eq}W_{ji}.
$$

The corresponding exact pair flows are \(16/7\), \(4/7\), and \(6/7\).

The rate ratios are

$$
\frac{W_{01}}{W_{10}}=\frac12,\qquad
\frac{W_{12}}{W_{21}}=\frac12,\qquad
\frac{W_{02}}{W_{20}}=\frac14.
$$

Because \(\beta=\log 2\),

$$
\frac{W_{ij}}{W_{ji}}
=
e^{-\beta(q_j-q_i)}
=
2^{-(q_j-q_i)}.
$$

Inside this reversible sector, \(q\) is therefore not independent of \(K\): the edge ratios determine the potential differences up to one additive constant.

This is classical detailed-balance structure. The project-specific role of the calculation is diagnostic, not a novelty claim.

## 4. Cycle consistency as an obstruction

A scalar potential reconstructed from edge ratios must be globally consistent around every cycle.

For the reversible model,

$$
W_{01}W_{12}W_{20}=4\cdot3\cdot4=48,
$$

while

$$
W_{10}W_{21}W_{02}=8\cdot6\cdot1=48.
$$

Now change only

$$
W_{02}:1\longrightarrow2.
$$

The forward and reverse cycle products become

$$
48\neq96.
$$

The path \(0\to1\to2\) still demands \(q_2-q_0=2\), while the modified direct edge \(0\leftrightarrow2\) demands \(q_2-q_0=1\).

No single scalar state potential can satisfy both requirements.

### Consequence

A state scalar may represent a reversible potential sector, but arbitrary nonequilibrium driving can carry information that lives on cycles, edges, or reservoirs rather than in one scalar state function.

The correct response is not to add a convenient scalar. The missing structure must be justified by the physical obstruction.

## 5. What happens to \(R\)?

Define

$$
i\,R\,j
\quad\Longleftrightarrow\quad
W_{ij}>0.
$$

Then \(R\) is the support graph of \(K\). In this representation,

$$
K\Longrightarrow R.
$$

If a model starts from full transition rates, retaining an independent copy of the support relation is redundant. If a deeper theory starts only from admissibility before rates are known, \(R\) can still be the earlier informational layer.

This separates logical order of construction from independent physical content.

## 6. Equilibrium occupancy and current occupancy

For the declared irreducible reversible generator, the equilibrium distribution is fixed by \(K\) after normalization. Thus \(\pi^{\rm eq}\) is not an independent free equilibrium parameter.

A current occupancy \(\pi(t)\) is different. The same generator can be prepared with different initial distributions, producing different instantaneous flows.

The bridge therefore distinguishes:

- stationary occupancy derived from a specified dynamical regime;
- current occupancy as state information.

## 7. Exact occupancy dependence under coarse-graining

Partition the microstates as

$$
A=\{0,1\},\qquad B=\{2\}.
$$

The exit rates to \(B\) are

$$
W_{02}=1,\qquad W_{12}=3.
$$

If all conditional occupancy inside \(A\) lies on state \(0\), the macro rate is \(1\). If it lies on state \(1\), the macro rate is \(3\).

Under equilibrium conditioning,

$$
\rho(0\mid A)=\frac23,\qquad
\rho(1\mid A)=\frac13,
$$

so

$$
k_{A\to B}^{\rm eq}
=
\frac23(1)+\frac13(3)
=
\frac53.
$$

The microscopic \(K\) and the partition are unchanged.

Therefore a unique macro rate is not determined by \(K\) and a partition alone unless an occupancy rule or a lumpability condition removes the ambiguity.

This is a classical coarse-graining fact. Its value here is that the repository's occupancy distinction survives contact with a standard physical model.

## 8. Are \(q\) and \(\mu\) separately identifiable?

Suppose a coarse state has energy \(E_i\) and degeneracy \(\mu_i>0\). Canonical weights are

$$
w_i=\mu_i e^{-\beta E_i}.
$$

With \(\beta=\log2\), compare

$$
E=(0,1,2),\qquad \mu=(1,1,1)
$$

with

$$
E'=(1,1,2),\qquad \mu'=(2,1,1).
$$

Both give

$$
w=
\left(
1,\frac12,\frac14
\right).
$$

Equilibrium weights therefore identify only the combination

$$
F_i
=
E_i-\frac1\beta\log\mu_i.
$$

If the repository's \(q\) is mapped to energy and \(\mu\) to degeneracy, equilibrium data alone do not identify them separately.

## 9. Reduction table

| Component | Status in this reversible pilot | Reason |
|---|---|---|
| \(R\) | derived from \(K\) | support of positive rates |
| \(q\) | derivable up to a constant in the reversible sector | rate ratios satisfy cycle consistency |
| scalar \(q\) outside that sector | generally insufficient | nonzero cycle affinity obstructs a global potential |
| \(\mu\) | not separately identified by equilibrium weights in the degeneracy interpretation | only the effective free-energy combination is fixed |
| \(K\) | primary dynamical input in this pilot | microscopic transition rates |
| \(\pi^{\rm eq}\) | derived from \(K\) in the declared reversible regime | stationarity and detailed balance |
| current \(\pi(t)\) | additional state information unless preparation/history is supplied | the same \(K\) admits different transient occupancies |

The five-part architecture therefore does not remain five independent physical primitives in this model.

## 10. Falsification and correction criteria

### F1 — scalar-potential failure

If accepted or measured rates have nonzero cycle affinity, a single state scalar \(q\) cannot represent all thermodynamic driving through potential differences.

**Response:** retain the driving in \(K\), or introduce edge/reservoir information only when independently justified.

### F2 — occupancy redundancy

If a declared regime determines \(\pi\) uniquely from \(K\) and the preparation protocol, \(\pi\) should not be counted as an independent primitive in that regime.

### F3 — measure redundancy

If all observables depend on \(q\) and \(\mu\) only through one combination, compress the representation unless independent measurements separate them.

### F4 — coarse-graining failure

If a macro transition law ignores occupancy while exit rates differ inside a macro block, it must prove lumpability or be rejected.

### F5 — empirical bridge failure

The map from physical data to framework variables must be fixed before withheld observables are examined. A post-hoc remapping is exploratory, not prospective evidence.

## 11. Next test

The next test uses published electronic stochastic-thermodynamics systems. A two-state single-electron box is used only for calibration of meanings. A multi-state electronic dot is the preferred next stress test for occupancy and nonequilibrium structure.

No spacetime, gravity, quantum-gravity, or ontological conclusion follows from this pilot.
