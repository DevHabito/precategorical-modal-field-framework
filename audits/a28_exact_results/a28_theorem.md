# A28 — q-Score Context–Scale Incompatibility

## Theorem

Let `D_S(x,y)` be the difference between scalar scores assigned to two
alternatives `x,y` in a finite context `S`. Assume:

1. Extension stability: adding arbitrary alternatives leaves `D_S(x,y)`
   unchanged.
2. Positive-affine invariance:
   `D(ax+b,ay+b)=D(x,y)` for every `a>0`.
3. Continuity and cardinality: `D` is continuous in quantitative inputs and
   `D(x,x)=0`.

Extension stability removes all dependence on the surrounding context.
Translation invariance gives `D(x,y)=h(x-y)`. Scale invariance gives
`h(a d)=h(d)` for all `a>0`. Hence `h` is constant on positive separations
and constant on negative separations. Continuity at zero and `h(0)=0` force
both constants to zero.

Therefore the only continuous cardinal score satisfying all assumptions is
trivial.

## Consequences

- Raw q differences are extension-stable and cardinal, but need a scale
  convention or a free lambda.
- Local z-score and MAD normalization are positive-affine invariant and
  cardinal, but context-dependent.
- Rank is monotone-invariant but ordinal and context-dependent.
- Global normalization is affine-invariant and cardinal but nonlocal.
- A nontrivial extension-stable affine-invariant escape must be discontinuous
  and ordinal, or must receive an independently fixed scale.

This is a structural no-go, not a statement that any one candidate is
empirically false.
