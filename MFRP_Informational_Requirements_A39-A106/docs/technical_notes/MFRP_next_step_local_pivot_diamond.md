# Exact Local Pivot Diamond and Orientation Selection

**Programme:** Modal Field Research Programme  
**Provisional audit:** A72  
**Author line:** Felipe Gianini Romero  
**Status:** exact global theorems for \(M=10,11,12\) plus an exact local pivot-selection theorem; not an arbitrary-\(M\) oriented-matroid theorem

## Technical abstract

A71 showed that the weakest inherited contact signature changes Cramer
orientation at \(M=10\), becomes dual-infeasible, and is replaced by a new
optimal phase sequence.

A72 asks a more local and more precise question:

> Once the optimizer reaches the common late-stage contact pattern, which
> admissible pivot route is selected, and why?

The audited family is

\[
\operatorname{supp}P\subseteq\{0,\ldots,M\},
\qquad
M\in\{10,11,12\},
\]

with

\[
\mathbb E[X]=\frac M2,
\qquad
\mu=1,
\qquad
\delta=\frac1{1875},
\]

and the fixed completion

\[
D_\alpha=\{\alpha,3,4\},
\qquad
2\le\alpha<3.
\]

The exact integer catalogues for \(M=11\) and \(M=12\) contain

\[
84+84=168
\]

rationally solved designs. In both cases the unique winner is

\[
\boxed{\{2,3,4\}.}
\]

The continuous problems for \(M=11\) and \(M=12\) each decompose into six
exact algebraic phases and five simple finite transitions. Together with the
A71 \(M=10\) theorem, all three supports satisfy

\[
\boxed{
\frac{d\rho_M}{d\alpha}>0
\quad\text{for every }2\le\alpha<3.
}
\]

Thus

\[
\boxed{
\alpha^\star=2
}
\]

is the unique global first-anchor optimum for all three declared supports.

More importantly, the three exact phase sequences share a common normalized
grammar. Let

\[
h=\left\lfloor\frac M2\right\rfloor.
\]

The first four signatures are:

\[
\begin{aligned}
P_1&=\{1,4,M\},
&
Q_1&=\{0,2,h,h+1\},\\
P_2&=\{0,1,4,M\},
&
Q_2&=\{2,h,h+1\},\\
P_3&=\{0,4,M\},
&
Q_3&=\{1,2,h,h+1\},\\
P_S&=\{0,3,4,M\},
&
Q_S&=\{1,h,h+1\},
\end{aligned}
\]

with active bands

\[
\alpha+,\qquad\beta-,\qquad\gamma+.
\]

All three terminate at

\[
P_T=\{0,3,M\},
\qquad
Q_T=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,\qquad\gamma-.
\]

Between the common start \(S\) and terminal state \(T\), two different exact
intermediate signatures occur.

### Route A

\[
P_A=\{0,3,M\},
\qquad
Q_A=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,\qquad\beta-.
\]

This route is selected by

\[
M=10,11.
\]

### Route B

\[
P_B=\{0,3,4,M\},
\qquad
Q_B=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,\qquad\beta-,\qquad\gamma-.
\]

This route is selected by

\[
M=12.
\]

The unused cross routes are not rejected by an informal preference or by
numerical tie-breaking.

At \(M=11\), the Route-B candidate satisfies

\[
\boxed{
\lambda_{\gamma^-}<0
}
\]

throughout the entire exact phase-5 interval. It is therefore dual-infeasible.

At \(M=12\), the Route-A candidate has

\[
\boxed{
\bar c_{P_4}<0
}
\]

throughout the entire exact phase-5 interval, where \(\bar c_{P_4}\) is the
reduced cost of the omitted primal contact \(x=4\). It is therefore
dual-infeasible.

Hence the terminal route is selected by exact primal-dual orientation:

\[
\boxed{
M=10,11:\ S\rightarrow A\rightarrow T,
}
\]

\[
\boxed{
M=12:\ S\rightarrow B\rightarrow T.
}
\]

This is an exact local pivot-diamond theorem. It does not yet prove that the
complete active-basis graph is an oriented matroid or that the same four-node
diamond governs arbitrary support size.

---

## 1. Exact catalogue results

