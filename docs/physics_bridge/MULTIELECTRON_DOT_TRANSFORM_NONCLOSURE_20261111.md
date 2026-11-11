# Bridge 1B — transform non-closure in a published multi-electron dot model

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic bridge theorem + exact finite witness  
**Physical source:** published multi-electron Markov model; no empirical validation claim  
**Novelty status:** not assessed; the moment-shift mechanism is mathematically elementary and must not be advertised as new physics

## 1. Why this bridge is different from C2

The repository's mathematical claim C2 studies non-closure under a centered contraction of quantitative marks.

The multi-electron dot studied by C. Salhani, K. Chida, T. Shimizu, T. Hayashi, and K. Nishiguchi evolves differently. Its measured state distribution follows a birth-death master equation.

I therefore do **not** identify the published dynamics with C2.

Instead, I ask a new and narrower bridge question:

> Does the actual published master equation close on one exponential score, or does its evolution require additional transform information?

This question is derived from the physical model itself.

## 2. Published master equation

Let \(N\in\mathbb Z\) be the excess electron number in the dot and let \(\rho_N(t)\) be its probability.

The published model is

$$
\dot\rho_N(t)
=
\Gamma^+(t)\rho_{N-1}(t)
-
[\Gamma^+(t)+\Gamma_N^-]\rho_N(t)
+
\Gamma_{N+1}^-\rho_{N+1}(t).
$$

The rates are

$$
\Gamma^+(t)
=
\Gamma_0 e^{-\beta eV(t)}
$$

and

$$
\Gamma_N^-
=
\Gamma_0 e^{\beta\mu_N},
\qquad
\mu_N=2E_{\rm C}\left(N-\frac12\right).
$$

Define

$$
c=2\beta E_{\rm C}>0.
$$

Then

$$
\Gamma_N^-
=
\Gamma_0 e^{-\beta E_{\rm C}}e^{cN}.
$$

The experiment reports \(E_{\rm C}=9.8\) meV and operates at room temperature with time-resolved single-electron counting. The present theorem uses only the stated master equation and rate law.

## 3. Exponential transform

For a parameter \(\lambda\), define

$$
G_\lambda(t)
=
\sum_N \rho_N(t)e^{-\lambda N},
$$

whenever the sum is finite.

The corresponding log-transform score is

$$
Q_\lambda(t)
=
-\frac1\lambda\log G_\lambda(t)
$$

for \(\lambda\neq0\).

This is the same mathematical family of exponential scores studied elsewhere in the repository, but the dynamics below are derived from the published electronic model rather than imported from C2.

## 4. Exact transform evolution identity

Apply the birth-death generator to

$$
f_\lambda(N)=e^{-\lambda N}.
$$

A birth event \(N\to N+1\) changes \(f_\lambda\) by

$$
f_\lambda(N+1)-f_\lambda(N)
=
e^{-\lambda N}(e^{-\lambda}-1).
$$

A death event \(N\to N-1\) changes it by

$$
f_\lambda(N-1)-f_\lambda(N)
=
e^{-\lambda N}(e^\lambda-1).
$$

Therefore

$$
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
(e^\lambda-1)
\sum_N \rho_N\Gamma_N^-e^{-\lambda N}.
$$

Using

$$
\Gamma_N^-
=
\Gamma_0e^{-\beta E_{\rm C}}e^{cN},
$$

the second sum becomes

$$
\Gamma_0e^{-\beta E_{\rm C}}
\sum_N\rho_Ne^{-(\lambda-c)N}.
$$

Hence

$$
\boxed{
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
\Gamma_0e^{-\beta E_{\rm C}}(e^\lambda-1)
G_{\lambda-c}.
}
$$

This identity is exact under the published master equation.

### Immediate consequence

The evolution of one transform value \(G_\lambda\) is generically coupled to a second transform value \(G_{\lambda-c}\).

Thus one fixed transform does not form an autonomous scalar state unless an additional relation closes the shifted transform.

## 5. Score evolution

For \(\lambda\neq0\),

$$
\dot Q_\lambda
=
-\frac1\lambda\frac{\dot G_\lambda}{G_\lambda}.
$$

Therefore

$$
\boxed{
\dot Q_\lambda
=
-\frac1\lambda
\left[
\Gamma^+(t)(e^{-\lambda}-1)
+
\Gamma_0e^{-\beta E_{\rm C}}(e^\lambda-1)
\frac{G_{\lambda-c}}{G_\lambda}
\right].
}
$$

One score \(Q_\lambda\) is not enough to evaluate this derivative unless the ratio \(G_{\lambda-c}/G_\lambda\) is known from other information.

