# MFRP next step: exact continuum atlas for the legacy gamma-minus segments

## Question

A102 contains eighteen rational phase witnesses whose unique strict finite-LP lift has

\[
P=\{0,j-1,j,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with the active bands \(\alpha+\), \(\beta-\), and \(\gamma-\). A106 asks whether each pointwise certificate persists throughout its complete A95/A102 rational source segment, only on a proper witness-containing subcomponent, or fails internally.

The family, source segments, and active-band signature are frozen before the continuum computation. No support atom or active constraint is added after a boundary is found.

## Exact symbolic reduction

Only the alpha row varies with the probe \(s\). The exact inverse at the reference probe \(s=1/8\) is updated by a Sherman-Morrison rank-one row formula. This yields one sparse common denominator and sparse numerator polynomials for every strict KKT condition:

- eight basic variables;
- three active dual multipliers;
- every reduced cost for unused \(P\)- and \(Q\)-atoms;
- the three inactive opposite-band slacks.

Across the eighteen records, A106 reconstructs 2,410 KKT conditions and 2,428 numerator/denominator sign obligations. As an independent implementation check, all 2,410 rational-function values at the source witnesses are compared exactly with direct matrix inversion of the full finite-LP basis. The comparison closes with 2,410/2,410 literal rational equalities.

## Classification

The exact continuum census is:

| Classification | Count |
|---|---:|
| Complete source-segment coverage | 1 |
| Proper witness-containing strict component | 17 |
| Internal failure or unresolved | 0 |

The single complete source segment is the left side of the inverse compressed exchange at

\[
M=28,
\]

with source interval

\[
\left(\frac{129}{1000},\frac{19385984695877734883871}{147573952589676412928000}\right).
\]

The other seventeen bases remain strict from the lower source endpoint up to one internal algebraic boundary. No record has an internal left boundary.

## Uniform finite-atlas boundary mechanism

For every one of the seventeen partial components, the selected right boundary is the root at which the lower adjacent basic mass vanishes:

\[
p_{j-1}=0.
\]

Thus the legacy gamma-minus basis exits by losing the lower adjacent atom of \(P\). This is a uniform mechanism across the eighteen-record finite atlas, not an all-\(M\) theorem.

A106 identifies 22 sign-changing candidate roots. Seventeen are selected as the nearest witness-containing boundaries. Five exact bracket-ordering inequalities prove that the remaining candidates lie farther from the witness. Every selected boundary has:

- an exact rational isolating bracket;
- opposite endpoint signs;
- a fixed nonzero derivative sign on the bracket;
- exact positivity of every other KKT condition on the complete boundary hull;
- an exact rational point beyond the boundary where \(p_{j-1}<0\).

Hence the seventeen partial classifications are genuine failures of the frozen basis beyond the selected roots, not merely failures of the proof technique.

## Result

A106 proves that all eighteen legacy gamma-minus pointwise lifts persist on nontrivial open intervals. One covers its complete source segment, while seventeen cover exact one-sided strict subcomponents. There are no unresolved segments.

The result remains restricted to the eighteen A95/A102 rational source segments. It does not cover the 922 legacy gamma-plus witnesses, complete A92 algebraic cells, arbitrary values of \(M\), altered transforms or noise contracts, or any physical interpretation.

## Next rigorous target

The remaining natural family contains 922 legacy gamma-plus witnesses. A direct monolithic continuum atlas would be unnecessarily expensive and difficult to audit. The next step should therefore begin with an exact deterministic partition and a first preregistered batch, while preserving a global key manifest. Each batch must use the same strengthened standard: direct-matrix/rank-one regression, exact competing-root ordering, complete hull certification, and rational outside counterexamples.
