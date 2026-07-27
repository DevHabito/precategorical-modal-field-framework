# Sharp Prediction Intervals from Finite Exponential Data

**Programme:** Modal Field Research Programme  
**Provisional audit:** A39  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01; no new physical assumptions

## Technical abstract

MFRP-TR-2026-01 separates exact static aggregation from autonomous dynamic closure. A subsequent finite-grid theorem shows that no finite positive set of exponential effective scores closes the centered contraction on the unrestricted class of finite distributions. This note turns that obstruction into a quantitative result.

For a probability law supported on a compact interval \([L,U]\), with known mean and finitely many Laplace values

\[
L(\lambda_j)=\int e^{-\lambda_j x}\,dP(x),
\]

the sharp lower and upper values of an omitted transform \(L(\mu)\) are generalized moment problems. Extrema exist, and an optimizer can be chosen with at most \(r+2\) atoms when \(r\) transform values, the mean, and normalization are fixed. Dual exponential-polynomial envelopes convert any admissible coefficients into certified bounds.

For the exact five-point constraints inherited from the two-score nonclosure witness,

\[
\operatorname{supp}P\subset[0,4],\qquad
\mathbb E[X]=2,
\]

\[
L(\log2)=\frac{31}{80},\qquad
L(2\log2)=\frac{341}{1280},
\]

we certify the sharp omitted-transform interval at \(\mu=\tfrac12\log2\):

\[
0.5599571720587944588199174791268\ldots
\le L(\mu)\le
0.5630735173874428658558427940415\ldots .
\]

Consequently,

\[
1.657209591181684697263491194551\ldots
\le Q_\mu\le
1.673223214081462136913149478560\ldots,
\]

and, for the centered contraction with \(a=\tfrac12\),

\[
1.828604795590842348631745597275\ldots
\le Q'_{\log2}\le
1.836611607040731068456574739280\ldots .
\]

The bounds are sharp. A Krawczyk interval certificate validates the primal-dual contact systems inside boxes of radius \(10^{-30}\). Global dual feasibility follows from the extended complete Chebyshev property of the relevant exponential-polynomial system. The result is conditional on the bounded-support and moment contracts; it does not establish a physical mark, scale, contraction law, or empirical interpretation.

---

## 1. Starting point

For a probability distribution \(P\) on \(\mathbb R\), define

\[
L_P(\lambda)=\int e^{-\lambda x}\,dP(x),
\qquad
Q_P(\lambda)=-\frac{1}{\lambda}\log L_P(\lambda),
\quad \lambda>0,
\]

and let

\[
m_P=\int x\,dP(x).
\]

Under the centered contraction

\[
x' = m_P+a(x-m_P),\qquad 0<a<1,
\]

the exact transport identity is

