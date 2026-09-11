# A111/A111B — Exact tail reconnaissance after the replicated finite A109 theorem

## Epistemic status

These are **finite exact reconnaissance tests**, not an all-M theorem.

The A110 finite structural theorem is independently replicated on `14 <= M <= 520`.
A111 asks whether the newly isolated structural inequalities show an immediate
failure beyond that finite cutoff.

No new canonical full-KKT/full-atlas outcome after rank 430 is inspected.

## A111 preregistered tail sample

Frozen SHA-256:

`0dce412234d4e20f605b92731f79b4ca121bf3726ef562bfc7a2129980005c59`

Exact M values:

`521, 522, 523, 600, 700, 800, 900, 1000, 1200, 1500, 2000`

Exact probes:

`129/1000, 131/1000, 133/1000`

For each probe the three candidate offsets `b+1,b+2,b+3` were tested.

Outcome:

- exact cases: **99**
- unique `(M,j)` pairs: **58**
- strict local-max cases: **33**
- exact failures: **0**
- verdict: `PASS_RECONNAISSANCE_NO_COUNTEREXAMPLE`

Every preregistered case preserved:

- negative slopes for the six residual reduced-cost functions;
- the `RQ(2)` minimum-threshold ordering;
- positive dual denominator;
- negative `N_gamma / E_j` proportionality factor;
- local compressed maximum => positive actual `RQ(2)`;
- primal adjacent affine slopes `(-,+)`;
- `A<0`, `B>0`, and `t'>0` at the exact probe;
- the q_h barrier relative to `p_(j+1)`.

## A111B tight-edge stress

A111 showed that the smallest relative margins occurred near the upper source
endpoint as M increased, so a second test was frozen before execution.

Frozen SHA-256:

`db55910ccb04c43667f8fe0509748f8c166e21f478bd6af2faa7970c06fcdfe6`

Tested:

- `M = 2500, 3000, 4000, 5000`
- `s = 133/1000`
- offsets `b+1,b+2,b+3`

Outcome:

- exact cases: **12**
- strict local-max cases: **4**
- exact failures: **0**
- verdict: `PASS_NO_COUNTEREXAMPLE`

The exact signs remain positive through M=5000.

The dimensionless decimal margins below are diagnostics only; their signs were
established with exact rational arithmetic:

| M | selected j | RQ2 relative margin | smallest threshold gap | gamma relative margin |
|---:|---:|---:|---:|---:|
| 2500 | 432 | 2.703287726834342097e-14 | 6.695098302616497733e-14 | 2.027846814881161840e-13 |
| 3000 | 518 | 8.446437315896868076e-17 | 3.226833699000595906e-16 | 1.023186343377405646e-15 |
| 4000 | 689 | 2.111667841001196182e-20 | 7.975496713779276094e-21 | 6.260203926648817361e-21 |
| 5000 | 861 | 3.002474366780970829e-25 | 1.852667378508876750e-25 | 3.357036350937443343e-25 |

## Interpretation

The positive signs do not disappear immediately after M=520.  However the
relative margins become very small as M grows.  Therefore a larger finite scan
would add little mathematical value: the next useful step is an **analytic
tail bound**, not brute-force extrapolation.

The strongest target is to prove, under the large-M compressed-contact
hypotheses, that

1. `RQ(2)` remains the first reduced-cost threshold;
2. strict local compressed maximality forces `RQ(2)>0`;
3. the dual denominator remains positive;
4. the adjacent primal monotonicities remain strict.

If one of these fails analytically, the correct response is to locate an exact
large-M counterexample.  Zero failures in A111/A111B alone do not establish
any universal or all-M claim.
