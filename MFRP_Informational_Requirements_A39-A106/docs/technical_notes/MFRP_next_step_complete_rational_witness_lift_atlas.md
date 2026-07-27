# A102 — Complete exact rational-witness lift atlas

## Status

**Complete pointwise exact lift atlas for all 1,063 A95 rational phase-segment witnesses, with exact provenance, source-certificate validation, and an independent replay layer.**

A95 converted the 858 exact A94 compressed-objective cells into 1,063 open phase segments:

- one rational witness for every fixed phase;
- two rational witnesses, one on each side, for every simple adjacent transition.

At those witnesses, A95 found:

\[
980
\]

unique strict lifts in the original natural families and

\[
83
\]

witnesses with no natural lift.

A97–A101 subsequently resolved all 83 obstructions. A102 freezes the complete witness key set and merges every resolution into one exact atlas.

No contract parameter is changed and no unresolved witness is removed.

## Frozen witness key

Every atlas row is identified by the six-field key

\[
(M,b,\text{compressed phase},\text{phase side},s,j),
\]

where:

- \(M\) is the support maximum;
- \(b\) is the A92 algebraic base contact;
- \(s\) is the exact rational interior witness;
- \(j\) is the unique compressed maximizer at that witness.

The A95 catalogue contains exactly

\[
\boxed{1063}
\]

such keys, and A102 verifies that all 1,063 are distinct.

## Exact resolution partition

Every key receives exactly one resolution class.

| Broad resolution class | Witnesses |
|---|---:|
| legacy natural lift | 980 |
| endpoint-released, gamma inactive | 76 |
| q0/q1 co-entry, gamma inactive | 3 |
| q0/q1 co-entry, gamma− active | 4 |
| **Total** | **1,063** |

The detailed natural-family split is:

| Detailed class | Witnesses |
|---|---:|
| legacy three-band, gamma+ | 922 |
| legacy three-band, gamma− | 18 |
| legacy compressed two-band | 40 |
| endpoint-released, gamma inactive | 76 |
| q0/q1, gamma inactive | 3 |
| q0/q1, gamma− active | 4 |

Thus the original A95 obstruction set closes exactly as

\[
\boxed{83=76+3+4}.
\]

The three post-A95 resolution sets are pairwise disjoint and their union is exactly the 83-key A95 obstruction set.

## Architecture classes

### 1. Legacy natural families

The 980 A95 natural passes use one of:

\[
P=\{0,j,M\},\qquad Q=\{1,h,h+1\},
\]

with \(\gamma\) inactive, or

\[
P=\{0,k,k+1,M\},\qquad Q=\{1,h,h+1\},
\]

with one active gamma orientation.

The exact counts are 40 compressed, 922 gamma+, and 18 gamma−.

### 2. Endpoint-released family

Seventy-six former obstructions are resolved by

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

with active \(\alpha+\), \(\beta-\), and inactive \(\gamma\).

### 3. q0/q1 co-entry with gamma inactive

Three witnesses, at

\[
M\in\{396,455,496\},
\]

require

\[
P=\{j,M\},\qquad Q=\{0,1,h,h+1\},
\]

with active \(\alpha+\), \(\beta-\), and inactive \(\gamma\).

### 4. q0/q1 co-entry with gamma− active

Four witnesses, at

\[
M\in\{443,449,484,490\},
\]

require

\[
P=\{j-1,j,M\},\qquad Q=\{0,1,h,h+1\},
\]

with active \(\alpha+\), \(\beta-\), and \(\gamma-\).

## Complete KKT condition census

Under the frozen finite-LP contract, every selected architecture has

\[
2M+9
\]

strict KKT conditions: basic variables, active-band multipliers, all nonbasic atom reduced costs, and all inactive-band slacks.

Summed over the complete 1,063-witness atlas, A102 records

\[
\boxed{676\,847\text{ exact KKT conditions}}.
\]

The broad-class totals are:

| Resolution class | Exact KKT conditions |
|---|---:|
| legacy natural | 615,414 |
| endpoint-released, gamma inactive | 54,944 |
| q0/q1, gamma inactive | 2,721 |
| q0/q1, gamma− active | 3,768 |
| **Total** | **676,847** |

For the 980 natural rows, A102 validates the exact A95 PASS classification, the unique selected branch, the frozen source verdict and gates, and the source-file hashes.

For the two unrestricted discovery certificates, A102 additionally parses every exact rational condition directly:

- A98: 801/801 positive conditions and exact primal–dual equality;
- A100: 895/895 positive conditions and exact primal–dual equality.

## Independent replay layer

A102 does not pretend that copying an earlier JSON row is an independent reconstruction. It therefore adds a separate replay layer.

It independently re-evaluates:

- all 83 post-A95 obstruction resolutions;
- all 40 legacy compressed natural lifts;
- all 18 legacy gamma− natural lifts;
- 42 deterministic, support-spread legacy gamma+ natural lifts.

Thus

\[
\boxed{183}
\]

selected branches are independently recomputed in A102.

Results:

\[
\boxed{183/183\text{ strict exact KKT passes}},
\]

with:

- zero replay failures;
- zero support mismatches;
- zero active-band mismatches;
- zero condition-count mismatches.

The remaining 880 natural rows retain the already exact A95 source certificates rather than being redundantly recomputed in this consolidation audit.

## Provenance closure

A102 pins 18 source inputs from A95, A97, A98, A99, A100, and A101 by SHA-256. These include:

- source result JSONs;
- source catalogues and full certificates;
- the six relevant audit programs.

Every merged row records:

- the exact witness key;
- the source audit that resolves it;
- the source result or certificate path;
- the selected supports;
- the active bands;
- the source KKT condition count;
- whether an independent A102 replay was performed.

No key is missing, duplicated, multiply routed, or unresolved.

## Scientific conclusion

The finite rational-witness lift problem opened by A95 is now completely closed:

\[
\boxed{
\text{every one of the 1,063 declared rational phase witnesses has a strict exact global finite-LP KKT certificate.}
}
\]

This closure was not achieved by changing the contract. The 83 failures forced three broader active-set families, and each new family remained falsifiable on the residual witnesses.

## What A102 does not prove

A102 does not establish:

1. a lifted KKT theorem on the complete interior of all 858 algebraic A94 cells;
2. interval persistence for every one of the 1,063 witness bases;
3. that the four broad architecture classes remain exhaustive outside the declared interval or beyond \(M=520\);
4. a universal support theorem for arbitrary means, channels, tolerances, or transforms;
5. any physical, spatial, temporal, material, or ontological interpretation.

Only A97, A99, and A101 presently establish open-interval persistence, and only for three representative bases.

## Next rigorous target

The next useful step is no longer another pointwise obstruction search.

A103 should determine how far the pointwise atlas can be promoted toward a continuum lifted theorem. A defensible first target is the complete endpoint-released class:

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

with gamma inactive.

For the 76 A97-resolved witnesses, A103 should:

1. construct symbolic or interval-rational KKT conditions on each parent A94 phase segment;
2. certify the maximal connected strict component containing the rational witness;
3. detect whether the component covers the full phase segment;
4. preserve any internal root, basis exit, or counterexample;
5. classify full-cell, partial-cell, and point-only support.

That would begin the transition from a complete pointwise atlas to a genuine continuum lift atlas without assuming that all 76 bases persist.
