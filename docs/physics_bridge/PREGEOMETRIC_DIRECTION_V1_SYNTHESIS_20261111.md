# Pregeometric Direction V1 — canonical synthesis

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** canonical synthesis of the direction/order branch  
**Physical status:** no derivation of physical time has been established  
**Novelty status:** most mathematical ingredients are classical; project value is the obstruction-driven organization and exact finite audits

## 1. Central question

The current foundational architecture

$$
(R,q,\mu,K,\pi)
$$

supports relational, quantitative, measure-theoretic, transition, and occupancy operations.

It does not yet explain the origin of temporal direction.

The direction branch asks a smaller question:

> Starting from information that is not already interpreted temporally, what is required before a strict orientation or order can be selected without arbitrary labels?

This is not yet the full problem of time.

It concerns only the origin and identifiability of direction.

## 2. Hard anti-circularity boundary

A candidate direction is not emergent if it is imported through:

- timestamps;
- iteration labels interpreted temporally;
- a primitive relation already called “precedence”;
- a transition kernel whose arrow already means earlier-to-later;
- an externally chosen vertex numbering;
- a topological ordering selected after the graph is built.

The arrow of a primitive object must first have a non-temporal meaning.

## 3. Orderability comes before order

Process-matrix and indefinite-causal-order literature prevents the programme from assuming that every primitive structure has one definite global causal order.

The correct sequence is:

1. test whether the structure is orderable in the intended sense;
2. reconstruct an order only in an orderable sector;
3. retain causal indefiniteness or ambiguity when orderability fails.

Thus a DAG is an output only under stated conditions, not a universal starting requirement.

## 4. Symmetry no-go

Let \(\mathfrak P\) be a primitive structure with an automorphism \(\sigma\) satisfying

$$
\sigma(a)=b,
\qquad
\sigma(b)=a.
$$

Any strict relation derived by an isomorphism-equivariant deterministic rule must obey

$$
a\prec b
\iff
\sigma(a)\prec\sigma(b).
$$

Therefore

$$
a\prec b
\Longrightarrow
b\prec a,
$$

contradicting asymmetry.

Hence

$$
\boxed{
\text{a swap symmetry blocks canonical strict orientation of the swapped pair}.
}
$$

This finite logical core has end-to-end Lean/kernel verification in
PhysicalBridgeSymmetryOrientation.lean (run 744).

## 5. C1 label correction

The C1 formalization uses minimum-labeled SCC representatives for a finite code.

That is a valid coding convention.

It is not a physically invariant primitive.

The eligible structural object is the SCC equivalence class and its quotient relation up to isomorphism.

Thus:

$$
\boxed{
\text{SCC quotient: structural};
\qquad
\text{minimum representative: encoding convention}.
}
$$

## 6. F1 — intrinsic orientability audit

The two C1 witnesses were exhaustively tested over all

$$
5!=120
$$

vertex relabelings.

### graphA

Directed automorphism group:

$$
|\operatorname{Aut}(G_A)|=4.
$$

Undirected skeleton:

$$
|\operatorname{Aut}(|G_A|)|=8.
$$

Every directed cycle edge becomes equivalent to its reverse after arrow removal.

### graphB

Directed automorphism group:

$$
|\operatorname{Aut}(G_B)|=6.
$$

Undirected skeleton:

$$
|\operatorname{Aut}(|G_B|)|=12.
$$

The one-way triangle edges become reverse-equivalent after arrow removal.

Therefore the current one-way directions are information already present in directed \(R\).

They are not recovered from the unoriented connectivity.

## 7. Reconnection with A21-A24

The older foundational programme already contained the correct abstract obstruction.

### A21

Purely endogenous equivariant evolution cannot distinguish latent representatives that remain related by the declared symmetry.

### A22

An added mark can break the degeneracy only when its conditional law contains information not fixed by the relation.

### A23

A q-field can evade the R-only identifiability limit only if it is genuinely additional information.

### A24

A declared local transition kernel can make within-row q-contrasts operational.

These results are fully consistent with the newer automorphism gate.

They already implied that direction cannot appear from relation-preserving equivariant processing alone.

## 8. q is additional information, not automatically direction

The A24 witness is

$$
K_\beta(i,j)
=
\frac{
A_{ij}e^{-\beta q_{ij}}
}{
\sum_kA_{ik}e^{-\beta q_{ik}}
}.
$$

