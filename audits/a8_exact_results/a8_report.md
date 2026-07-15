# A8 — Canonical Internal Order Audit

## Exact scope

- Vertices: 5
- Possible directed non-loop edges: 20
- Labeled digraphs enumerated: 1,048,576
- Distinct labeled condensation-poset codes: 5,234

## Main counts

- Strongly connected: 565,080
- Nontrivial condensation: 483,496
- Nontrivial chain condensations: 390,780
- Nontrivial graded condensations: 482,296
- Nontrivial nongraded condensations: 1,200

## Exact negative findings

1. Reversing all edges preserves SCCs and dualizes the condensation order.
   Height, width, SCC count, and gradedness cannot choose a temporal arrow.

2. Gradedness is nearly universal at n=5:
   0.997518077
   of nontrivial condensations are graded. It is therefore weak as a selector.

3. A single edge flip changes the labeled condensation structure in
   0.292968750 of all graph-edge pairs,
   and changes height in 0.254760742.

4. The profile is not determined solely by exact labeled in/out degrees:
   47,361 degree fibers contain more than one
   (SCC count, height, width) profile.

## Scientific status

The SCC condensation is a canonical, static partial order derived without
external time or geometry. However, the exact audit does not justify calling
it physical time. It supplies precedence only after the directed relation has
already been chosen, is dual under edge reversal, is strongly density
dependent, and is moderately fragile under one-edge perturbations.
