# A33 — Projective Branch Fractions

## Ratio theorem
Let a refinement hierarchy carry a positive finitely additive weight W. For
every node A partitioned into children B_a,

W(A) = sum_a W(B_a).

Then

p(B_a | A) = W(B_a) / W(A)

is normalized, and the probability of every leaf is W(l)/W(root), independent
of grouping and refinement order.

Conversely, a path-independent branching law additive under disjoint
regrouping defines such a weight up to one common multiplicative constant.
Projectivity therefore selects the ratio architecture, not terminal weights.

## q-weighted law
For terminal q marks and base masses mu,

W_lambda(A) = sum_{l in A} mu_l exp(-lambda q_l)

is additive. The split W_lambda(B)/W_lambda(A) is exactly projective and its
sufficient subtree message composes by addition.

Using exp(-lambda times child mean q), with or without multiplying by child
mass, is generally nonadditive and grouping-dependent.

## Maximum relative entropy
Maximizing relative entropy with reference mu and a fixed expected-q
constraint gives p_l proportional to mu_l exp(-lambda q_l). Hierarchical
factorization is exact only when subtree partition sums are transmitted.

## Boundary
The theorem does not derive mu, q, lambda, the expected-q constraint, or a
physical refinement hierarchy.