It is invariant under independent source-row offsets

$$
q_{ij}\mapsto q_{ij}+c_i.
$$

A raw reciprocal score

$$
D_{ij}=q_{ij}-q_{ji}
$$

therefore transforms as

$$
D_{ij}'=D_{ij}+c_i-c_j.
$$

Its sign can be changed arbitrarily without changing the observable transition matrix.

Hence

$$
\boxed{
\operatorname{sign}(q_{ij}-q_{ji})
\text{ is not an observable reciprocal direction under the current A24 gauge}.
}
$$

This algebraic core has end-to-end Lean/kernel verification (run 749).

## 9. Gauge-invariant loop information survives

Although the local reciprocal score fails, the closed-cycle circulation

$$
\mathcal C_q(C)
=
\sum_C(q_{ij}-q_{ji})
$$

is invariant under the row gauge.

For the A24 kernel,

$$
\boxed{
\sum_C
\log\frac{K(i,j)}{K(j,i)}
=
-\beta\mathcal C_q(C).
}
$$

Reversing the cycle changes its sign.

The finite algebraic identities have end-to-end Lean/kernel verification (run 752).

This is classical cycle-affinity/Hodge structure.

## 10. C1 cycle-space dimension

Both C1 witness skeletons have

$$
|V|=5,\qquad |E|=4,\qquad c=2.
$$

Therefore

$$
\boxed{
\beta_1=|E|-|V|+c=1.
}
$$

The real edge-field space modulo vertex gradients is one-dimensional.

Thus each witness has exactly one independent cyclic gauge degree of freedom.

This tells us where a loop asymmetry can live.

It does not tell us what that loop variable means physically.

## 11. Magnetic-loop calibration

A four-site tight-binding ring threaded by magnetic flux supplies a classical physical realization of the same mathematical pattern:

- local Peierls phases are gauge-dependent;
- the closed-loop phase is gauge-invariant;
- changing the loop flux changes observable spectra.

The numerical regression preserved spectra under local gauge changes to errors below \(10^{-15}\).

This establishes an important semantic warning:

$$
\boxed{
\text{a physical gauge-invariant loop class need not be time}.
}
$$

Magnetic holonomy is physically real but is not a temporal coordinate.

## 12. Chirality is not precedence

In the uniform-flux four-site ring,

$$
[T,H(\Phi)]=0
$$

for cyclic translation, while reflection sends

$$
\Phi\mapsto-\Phi.
$$

The flux distinguishes loop chirality while all sites remain equivalent under rotation.

Therefore:

$$
\boxed{
\text{chirality}
\not\Rightarrow
\text{a first vertex or temporal precedence}.
}
$$

This separates loop orientation from event ordering.

## 13. Symmetry-breaking information is operation-relative

A22 identified binary marks as the smallest nontrivial alphabet.

The later exact cycle audits show why that is only a lower bound.

For the C4 skeleton:

- 12 of 16 binary vertex markings orient the selected edge \((0,1)\);
- 0 of 16 select global cycle chirality;
- 0 of 16 fully distinguish the graph.

With three symbols:

- 72 markings orient the selected edge;
- 24 select chirality;
- 24 fully distinguish the graph.

Thus the required information depends on the requested operation.

The correct question is not “how many bits break symmetry?”

It is:

$$
\boxed{
\text{which symmetry must be broken for this operation?}
}
$$

## 14. Orientability is not polarity

A marked structure can admit an automorphism-invariant acyclic orientation without being fully rigid.

For the C4 skeleton:

$$
\boxed{
10/16
}
$$

binary colorings admit at least one invariant acyclic orientation.

However, if \(O\) is such an orientation, its global reverse

$$
O^{\mathrm{op}}
$$

is also invariant and acyclic.

Therefore static symmetry breaking can remove an obstruction to ordering without selecting which polarity is physically intended.

This yields the current chain:

$$
\boxed{
\text{symmetry breaking}
\to
\text{orientability}
\to
\text{polarity}
\to
\text{physical order}
\to
\text{duration}.
}
$$

## 15. What can provide polarity in established physics?

Examples exist, but each adds semantics beyond a static marked graph.

### Operational signalling

Intervention at \(A\) changes response statistics at \(B\).

