# Markov Thermal Pilot — first controlled physical bridge

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite diagnostic + literature-grounded interpretation  
**Physical status:** no empirical validation and no claim of new stochastic thermodynamics

## 1. Question

The repository currently uses the provisional informational architecture

[
mathcal M=(R,q,mu,K,pi),
]

where (R) is relational structure, (q) is a quantitative mark, (mu) is additive mass or multiplicity, (K) is a conditional transition law, and (pi) is source occupancy.

This notation is useful internally, but physics does not owe the framework five independent primitives.

The first physical-bridge question is therefore:

> In an established finite Markov jump model, which of (R,q,mu,K,pi) are actually independent, which are derivable, and which are only one possible representation of the same physical information?

The purpose of the pilot is to make the framework lose unnecessary structure if physics permits it.

## 2. Why a Markov jump process is a useful first test

Stochastic thermodynamics already provides an operational language for:

- states and allowed transitions;
- transition rates;
- probability occupancy;
- equilibrium and nonequilibrium steady states;
- detailed balance and local detailed balance;
- probability currents and coarse-graining.

This makes it a better first bridge than spacetime. The variables can be compared with accepted physical objects before any pregeometric interpretation is attempted.

The model below is intentionally small. Small size is an advantage here: every statement can be checked exactly, and no numerical fitting is needed.

## 3. Exact reversible model

Consider three states (0,1,2). Work in units in which

[
eta=log 2
]

and introduce the candidate state potential

[
q=(0,1,2).
]

The positive off-diagonal transition rates are

[
W=
egin{pmatrix}
0 & 4 & 1\
8 & 0 & 3\
4 & 6 & 0
end{pmatrix}.
]

The continuous-time generator has diagonal entries equal to minus the total outgoing rate.

The exact stationary distribution used in the audit is

[
pi^{m eq}
=
left(
rac47,rac27,rac17
ight).
]

For every unordered pair (i,j),

[
pi_i^{m eq} W_{ij}
=
pi_j^{m eq} W_{ji}.
]

The exact flows are

[
rac{16}{7},qquad
rac{4}{7},qquad
rac{6}{7}
]

for the pairs (01,02,12), respectively.

Thus this finite model is reversible.

The rate ratios satisfy

[
rac{W_{01}}{W_{10}}=rac12,
qquad
rac{W_{12}}{W_{21}}=rac12,
qquad
rac{W_{02}}{W_{20}}=rac14.
]

Because (eta=log2),

[
rac{W_{ij}}{W_{ji}}
=
e^{-eta(q_j-q_i)}
=
2^{-(q_j-q_i)}
]

for all three edges.

### Interpretation

Inside this reversible sector, (q) is not independent of (K). The edge ratios determine the potential differences,

[
q_j-q_i
=
-rac{1}{eta}
lograc{W_{ij}}{W_{ji}},
]

provided those differences are globally consistent.

Only an additive constant remains free. This is the same shift redundancy already present in the repository's abstract (q)-layer.

This is not a new theorem. It is a direct use of detailed-balance structure. Its value here is diagnostic: a physical embedding can make one of the provisional framework variables derivable.

## 4. Cycle consistency is the obstruction

A global scalar potential reconstructed from edge ratios can exist only if the inferred differences add consistently around cycles.

For the reversible model,

[
W_{01}W_{12}W_{20}
=
4cdot3cdot4
=
48,
]

while

[
W_{10}W_{21}W_{02}
=
8cdot6cdot1
=
48.
]

The cycle product is therefore balanced.

Now change only one rate,

[
W_{02}:1longrightarrow2.
]

The two cycle products become

[
48
quad	ext{and}quad
96.
]

The cycle condition fails exactly.

The ratios now demand incompatible potential differences. Along the path (0	o1	o2), the rates imply

[
q_2-q_0=2,
]

whereas the modified direct edge (0leftrightarrow2) implies

[
q_2-q_0=1.
]

No single state scalar (q) can satisfy both statements.

### Consequence for the framework

A scalar state mark may be sufficient for a reversible potential sector, but it cannot encode arbitrary nonequilibrium driving.

If a future physical version of the framework needs nonequilibrium cycle affinities, they must either:

- be carried by (K) itself;
- be represented by edge- or reservoir-resolved variables;
- or be derived from a richer physical structure.

