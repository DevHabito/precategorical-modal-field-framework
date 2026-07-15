# A10 — Internal Duration Audit

## Exact scope

- Labeled loopless digraphs: 1,048,576
- Vertices: 5
- Distinct labeled SCC-condensation posets: 5,234

## Candidates

- L(x,y): longest-chain length.
- V(x,y): interval cardinality minus one.
- R(x,y): rank difference under the standard normalization in which all
  minimal elements have rank zero.
- P(x,y): difference of an integer cover potential, if one exists, without
  forcing distinct minimal elements to share a value.

## Exact algebra

For x<y<z:

L(x,z) >= L(x,y)+L(y,z)

because chains through y can be concatenated.

V(x,z) >= V(x,y)+V(y,z)

because [x,y] union [y,z] is contained in [x,z], with intersection {y}.

When the standard rank exists, its difference is additive and equals
longest-chain length on every comparable pair. The same is true for an
integer unit-cover potential. These are distinct existence conditions:
standard rank fixes every minimal element at zero, whereas the weaker cover
potential only demands path-independent unit increments. Neither creates a
new duration beyond longest-chain length in the sector where it exists.

## Interpretation limit

Longest-chain length approximates proper time only in special causal-set
ensembles with a demonstrated manifold correspondence and a dimension-
dependent calibration. This audit supplies neither of those assumptions.
Interval cardinality is a volume-like count, not duration by itself.

## Coarse-graining obstruction

For a<b<c<d and the partition {a,b}|{c}|{d}, the quotient is A<B<C.
Using maximal fine longest-chain separations between fibers gives ratios
1/2 for A-B and 2/3 for A-C. No single scale factor preserves both.
