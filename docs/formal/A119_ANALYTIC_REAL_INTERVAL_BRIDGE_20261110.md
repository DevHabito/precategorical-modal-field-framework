# A119: analytic real-number interpretation of the rational interval certificate

**Date:** 2026-11-10  
**Branch:** research/a115-a119-uniform-remainder-20261110  
**Status:** hand-auditable argument conditional on exact arithmetic inclusion outputs; **not yet kernel-proved over \(\mathbb R\)**.  
**Mathematical object:** A119's explicit rational critical expression for the reduced two-active-band C2(k) family. This is not an unrestricted F2/F3 optimization theorem.

## Question

The Lean evaluator currently proves positivity for **rational** arguments. Does the exact rational interval arithmetic used by the original 35-box certificate also cover **real** arguments, rather than merely a dense subset?

**Yes, at the level of an analytic interval-inclusion argument**, provided the evaluator's boxes actually have positive lower bounds and all divisor intervals exclude zero. No density-based limit or continuity argument is needed.

## Proposition (soundness of rational-endpoint inclusion for real evaluation)

Let \(I=[a,b]\) be a closed interval with rational endpoints \(a\le b\), viewed inside \(\mathbb R\). Use the following exact endpoint operations, all computed in \(\mathbb Q\):

\[
\begin{aligned}
I+J &= [a+c,b+d],\\
I-J &= [a-d,b-c],\\
I\cdot J &=
[\min(ac,ad,bc,bd),\,\max(ac,ad,bc,bd)],\\
J^{-1} &= [1/d,1/c] \qquad
\text{only when } 0<c\le d \text{ or } c\le d<0,\\
I/J &= I\cdot J^{-1}.
\end{aligned}
\]

Use point powers by repeated multiplication (the conservative inclusion rule); all exact rational constants are singleton intervals. On an interval program composed of finitely many such operations, return **failure** rather than a finite output whenever a requested reciprocal interval touches or crosses zero.

If the evaluator returns a finite rational output interval \(K=[L,U]\), then for **every real** choice of its input variables within their original rational-endpoint boxes, its real-valued expression is defined and belongs to \([L,U]\).

### Proof

Proceed by structural induction over the expression tree.

1. Literal and variable cases are immediate since \(\mathbb Q\hookrightarrow\mathbb R\) preserves order.
2. Addition, negation and subtraction follow from the ordinary order inequalities in \(\mathbb R\).
3. If \(x\in[a,b]\), \(y\in[c,d]\), the product \(xy\) is between the smallest and largest of the four corner products. One direct proof fixes \(y\): for \(y\ge0\), \(ay\le xy\le by\); for \(y<0\), the inequalities reverse. Each of \(ay\), \(by\) is itself bounded by the smaller and larger endpoint products with \(c,d\), according to the sign of the fixed multiplier. No rationality of \(x,y\) is used.
4. If \(0<c\le y\le d\), then \(1/d\le1/y\le1/c\). Exactly the same order holds when \(c\le y\le d<0\). The sign-separated denominator interval excludes zero for every real point, so division is defined and the product enclosure in step 3 applies.
5. Natural powers are repeated products; their enclosure follows inductively from step 3.
6. The induction hypothesis applies to each child expression. A successful parent interval contains the composition of the child's actual real values by steps 1–5.

Consequently any rational lower endpoint \(L>0\) output by this evaluator is a **uniform strict lower bound for the corresponding real-valued expression on that whole real input box**.

## Applying it to the 35-box Xi-hat arithmetic

The checked-in Python Fraction evaluator [a119_compact_35box_fraction_certificate_20261110.py](../../audits/a119_compact_35box_fraction_certificate_20261110.py) uses exactly these rational operations, with a fail-closed denominator check and the source interval \([129/1000,133/1000]\). The independent exact-arithmetic [CI run 42855045033](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42855045033) passed its 35-box certificate.

The output's smallest **reported interval lower endpoint** is

\[
L_{\min}=
\frac{436152226670319684540420616481093}
     {4002264870000313289466234723750000}>0.
\]

The complete finite manifest uses 14 even and 21 odd boxes, with closed subdivisions that cover the frozen enlarged critical rectangles. If these exact 35 inclusions are correctly implemented and evaluated, the proposition proves **real** positivity of the explicit rational function \(\widehat\Xi_{p,r}\) throughout the corresponding real rectangles as well. The positive rational lower endpoint \(L_{\min}\) is uniform across all boxes, so no limit argument can weaken strict positivity to merely nonnegativity.

This is a valid *mathematical interpretation* of an interval computation, not a new 35-box computation or an independent source-derivation of its rational function. The existing Lean interval soundness theorems and 14 currently verified boxes are stated over \(\mathbb Q\); extending their formal semantics to \(\mathbb R\) is a **separate, still-open Lean task**.

## Important boundaries

This analytic extension does **not** prove that \(\widehat\Xi\) equals the coefficient \(\Xi_p\) produced by the A115–A118 collision asymptotics under \(\Lambda_p=0\). The full source-to-coefficient chain, high-deficit analytic cutoff, and uniform \(O(M^{-3})\) remainder remain separate proof gates.

Likewise, positivity of a reduced critical expression is not a primal/dual optimality certificate for the full moment LP, and it does not imply that the corresponding reduced measures are feasible for F2 or F3.

Nothing about this argument establishes historical novelty; rational interval inclusion is a standard mathematical technique.

## Lean formalization target

Implement a real-valued semantics \(\operatorname{eval}_{\mathbb R}\) for the existing rational-constant expression tree, and prove

\[
\mathrm{intervalValue}(e,S,A)=\mathrm{some}([L,U])
\ \Longrightarrow\
L\le\operatorname{eval}_{\mathbb R}(e,s,\alpha)\le U
\]

for all real \(s,\alpha\) in the real interpretations of \(S,A\). Reuse Mathlib's order and field lemmas; never assume absence of zero in a denominator without the interval guard. Then connect the real semantics to a **separate** \(\widehat\Xi^\mathbb R\) definition and replay the finite certificates already being compiled for rational endpoints.

The math argument above supplies a clear proof outline but **must not be reported as already Lean-certified**. Maintain the distinction between the verified Python endpoint arithmetic, a general real ordered-field proof, and kernel verification of that proof.
