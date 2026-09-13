# A114-B2-B logical audit

## Verdict

**PASS.** No use of the target conclusion was found in either bridge.

## Dependency graph

### Bridge A

Input:

- frozen tail contract `M>=521`, `129/1000<=s<=133/1000`;
- `j=b+2`;
- exact A112-A k-space formula for `F_j^up`;
- A89/A112-A slope and `b>=89` gates;
- independently re-audited A112-A V2 cofactor/remainder bounds.

Output:

`Phi=F_j^up<0 => 3j-h>=13`.

No gamma-minus primal mass is used in Bridge A.

### Bridge B

Input:

- `h>=260`;
- `1/3<j/h<3/8`;
- `3j-h>=13`;
- frozen beta, gamma and parity-normalized epsilon.

Equations used:

- P normalization and mean;
- Q normalization, mean and target;
- active beta-minus;
- active gamma-minus.

Output:

`p_j>0 => p_0<0` for the pure central-Q gamma-minus basis.

The alpha equation, compressed objective and `Phi` do not appear in Bridge B.

## Denominator orientation

The symbolic certificate derives the common denominator rather than assuming its sign. It writes it as a positive scalar times

`(U(h+1)-1) * D2`

(with an additional positive factor `U` for `c_j`). The first factor is negative for `h>=260`. The exact leading/remainder certificate proves `D2>0` in both parities. Hence the denominator orientation used for all coefficient signs is fixed independently.

## Zero-order logic

The certificate proves

`a0<0<c0`, `cj<0<aj`, `K=c0*aj-cj*a0<0`.

Thus both zeros are positive and

`t_j-t_0 = K/(a0*aj) > 0`

because `a0*aj<0`. Therefore `p_j>0` forces `t>t_j>t_0`, hence `p_0<0`.

## Negative controls

The fourteen finite A102 strict-`b+2` gamma-minus witnesses are not excluded: all have `3j-h<13` and remain strictly primal positive. This directly checks that the proof has not silently replaced a tail statement by an all-M statement.

## Non-dependencies

The theorem does not depend on:

- the exploratory architecture tree;
- unrestricted high-precision simplex output;
- A102 class frequencies;
- the endpoint-released, QI or QA candidate passes;
- any fitted numerical architecture threshold.

Those computations are falsification/context only.