## 6. Exact four-state non-closure witness

The preceding identity says that the shifted transform matters. I now show that normalization, mean electron number, and one transform value do not generally determine that shifted transform.

Let

$$
z=e^{-\lambda},
\qquad
y=e^{-(\lambda-c)}.
$$

Consider distributions supported on

$$
N\in\{0,1,2,3\}.
$$

Define the perturbation vector

$$
v=(-z,\;2z+1,\;-z-2,\;1).
$$

It satisfies

$$
\sum_{n=0}^3v_n=0,
$$

$$
\sum_{n=0}^3nv_n=0,
$$

and

$$
\sum_{n=0}^3v_nz^n=0.
$$

Therefore, starting from any strictly positive interior distribution \(p\), sufficiently small perturbations

$$
p^\pm=p\pm\varepsilon v
$$

have the same:

- total probability;
- mean electron number;
- transform \(G_\lambda\).

But at the shifted transform,

$$
\sum_{n=0}^3v_ny^n
=
(y-1)^2(y-z).
$$

Thus, whenever

$$
y\neq1
\quad\text{and}\quad
y\neq z,
$$

the two distributions have different \(G_{\lambda-c}\).

In physical parameters these exclusions are

$$
c\neq0
$$

and

$$
\lambda\neq c.
$$

The model has \(c=2\beta E_{\rm C}>0\), so the only exceptional transform parameter in this statement is \(\lambda=c\).

### Theorem

For the published multi-electron birth-death model, if

$$
c>0,\qquad \lambda\neq0,\qquad \lambda\neq c,
$$

there exist finite-support probability distributions with equal mean electron number and equal \(Q_\lambda\) but different instantaneous \(\dot Q_\lambda\) under the same instantaneous external drive.

The proof is constructive: use the four-state perturbation above and the exact transform-evolution identity.

## 7. Concrete rational witness

For an exact arithmetic audit, choose

$$
z=\frac12,
\qquad
y=\frac34.
$$

This corresponds algebraically to one transform point and one shifted transform point; it is used only as an exact finite witness, not as a fit to the experimental \(E_{\rm C}/k_{\rm B}T\).

Take

$$
p^+
=
\left(
\frac9{40},
\frac7{20},
\frac18,
\frac3{10}
\right),
$$

and

$$
p^-
=
\left(
\frac{11}{40},
\frac3{20},
\frac38,
\frac15
\right).
$$

Both have mean

$$
\frac32
$$

and both satisfy

$$
G_z=\frac{15}{32}.
$$

At the shifted point,

$$
G_y(p^+)=\frac{219}{320},
$$

while

$$
G_y(p^-)=\frac{437}{640}.
$$

Their exact difference is

$$
\frac1{640}.
$$

Therefore the physical transform derivative differs whenever the coefficient multiplying \(G_{\lambda-c}\) is nonzero.

## 8. What this says about the repository

This is the first bridge in which the repository's general concern about dynamic closure meets a published physical master equation without identifying that equation with the earlier C2 update.

The result is narrower and cleaner:

> A physically established birth-death model generates its own transform hierarchy. One exponential score at one parameter is not generically dynamically autonomous.

This does not prove C2 physically. It shows that a related non-closure issue arises independently in a real stochastic-thermodynamic model.

## 9. What it does not say

This result does not establish:

- a new law of stochastic thermodynamics;
- that the transform hierarchy is absent from existing birth-death literature;
- that \(Q_\lambda\) is the best physical macrostate;
- that the experiment itself prepared the four-state witness distributions;
- that the four-state rational witness uses the experiment's numerical parameters;
- that C2 has been experimentally validated;
- any spacetime or pregeometric consequence.

## 10. Empirical route

The paper reports time-resolved distributions \(\rho_N(t)\), transition rates, a charging energy \(E_{\rm C}=9.8\) meV, a baseline rate \(\Gamma_0=0.1\) Hz, and a driven multi-state nonequilibrium protocol.

A genuine empirical closure test would require the underlying time-series distributions or raw electron-count trajectories.

The protocol should then be frozen before the final comparison:

1. choose \(\lambda\);
2. compute \(G_\lambda(t)\) and \(G_{\lambda-c}(t)\);
3. estimate \(\dot G_\lambda(t)\) from held-out time points;
4. compare a one-score predictor against the exact two-transform identity;
5. quantify whether adding \(G_{\lambda-c}\) improves out-of-sample prediction by the amount required by the master equation.

Until raw or sufficiently tabulated data are recovered, the present result remains an analytic bridge theorem grounded in the published physical model, not an experimental validation.

