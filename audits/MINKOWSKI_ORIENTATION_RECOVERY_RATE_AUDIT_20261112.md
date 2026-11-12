# Audit: leading Minkowski orientation-recovery error law for d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** adversarial dependency and rate audit  
**Target theorem:** \(1-p_d^{\mathrm{UPO}}(n)\sim K_d^{\mathrm{twin}}n^{-4/d}\) for fixed integer \(d\ge4\)

## 1. Purpose

This audit was written after assembling the leading orientation-recovery error law.

The goal is to check that no failure class omitted from the proof can survive at the same order as the comparable true-twin event.

The audit also records two corrections made during review:

1. the overlapping-true-twin second-moment argument was simplified to use the global pair tail plus the uniform comparable-ball bound;
2. the near-whole tip-clearance theorem was restricted to the event of a unique edge-containing component, which is exactly the scope used in the final assembly.

## 2. Leading candidate

The true-twin occurrence theorem gives

\[
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

The factorial second moment satisfies

\[
\mathbb E[T_n(T_n-1)]
=
o(n^{-4/d}),
\]

so the first moment is not inflated by clustering of twin pairs.

For overlapping twin pairs, the reviewed proof now uses

\[
F_d(t)=O(t^{\beta_d})
\]

and

\[
\sup_x\mu(B_t(x))=O(t^2)
\]

to obtain

\[
H_{\mathrm{overlap}}(t)
=
O(t^{\beta_d+2}),
\]

hence

\[
O(n^{1-\beta_d})
=
O(n^{-1-4/d})
\]

for \(d\ge4\).

No special \(d=4\) local bound is required.

## 3. Lower-bound logic

An adjacent true-twin pair is a size-two non-stable module whenever its edge-containing component contains at least one additional vertex.

If the pair forms an isolated \(K_2\) while another edge-containing component exists, orientation recovery already fails by independent component reversal.

The only recoverable graph containing an adjacent true-twin pair is therefore the degenerate graph whose only edge-containing component is that single \(K_2\).

Fixed positive-volume timelike-ordered open regions produce a connected component with at least three vertices with probability

\[
1-e^{-\Theta(n)}.
\]

Hence

\[
1-p_d^{\mathrm{UPO}}(n)
\ge
\Pr(T_n>0)-e^{-\Theta(n)}.
\]

This yields the required lower asymptotic.

## 4. Failure-class partition for the upper bound

Work on the event

\[
T_n=0.
\]

Any remaining orientation-recovery failure belongs to one of the following categories.

### A. Residual local escalation failure

A low-disagreement edge has sampled splitters but none forces a constant-factor increase in disagreement.

Its probability is bounded by

\[
O(n^{1-\beta_d}).
\]

For \(d\ge4\),

\[
O(n^{-1-4/d}).
\]

### B. Multiple edge-containing components

Outside the residual escalation event, every edge in every component reaches a positive-disagreement core edge.

Uniform splitter concentration then forces every edge-containing component to have linear size.

Two such components therefore produce a balanced graph module.

The balanced-module sampling theorem gives a superpolynomial bound.

Thus

\[
\Pr(
\text{multiple nontrivial components},\,
T_n=0
)
=
O(n^{-1-4/d})
+
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### C. Unique nontrivial component but internal non-UPO

The classical connected-UPO criterion gives a proper non-stable module.

Outside residual escalation, an internal edge reaches a core edge while remaining inside the module.

Uniform splitter concentration therefore forces the module to have linear size.

The remaining possibilities are balanced-linear or near-whole.

### D. Balanced-linear internal module

A deterministic diagonal sequence

\[
\varepsilon_n\downarrow0
\]

is chosen slowly enough that graphon cut-distance sampling still separates the causal graphon from every graphon containing a homogeneous set of mass in

\[
[\varepsilon_n,1-\varepsilon_n].
\]

The probability is at most

\[
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### E. Near-whole internal module

This case is used only after multiple edge-containing components have been excluded.

The unique edge-containing component assumption is essential.

The tip-clearance theorem then gives

\[
O(n^{1-d})
+
e^{-\Theta(n)}.
\]

## 5. Rate comparison

For \(d\ge4\), the leading scale is

\[
n^{-4/d}.
\]

### Residual escalation

\[
\frac{
n^{-1-4/d}
}{
n^{-4/d}
}
=
n^{-1}
\to0.
\]

### Non-twin component ambiguity

Same polynomial residual plus a superpolynomial term.

### Balanced modules

\[
\exp\!\left(
-\frac{n}{2\log n}
\right)
=
o(n^{-m})
\]

for every fixed \(m>0\).

### Near-whole modules

\[
\frac{
n^{1-d}
}{
n^{-4/d}
}
=
n^{-(d-1-4/d)}.
\]

For

\[
d\ge4,
\]

\[
d-1-\frac4d>0.
\]

Thus

\[
n^{1-d}
=
o(n^{-4/d}).
\]

No reviewed non-twin class remains at the leading scale.

## 6. Scope correction for the tip-clearance theorem

The middle-band argument uses the fact that a sampled middle-degree nonneighbor \(z\) of the complete external vertex \(u\) must either:

1. belong to the same unique edge-containing component and hence have one of the two module external types; or
2. be isolated.

This is false if another edge-containing component is allowed.

The theorem file has therefore been corrected to work explicitly on the unique-edge-containing-component event.

The final error-law proof applies it only after the component-ambiguity event has already been removed.

No circularity is introduced.

## 7. Middle-band geometry check

For a past-tip point

\[
x=(-1+s,s\rho e_1),
\]

the explicit middle band uses

\[
\tau\in[1/3,1/2],
\]

\[
h\in[s/4,s/3],
\]

and

\[
e_1\cdot\omega\le0.
\]

The spacelike margin is

\[
|\mathbf z-\mathbf x|^2-(t_z-t_x)^2
=
\Theta(s)
\]

uniformly over

\[
0\le\rho\le1.
\]

The band volume is therefore

\[
\Theta(s).
\]

The tip co-degree satisfies

\[
1-Q_d(x)
=
\frac d2s+O(s^2)
\]

uniformly in \(\rho\), so the band captures a fixed fraction of the co-degree.

The graphon degree of band points approaches

\[
(1-\tau)^{d/2},
\]

which is uniformly bounded away from zero and one on the fixed \(\tau\)-interval.

The repository script

tools/verify_tip_middle_band.py

provides a finite-grid regression of these statements.

## 8. Exact leading constant

For \(d\ge4\),

\[
F_d(\varepsilon)
\sim
C_d^{\mathrm{edge}}
\varepsilon^{2+4/d}.
\]

The Laplace-Stieltjes transfer gives

\[
K_d^{\mathrm{twin}}
=
\frac12
C_d^{\mathrm{edge}}
\Gamma\!\left(
3+\frac4d
\right).
\]

The independent quadrature script

tools/minkowski_alld_true_twin_constants.py

checks the closed integral formula.

For \(d=4\),

\[
C_4^{\mathrm{edge}}
=
3\pi,
\]

and

\[
K_4^{\mathrm{twin}}
=
9\pi.
\]

This reproduces the independently derived \(d=4\) theorem.

## 9. Dependency structure

The quantitative theorem depends on:

1. exact Minkowski interval-volume geometry;
2. all-dimensional small-edge tail;
3. uniform comparable-ball \(O(t^2)\) theorem;
4. true-twin first and second moments;
5. constant-factor non-twin edge escalation;
6. causal-graphon primeness;
7. graphon cut-distance sampling;
8. tip middle-band geometry.

None of these statements uses the final error law as an assumption.

The dependency graph remains acyclic.

## 10. Literature boundary

Classical inputs include:

- UPO and transitive-orientation forcing;
- graph modules;
- weakly homogeneous graphon sets;
- cut-distance sampling;
- Chernoff and Laplace-Stieltjes estimates.

The project-specific inputs are the Lorentzian disagreement tails, the uniform comparable-ball geometry, and the tip middle-band construction.

The targeted review has not located an existing theorem with the asymptotic law

\[
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d n^{-4/d}
\]

for arrow-erased Minkowski sprinklings.

This is limited negative evidence only.

## 11. Audit verdict

No surviving failure class was found at order

\[
n^{-4/d}
\]

other than comparable true twins.

The theorem

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}
}
\]

for fixed

\[
d\ge4
\]

survives the present internal audit.

The principal items requiring independent expert review before publication are:

1. the all-dimensional small-disagreement asymptotic and constant;
2. the uniform comparable-ball estimate;
3. the graphon-prime cut-distance separation argument;
4. the middle-band tip-clearance lemma.

No claim of external peer verification is made.
