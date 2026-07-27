# Scale-Normalized Noise and the Boundary-Pair Law

**Programme:** Modal Field Research Programme  
**Provisional audit:** A64  
**Author line:** Felipe Gianini Romero  
**Status:** exact scale-normalization theorem plus exhaustive boundary-pair stress atlas; no continuous-anchor theorem

## Technical abstract

A63 showed that the first two catalogue anchors repeatedly appeared at

\[
\mu+1
\quad\text{and}\quad
\mu+2,
\]

but its fixed absolute error

\[
\varepsilon=10^{-4}
\]

did not represent the same relative information quality when the target
exponent, support, or mean changed.

A64 first removes this scale ambiguity.

Let

\[
L_\mu(P)
=
\sum_{x=0}^{M}p_x2^{-\mu x},
\]

with

\[
\sum_xp_x=1,
\qquad
\sum_xxp_x=m.
\]

Set

\[
a=\lfloor m\rfloor,
\qquad
\theta=m-a.
\]

The sharp lower bound is

\[
\boxed{
\ell_\mu(M,m)
=
(1-\theta)2^{-\mu a}
+
\theta2^{-\mu(a+1)}.
}
\]

When \(m\) is an integer, this reduces to

\[
\ell_\mu(M,m)=2^{-\mu m}.
\]

The bound is attained by the distribution concentrated on the two adjacent
states

\[
a
\quad\text{and}\quad
a+1
\]

with weights \(1-\theta\) and \(\theta\).

A dimensionless error contract is therefore

\[
\boxed{
\varepsilon_{\rm abs}
=
\delta\,\ell_\mu(M,m).
}
\]

If the target itself were measured with this tolerance, then

\[
|L_\mu(P)-L_\mu(Q)|
\le
2\delta\ell_\mu
\]

implies

\[
\boxed{
\frac{L_\mu(P)}{L_\mu(Q)}
\le
1+2\delta,
}
\]

after orienting the ratio so that the numerator is larger. Consequently,

\[
\boxed{
\mathcal R_{\rm direct}^{Q}
\le
\frac12\log_2(1+2\delta).
}
\]

This bound no longer depends on the raw magnitude of the target transform.

The normalized contract was then tested over:

- supports
  \[
  \{0,\ldots,M\},
  \qquad
  M=5,6,7,8,9;
  \]
- mean fractions
  \[
  \frac14,\frac13,\frac25,\frac12;
  \]
- target exponents
  \[
  \mu=1,2,3;
  \]
- relative error levels
  \[
  \delta
  =
  0,\frac1{7500},\frac1{1875},\frac1{750}.
  \]

This gives

\[
\boxed{240\text{ contracts}.}
\]

For every contract, all

\[
\binom93=84
\]

three-anchor designs from

\[
\{\mu+1,\ldots,\mu+9\}
\]

were solved. The atlas contains

\[
\boxed{20\,160\text{ complete design optimizations}.}
\]

Near-optimal candidates were independently recomputed with a second HiGHS
algorithm. The largest cross-algorithm ratio discrepancy was

\[
\boxed{
4.05\times10^{-13}.
}
\]

The results are:

\[
\boxed{
\text{every optimal design uses }\mu+1
\quad(240/240),
}
\]

and

\[
\boxed{
\text{every contract admits an optimal design containing }
\{\mu+1,\mu+2\}
\quad(240/240).
}
\]

However, the stronger statement

> every optimizer must contain \(\mu+2\)

is false. It held in

\[
235/240
\]

contracts, while five contracts admitted numerically tied optimizers that did
not contain the full boundary pair.

More decisively, one non-uniqueness case was certified exactly:

\[
M=5,
\qquad
m=\frac54,
\qquad
\mu=3,
\qquad
\delta=\frac1{1875}.
\]

Here

\[
\varepsilon_{\rm abs}
=
\frac1{19200}.
\]

The boundary-pair design

\[
\{4,5,7\}
\]

and the non-boundary-pair design

\[
\{4,7,12\}
\]

have exactly the same minimax ratio:

\[
\boxed{
\frac{
1813793639768317
}{
1800783220223842
}.
}
\]

Both exact primal and dual programmes return this same rational value.

