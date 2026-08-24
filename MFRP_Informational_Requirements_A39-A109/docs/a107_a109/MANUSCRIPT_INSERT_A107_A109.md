# Manuscript-ready section: exact adjacent-boundary structure in the legacy gamma-plus family

## Prospective continuum boundary study

After the A106 gamma-minus continuum atlas, the remaining large legacy class was the three-band gamma-plus family. For this family the basic supports are

\[
P=\{0,j,j+1,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with active `alpha+`, `beta-`, and `gamma+`. Only the source-probe alpha row varies across a frozen source segment, so the KKT system admits an exact rank-one reconstruction with a common denominator and exact rational numerator polynomials for every basic variable, active dual variable, reduced cost, and inactive slack.

The first structural conjecture was one-sided: partial strict components appeared to terminate when the upper adjacent basic mass `p_{j+1}` reached zero on the left. That conjecture is false. Canonical rank 105 (`M=119`, `j=22`) is an exact counterexample. Its full KKT atlas gives a proper strict subcomponent whose selected boundary is instead the **right** zero of `basic_p_22`. The selected root is isolated by an exact rational bracket, its derivative is negative throughout the bracket, all 248 core conditions certify, and an independent direct-matrix regression gives 988 exact comparisons with zero discrepancy. The one-sided statement is therefore rejected rather than repaired.

The replacement candidate is two-sided and local. Writing each adjacent basic variable as

\[
p_k(s)=\frac{N_k(s)}{D(s)},
\]

we test the rule

\[
p_{j+1}=0 \quad\text{as the candidate left boundary},
\qquad
p_j=0 \quad\text{as the candidate right boundary},
\]

under exact positivity of `D`, strict increase of `N_{j+1}`, strict decrease of `N_j`, and positivity of both adjacent variables at the frozen witness. The endpoint sign pair then predicts full coverage, a left partial component, a right partial component, or the logically possible two-sided partial component.

The development fit on canonical ranks 1-105 was post-hoc and is not counted as prospective evidence. The rule was subsequently frozen before future outcomes. In the stored prospective sequence through canonical rank 414, 309 records are mathematically resolved and 308 count as strict-clean prospective cases because one previously documented rank (295) has a protocol-ordering exception. The resolved sequence contains 215 full source-segment coverages and 94 proper strict subcomponents. Of the partial components, 88 terminate at the left adjacent variable and 6 at the right adjacent variable. No two-sided case and no non-adjacent selected KKT obstruction has been observed in that sequence. Independent symbolic-versus-direct matrix checks total 475,782 exact rational comparisons with zero mismatch; the strict-clean comparison count is 473,770.

These results are finite prospective evidence, not an all-catalogue theorem. In particular, the computation does not prove that a non-adjacent reduced cost or slack can never become the first obstruction on an untested gamma-plus record. A single exact future counterexample would refute the universal form of the adjacent-boundary conjecture.

The next holdout, A109-H19, is frozen on canonical ranks 415-430 and remains unexecuted in the supplied update. It predicts eleven full records and five partial records: four left boundaries and one right boundary. The right-branch prediction is frozen at rank 428, where `basic_p_56` is predicted to be the right boundary. This holdout therefore remains a genuine prospective test rather than a retrospective fit.
