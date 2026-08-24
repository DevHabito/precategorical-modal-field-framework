# Structural Generalization Beyond the Six-State Example

**Programme:** Modal Field Research Programme  
**Provisional audit:** A63  
**Author line:** Felipe Gianini Romero  
**Status:** exact finite-support nonidentifiability theorem plus cross-contract design atlas; no physical universality claim

## Technical abstract

The previous sequence solved one carefully controlled six-state contract based
on the support

\[
\{0,1,2,3,4,5\}.
\]

A63 asks which conclusions survive when the support, mean, target transform,
and noise contract are changed.

The result has two different logical levels.

First, finite-grid nonidentifiability generalizes exactly.

Let

\[
X=\{x_1<\cdots<x_m\}
\]

be any finite support. Suppose the available information consists of:

- normalization;
- the mean;
- \(k\) distinct Laplace observations at exponents
  \(\lambda_1,\ldots,\lambda_k\).

Let the omitted target exponent

\[
\mu
\]

be distinct from all observed exponents.

If

\[
\boxed{
m\ge k+3,
}
\]

then there exist two distinct probability distributions with:

\[
\sum_i p_i=\sum_i q_i=1,
\]

\[
\sum_i x_ip_i=\sum_i x_iq_i,
\]

\[
L_p(\lambda_j)=L_q(\lambda_j)
\qquad
(j=1,\ldots,k),
\]

but

\[
\boxed{
L_p(\mu)\ne L_q(\mu).
}
\]

The proof uses the extended complete Chebyshev system

\[
\left\{
1,\;
x,\;
e^{-\lambda_1x},\ldots,e^{-\lambda_kx},\;
e^{-\mu x}
\right\}.
\]

Its evaluation matrix on distinct support points has full row rank. Therefore
the target row is not in the span of normalization, mean, and the observed
transform rows. A null direction exists that preserves every observed
quantity while changing the target.

This is not specific to:

- six states;
- equally spaced exponents;
- mean \(5/2\);
- target exponent \(1\);
- error \(10^{-4}\).

An exact collision remains feasible under every positive observation
tolerance, because its observed differences are already zero.

Second, the optimal-design pattern was audited over 32 changed contracts:

- support
  \[
  \{0,\ldots,M\},
  \qquad
  M\in\{5,6,7,8\};
  \]
- mean
  \[
  M/2
  \quad\text{or}\quad
  2M/5;
  \]
- target exponent
  \[
  \mu\in\{1,2\};
  \]
- error
  \[
  \varepsilon=0
  \quad\text{or}\quad
  10^{-4}.
  \]

For every target, the three-anchor catalogue was

\[
\{\mu+1,\ldots,\mu+9\}.
\]

Every one of the 84 designs per contract was exhaustively ranked using
independent primal and dual linear programmes. This produced

\[
\boxed{
5376
}
\]

numerical LP solutions. The maximum primal–dual ratio discrepancy was

\[
\boxed{
3.23\times10^{-11}.
}
\]

For every contract, the winner and runner-up were then solved and certified
with exact rational primal and dual programmes. Exact constructive collision
witnesses were also generated for every winning design.

The atlas found:

\[
\boxed{
\text{first anchor}=\mu+1
\quad\text{in }32/32\text{ contracts},
}
\]

\[
\boxed{
\text{second anchor}=\mu+2
\quad\text{in }32/32\text{ contracts},
}
\]

and, with exact data,

\[
\boxed{
\text{third anchor}=\mu+3
\quad\text{in }16/16\text{ exact contracts}.
}
\]

Under positive absolute noise, however, the third-anchor offsets were

\[
\boxed{
\{3,4,5,7,9\}.
}
\]

The catalogue endpoint was selected in only

\[
\boxed{
10/16
}
\]

noisy contracts.

Therefore the main structural conclusion is:

\[
\boxed{
\text{the boundary pair is robust, but the extreme third anchor is
contract-dependent.}
}
\]

The original compactified behavior survives for some contracts, but it is not
a universal law of the framework.

---

## 1. General finite-support theorem

Define the observation matrix

\[
A=
\begin{pmatrix}
1&\cdots&1\\
x_1&\cdots&x_m\\
e^{-\lambda_1x_1}&\cdots&e^{-\lambda_1x_m}\\
\vdots&&\vdots\\
e^{-\lambda_kx_1}&\cdots&e^{-\lambda_kx_m}
\end{pmatrix}.
\]

Define the omitted target row

\[
g=
\begin{pmatrix}
e^{-\mu x_1}&\cdots&e^{-\mu x_m}
\end{pmatrix}.
\]

The functions

\[
1,\;
x,\;
e^{-\lambda_1x},\ldots,e^{-\lambda_kx},\;
e^{-\mu x}
\]