Therefore the strongest statement presently supported is:

\[
\boxed{
\text{there exists a minimax-optimal design containing }
\{\mu+1,\mu+2\}.
}
\]

The available evidence does not support uniqueness of that pair.

---

## 1. Sharp target-scale theorem

The sequence

\[
f_\mu(x)=2^{-\mu x}
\]

is strictly convex in \(x\).

The affine line through the adjacent points

\[
(a,f_\mu(a))
\quad\text{and}\quad
(a+1,f_\mu(a+1))
\]

lies below the discrete convex sequence at every integer support point.

Thus there exist constants \(c_0,c_1\) such that

\[
f_\mu(x)\ge c_0+c_1x
\]

for all

\[
x=0,\ldots,M,
\]

with equality at \(a\) and \(a+1\).

Taking expectations gives

\[
L_\mu(P)
\ge
c_0+c_1m
=
\ell_\mu(M,m).
\]

The adjacent two-point distribution attains equality, proving sharpness.

A64 generated exact rational affine-minorant certificates for every support,
mean, and target combination in the atlas.

---

## 2. Why absolute error was misleading

Suppose two targets have very different guaranteed scales:

\[
\ell_{\mu_1}
\gg
\ell_{\mu_2}.
\]

Applying the same absolute error \(\varepsilon\) to both means that the second
target receives much larger relative uncertainty:

\[
\frac{\varepsilon}{\ell_{\mu_2}}
\gg
\frac{\varepsilon}{\ell_{\mu_1}}.
\]

That was the reason target exponent \(2\) appeared much more strongly driven
toward the far catalogue endpoint in the A63 fixed-error atlas.

The normalized contract fixes

\[
\frac{\varepsilon_{\rm abs}}{\ell_\mu}
=
\delta.
\]

This does not make different target exponents mathematically identical, but
it ensures that they are compared at the same guaranteed relative target
scale.

---

## 3. Direct-target benchmark

If

\[
L_\mu(P)\ge L_\mu(Q),
\]

then

\[
L_\mu(P)
\le
L_\mu(Q)+2\delta\ell_\mu.
\]

Since

\[
L_\mu(Q)\ge\ell_\mu,
\]

we obtain

\[
\frac{L_\mu(P)}{L_\mu(Q)}
\le
1+
\frac{
2\delta\ell_\mu
}{
L_\mu(Q)
}
\le
1+2\delta.
\]

This is a universal scale-free benchmark. It is an upper bound and is not
claimed to be attained for every support and mean.

---

## 4. Stress-atlas domain

The declared atlas deliberately extends beyond A63:

| Axis | A64 values |
|---|---|
| Support maximum | \(5,6,7,8,9\) |
| Mean fraction | \(1/4,1/3,2/5,1/2\) |
| Target exponent | \(1,2,3\) |
| Relative error | \(0,1/7500,1/1875,1/750\) |
| Anchor budget | 3 |
| Candidate offsets | \(1,\ldots,9\) |

The means are restricted to the lower half of the support. This is a declared
compact test domain, not a theorem for every admissible mean.

All numerical programmes were internally rescaled by their exact sharp lower
bounds. This improved conditioning without changing the minimax ratio.

---

## 5. First-anchor result

Across all 240 contracts, every numerically optimal design used

\[
\boxed{
\lambda_1^\star=\mu+1.
}
\]

This includes non-unique contracts: even when several designs tied, every
tied optimizer retained the first boundary anchor.

This is stronger than merely observing that one winner happened to include
the boundary point.

The first-anchor law is now the most persistent design feature in the
programme.

It remains an atlas theorem, not yet a symbolic theorem over continuous
anchors.

---

## 6. Boundary-pair existence

For all 240 contracts, at least one minimax-optimal design contained

\[
\boxed{
\{\mu+1,\mu+2\}.
}
\]

Thus the boundary pair survived changes in:

- support size;
- mean;
- target scale;
- four relative-noise levels.

This supports the existence statement:

> a boundary-pair optimizer is available.

It does not support:

> the boundary pair is present in every optimizer.

---

## 7. Exact non-uniqueness counterexample

Consider

\[
M=5,
\qquad
m=\frac54,
\qquad
\mu=3.
\]

