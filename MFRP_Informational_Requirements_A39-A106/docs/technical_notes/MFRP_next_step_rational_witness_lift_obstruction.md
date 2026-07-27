# A95 — Exact Rational-Witness Lift Atlas and Restricted-Family Obstruction

## Status

Exact finite rational-witness KKT audit built on the complete A94 compressed-objective atlas.

The declared source contract is

\[
14\le M\le520,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

A94 partitions this domain into 858 algebraic cells and proves the global compressed-maximizer phase in every cell. A95 does **not** yet certify the full lifted LP on whole cells. It asks a prior falsifiable question: at exact interior witnesses, does the compressed maximizer lift to the contact families that had been used through A78–A82?

## Natural lift triad

If the A94 compressed maximizer is the contact \(j\), the three natural lifted candidates are

\[
C_j:\quad P=\{0,j,M\},
\]

with \(\gamma\) inactive,

\[
L_j^-:\quad P=\{0,j-1,j,M\},\qquad \gamma-,
\]

and

\[
L_j^+:\quad P=\{0,j,j+1,M\},\qquad \gamma+.
\]

All candidates retain

\[
Q=\{1,h,h+1\},
\qquad h=\lfloor M/2\rfloor,
\]

and the active \(\alpha+\), \(\beta-\) contract.

Each candidate is tested against the **complete finite LP KKT system**:

1. all basic variables;
2. all active band multipliers;
3. every nonbasic reduced cost on the full support \(\{0,\ldots,M\}\);
4. every inactive observation-band slack.

A strict pass is therefore a full KKT certificate for that candidate at the declared rational witness, not merely a comparison inside the three-candidate set.

## Witness construction

Each fixed A94 phase contributes one exact rational interior witness. Each simple transition cell contributes one witness on each open side of its isolated algebraic root. The resulting atlas contains

\[
\boxed{1063\text{ open phase-segment witnesses}}.
\]

The witness selector uses the first low-denominator decimal rational strictly inside the exact open segment. No floating-point value decides a KKT status.

## Main result

The natural lift triad was evaluated

\[
3\times1063=\boxed{3189}
\]

times in exact arithmetic.

The result is

\[
\boxed{980\text{ segments with exactly one strict natural lift}},
\]

\[
\boxed{83\text{ segments with no strict natural lift}},
\]

and

\[
\boxed{0\text{ segments with multiple strict natural lifts}}.
\]

The 980 successful lifts divide as follows:

| Lift family | Strict passes |
|---|---:|
| \(L_j^+\) | 922 |
| \(L_j^-\) | 18 |
| \(C_j\) | 40 |

The negative result is not rare numerical noise. The 83 obstruction segments span 75 support sizes, beginning at

\[
\boxed{M=125}
\]

and continuing through the declared upper boundary \(M=520\).

## Where the obstructions occur

The 83 failures occur only in four compressed-phase locations:

| Compressed phase location | Obstruction segments |
|---|---:|
| right side of \(b+1\to b+2\) | 46 |
| fixed unique \(b+2\) | 12 |
| fixed unique \(b+3\) | 14 |
| right side of \(b+2\to b+3\) | 11 |

No obstruction occurs:

- on the left side of an A94 transition;
- in a fixed unique-\(b+1\) cell.

This directional asymmetry is an exact finite observation. A95 does not yet promote it to a universal theorem.

## First exact obstruction

The first obstruction occurs at

\[
M=125,
\qquad
s=\frac{33}{250},
\qquad
j=24.
\]

The three natural candidates fail by primal feasibility:

- \(C_{24}\): negative basic atom at \(p_0\);
- \(L_{24}^-\), with contacts \(\{23,24\}\): negative basic atom at \(p_0\);
- \(L_{24}^+\), with contacts \(\{24,25\}\): negative basic atom at \(p_{25}\).

A95 then exhausts **every** previously declared two-band and adjacent three-band contact candidate at this witness. There are

\[
3M-5=\boxed{370}
\]

candidates. Their first failing KKT classes are:

| Failure class | Count |
|---|---:|
| primal infeasible | 349 |
| reduced-cost infeasible | 20 |
| active-dual infeasible | 1 |
| strict pass | 0 |

Thus the failure is not repaired by moving to a distant contact inside the old F2/F3 catalogue.

## Exhaustive prefix stress

To test whether the first obstruction was isolated, A95 exhausts every old F2/F3 candidate at every obstruction witness through and including the first A90 offset-three support \(M=325\).

This natural prefix contains

\[
\boxed{29\text{ obstruction witnesses}}
\]

and

\[
\boxed{19,421\text{ exact candidate KKT evaluations}}.
\]

The aggregate result is:

| Failure class | Count |
|---|---:|
| primal infeasible | 18,323 |
| reduced-cost infeasible | 1,069 |
| active-dual infeasible | 29 |
| strict pass | 0 |

Therefore, throughout the declared prefix, the old contact-support architecture is structurally incomplete at the obstruction witnesses.

## Scientific consequence

A94 proves globality of the **compressed objective**. A95 proves that this does not automatically imply liftability to the frozen full-LP basis families.

The correct implication is now:

\[
\text{compressed global maximizer}
\centernot\Rightarrow
\text{valid lifted F2/F3 KKT branch}.
\]

This is a genuine obstruction, not a reason to insert an unmotivated atom or modify the contract until the failure disappears.

The missing active set may require one or more of the following:

- a different \(Q\)-support;
- nonadjacent or additional \(P\)-contacts;
- a different active-band signature;
- a degenerate or higher-support basis not represented in the old catalogue.

A95 does not choose among these possibilities.

## Evidence discipline

A95 proves:

1. exact natural-triad KKT classification at all 1,063 open A94 phase-side witnesses;
2. 980 unique strict lifts and 83 exact natural-lift obstructions;
3. no multiple strict lift at any witness;
4. exact first obstruction at \((M,s)=(125,33/250)\);
5. complete failure of all 370 old F2/F3 candidates at the first obstruction;
6. complete failure of all 19,421 old-family candidates in the declared obstruction prefix through \(M=325\).

A95 does **not** prove:

1. a continuum lifted-KKT classification on any entire A94 cell;
2. that no basis outside F2/F3 can pass;
3. the actual full-LP optimum at the obstruction witnesses;
4. a universal support-size law;
5. any physical, spacetime, matter, or pre-temporal interpretation.

## Next rigorous target

A96 should begin at the first obstruction rather than broadening the ontology.

The correct task is:

> Solve the complete LP at \(M=125\), \(s=33/250\), discover its actual active set without imposing the old contact pattern, reconstruct that basis in exact rational arithmetic, and certify primal-dual equality and the complete KKT system.

Only after the first missing active set is known should the programme ask whether the same replacement family recurs on the remaining 82 obstruction segments.
