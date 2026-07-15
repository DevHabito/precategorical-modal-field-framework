# A24 — Operational Criterion for the RZS q-Field

## Criterion

A q-field is operational relative to an observation class only when there is
a specified observable kernel `K(O|R,q)` that is not constant on
gauge-inequivalent q configurations.

A valid relational operationalization should satisfy:

1. gauge invariance;
2. relabeling equivariance;
3. declared relational locality;
4. nontrivial sensitivity to gauge-invariant q contrasts;
5. inferability of at least some q information from observable frequencies.

## Local transition witness

For a directed graph,

`P(i->j|q) proportional to A_ij exp(-beta q_ij)`.

It obeys

`log(P(i->j)/P(i->k)) = -beta(q_ij-q_ik)`.

Therefore q contrasts are statistically recoverable when beta is calibrated.

## Identifiability limits

- Adding a common q offset leaves the transition law unchanged.
- This particular local coupling is also invariant under a separate offset
  for every source row.
- Replacing q by `a q` and beta by `beta/a` leaves the law unchanged.

Thus the observation identifies only dimensionless products of a coupling
strength with local q contrasts.

## Negative statements

- q inferred only from the relation contains no information beyond it.
- q with no q-dependent observable coupling is empirically silent.

## Boundary

The softmax kernel is a mathematical witness, not an asserted law of the RZS.
The actual origin and operational coupling of q remain unresolved unless the
theory supplies them independently.
