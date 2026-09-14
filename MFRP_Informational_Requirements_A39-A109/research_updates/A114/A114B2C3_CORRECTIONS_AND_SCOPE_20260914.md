# A114-B2-C3 — corrections, rejected routes, and scope

## Authoritative correction: QA common-mass convexity shortcut is false

During construction of the QI/QA proof, an intermediate argument claimed that because the gamma-zero QA basis lies on the alpha+/beta- edge between endpoint-released E and QI, positivity of all common masses would follow by convexity.

That statement is false on the QA side.

The independent exact `Fraction` crosscheck gives the three QA controls

- `M=521, s=129/1000`,
- `M=970, s=129/1000`,
- `M=1000, s=129/1000`,

for which the rival QI basis already has

`q1^QI < 0`.

Therefore QI is not a primal-feasible endpoint there and cannot be used to infer positivity of the QA common masses.

The final theorem keeps only the legitimate edge consequences:

- `q0^QA>0`;
- `p_(j-1)^QA>0`.

The remaining QA masses are proved independently from the QA Cramer system:

- positive `Ut` numerator and `D_QA>0`;
- `U p_(j-1)/(Ut) < 1/4`;
- exact P normalization/mean formulas for `p_j,p_M`;
- exact beta-minus minus gamma-minus equation for `q1`;
- exact central-Q block for `q_h,q_(h+1)`.

The logical audit fails if the rejected convexity shortcut is reintroduced into the theorem text.

## Exact-control execution note

A new all-six complete atom scan in one `Fraction` process was attempted during the C3 session but exceeded the interactive execution budget. This is not counted as a failed mathematical gate.

The repository already contains the independently written `A114B2C_12_POINT_FULL_KKT_SUMMARY_20260913.json`, which gives complete `2M+9` exact KKT scans for the same three QI and three QA controls. C3 therefore uses that pre-existing artifact as its full atom-by-atom regression layer and adds a newly written independent `Fraction` reconstruction of the raw QI/QA matrices, pivot signs, primal/dual/slack gates, and ECT sentinels.

Finite controls remain regression/falsification evidence only. They are not premises of the all-tail theorem.

## Strict scope

A114-B2-C3 covers only

- `M>=521`;
- `129/1000<=s<=133/1000`;
- strict compressed maximizer `j=b+2`;
- `Phi<0`;
- residual interior `p0^C<0` and `r_E(q0)<0`;
- strict classifier sign `Gamma=S_(gamma-)^QI !=0`.

It does not classify strict uniqueness on

- `Phi=0`;
- `p0^C=0`;
- `r_E(q0)=0`;
- `Gamma=0`;

and makes no claim outside the frozen source/tail contract or any physical interpretation.

## Historical dependency discipline

The proof does not depend on A108's refuted one-sided boundary conjecture. It imports C1/C2/B2-B/source-box results only inside their promoted contracts and uses the established generalized-Vandermonde / extended-Chebyshev zero-count structure for the displayed exponential families.