Adding a new scalar merely to repair the contradiction would be ad hoc. The obstruction tells us what kind of information is missing.

## 5. What happens to (R)?

For a continuous-time Markov chain, define

[
i,R,j
quadLongleftrightarrowquad
W_{ij}>0.
]

Under this identification, (R) is simply the support graph of (K).

Therefore

[
KLongrightarrow R
]

in this physical representation.

This does not make the repository's relational layer useless. It changes its role.

If a model begins from (K), keeping a second independent copy of (R) would be redundant. If a more fundamental theory begins from an allowed-transition relation before rates are known, (R) may remain the earlier informational layer.

The physical model therefore distinguishes **logical ordering of construction** from **independent physical observables**.

## 6. Equilibrium occupancy and transient occupancy are different questions

For an irreducible reversible generator, the stationary distribution is determined by the transition rates after normalization. In the present model,

[
pi^{m eq}
=
left(
rac47,rac27,rac17
ight)
]

is therefore not an additional free equilibrium parameter.

At a given finite time, however, the current occupancy need not equal the stationary distribution.

The same generator (K) can be prepared with different initial distributions. Those distributions evolve under the same master equation but produce different instantaneous flows.

Thus the statement

[
KLongrightarrow pi
]

is true only after the state-selection rule has been specified, for example equilibrium, a particular stationary state, or an initial condition plus elapsed time.

The framework should therefore distinguish:

- **stationary occupancy derived from a declared dynamical regime**, and
- **current occupancy as state information**.

This distinction matters directly for coarse-graining.

## 7. Exact occupancy dependence under coarse-graining

Partition the three microstates into

[
A={0,1},
qquad
B={2}.
]

The microscopic exit rate from state (0) to block (B) is

[
W_{02}=1,
]

while the exit rate from state (1) to (B) is

[
W_{12}=3.
]

If the current system is known only to be somewhere in block (A), the macro transition rate (A	o B) depends on the conditional occupancy inside (A).

If all conditional mass is on state (0),

[
k_{A	o B}=1.
]

If all conditional mass is on state (1),

[
k_{A	o B}=3.
]

Under equilibrium conditioning,

[
ho(0mid A)=rac23,
qquad
ho(1mid A)=rac13,
]

and therefore

[
k_{A	o B}^{m eq}
=
rac23(1)+rac13(3)
=
rac53.
]

The microscopic generator and the partition are unchanged in all three cases.

### Consequence

A unique macro rate is not determined by (K) and the partition alone unless an occupancy rule or a lumpability condition removes the ambiguity.

This reproduces, inside a standard physical model, the role assigned to (pi) by the repository's coarse-graining analysis.

The result is classical. The point of the pilot is not priority. It is that the repository's occupancy distinction survives contact with an accepted physical formalism.

## 8. Are (q) and (mu) separately physical?

A second reduction appears at equilibrium.

Suppose a coarse state has an energy-like value (E_i) and a degeneracy or multiplicity (mu_i>0). Canonical equilibrium weights have the form

[
w_i
=
mu_i e^{-eta E_i}.
]

With (eta=log2),

[
w_i=mu_i 2^{-E_i}.
]

Consider two exact representations:

[
E=(0,1,2),
qquad
mu=(1,1,1),
]

and

[
E'=(1,1,2),
qquad
mu'=(2,1,1).
]

Both produce exactly

[
w=
left(
1,rac12,rac14
ight).
]

The equilibrium distribution is therefore identical.

The identifiable combination is the effective free-energy-like quantity

[
F_i
=
E_i-rac{1}{eta}logmu_i.
]

In the chosen log-base-two units,

[
F_i=E_i-log_2mu_i,
]

and both representations give

[
F=(0,1,2).
]

### Consequence

If the repository's (q) is identified with energy while (mu) is identified with degeneracy, equilibrium data do not identify them separately.

A physical bridge must decide which quantity is operationally primary:

- raw energy plus degeneracy;
- an effective free energy;
- or some other measured quantity.

The abstract separation ((q,mu)) remains useful for bookkeeping, but physics may package the same information more economically.

## 9. Reduction table for this pilot