The sharp target lower bound is

\[
\ell_3
=
\frac{25}{256}.
\]

At

\[
\delta=\frac1{1875},
\]

the absolute tolerance becomes

\[
\varepsilon
=
\frac{25}{256\cdot1875}
=
\frac1{19200}.
\]

The designs

\[
D_1=\{4,5,7\}
\]

and

\[
D_2=\{4,7,12\}
\]

both have exact ratio

\[
\rho(D_1)
=
\rho(D_2)
=
\frac{
1813793639768317
}{
1800783220223842
}.
\]

The second design omits the anchor \(\mu+2=5\).

Therefore a theorem asserting that every optimum contains the complete
boundary pair would be false without additional assumptions.

Possible assumptions capable of restoring uniqueness include:

- strict measurement costs;
- a penalty for extreme exponents;
- generic nondegeneracy conditions;
- a continuous design domain with a specified tie-breaking rule;
- restrictions on active supports.

None of these should be added merely to rescue a preferred statement.

---

## 8. Target-shift alignment

For each fixed support, mean, and relative error, A64 compared the optimal
third-anchor offset across target exponents \(1,2,3\).

The alignment rates were:

| Relative error \(\delta\) | Groups with identical third offset |
|---:|---:|
| \(0\) | \(20/20=100\%\) |
| \(1/7500\) | \(9/20=45\%\) |
| \(1/1875\) | \(13/20=65\%\) |
| \(1/750\) | \(15/20=75\%\) |

Exact observations remain perfectly translation-aligned:

\[
\{\mu+1,\mu+2,\mu+3\}.
\]

Positive normalized noise does not preserve perfect translation covariance.
Different target powers still interact differently with the hidden support.

However, on the original A63 comparison grid, normalization improved the
target-\(1\)/target-\(2\) alignment from

\[
\frac28=25\%
\]

under fixed absolute error to

\[
\frac68=75\%.
\]

Thus normalization removes a major scale artifact but not all target
dependence.

---

## 9. What A64 proves and what it does not

### Exact results

1. The sharp lower bound \(\ell_\mu(M,m)\).
2. The dimensionless error construction
   \[
   \varepsilon=\delta\ell_\mu.
   \]
3. The direct-target bound
   \[
   \rho\le1+2\delta.
   \]
4. The exact rational non-uniqueness counterexample.

### Exhaustive atlas results

1. Every optimum uses the first boundary anchor in all 240 contracts.
2. Every contract admits a boundary-pair optimizer.
3. Most contracts have the pair in every numerical optimizer.
4. Seven contracts showed numerical non-uniqueness.
5. Five contracts admitted tied optimizers lacking the second boundary anchor.
6. Normalization improves target-scale comparability.

### Not established

1. A continuous-anchor boundary-pair theorem.
2. A proof for every finite support and every mean.
3. Uniqueness of the pair.
4. Translation invariance under positive noise.
5. A theorem for relative error attached separately to each observed
   transform.
6. A result for supports beyond the declared compact atlas.

---

## 10. Scientific conclusion

A64 narrows the plausible theorem rather than inflating it.

The data support:

\[
\boxed{
\text{the first admissible anchor is structurally privileged.}
}
\]

They also support:

\[
\boxed{
\text{a minimax-optimal design containing the first two boundary anchors
exists throughout the declared atlas.}
}
\]

They reject:

\[
\boxed{
\text{the boundary pair must occur uniquely in every optimal design.}
}
\]

This is progress. A correct existence theorem with explicit degeneracies is
stronger science than an elegant but false uniqueness law.

---

## 11. Next rigorous target

The next mathematical step should focus first on the stronger surviving
statement:

\[
\boxed{
\lambda_1^\star=\mu+\Delta.
}
\]

Unlike the complete pair, the first boundary anchor occurred in every tied
optimizer across the entire atlas.

A tractable proof programme is:

1. fix the other two anchors;
2. compare the minimax risk as the first anchor moves away from the exclusion
   boundary;
3. identify the active primal–dual phase;
4. prove monotonicity by total positivity or Bernstein signs;
5. then study whether an optimal completion always exists with the second
   anchor adjacent.

This separates the likely theorem from the part already known to be
degenerate.