\[
Q_{P'}(\lambda)=(1-a)m_P+aQ_P(a\lambda).
\]

The finite-grid nonclosure theorem shows that finitely many fixed positive values of \(Q\), even when combined with the mean, do not generally determine the omitted value at \(a\lambda\). The correct next question is not whether the missing value can be guessed, but what range it can occupy under explicit additional information.

This note adds one additional contract only:

\[
\operatorname{supp}P\subset[L,U].
\]

No distribution family, Gaussian closure, maximum-entropy law, or physical interpretation is assumed.

## 2. Generalized moment formulation

Fix distinct observed parameters

\[
\Lambda=\{\lambda_1,\ldots,\lambda_r\}\subset(0,\infty)
\]

and supplied values

\[
m,\qquad s_j=L_P(\lambda_j).
\]

Define the feasible moment class

\[
\mathcal F=
\left\{
P\in\mathcal P([L,U]):
\int x\,dP=m,
\quad
\int e^{-\lambda_jx}\,dP=s_j
\ \forall j
\right\}.
\]

For an omitted parameter \(\mu>0\), define

\[
\underline L_\mu=
\inf_{P\in\mathcal F}\int e^{-\mu x}\,dP(x),
\]

\[
\overline L_\mu=
\sup_{P\in\mathcal F}\int e^{-\mu x}\,dP(x).
\]

### Proposition 1 — existence of sharp bounds

If \(\mathcal F\neq\varnothing\), both extrema are attained.

### Proof

The set of probability measures on the compact interval \([L,U]\) is weak-* compact. The supplied moment constraints are closed because their integrands are continuous. Hence \(\mathcal F\) is compact. The omitted-transform functional is continuous and linear in the measure, so it attains its minimum and maximum. \(\square\)

### Proposition 2 — finite atomic extremizers

An optimizer may be chosen with at most

\[
r+2
\]

support points.

### Justification

The feasible set is cut out by \(r+2\) affine equalities: normalization, the mean, and \(r\) transform values. Standard extreme-point results for generalized moment sets imply that an extreme feasible measure has no more atoms than the number of independent restrictions. Since a linear objective attains an optimum at an extreme point, an optimizer can be chosen with at most \(r+2\) atoms.

This is a support-size theorem, not a claim that every optimizer has exactly \(r+2\) atoms.

## 3. Dual envelopes

Let

\[
h_y(x)=y_0+y_1x+\sum_{j=1}^r y_{j+1}e^{-\lambda_jx}.
\]

If

\[
h_y(x)\le e^{-\mu x}\qquad\forall x\in[L,U],
\]

then every feasible measure satisfies

\[
y_0+y_1m+\sum_{j=1}^r y_{j+1}s_j
\le L_P(\mu).
\]

Likewise, if

\[
h_y(x)\ge e^{-\mu x}\qquad\forall x\in[L,U],
\]

then

\[
L_P(\mu)\le
y_0+y_1m+\sum_{j=1}^r y_{j+1}s_j.
\]

Thus the dual problems are

\[
\underline L_\mu
\ge
\sup_y
\left\{
y_0+y_1m+\sum_j y_{j+1}s_j:
 h_y\le e^{-\mu x}\text{ on }[L,U]
\right\},
\]

\[
\overline L_\mu
\le
\inf_y
\left\{
y_0+y_1m+\sum_j y_{j+1}s_j:
 h_y\ge e^{-\mu x}\text{ on }[L,U]
\right\}.
\]

Weak duality is immediate. For the concrete result below, sharpness is proved directly by constructing feasible primal measures and dual envelopes with the same objective values. Therefore no unverified general strong-duality assumption is needed.

## 4. Transport of the sharp interval

Because \(Q_\mu=-\mu^{-1}\log L_\mu\) decreases with \(L_\mu\),

\[
-\frac{1}{\mu}\log\overline L_\mu
\le Q_\mu\le
-\frac{1}{\mu}\log\underline L_\mu.
\]

For the centered contraction,

\[
Q'_{\lambda}=(1-a)m+aQ_{a\lambda}.
\]

Therefore, when \(\mu=a\lambda\), the sharp future interval is

\[
(1-a)m-
\frac{a}{\mu}\log\overline L_\mu
\le Q'_{\lambda}\le
(1-a)m-
\frac{a}{\mu}\log\underline L_\mu.
\]

Sharpness is inherited because the transport map is monotone affine in \(Q_\mu\).

## 5. Exact concrete constraint set

Use

\[
[L,U]=[0,4],
\qquad
\lambda_1=\log2,
\qquad
\lambda_2=2\log2,
\qquad
\mu=\frac12\log2.
\]

Fix

\[
\mathbb E[X]=2,
\qquad
L(\lambda_1)=\frac{31}{80},
\qquad
L(\lambda_2)=\frac{341}{1280}.
\]

These values are feasible. In particular, both exact finite-grid witnesses

\[
p^+=\left(
\frac{41}{200},\frac4{25},\frac{61}{200},\frac9{100},\frac6{25}
\right),
\]

\[
p^-=\left(
\frac{39}{200},\frac6{25},\frac{19}{200},\frac{31}{100},\frac4{25}
\right)
\]

on the support \(\{0,1,2,3,4\}\) obey all three constraints.

The extremizers need not equal these witnesses.

## 6. Sharp lower transform

The certified minimizing measure has two interior atoms:

\[
P_{\min}=w\,\delta_{x_1}+(1-w)\delta_{x_2},
\]

with

\[
x_1=0.281773719323071362811894223195\ldots,
\]

\[
x_2=3.055205199541641334998877053148\ldots,
\]

\[
w=0.380469179450751095184194782058\ldots .
\]

It satisfies the normalization, mean, and two observed transform constraints.

The lower dual envelope is

\[
h_-(x)=y_0+y_1x+y_2e^{-\lambda_1x}+y_3e^{-\lambda_2x},
\]

where

\[
\begin{aligned}
y_0&=0.477349599790244990141528985626\ldots,\\
y_1&=-0.068014244524767416852425638067\ldots,\\
y_2&=0.659141548109581056425486512890\ldots,\\
y_3&=-0.138064660924352776939866291090\ldots .
\end{aligned}
\]

Let

\[
r_-(x)=e^{-\mu x}-h_-(x).
\]

The contact equations are

\[
r_-(x_1)=r_-'(x_1)=r_-(x_2)=r_-'(x_2)=0.
\]

The Krawczyk operator certifies a unique solution of the complete primal-dual system inside a box of radius \(10^{-30}\) around the values above. Interval evaluation gives

\[
r_-(0)>0.0015735130245267303728507925734,
\]

\[
r_-(4)>0.0040503466337116142765020122851.
\]

The five functions

\[
1,\quad x,\quad e^{-\mu x},\quad e^{-\lambda_1x},\quad e^{-\lambda_2x}
\]

form an extended complete Chebyshev system on \([0,4]\). Hence a nonzero linear combination has at most four zeros counting multiplicity. The two certified double contacts already account for four zeros. Since the residual is positive at the endpoints, it cannot change sign. Therefore

\[
h_-(x)\le e^{-\mu x}
\qquad\forall x\in[0,4].
\]

Because the primal measure is supported entirely on contact points, primal and dual values agree. Thus

\[
\underline L_\mu=
0.559957172058794458819917479126819715636352009482\ldots .
\]

## 7. Sharp upper transform

The certified maximizing measure has support at the two endpoints and one interior point:

\[
P_{\max}=w_0\delta_0+w_1\delta_x+w_4\delta_4,
\]

with

\[
x=1.706620438632002877784597012279\ldots,
\]

\[
\begin{aligned}
w_0&=0.219316039422888895580042571501\ldots,\\
w_1&=0.489555179273828681575755554135\ldots,\\
w_4&=0.291128781303282422844201874364\ldots .
\end{aligned}
\]

The upper envelope has coefficients

\[
\begin{aligned}
y_0&=0.462697760713329471569616638142\ldots,\\
y_1&=-0.064012986755202832290252899933\ldots,\\
y_2&=0.704091297028579000997781787006\ldots,\\
y_3&=-0.166789057741908472567398425149\ldots .
\end{aligned}
\]

Define

\[
r_+(x)=h_+(x)-e^{-\mu x}.
\]

The contact conditions are

\[
r_+(0)=r_+(x)=r_+'(x)=r_+(4)=0.
\]

Again the complete contact system has a unique root in a radius-\(10^{-30}\) Krawczyk box. Interval evaluation gives

\[
r_+'(0)>
0.0257404363767228415426877980678,
\]

\[
r_+'(4)<
-0.00696882210720328180723106905958.
\]

The endpoint contacts, together with one double interior contact, account for four zeros. The ECT zero bound excludes additional zeros. The derivative signs fix the orientation, so

\[
h_+(x)\ge e^{-\mu x}
\qquad\forall x\in[0,4].
\]

Complementarity at the support points yields

\[
\overline L_\mu=
0.563073517387442865855842794041514628784443068397\ldots .
\]

## 8. Sharp score and one-step intervals

The omitted effective-score interval is

\[
1.657209591181684697263491194550953839917076104349\ldots
\le Q_\mu
\]

\[
Q_\mu\le
1.673223214081462136913149478560285680732032853903\ldots .
\]

With

\[
a=\frac12,
\qquad m=2,
\qquad \lambda=\log2,
\]

the exact transport law becomes

\[
Q'_{\log2}=1+\frac12Q_{(\log2)/2}.
\]

Therefore

\[
1.828604795590842348631745597275476919958538052174\ldots
\le Q'_{\log2}
\]

\[
Q'_{\log2}\le
1.836611607040731068456574739280142840366016426951\ldots .
\]

The width is

\[
0.008006811449888719824829142004665920407478374777\ldots .
\]

This width is the exact unresolved one-step uncertainty under the stated bounded-support and moment information. It is not sampling error and not a confidence interval. It is an identification interval over all admissible microscopic laws.

## 9. What this adds to the programme

The result produces a three-level hierarchy.

### Exact closure

Carry the full required parameter orbit, an equivalent transform representation, or a justified invariant family.

### Certified partial prediction

Carry finite transform data plus explicit support or tail information. The missing future score is then confined to a sharp interval.

### Uncontrolled approximation

Insert an assumed distribution family or truncate cumulants without proving an error bound. This may be useful, but it is not exact and should not be described as closure.

The A39 result occupies the second level. It converts the nonclosure obstruction into a computable and auditable prediction set.

## 10. Claim classification

### Established

1. Under compact support, the omitted exponential transform has attained sharp extrema.
2. Extremizers can be chosen finitely atomic, with at most the number of supplied affine constraints.
3. The supplied five-point constraint set has the sharp omitted-transform interval stated above.
4. The interval is certified by matching primal and dual constructions.
5. The resulting one-step \(Q_{\log2}\) interval is sharp under the centered contraction.

### Conditional inputs

1. support \([0,4]\);
2. mean \(2\);
3. the two exact observed Laplace values;
4. the centered contraction with \(a=1/2\);
5. the standard ECT theorem for real exponential-polynomial systems.

### Not established

1. a physical reason for the support interval;
2. a physical origin or measurement map for \(q\);
3. a physical value of \(\lambda\);
4. empirical validity of the centered contraction;
5. novelty of generalized moment duality or finite-atomic extremizers;
6. a universal error rate without support, tail, or regularity assumptions;
7. closure for nonlinear or stochastic microscopic updates.

## 11. Reproducibility

The companion script

`a39_sharp_prediction_interval_audit.py`

uses only `mpmath` and performs:

1. high-precision solution of both primal-dual contact systems;
2. interval Jacobian construction;
3. Krawczyk strict-inclusion tests in radius-\(10^{-30}\) boxes;
4. interval verification of the robust sign conditions;
5. interval propagation to \(L_\mu\), \(Q_\mu\), and \(Q'_{\log2}\);
6. a machine-readable JSON result with ten explicit gates.

The run verdict is

`PASS_SHARP_OMITTED_TRANSFORM_AND_FUTURE_SCORE_INTERVAL`.

The script does not numerically prove the general ECT theorem. That theorem is the analytic input used to promote the verified contact and sign data into global envelope inequalities.

## 12. Literature position

Finite generalized moment restrictions, finite-atomic extreme measures, and optimization over moment sets are classical. Relevant sources include:

- G. Winkler, “Extreme Points of Moment Sets,” *Mathematics of Operations Research* 13(4), 581–587, 1988. DOI: 10.1287/moor.13.4.581.
- I. Pinelis, “On the Extreme Points of Moments Sets,” *Mathematical Methods of Operations Research* 83, 325–349, 2016. DOI: 10.1007/s00186-015-0530-0.
- D. Henrion, M. Kružík, and S. Weis, “Extreme Points and Faces in the Moment Problem,” arXiv:2606.21391, 2026.

The programme-specific contribution here is not the general moment machinery. It is the exact application of that machinery to the parameter-rescaling nonclosure of the centered contraction, together with an explicit interval-certified primal-dual witness.

## 13. Next rigorous question

The next step should not add another arbitrary observable. It should study how the identification width behaves as information is added.

For example:

\[
\Delta_T(\Lambda,[L,U])
=
\sup Q_T(\lambda)-\inf Q_T(\lambda)
\]

under a supplied finite grid and finite horizon.

The immediate tasks are:

1. prove monotonicity of the sharp interval under grid refinement;
2. derive convergence as observed parameters accumulate at the required orbit points;
3. obtain explicit error rates from analyticity, support width, or derivative bounds;
4. test optimal parameter placement for a fixed observation budget;
5. separate worst-case identification width from statistical estimation error.

That would turn the present one-step certificate into a general theory of controlled finite-information prediction.