| \(M\) | Winner | Winner ratio | Runner-up | Runner ratio |
|---:|---:|---:|---:|---:|
| 11 | (2, 3, 4) | 1.412980408836 | (2, 3, 5) | 1.440359549903 |
| 12 | (2, 3, 4) | 1.535192181891 | (2, 3, 5) | 1.585827068512 |

The winner–runner gaps are strictly positive exact rational numbers.

For \(M=11\),

\[
\rho_{11}(2,3,4)
=
\frac{
5501158849148875501
}{
3893301573571935664
}.
\]

For \(M=12\),

\[
\rho_{12}(2,3,4)
=
\frac{
819447706985393983789219
}{
533775325755046576691200
}.
\]

The best three designs at each support have independently matching exact
primal and dual values.

---

## 2. Global continuous results

The exact future risks are:

| \(M\) | \(Q_M(2)\) | \(Q_M(3^-)\) |
|---:|---:|---:|
| 10 | 0.173468349929308 | 0.613963668340002 |
| 11 | 0.249370731324749 | 0.751487377256716 |
| 12 | 0.309209634802901 | 0.921475642412741 |

Every support has six exact phases and five simple finite transitions.

| \(M\) | \(\alpha_1\) | \(\alpha_2\) | \(\alpha_3\) | \(\alpha_4\) | \(\alpha_5\) |
|---:|---:|---:|---:|---:|---:|
| 10 | 2.562390719601230 | 2.668041905502717 | 2.768365791805390 | 2.943788401780076 | 2.947546794911715 |
| 11 | 2.682118597665336 | 2.753206938217223 | 2.825650480313282 | 2.956846395587855 | 2.959134409400444 |
| 12 | 2.792307658265627 | 2.836106042420663 | 2.884211786882878 | 2.960539395602535 | 2.971772883997700 |

The positive first-channel band is active in all

\[
\boxed{18}
\]

phases, and the exact derivative is positive in all 18 phases.

---

## 3. Complete phase signatures

| \(M\) | Phase | Active \(P\)-support | Active \(Q\)-support | Active bands |
|---:|---:|---:|---:|---|
| 10 | 1 | [1, 4, 10] | [0, 2, 5, 6] | alpha+, beta-, gamma+ |
| 10 | 2 | [0, 1, 4, 10] | [2, 5, 6] | alpha+, beta-, gamma+ |
| 10 | 3 | [0, 4, 10] | [1, 2, 5, 6] | alpha+, beta-, gamma+ |
| 10 | 4 | [0, 3, 4, 10] | [1, 5, 6] | alpha+, beta-, gamma+ |
| 10 | 5 | [0, 3, 10] | [1, 5, 6] | alpha+, beta- |
| 10 | 6 | [0, 3, 10] | [1, 5, 6] | alpha+, gamma- |
| 11 | 1 | [1, 4, 11] | [0, 2, 5, 6] | alpha+, beta-, gamma+ |
| 11 | 2 | [0, 1, 4, 11] | [2, 5, 6] | alpha+, beta-, gamma+ |
| 11 | 3 | [0, 4, 11] | [1, 2, 5, 6] | alpha+, beta-, gamma+ |
| 11 | 4 | [0, 3, 4, 11] | [1, 5, 6] | alpha+, beta-, gamma+ |
| 11 | 5 | [0, 3, 11] | [1, 5, 6] | alpha+, beta- |
| 11 | 6 | [0, 3, 11] | [1, 5, 6] | alpha+, gamma- |
| 12 | 1 | [1, 4, 12] | [0, 2, 6, 7] | alpha+, beta-, gamma+ |
| 12 | 2 | [0, 1, 4, 12] | [2, 6, 7] | alpha+, beta-, gamma+ |
| 12 | 3 | [0, 4, 12] | [1, 2, 6, 7] | alpha+, beta-, gamma+ |
| 12 | 4 | [0, 3, 4, 12] | [1, 6, 7] | alpha+, beta-, gamma+ |
| 12 | 5 | [0, 3, 4, 12] | [1, 6, 7] | alpha+, beta-, gamma- |
| 12 | 6 | [0, 3, 12] | [1, 6, 7] | alpha+, gamma- |

The first four rows at each support instantiate the same symbolic grammar.
Only the order of the two terminal pivots changes.

---

## 4. Local pivot diamond

The common start and terminal signatures are:

\[
S:
\begin{cases}
P=\{0,3,4,M\},\\
Q=\{1,h,h+1\},\\
\text{bands}=\{\alpha+,\beta-,\gamma+\},
\end{cases}
\]