## 11. Literature boundary

The master equation, transition-rate law, stochastic-thermodynamic interpretation, and nonequilibrium heat decomposition belong to the published work of Salhani et al. and to established stochastic thermodynamics.

The four-state witness and the use of the exact transform shift as a repository bridge are recorded here as a project derivation.

No priority claim is made until a targeted literature review of generating-function closure for birth-death processes is completed.


## 12. Exact commensurate closure ladder

The transform shift does not imply universal non-closure.

Let

$$
c=2\beta E_{\rm C}
$$

and define, for positive integers \(j\),

$$
H_j(t)=G_{jc}(t).
$$

Because

$$
G_0(t)=\sum_N\rho_N(t)=1,
$$

the exact transform equation gives

$$
\boxed{
\dot H_j
=
\Gamma^+(t)(e^{-jc}-1)H_j
+
\Gamma_0e^{-\beta E_{\rm C}}(e^{jc}-1)H_{j-1}.
}
$$

This system is lower triangular in the ordered family

$$
(H_1,H_2,\ldots,H_m).
$$

### Scalar closure at \(\lambda=c\)

For \(j=1\),

$$
\boxed{
\dot G_c
=
\Gamma^+(t)(e^{-c}-1)G_c
+
\Gamma_0e^{-\beta E_{\rm C}}(e^c-1).
}
$$

Since \(G_0=1\), the right-hand side contains no additional transform.

Thus the physical model has an exact one-transform closed observable at the distinguished parameter

$$
\lambda=c=2\beta E_{\rm C}.
$$

This parameter is not inserted to repair a failed closure. It is selected by the exponential state dependence already present in the published death rate.

### Finite closure for integer multiples

For

$$
\lambda=mc,
\qquad
m\in\mathbb N,
$$

the natural shift chain is

$$
G_{mc}
\to
G_{(m-1)c}
\to
\cdots
\to
G_c
\to
G_0=1.
$$

Therefore the vector

$$
\boxed{
(G_c,G_{2c},\ldots,G_{mc})
}
$$

is an exact finite closed triangular state under the published master equation.

The closure dimension supplied by this construction is \(m\).

### Generic parameter

For a parameter \(\lambda\) whose ratio \(\lambda/c\) is not a positive integer, repeated application of the same shift produces

$$
\lambda,\quad
\lambda-c,\quad
\lambda-2c,\quad\ldots
$$

without reaching \(0\) after a positive integer number of steps.

Therefore the **natural transform-shift ladder** does not terminate at the normalization \(G_0=1\).

This statement is intentionally limited. It does **not** prove that no other finite-dimensional nonlinear representation can close the dynamics at such a parameter.

## 13. Why the closure ladder matters

The bridge now has both a failure statement and a positive closure theorem.

For generic \(\lambda\), one fixed score is not dynamically autonomous because its derivative needs a shifted transform.

At the physically selected lattice

$$
\lambda\in c\mathbb N,
$$

the hierarchy closes after finitely many levels.

The first point,

$$
\lambda=c,
$$

is especially important: a scalar exponential score is exactly closed.

This changes the interpretation of the bridge. The physical lesson is not

> exponential scores never close.

The correct statement is

> closure depends on how the transform parameter is positioned relative to the exponential scale already built into the transition rates.

That dependence is derived from the physical master equation rather than added as an auxiliary assumption.

## 14. Verification

A separate exact audit evaluates the generator action at the commensurate transform points using rational arithmetic.

For the audit, write

$$
r=e^{-c}
$$

and choose the exact diagnostic values

$$
r=\frac12,\qquad
\Gamma^+=3,\qquad
\Gamma_0e^{-\beta E_{\rm C}}=\frac57,
$$

with current finite-support distribution

$$
p=
\left(
\frac1{10},\frac2{10},\frac3{10},\frac4{10}
\right).
$$

For \(j=1,2,3,4\), the direct generator derivative agrees exactly with

$$
\Gamma^+(r^j-1)G_{jc}
+
\Gamma_0e^{-\beta E_{\rm C}}(r^{-j}-1)G_{(j-1)c}.
$$

The exact derivative values are

$$
\frac{127}{560},\quad
\frac{339}{1120},\quad
\frac{5453}{10240},\quad
\frac{247245}{229376}.
$$

The audit is a regression check of the analytic identity, not an independent proof and not an experimental result.

## 15. Updated interpretation

Bridge 1B now supports three distinct statements:

1. **generic one-score non-autonomy:** one \(G_\lambda\) generally requires \(G_{\lambda-c}\);
2. **constructive non-closure:** equal mean and equal \(Q_\lambda\) need not determine \(\dot Q_\lambda\);
3. **commensurate exact closure:** when \(\lambda=mc\), the natural transform hierarchy closes exactly after \(m\) levels.

The combination is more informative than a blanket non-closure claim.

No novelty claim is attached to the finite closure ladder until specialized generating-function and functional-equation literature is reviewed more deeply.


## 16. Independent stationary-distribution consistency gate

Under the paper's time-averaged-rate approximation, the phase-averaged model gives the stationary distribution

$$
\rho_N^{\rm ss}
=
Z(\nu)^{-1}
\exp\left[-a(N-\nu)^2\right],
$$

with

$$
a=\beta E_{\rm C},
\qquad
\nu=
\frac{\log(\Gamma^+/\Gamma_0)}{2a}.
$$

Because the state index is integer,

$$
Z(\nu-k)=Z(\nu)
$$

for every integer \(k\).

Recall that

$$
c=2a.
$$

For \(k\in\mathbb N\),

$$
G_{kc}^{\rm ss}
=
\sum_N\rho_N^{\rm ss}e^{-2akN}.
$$

Completing the square gives

$$
-a(N-\nu)^2-2akN
=
-a[N-(\nu-k)]^2
-a(2k\nu-k^2).
$$

Therefore

$$
G_{kc}^{\rm ss}
=
e^{-a(2k\nu-k^2)}
\frac{Z(\nu-k)}{Z(\nu)}.
$$

Using integer-shift invariance of the normalization,

$$
\boxed{
G_{kc}^{\rm ss}
=
e^{ak^2}
\left(\frac{\Gamma_0}{\Gamma^+}\right)^k.
}
$$

### Agreement with the triangular closure

The stationary triangular equation gives

$$
G_{kc}^{\rm ss}
=
\frac{\Gamma_0}{\Gamma^+}
e^{a(2k-1)}
G_{(k-1)c}^{\rm ss}.
$$

Starting from \(G_0=1\), iteration yields

$$
G_{kc}^{\rm ss}
=
\left(\frac{\Gamma_0}{\Gamma^+}\right)^k
e^{a\sum_{j=1}^k(2j-1)}
=
\left(\frac{\Gamma_0}{\Gamma^+}\right)^k e^{ak^2}.
$$

Within the averaged-rate coarse-grained model, the transform closure and its stationary discrete-Gaussian solution give the same transform values by independent algebraic routes.

For \(k=1\),

$$
\boxed{
G_c^{\rm ss}
=
e^{\beta E_{\rm C}}\frac{\Gamma_0}{\Gamma^+}.
}
$$

If the published phase-averaged rate

$$
\Gamma^+
=
\Gamma_0 I_0(\beta eS_{\rm AC})
$$

is used, this becomes

$$
\boxed{
G_c^{\rm ss}
=
\frac{e^{\beta E_{\rm C}}}
{I_0(\beta eS_{\rm AC})}.
}
$$

This is a parameter-free consequence once the experimentally calibrated \(E_{\rm C}\), \(T\), and drive amplitude are supplied.

It is a consistency consequence of the published model, not a new thermodynamic law.

## 17. Stationary consistency audit

A rational surrogate audit writes

$$
s=e^{-a}
$$

and chooses

$$
s=\frac12,
\qquad
\frac{\Gamma_0}{\Gamma^+}=\frac23.
$$

The stationary formula

$$
H_k^{\rm ss}
=
\left(\frac{\Gamma_0}{\Gamma^+}\right)^k
s^{-k^2}
$$

agrees exactly with the triangular recurrence through \(k=4\).

The audited values are

$$
\frac43,\quad
\frac{64}{9},\quad
\frac{4096}{27},\quad
\frac{1048576}{81}.
$$

As in the other audits, this checks the algebra; it is not experimental evidence.


## 18. Scope correction for randomized phase

The transform-shift identity is exact for the master equation at a specified drive phase or deterministic drive history.

The experiment randomizes phase between repetitions. Averaging the exact conditioned equations introduces correlations such as

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{\lambda,\phi}),
$$

so a closed conditioned transform system does not automatically remain closed after phase averaging.

The replacement

$$
\Gamma^+(t)\approx\Gamma_0 I_0(\beta eS_{\rm AC})
$$

belongs to the paper's coarse-grained averaged-rate treatment.

Therefore:

- the generator identities and finite transform ladders remain exact at fixed phase;
- stationary formulas using the constant averaged rate are exact inside that approximating model;
- promotion of exact experimental closure requires phase-resolved information.