| Component | Status in the reversible thermal pilot | Reason |
|---|---|---|
| (R) | derived from (K) | support of positive transition rates |
| (q) | derivable up to a constant in the reversible sector | log rate ratios satisfy the cycle condition |
| (q) outside the reversible sector | generally insufficient as one state scalar | nonzero cycle affinity obstructs a global potential |
| (mu) | not separately identified by equilibrium weights in the degeneracy interpretation | only (E-eta^{-1}logmu) is fixed |
| (K) | primary dynamical input in this pilot | specifies microscopic transition rates |
| (pi^{m eq}) | derived from (K) for the declared reversible equilibrium | stationary detailed balance |
| current (pi(t)) | additional state information unless preparation/history is supplied | the same (K) admits different transient occupancies |

The provisional five-part architecture therefore does **not** remain five independent physical primitives in this model.

That is a useful outcome.

## 10. What this pilot tests and what it does not

### Supported by exact calculation

1. The declared reversible rates satisfy detailed balance exactly.
2. Their rate ratios reconstruct the chosen scalar potential differences.
3. The Kolmogorov cycle product agrees in the reversible model.
4. A one-rate perturbation breaks cycle consistency exactly.
5. The same microscopic (K) and partition produce different macro rates under different source occupancies.
6. Two distinct ((E,mu)) representations produce identical equilibrium weights.

### Classical background, not project novelty

- detailed balance;
- Kolmogorov cycle consistency;
- local detailed balance;
- Markov coarse-graining and lumpability;
- canonical degeneracy factors;
- reconstruction of equilibrium potentials from reversible rate ratios.

### Not established

This pilot does not show that:

- the repository describes a new physical field;
- (q) is fundamentally energy or free energy;
- (mu) is a fundamental physical measure;
- (pi) is a new physical degree of freedom;
- stochastic thermodynamics is derived from the pre-categorical framework;
- spacetime or geometry emerges;
- the framework is empirically validated.

## 11. Falsification and correction criteria

The bridge is useful only if it can fail.

### F1 — scalar-potential failure

If measured or accepted transition rates have nonzero cycle affinity, a single state scalar (q) cannot represent all thermodynamic driving through potential differences.

**Required response:** retain the driving in (K) or introduce a physically justified edge/reservoir structure. Do not repair the model with an arbitrary scalar.

### F2 — occupancy redundancy

If a declared physical regime determines (pi) uniquely from (K) and the preparation protocol, then (pi) should not be counted as an independent primitive in that regime.

### F3 — measure redundancy

If all observables used in a physical application depend on (q) and (mu) only through one combination, the representation should be compressed unless an independent measurement separates them.

### F4 — coarse-graining failure

If a proposed macro transition law ignores occupancy while microscopic exit rates differ inside a macro block, it must either prove lumpability or be rejected.

### F5 — empirical bridge failure

A proposed mapping from physical data to ((R,q,mu,K,pi)) must be specified before testing withheld observables. If the mapping is changed after seeing the target result, the test is not prospective evidence.

## 12. Next physical test

The next step should not be a larger abstract model. It should be a physical Markov system with published or reproducible rates.

A suitable target should provide:

1. experimentally meaningful state labels;
2. measured or independently derived transition rates;
3. a controlled temperature or reservoir model;
4. enough transitions to contain at least one nontrivial cycle;
5. time-resolved occupancy data or a documented preparation protocol;
6. a nontrivial coarse-graining.

Chemical reaction networks, molecular conformational switching, or small electronic circuits are natural candidates because current stochastic-thermodynamics literature treats all three classes within Markov jump descriptions.

The first prospective task will be:

> infer the bridge variables from one subset of the physical information, freeze the mapping, and test a quantity that was not used in the construction.

That is the point at which the programme begins to move from internal mathematical consistency toward physical evidence.

## 13. Bottom line

The first physical bridge does not tell us that the full tuple

[
(R,q,mu,K,pi)
]

is fundamental.

It tells us something more useful:

> the independence of those components is regime-dependent and must be tested rather than assumed.

In reversible thermal dynamics, (R), (q), and equilibrium (pi) can become derived from (K), while transient occupancy remains necessary for generic coarse-graining. A nonequilibrium cycle can destroy the global scalar-potential representation altogether. Energy-like marks and degeneracy can also collapse into one effective free-energy combination.

This is the kind of pressure the physical programme needs. The framework should become smaller where physics makes variables redundant and richer only where a demonstrated obstruction requires additional information.
