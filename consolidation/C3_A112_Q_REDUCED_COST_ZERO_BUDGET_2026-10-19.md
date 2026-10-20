# C3 / A112 — six-function Q reduced-cost zero budget

**Date:** 2026-10-19  
**Scope:** an analytic **conditional** reduction of all nonbasic Q
reduced-cost signs to five integer checkpoints, for the frozen
six-function exponential family. This does **not** independently prove
that the five checkpoints are positive on the full A112 source window.

## 1. Why these six functions appear

For a fixed gamma-plus equality basis, the Q-column of the full
primal/dual LP has the form

```text
a_Q(x) = (0,1,0,x,tau^x,-s^x,+beta^x,-gamma^x).
```

Thus its reduced cost, `r_Q(x) = a_Q(x) · y`, is in the real span

```text
1, x, gamma^x, beta^x, s^x, tau^x.                 (1)
```

Here `gamma=1/16 < beta=1/8 < s < tau=1/2 < 1`
on the frozen source interval. With
`lambda_1=log(gamma) < lambda_2=log(beta)
< lambda_3=log(s) < lambda_4=log(tau)<0`,
the functions in (1) are

```text
1, x, exp(lambda_1*x), ..., exp(lambda_4*x).
```

Their successive Wronskians are nonzero, and in this function order
they are positive: for the first two, `W_1=W_2=1`, while for
`k=3,...,6`,

```text
W_k(x) =
  exp((lambda_1+...+lambda_(k-2))*x)
  * PRODUCT_i lambda_i^2
  * PRODUCT_(i<j) (lambda_j-lambda_i) > 0,         (2)
```

where the products range over `1<=i<j<=k-2`. This follows by
expanding the first two columns of the derivative matrix and
factoring the ordinary Vandermonde in the remaining exponential
rates.

Consequently (1) is a classical six-function extended complete
Chebyshev system. Any **nonzero** element has at most **five** real
zeros **counting multiplicities** on the line.

This is an elementary specialization of a classical theorem, not
a newly discovered zero-count bound.

## 2. The precise Q checkpoint lemma

Let `h>=4` and `M>=h+3`. Suppose a nonzero real-analytic
function `r(x)` belongs to the span (1), with

```text
r(1)=r(h)=r(h+1)=0,
r(0)>0, r(2)>0, r(h-1)>0, r(h+2)>0, r(M)>0.
```

Then

```text
r(k)>0  for every integer k in {0,...,M}\{1,h,h+1}.  (3)
```

### Proof by exhausting the zero budget

Because `r(0)>0`, `r(1)=0`, `r(2)>0`, the interval `(0,2)`
contains **at least two zeros counted with multiplicity**:

- if `r'(1)=0`, the zero at 1 has multiplicity at least two;
- if `r'(1) != 0`, the zero at 1 changes sign, so continuity
  together with the positive values at 0 and 2 forces another zero
  strictly between one of those endpoints and 1.

Together with the zeros at `h` and `h+1`, this consumes at least
**four of the five** allowed zeros, counting multiplicity.

If some `x0 in (2,h-1)` had `r(x0)<=0`, the strictly positive
endpoints at 2 and `h-1` would force at least two further zeros
counting multiplicity: two crossings if `r(x0)<0`, or a zero of
multiplicity at least two if `r(x0)=0` and the function does not
change sign; when it does change sign, an additional crossing
must restore positivity before the right endpoint.

That produces at least six zeros, contradicting (2).
Hence `r(x)>0` throughout `[2,h-1]`.

Exactly the same argument, using checkpoints `h+2` and `M`,
proves `r(x)>0` on `[h+2,M]`.

The remaining integer points are 0 and the three stipulated basic
zeros. This proves (3).

The proof makes no assumption about the sign of `r(x)` in the real
gaps `(h-1,h)` or `(h+1,h+2)`, which contain no nonbasic
integer atom. Claiming positivity for all real `x` would be
a stronger and generally unsupported assertion.

## 3. Exact scope in the A112 chain

The historical A112-C claim that five Q checkpoints protect all
unused integer Q atoms can be reduced to this classical zero-budget
argument **provided**:

1. the residual Q column really has the six-function representation
   (1), with the correct active-band signs;
2. the three Q basic reduced costs are exactly zero;
3. all five checkpoint costs are strictly positive;
4. the source satisfies the distinct-node order
   `gamma<beta<s<tau<1`;
5. the integer Q atom domain is exactly `0,...,M`.

Conditions (1), (2), (4), (5) are structural consequences of the
specified frozen LP, independent of compressed-maximality.
**Condition (3) remains the quantitative A112-C job.**
In particular, this reasoning does not establish
`r_Q(2)>0 => r_Q(0),r_Q(h-1),r_Q(h+2),r_Q(M)>0` uniformly;
that implication requires separate determinant/threshold margins.

This proof also does **not** establish the P-type collapse to the
single `r_P(1)` gate. The P function has its own support zeros,
and the Q argument must not be copied there without checking its
zero-budget and endpoint orientations.

## 4. Assurance and classical provenance

Analytic reduction: the conditional Q checkpoint implication (3)
is derived above using the Wronskian identity and multiplicity-aware
zero counts.

Independent finite check **completed** in
[CI run 39341636770](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39341636770):
the direct `Fraction` dual solve reconstructed three strict gamma-plus
witnesses, at `(M,s,j)=(522,131/1000,91)`,
`(561,53/400,98)`, and `(561,13277/100000,99)`.
All have positive basic masses and active multipliers, exact zero
Q basic costs, five positive Q checkpoints and **strictly positive
costs for every other integer Q atom**. This checked both sides
of the historical A114-B1 pivot selection.

The analytic zero-budget implication is proved above independently of
these samples, but its hypotheses must still be established uniformly
over the frozen source window. A Lean formalization of the real-zero
argument has not been completed. Neither the finite controls nor the
conditional lemma proves the all-tail five-checkpoint inequalities.

Classical references:

- Karlin and Studden (1966), *Tchebycheff Systems: With Applications
  in Analysis and Statistics*.
- Novaes and Torregrosa (2017), *On extended Chebyshev systems with
  positive accuracy*, DOI:
  https://doi.org/10.1016/j.jmaa.2016.10.076.

The conditional deduction is mathematical but the underlying
ECT zero-count principle is pre-existing literature.
