# A9 — Relational Clock Audit

## Exact scope

- Labeled loopless digraphs: 1,048,576
- Vertices per digraph: 5
- Distinct labeled SCC-condensation posets: 5,234
- Nontrivial distinct condensation posets:
  5,233

## Clock candidates

1. Depth: longest-chain depth from minimal SCCs.
2. Balance: cardinality of principal down-set minus principal up-set.
3. Mean extension: expected position in the uniform distribution over all
   linear extensions.

All three are strict order-preserving functions on every comparable pair in
the exact enumeration.

## Interpretation limit

For any strictly increasing function f, f∘tau is another valid ordinal clock.
Therefore order alone fixes no duration, interval scale, or rate.

The reverse relation yields the dual poset. Balance and mean-extension clocks
reflect exactly under duality; the depth clock generally does not, because
depth from minima and depth from maxima need not be affinely equivalent.

## Scientific status

The candidates are canonical descriptors of a chosen orientation. They do
not select that orientation, are not unique on incomparable elements, are
not automatically compatible with coarse-graining, and are sensitive to
changes in the underlying relation. They are not physical clocks.
