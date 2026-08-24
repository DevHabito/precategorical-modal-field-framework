# A105 — Exact continuum atlas for the 40 legacy two-band segments

## Question

A102 contains forty exact rational witnesses whose strict finite-LP optimum belongs to the legacy two-band family

\[
P=\{0,j,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with \(\alpha+\) and \(\beta-\) active and both gamma inequalities inactive. A105 asks whether each pointwise certificate remains valid on its complete A95/A102 source segment, only on a proper witness-containing component, or fails internally.

The forty source records consist of:

- 14 `unique_b_plus_2` segments;
- 26 right-hand segments of `b_plus_1_to_b_plus_2` transitions.

## Exact symbolic reduction

Only the active alpha row depends on the probe \(s\). Around the exact reference \(s=1/8\), a Sherman–Morrison row update expresses every basic variable, active multiplier, unused-atom reduced cost, inactive-band slack, and the common basis denominator as a sparse rational polynomial in \(s\).

Across the forty records this gives:

- **24,312 exact KKT conditions**;
- **24,352 numerator/denominator sign obligations**;
- exact agreement with all forty pointwise condition counts routed by A102;
- no floating-point sign gate.

## Result

Every witness lies in a genuine open strict-KKT phase, but none of the forty legacy two-band bases covers its complete source segment:

\[
\boxed{0\text{ complete source-segment certificates}}
\]

\[
\boxed{40\text{ proper two-sided strict subcomponents}}
\]

\[
\boxed{0\text{ unresolved cases}}.
\]

All 14 `unique_b_plus_2` records and all 26 `b_plus_1_to_b_plus_2` right-side records are partial.

## Boundary mechanisms

A105 isolates two algebraic boundaries for every record, for a total of **80 selected roots**.

### Left boundary

For the six smallest supports

\[
M\in\{40,41,57,74,97,120\},
\]

the inactive \(\gamma-\) slack reaches zero as \(s\) decreases. For the remaining 34 records, the endpoint atom \(p_0\) reaches zero.

Thus the left boundary census is:

| Mechanism | Count |
|---|---:|
| inactive \(\gamma-\) slack reaches zero | 6 |
| basic mass \(p_0\) reaches zero | 34 |

### Right boundary

For all forty records, increasing \(s\) drives the inactive \(\gamma+\) slack to zero:

| Mechanism | Count |
|---|---:|
| inactive \(\gamma+\) slack reaches zero | 40 |

This gives a uniform right-hand exit law for the declared legacy two-band sample, but A105 does not promote that finite census to an all-\(M\) theorem.

## Competing roots and exact ordering

The endpoint scan identifies **181 sign-changing candidate roots**. Eighty are selected as the nearest boundaries of the witness-containing components. The remaining candidates are ordered away from the witness by **101 exact rational bracket inequalities**.

Every selected boundary has:

- opposite exact signs at the isolating endpoints;
- a derivative interval with fixed nonzero sign;
- a locally unique simple root;
- all nonselected KKT conditions strictly positive on the complete hull spanning the isolating brackets.

The audit also constructs **80 exact rational outside counterexamples**, one beyond each selected boundary, where the responsible KKT condition is strictly negative.

## Widths

The widest certified component occurs at \(M=40\), with approximate width

\[
4.8322971005358234\times10^{-4}.
\]

The narrowest occurs at \(M=502\), with approximate width

\[
8.446803405359654\times10^{-5}.
\]

These decimals are provided only for readability. The catalogue stores exact rational component endpoints and exact rational root brackets.

## Structural interpretation

The legacy two-band pointwise solutions are not isolated rational coincidences. They persist on open intervals. However, their complete source segments are too large:

- at low \(M\), decreasing \(s\) activates \(\gamma-\);
- after the first six supports, decreasing \(s\) removes the forced endpoint atom \(p_0\);
- for every one of the forty records, increasing \(s\) activates \(\gamma+\).

This is a genuine falsifiable limitation of the legacy two-band architecture. The result does not rescue the family by changing the contract or adding an untested parameter.

## Claim boundary

A105 proves exact continuum persistence only for the forty A102 records classified as `legacy_two_band_compressed`, inside their declared A95/A102 rational source segments. It does not prove:

- continuum lifting for the 940 legacy three-band witnesses;
- coverage of complete A92 algebraic cells;
- validity outside the declared probe interval or finite support range;
- a universal support or gamma-activation law;
- any physical, spacetime, or ontological interpretation.

## Independent standalone replay

A separate standalone package recomputed all forty exact records in isolated processes, reassembled the atlas, and regenerated the figure. The forty record JSON files, consolidated result, consolidated catalogue, and figure were compared against the integrated repository. All **43 comparisons** are SHA-256 identical.