form an extended complete Chebyshev system when the exponential parameters are
distinct.

Thus, on any \(k+3\) distinct support points,

\[
\operatorname{rank}
\begin{pmatrix}
A\\g
\end{pmatrix}
=
k+3.
\]

But

\[
\operatorname{rank}A=k+2.
\]

Consequently,

\[
g\notin\operatorname{rowspan}A.
\]

There exists

\[
h\in\ker A
\]

with

\[
gh\ne0.
\]

For any interior distribution \(p^{(0)}\), choose a sufficiently small
\(\theta>0\) and set

\[
p^{(+)}
=
p^{(0)}+\theta h,
\]

\[
p^{(-)}
=
p^{(0)}-\theta h.
\]

Then both remain valid probability distributions, satisfy the same mean and
the same observed transforms, but differ at the target.

### Positive-error corollary

Since

\[
A
\left(
p^{(+)}-p^{(-)}
\right)
=0,
\]

the same pair is feasible under any observation bands

\[
\left|
L_p(\lambda_j)-L_q(\lambda_j)
\right|
\le2\varepsilon_j
\]

with

\[
\varepsilon_j\ge0.
\]

Positive noise enlarges the feasible ambiguity; it cannot remove an exact
collision.

---

## 2. Exact determinant audit

The atlas used three observed transforms, so the decisive generalized
Vandermonde matrix has six rows:

\[
1,\quad
x,\quad
2^{-\lambda_1x},\quad
2^{-\lambda_2x},\quad
2^{-\lambda_3x},\quad
2^{-\mu x}.
\]

For both target exponents and every one of the 84 catalogued designs, the exact
determinant on support points

\[
0,1,2,3,4,5
\]

was nonzero.

The determinant audit covered

\[
\boxed{
168
}
\]

target–design combinations.

This verifies the rank condition used by the general theorem throughout the
catalogue.

---

## 3. Cross-contract design atlas

The audit changed four independent axes:

| Axis | Values |
|---|---|
| Support maximum | \(5,6,7,8\) |
| Mean | \(M/2,\;2M/5\) |
| Target exponent | \(1,2\) |
| Observation error | \(0,\;10^{-4}\) |

This gives

\[
4\times2\times2\times2=32
\]

contracts.

Each contract had

\[
\binom93=84
\]

candidate designs.

### Computational certification structure

All catalogue candidates were solved in two independent forms:

1. the direct Charnes–Cooper primal programme;
2. its numerical dual programme.

The top two rankings agreed in all contracts.

For each winner and runner-up:

- the primal optimum was recomputed exactly over the rationals;
- the dual optimum was recomputed exactly;
- primal and dual values agreed identically;
- the winner–runner gap was exactly positive.

The remaining designs were separated numerically from the exact runner-up and
the maximum primal–dual discrepancy was below \(3.3\times10^{-11}\).

---

## 4. Persistent structure

### First anchor

In all contracts,

\[
\boxed{
\lambda_1^\star=\mu+1.
}
\]

The first observation stayed at the closest permitted point to the target.

This persisted under changes to:

- support size;
- mean;
- target exponent;
- exact versus noisy observations.

### Second anchor

In all contracts,

\[
\boxed{
\lambda_2^\star=\mu+2.
}
\]

Thus the optimal catalogue design always retained a local two-anchor
resolution layer immediately beyond the exclusion boundary.

This is the strongest cross-contract regularity found by A63.

### Exact third anchor

When

\[
\varepsilon=0,
\]

all contracts selected

\[
\boxed{
\lambda_3^\star=\mu+3.
}
\]

Thus exact observations favored three consecutive anchors closest to the
omitted target:

\[
\{\mu+1,\mu+2,\mu+3\}.
\]

---

## 5. The noisy third anchor is not universal

With

\[
\varepsilon=10^{-4},
\]

the first two anchors remained fixed, but the third anchor varied.

### Target exponent \(\mu=1\)

| \(M\) | Mean | Winning design | Third offset |
|---:|---:|---:|---:|
| 5 | \(M/2\) | \((2,3,10)\) | 9 |
| 5 | \(2M/5\) | \((2,3,10)\) | 9 |
| 6 | \(M/2\) | \((2,3,6)\) | 5 |
| 6 | \(2M/5\) | \((2,3,8)\) | 7 |
| 7 | \(M/2\) | \((2,3,5)\) | 4 |
| 7 | \(2M/5\) | \((2,3,6)\) | 5 |
| 8 | \(M/2\) | \((2,3,4)\) | 3 |
| 8 | \(2M/5\) | \((2,3,5)\) | 4 |

For the central mean, the preferred third offset moved systematically:

