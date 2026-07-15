# A29.1 — Refinement Consistency, Base Measure, and Nondegeneracy

## Additive-mass refinement theorem

Let a finite marked context be represented by the measure

`nu = sum_j mu_j delta_{q_j}`

with positive masses `mu_j`. Let `T_nu(q)` be any context score determined
only by `nu` and the marked point. Define

`P_j = mu_j f(T_nu(q_j)) / sum_k mu_k f(T_nu(q_k))`

for positive `f`.

Refine alternative `r` into exact clones with the same q-value and masses
`mu_{r,a}` satisfying `sum_a mu_{r,a}=mu_r`. The measure `nu` is unchanged,
so every score `T_nu` is unchanged. The sum of clone weights is

`sum_a mu_{r,a} f(T_nu(q_r))
 = mu_r f(T_nu(q_r))`.

Therefore all macro probabilities are exactly preserved.

## Necessity within factorized clone models

For a factorized kernel `P_j proportional to a_j f(s_j)`, exact consistency
under arbitrary exact-clone refinements requires the coefficients of clones
to sum to the original coefficient. The coefficients therefore behave as a
finitely additive base mass.

## Naive cloning

If every listed alternative is assigned unit coefficient, splitting one
alternative into m clones multiplies its macro weight by m. Exact refinement
consistency fails even when the score itself is context-stable.

## Extreme-alternative limit of unweighted z-score

For n fixed old values and one new value M tending to positive infinity,

`z_old -> -1/sqrt(n)`,
`z_new -> sqrt(n)`.

The new probability approaches a strictly positive value, while odds among
old alternatives approach one. Numerical extremity does not create an
irrelevant alternative at fixed degree.

## Nondegeneracy limit

For a fixed weighted context with positive variance, the weighted mean,
variance, standardized scores, and normalized positive kernel are continuous
under addition of a bounded-score alternative whose mass tends to zero.

This convergence is not uniform as the original variance tends to zero.
At the zero-variance boundary the standardized score is undefined, and an
arbitrarily small mass at a separated score can cause an order-one change.

## Interpretation

A projectively coherent contextual normalization is mathematically possible,
but it requires a base measure or equivalent additive multiplicity data and
an explicit treatment of the zero-variance boundary. This theorem does not
identify either structure with physical volume or dynamics.