The intervention/response distinction provides polarity.

### Boundary preparation

A special state selects one relaxation sector under an otherwise symmetric law.

### Constitutive/dynamical law

A physical law can privilege one sign of a flux or response relative to supplied variables.

### External field

A magnetic field/flux can select loop chirality.

None of these examples proves the origin of universal time.

They show that polarity requires physical semantics, not merely distinguishability.

## 16. Boundary occupancy pi

A reflection-symmetric three-state Markov kernel with mirrored initial occupancies gives

$$
\langle x\rangle_{L,n}
=
1-\left(\frac34\right)^n,
$$

and

$$
\langle x\rangle_{R,n}
=
1+\left(\frac34\right)^n.
$$

The law is the same.

The boundary state selects the macroscopic sign of relaxation.

Thus

$$
\boxed{
\pi\text{ can carry effective-arrow information without being time}.
}
$$

This is analogous to the logical role of asymmetric boundary conditions in Past-Hypothesis discussions, while the literature also contains models pursuing arrows without a conventional Past Hypothesis.

## 17. q is not a temporal rank

The reversible Markov calibration gives a physically meaningful state potential \(q\), yet both q-increasing and q-decreasing transitions occur with positive rates.

Therefore a calibrated cardinal mark can be real and operational while not being a temporal coordinate.

Outside detailed balance, the missing information appears in non-integrable cycle structure rather than becoming a better scalar clock.

## 18. Current architecture boundary

Under the present canonical definitions:

- directed/precedence-like \(R\) already contains orientation;
- dynamical \(K\) already contains transition/succession semantics;
- \(q\) supplies cardinal information and possible asymmetry;
- \(\mu\) supplies refinement/multiplicity;
- \(\pi\) supplies state/preparation information.

Therefore

$$
\boxed{
(R,q,\mu,K,\pi)
\text{ does not currently derive time from a timeless substrate}.
}
$$

This is a scope boundary, not a failure of the informational architecture.

## 19. What has been rejected

The following strong identifications are rejected.

### Time = information degradation

Blackwell-equivalent reversible transformations can represent distinct change.

### Time direction = passive observational causal orientation

Markov-equivalent DAGs can leave direction observationally underdetermined.

### Time = SCC condensation

SCC condensation supplies only a lossy acyclic macro-order and no duration.

### Time requires external noise

Page-Wootters supplies reversible relational-time structure without environmental noise.

### Time = q

A calibrated q can be traversed in both directions.

### Time = loop circulation

Magnetic holonomy is a counterexample: physical loop chirality is not temporal precedence.

### Time = special pi

Boundary state can select an arrow only inside already defined dynamics.

## 20. Current open problem

The first unresolved stage is now **polarity**.

A candidate must answer:

> What physically justified, non-temporal semantics selects one of two reversed, symmetry-compatible orientations?

It must not answer by:

- vertex label;
- arbitrary sign convention;
- timestamp;
- update number;
- already-temporal transition language;
- post-hoc choice after inspecting the desired direction.

## 21. Next finite research question

The smallest useful target is:

> Given a timeless marked relational structure and a declared non-temporal operational primitive, does that primitive define a reversal-odd quantity whose sign is gauge-invariant, label-invariant, and experimentally meaningful?

This question is intentionally narrower than “derive time.”

Examples of candidate primitive semantics to audit include:

- intervention versus response;
- one-way resource convertibility;
- recoverability asymmetry;
- boundary/state constraints;
- process-theoretic input/output structure.

For each candidate the project must ask whether the polarity is truly derived or merely encoded in the definition.

## 22. Promotion rule

No candidate direction should be called temporal until it passes:

1. anti-circularity;
2. label/isomorphism invariance;
3. gauge invariance;
4. symmetry/orbit audit;
5. orderability;
6. polarity;
7. operational semantics;
8. recovery of an accepted causal/clock structure;
9. separation from duration;
10. a discriminating physical test or a rigorous recovery theorem.

## 23. Current conclusion

The project has not derived time.

It has done something more modest and useful: it has isolated several distinct mathematical notions that are easily conflated under the word “direction.”

The current frontier is no longer “invent a time equation.”

It is:

$$
\boxed{
\text{find or rule out a non-temporal physical source of polarity}.
}
$$

That is now the canonical direction problem.