\[
9,\;5,\;4,\;3
\]

as the support maximum increased from \(5\) to \(8\).

For the lower mean, it moved:

\[
9,\;7,\;5,\;4.
\]

Thus the extreme anchor that was optimal in the original six-state model
retracted inward as additional support states were introduced.

### Target exponent \(\mu=2\)

With the same absolute error \(10^{-4}\), every target-\(2\) noisy contract
selected the far catalogue endpoint:

\[
\boxed{
(3,4,11).
}
\]

This is not evidence of target-translation invariance. The target transform is
smaller at exponent \(2\), so the same absolute error represents a larger
relative uncertainty.

The result exposes an important scaling issue:

\[
\boxed{
\text{fixed absolute noise is not invariant under target-exponent shifts.}
}
\]

Future comparisons between target scales should include relative or
transform-normalized error contracts.

---

## 6. Constructive witness outside the original example

Consider the nine-state support

\[
\{0,1,\ldots,8\},
\]

central mean

\[
4,
\]

target exponent

\[
1,
\]

and the noisy winning design

\[
(2,3,4).
\]

An exact null direction is

\[
h=
(1,-30,281,-988,1248,-512,0,0,0).
\]

With the exact rational step

\[
\theta=\frac1{22464},
\]

the two constructed distributions:

- are nonnegative;
- are normalized;
- both have mean \(4\);
- agree exactly at exponents \(2,3,4\);
- disagree at target exponent \(1\).

Their constructive future-score separation is approximately

\[
0.00152022716002554.
\]

This is a concrete collision outside the original six-state contract.

The witness is not claimed to attain the minimax optimum. Its role is to
constructively demonstrate that the ambiguity persists.

---

## 7. What generalized and what did not

### Generalized as a theorem

1. Finite-grid nonidentifiability.
2. Existence of exact collision directions.
3. Persistence under positive error bands.
4. The requirement that identification needs enough independent information,
   not merely more optimization.

### Persisted across the 32-contract atlas

1. The first anchor lies at the exclusion boundary.
2. The second anchor is the next adjacent exponent.
3. Exact data favor the three nearest catalogue anchors.

### Did not generalize universally

1. The far or compactified third anchor.
2. The numerical value
   \[
   \beta^\star\approx2.728401.
   \]
3. The original noise phase diagram.
4. The specific minimax-risk floor.
5. The claim that increasing the third exponent is always optimal.

The correct generalized statement is not:

> the third anchor belongs at infinity.

It is:

> positive noise creates a local-versus-global information tradeoff whose
> optimum depends on the microscopic contract.

---

## 8. Scientific interpretation

The research now has a hierarchy of claims.

### Structural level

A finite collection of Laplace-type measurements generally cannot identify an
omitted transform when the hidden distribution has enough degrees of freedom.

This is independent of the original numerical example.

### Design level

The two observations nearest the exclusion boundary repeatedly carry the
local resolution burden.

This pattern survived every declared variation in the atlas.

### Contract-dependent level

The third observation controls more global or tail-sensitive information.
Its optimal position depends on:

- support length;
- mean location;
- target scale;
- absolute noise.

That dependence is not a weakness. It identifies which part of the design
must be calibrated to the application rather than declared universal.

---

## 9. Logical status

### Established

1. An exact general finite-support nonidentifiability theorem.
2. Exact determinant verification for all catalogue designs.
3. Exact collision witnesses for every winning contract.
4. A 32-contract, 84-design-per-contract exhaustive atlas.
5. Independent primal–dual numerical ranking of all designs.
6. Exact rational primal–dual certificates for every winner and runner-up.
7. Complete persistence of the first two anchor positions.
8. Complete persistence of the nearest third anchor under exact data.
9. Demonstrated non-universality of the noisy third anchor.

### Not established

1. The atlas is not a continuous-anchor global optimization.
2. Only three-observation budgets were tested.
3. Supports remain finite and equally spaced.
4. Only two means and two target exponents were audited.
5. Positive noise was fixed in absolute units.
6. Continuous microscopic support was not tested.
7. The persistent boundary-pair pattern is an exact atlas result, not yet a
   theorem for arbitrary contracts.

---

## 10. Next rigorous target

A63 changes the research direction.

It is no longer sensible to optimize the original six-state contract more
deeply. The next step should test the strongest surviving design regularity:

\[
\boxed{
\lambda_1^\star=\mu+\Delta,
\qquad
\lambda_2^\star=\mu+\Delta+1.
}
\]

The next theorem should ask whether the boundary pair can be proved for a
family of support sizes and means, rather than merely observed in the atlas.

In parallel, the noise contract should be normalized relative to the target
transform, so that changing \(\mu\) does not silently change the effective
signal-to-noise ratio.