and

\[
T:
\begin{cases}
P=\{0,3,M\},\\
Q=\{1,h,h+1\},\\
\text{bands}=\{\alpha+,\gamma-\}.
\end{cases}
\]

The two intermediate signatures are:

\[
A:
\begin{cases}
P=\{0,3,M\},\\
Q=\{1,h,h+1\},\\
\text{bands}=\{\alpha+,\beta-\},
\end{cases}
\]

and

\[
B:
\begin{cases}
P=\{0,3,4,M\},\\
Q=\{1,h,h+1\},\\
\text{bands}=\{\alpha+,\beta-,\gamma-\}.
\end{cases}
\]

The observed paths are:

\[
S\longrightarrow A\longrightarrow T
\quad(M=10,11),
\]

and

\[
S\longrightarrow B\longrightarrow T
\quad(M=12).
\]

This is a pivot-order bifurcation, not a failure of the boundary law.

---

## 5. Exact exclusion of the unused \(M=11\) route

Consider the Route-B basis at \(M=11\):

\[
P=\{0,3,4,11\},
\qquad
Q=\{1,5,6\},
\]

with active bands

\[
\alpha+,\qquad\beta-,\qquad\gamma-.
\]

On the exact interval occupied by the true phase 5, the candidate multiplier
for the negative \(\gamma\)-band has no numerator root, no denominator root,
and one exact rational sample with negative sign.

Therefore:

\[
\boxed{
\lambda_{\gamma^-}(s)<0
}
\]

throughout that interval.

Since active inequality multipliers must be nonnegative, Route B cannot be
the optimal intermediate at \(M=11\).

---

## 6. Exact exclusion of the unused \(M=12\) route

Consider the Route-A basis at \(M=12\):

\[
P=\{0,3,12\},
\qquad
Q=\{1,6,7\},
\]

with active bands

\[
\alpha+,\qquad\beta-.
\]

On the exact interval occupied by the true phase 5, the reduced cost of the
omitted \(P\)-state \(x=4\) has no numerator root, no denominator root, and
one exact rational sample with negative sign.

Therefore:

\[
\boxed{
\bar c_{P_4}(s)<0
}
\]

throughout that interval.

A negative reduced cost means that the candidate basis can be improved by
admitting the missing contact \(x=4\). Route A therefore cannot be the
optimal intermediate at \(M=12\).

---

## 7. What A72 proves

1. Exact global continuous theorems for \(M=11\) and \(M=12\).
2. Exact integer-catalogue winners \(\{2,3,4\}\) at both supports.
3. A common first-four-phase contact grammar for \(M=10,11,12\).
4. A common terminal signature for all three supports.
5. Two exact terminal pivot routes between the same normalized endpoints.
6. A pivot-order bifurcation at \(M=12\).
7. Exact dual exclusion of the unused \(M=11\) route.
8. Exact reduced-cost exclusion of the unused \(M=12\) route.
9. Positive first-channel activity and positive derivative in all 18 phases.

---

## 8. What A72 does not prove

A72 does not establish:

1. enumeration of every locally feasible basis;
2. a complete oriented-matroid representation;
3. an elimination axiom for arbitrary candidate signatures;
4. a pivot grammar for all \(M\);
5. joint continuous optimization of the second and third anchors;
6. a uniform lower bound on pivot-orientation margins.

The term “pivot diamond” refers to the exact four signatures audited here. It
is not being used as evidence that every neighboring basis in the complete LP
basis graph has been enumerated.

---

## 9. Next rigorous target

The next step should enlarge the local basis neighborhood without pretending
to enumerate the complete combinatorial basis space.

For the late-stage state

\[
S=\{P=\{0,3,4,M\},\ Q=\{1,h,h+1\}\},
\]

the next audit should generate every **single-pivot adjacent basis** obtained
by:

- exchanging one primal contact;
- exchanging one dual contact;
- activating or deactivating one completion band;
- flipping one active completion-band sign when the rank contract permits.

For \(M=11,12,13\), each candidate should be classified as:

1. primal infeasible;
2. dual-multiplier infeasible;
3. reduced-cost infeasible;
4. observation-slack infeasible;
5. locally optimal.

That would provide the first complete local orientation-selection table and
allow an honest test of an oriented-matroid elimination rule.
